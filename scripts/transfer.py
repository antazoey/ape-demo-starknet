from ape import accounts
from rich import print as printr


def main():
    acct = accounts.load("janeway")
    printr(acct.balance)

    # argent_acct = accounts.load("janeway")
    # # printr(argent_acct.balance)

    # argent_acct.transfer(acct, everything)
