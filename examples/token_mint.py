import os
import sys
import json
from dotenv import load_dotenv

from hedera_sdk_python.client.client import Client
from hedera_sdk_python.account.account_id import AccountId
from hedera_sdk_python.crypto.private_key import PrivateKey
from hedera_sdk_python.tokens.token_mint_transaction import TokenMintTransaction
from hedera_sdk_python.client.network import Network
from hedera_sdk_python.tokens.token_id import TokenId

load_dotenv()

# Examples for different token types illustrated here for clarity. 

def fungible_token_mint():
    network = Network(network='testnet')
    client = Client(network)

    payer_id = AccountId.from_string(os.getenv('OPERATOR_ID'))
    payer_key = PrivateKey.from_string(os.getenv('OPERATOR_KEY'))
    supply_key = PrivateKey.from_string(os.getenv('SUPPLY_KEY'))
    token_id = TokenId.from_string(os.getenv('TOKEN_ID'))

    client.set_operator(payer_id, payer_key)

    transaction = (
        TokenMintTransaction()
        .set_token_id(token_id)
        .set_amount(20000) # Amount to mint in lowest denomination
        .freeze_with(client)
        .sign(payer_key)
        .sign(supply_key)
    )
    
    try:
        receipt = transaction.execute(client)
        if receipt and receipt.tokenId:
            print(f"Fungible token minting successful")
        else:
            print(f"Fungible token minting failed")
            sys.exit(1)
    except Exception as e:
        print(f"Fungible token minting failed: {str(e)}")
        sys.exit(1)

def load_metadata_from_json(file_path):
    """
    Loads NFT metadata from a JSON file.

    :param file_path: Path to the JSON file containing metadata.
    :return: List of byte arrays representing NFT metadata.
    """
    try:
        with open(file_path, 'r') as file:
            metadata = json.load(file)
            if not isinstance(metadata, list):
                raise ValueError("Metadata JSON must be a list of strings.")
            # Convert each metadata string to bytes
            return [m.encode('utf-8') for m in metadata]
    except Exception as e:
        print(f"Failed to load metadata from JSON: {str(e)}")
        sys.exit(1)

def nft_token_mint(metadata):
    network = Network(network='testnet')
    client = Client(network)

    payer_id = AccountId.from_string(os.getenv('OPERATOR_ID'))
    payer_key = PrivateKey.from_string(os.getenv('OPERATOR_KEY'))
    supply_key = PrivateKey.from_string(os.getenv('SUPPLY_KEY'))
    token_id = TokenId.from_string(os.getenv('TOKEN_ID'))

    client.set_operator(payer_id, payer_key)

    transaction = (
        TokenMintTransaction()
        .set_token_id(token_id)
        .set_metadata(metadata) # Mandatory list of byte array metadata for NFTs
        .freeze_with(client)
        .sign(payer_key)
        .sign(supply_key)
        
    )
    
    try:
        receipt = transaction.execute(client)
        if receipt and receipt.tokenId:
            print(f"NFT minting successful")

        else:
            print(f"NFT minting failed")
            sys.exit(1)
    except Exception as e:
        print(f"NFT minting failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    # To mint fungible tokens:
    fungible_token_mint() 
    #
    # To mint NFTs:
    # nft_token_mint()  #Commented out for illustration

