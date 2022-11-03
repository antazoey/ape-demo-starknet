from ape import chain


def main():
    for i in range(100):
        chain.mine()
        block = chain.provider.get_block(i)
        print(block)