from ape import accounts


def main():
    acct = accounts.load("StarkMe2")
    print(acct.balance)

    argent_acct = accounts.load("argentx0")
    print(argent_acct.balance)

    acct.transfer(argent_acct, "100 gwei")
