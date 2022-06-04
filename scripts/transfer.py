from ape import accounts


def main():
    acct = accounts.load("StarkMe2")
    print(acct.balance)

    argent_acct = accounts.load("argentx0")
    print(argent_acct.balance)

    argent_acct.transfer(acct, "900 gwei")
