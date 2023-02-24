import click
from ape.cli import NetworkBoundCommand, ape_cli_context


@click.command(cls=NetworkBoundCommand)
@ape_cli_context()
def cli(cli_ctx):
    container = cli_ctx.account_manager.containers["starknet"]
    account = container.test_accounts[0]
    account.declare(cli_ctx.project_manager.Bank)
    contract = account.deploy(cli_ctx.project_manager.Bank, 1000, account)
    receipt = contract.initialize(sender=account)
    receipt.show_trace()
