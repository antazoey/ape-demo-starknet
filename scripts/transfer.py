from ape import accounts


def main():
    acct = accounts.load("janeway")
    print(acct.balance)

    # argent_acct = accounts.load("janeway")
    # # print(argent_acct.balance)

    # argent_acct.transfer(acct, everything)
