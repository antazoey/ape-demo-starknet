from ape import accounts, project
from ape_starknet import tokens


def main():
    eth = tokens["eth"]
    print(f"ETH Address is {eth.address}")
    account = accounts.load("argentx")


    
    print(f"Account balance is {account.balance}")
    print(account.address in account.account_contracts)
    print(f"Account address is {account.address}")

    bank = project.Bank.at("0x01765b35F0E8BFD6Fa1043dDb2e4fa4026cB20927B1c1043aF24026f866eA952")
    receipt = bank.initialize(sender=account)

