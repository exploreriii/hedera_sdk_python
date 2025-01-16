import os
import sys
from dotenv import load_dotenv
from hedera_sdk_python.client.network import Network
from hedera_sdk_python.client.client import Client
from hedera_sdk_python.account.account_id import AccountId
from hedera_sdk_python.account.account_create_transaction import AccountCreateTransaction
from hedera_sdk_python.crypto.private_key import PrivateKey
from hedera_sdk_python.tokens.token_create_transaction import TokenCreateTransaction
from hedera_sdk_python.tokens.token_associate_transaction import TokenAssociateTransaction
from hedera_sdk_python.transaction.transfer_transaction import TransferTransaction
from hedera_sdk_python.tokens.token_delete_transaction import TokenDeleteTransaction
from hedera_sdk_python.response_code import ResponseCode
from hedera_sdk_python.consensus.topic_create_transaction import TopicCreateTransaction
from hedera_sdk_python.consensus.topic_message_submit_transaction import TopicMessageSubmitTransaction
from hedera_sdk_python.consensus.topic_update_transaction import TopicUpdateTransaction
from hedera_sdk_python.consensus.topic_delete_transaction import TopicDeleteTransaction
from hedera_sdk_python.consensus.topic_id import TopicId
from hedera_sdk_python.query.topic_info_query import TopicInfoQuery
from hedera_sdk_python.query.account_balance_query import CryptoGetAccountBalanceQuery
from hedera_sdk_python.tokens.token_type import TokenType

load_dotenv()

def load_operator_credentials():
    """Load operator credentials from environment variables."""
    try:
        operator_id = AccountId.from_string(os.getenv('OPERATOR_ID'))
        operator_key = PrivateKey.from_string(os.getenv('OPERATOR_KEY'))
    except Exception as e:
        print(f"Error parsing operator credentials: {e}")
        sys.exit(1)
    return operator_id, operator_key

def create_new_account(client, initial_balance=100000000):
    new_account_private_key = PrivateKey.generate()
    new_account_public_key = new_account_private_key.public_key()

    transaction = AccountCreateTransaction(
        key=new_account_public_key,
        initial_balance=initial_balance,
        memo="Recipient Account"
    )
    transaction.freeze_with(client)
    transaction.sign(client.operator_private_key)

    try:
        receipt = transaction.execute(client)
        new_account_id = receipt.accountId
        if new_account_id is not None:
            print(f"Account creation successful. New Account ID: {new_account_id}")
            print(f"New Account Private Key: {new_account_private_key.to_string()}")
            print(f"New Account Public Key: {new_account_public_key.to_string()}")
        else:
            raise Exception("AccountID not found in receipt. Account may not have been created.")
    except Exception as e:
        print(f"Account creation failed: {str(e)}")
        sys.exit(1)

    return new_account_id, new_account_private_key

def query_balance(client, account_id):
    balance = CryptoGetAccountBalanceQuery(account_id=account_id).execute(client)
    print(f"Account {account_id} balance: {balance.hbars}")
    return balance

def create_token(client, operator_id, admin_key):
    transaction = TokenCreateTransaction(
        token_name="ExampleToken",
        token_symbol="EXT",
        decimals=2,
        initial_supply=1000,
        treasury_account_id=operator_id,
        token_type=TokenType.FUNGIBLE_COMMON,
        admin_key=admin_key
    )
    transaction.freeze_with(client)
    transaction.sign(client.operator_private_key)
    transaction.sign(admin_key)

    try:
        receipt = transaction.execute(client)
    except Exception as e:
        print(f"Token creation failed: {str(e)}")
        sys.exit(1)

    if not receipt.tokenId:
        print("Token creation failed: Token ID not returned in receipt.")
        sys.exit(1)

    token_id = receipt.tokenId
    print(f"Token creation successful. Token ID: {token_id}")
    return token_id

def associate_token(client, recipient_id, recipient_private_key, token_id):
    transaction = TokenAssociateTransaction(
        account_id=recipient_id,
        token_ids=[token_id]
    )
    transaction.freeze_with(client)
    transaction.sign(client.operator_private_key)
    transaction.sign(recipient_private_key)

    try:
        receipt = transaction.execute(client)
        if receipt.status != ResponseCode.SUCCESS:
            status_message = ResponseCode.get_name(receipt.status)
            raise Exception(f"Token association failed with status: {status_message}")
        print("Token association successful.")
    except Exception as e:
        print(f"Token association failed: {str(e)}")
        sys.exit(1)

def transfer_token(client, recipient_id, token_id):
    transaction = TransferTransaction(
        token_transfers={
            token_id: {
                client.operator_account_id: -1,
                recipient_id: 1,
            }
        }
    ).freeze_with(client)
    transaction.sign(client.operator_private_key)

    try:
        receipt = transaction.execute(client)
        if receipt.status != ResponseCode.SUCCESS:
            status_message = ResponseCode.get_name(receipt.status)
            raise Exception(f"Token transfer failed with status: {status_message}")
        print("Token transfer successful.")
    except Exception as e:
        print(f"Token transfer failed: {str(e)}")
        sys.exit(1)

def delete_token(client, token_id, admin_key):
    transaction = TokenDeleteTransaction(token_id=token_id)
    transaction.freeze_with(client)
    transaction.sign(client.operator_private_key)
    transaction.sign(admin_key)

    try:
        receipt = transaction.execute(client)
        if receipt.status != ResponseCode.SUCCESS:
            status_message = ResponseCode.get_name(receipt.status)
            raise Exception(f"Token deletion failed with status: {status_message}")
        print("Token deletion successful.")
    except Exception as e:
        print(f"Token deletion failed: {str(e)}")
        sys.exit(1)

def create_topic(client):
    key = client.operator_private_key
    transaction = TopicCreateTransaction(
        memo="Python SDK created topic",
        admin_key=key.public_key()
    )
    transaction.freeze_with(client)
    transaction.sign(key)

    try:
        receipt = transaction.execute(client)
    except Exception as e:
        print(f"Topic creation failed: {str(e)}")
        sys.exit(1)

    if not receipt.topicId:
        print("Topic creation failed: Topic ID not returned in receipt.")
        sys.exit(1)

    topic_id = receipt.topicId
    print(f"Topic creation successful. Topic ID: {topic_id}")

    return topic_id

def submit_message(client, topic_id):
    transaction = TopicMessageSubmitTransaction(
        topic_id=topic_id,
        message="Hello, Python SDK!"
    )
    transaction.freeze_with(client)
    transaction.sign(client.operator_private_key)

    try:
        receipt = transaction.execute(client)
    except Exception as e:
        print(f"Message submission failed: {str(e)}")
        sys.exit(1)

    if receipt.status != ResponseCode.SUCCESS:
        status_message = ResponseCode.get_name(receipt.status)
        raise Exception(f"Message submission failed with status: {status_message}")

    print("Message submitted successfully.")

def update_topic(client, topic_id):
    key = client.operator_private_key
    transaction = TopicUpdateTransaction(
        topic_id=topic_id,
        memo="Python SDK updated topic"
    )
    transaction.freeze_with(client)
    transaction.sign(key)

    try:
        receipt = transaction.execute(client)
    except Exception as e:
        print(f"Topic update failed: {str(e)}")
        sys.exit(1)

    if receipt.status != ResponseCode.SUCCESS:
        status_message = ResponseCode.get_name(receipt.status)
        raise Exception(f"Topic update failed with status: {status_message}")

    print("Topic updated successfully.")

def delete_topic(client, topic_id):
    transaction = TopicDeleteTransaction(topic_id=topic_id)
    transaction.freeze_with(client)
    transaction.sign(client.operator_private_key)

    try:
        receipt = transaction.execute(client)
    except Exception as e:
        print(f"Topic deletion failed: {str(e)}")
        sys.exit(1)

    if receipt.status != ResponseCode.SUCCESS:
        status_message = ResponseCode.get_name(receipt.status)
        raise Exception(f"Topic deletion failed with status: {status_message}")

    print("Topic deleted successfully.")

def query_topic_info(client, topic_id):
    """Optional method to show how to query topic info."""
    try:
        topic_info = TopicInfoQuery(topic_id=topic_id).execute(client)
        print(f"Topic Info: {topic_info}")
    except Exception as e:
        print(f"Failed to retrieve topic info: {str(e)}")

def main():
    operator_id, operator_key = load_operator_credentials()
    admin_key = PrivateKey.generate()

    network_type = os.getenv('NETWORK')
    network = Network(network=network_type)
    client = Client(network)
    client.set_operator(operator_id, operator_key)

    recipient_id, recipient_private_key = create_new_account(client)
    query_balance(client, recipient_id)

    token_id = create_token(client, operator_id, admin_key)
    associate_token(client, recipient_id, recipient_private_key, token_id)
    transfer_token(client, recipient_id, token_id)
    delete_token(client, token_id, admin_key)

    topic_id = create_topic(client)
    submit_message(client, topic_id)
    update_topic(client, topic_id)
    query_topic_info(client, topic_id)
    delete_topic(client, topic_id)

if __name__ == "__main__":
    main()
