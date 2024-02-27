from brownie import network, accounts, config

LOCAL_ENVIRONMENTS = ['mainnet-fork','development']

def get_account(env_account = True):
    if network.show_active() == "development":
        account = accounts[0]
    else:
        if env_account:
            account = accounts.add(config['wallets']['from'])
        else:
            account = accounts.load("mainaddress")
    return account

def get_local_account(index:int=None):
    if index:
        return accounts[index]
    else:
        return accounts[0]