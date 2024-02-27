from brownie import network, accounts, BestiaToken
from scripts.helpers import get_account, get_local_account, LOCAL_ENVIRONMENTS
from web3 import Web3


def deploy_contract():
    account =  get_account()
    supply = Web3.toWei(10000000,'ether')
    token = BestiaToken.deploy(supply,{'from':account})
    print(f"Token {token.name()} can be found at {token.address}")
    print(f"Token Total Supply: {token.totalSupply()}")
    print(f"Token Balance of {account.address}: {token.balanceOf(account.address)}")
    if network.show_active() in LOCAL_ENVIRONMENTS:
        local_account = get_local_account(1);
        initial_local_account_balance = token.balanceOf(local_account.address)
        print(f"Initial Token Balance of {local_account.address}: {initial_local_account_balance}")
        token_to_transfer = Web3.toWei(1000,"ether")
        print(f"Transferring {token_to_transfer} from {account.address} to {local_account.address}")
        print(f"Approving Transfer for {local_account.address}")
        token.approve(local_account.address,token_to_transfer)
        print(f"Checking Allowance: {token.allowance(account.address,local_account.address)}")
        token.transfer(local_account.address,token_to_transfer,{'from':account})
        print(f"New Token Balance of {local_account.address}: {token.balanceOf(local_account.address)}")
        print(f"New Token Balance of {account.address}: {token.balanceOf(account.address)}")
    return token


def main():
    deploy_contract()