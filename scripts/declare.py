import ape
import click


def main():
    account = ape.accounts.containers["starknet"].test_accounts[0]
    class_hash = account.declare(ape.project.storage)
    click.echo(class_hash)
