import os
import sys
from dotenv import load_dotenv

from hedera_sdk_python.client.client import Client
from hedera_sdk_python.account.account_id import AccountId
from hedera_sdk_python.crypto.private_key import PrivateKey
from hedera_sdk_python.tokens.token_create_transaction import TokenCreateTransaction
from hedera_sdk_python.client.network import Network
from cryptography.hazmat.primitives import serialization
from hedera_sdk_python.tokens.token_type import TokenType

load_dotenv()

def create_token():
    network = Network(network='testnet')
    client = Client(network)

    operator_id = AccountId.from_string(os.getenv('OPERATOR_ID'))
    operator_key = PrivateKey.from_string(os.getenv('OPERATOR_KEY'))
    admin_key = PrivateKey.from_string(os.getenv('ADMIN_KEY'))
    
    client.set_operator(operator_id, operator_key)

    transaction = (
        TokenCreateTransaction()
        .set_token_name("MyToken")
        .set_token_symbol("MTK")
        .set_decimals(2)
        .set_initial_supply(10)
        .set_treasury_account_id(operator_id)
        .set_token_type(TokenType.FUNGIBLE_COMMON)
        .set_admin_key(admin_key)
        .freeze_with(client)
        .sign(operator_key)
        .sign(admin_key)
    )
    
    try:
        receipt = transaction.execute(client)
        if receipt and receipt.tokenId:
            print(f"Token created with ID: {receipt.tokenId}")
        else:
            print("Token creation failed: Token ID not returned in receipt.")
            sys.exit(1)
    except Exception as e:
        print(f"Token creation failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    create_token()
