from ape import accounts, project
from ape_starknet import tokens
from rich import print as printr


def main():
    eth = tokens["eth"]
    printr(f"ETH Address is {eth.address}")
    account = accounts.load("argentx")

    printr(f"Account balance is {account.balance}")
    printr(account.address in account.account_contracts)
    printr(f"Account address is {account.address}")

    bank = project.Bank.at("0x01765b35F0E8BFD6Fa1043dDb2e4fa4026cB20927B1c1043aF24026f866eA952")
    receipt = bank.initialize(sender=account)
    printr(receipt.dict())
