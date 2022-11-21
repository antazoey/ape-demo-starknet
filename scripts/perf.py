from ape import chain
from rich import print as printr


def main():
    for i in range(100):
        chain.mine()
        block = chain.provider.get_block(i)
        printr(block)
