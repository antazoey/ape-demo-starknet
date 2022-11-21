import click
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.cli import NetworkBoundCommand, ape_cli_context


def starknet_network_option():
    def callback(ctx, param, value):
        return f"starknet:{value}"

    options = ["testnet", "mainnet", LOCAL_NETWORK_NAME]
    return click.option(
        "--network",
        type=click.Choice(options),
        callback=callback,
        default=LOCAL_NETWORK_NAME,
    )


@click.command(cls=NetworkBoundCommand)
@ape_cli_context()
@starknet_network_option()
def cli(cli_ctx, network):
    if LOCAL_NETWORK_NAME in network:
        account = cli_ctx.account_manager.containers["starknet"].test_accounts[0]
    else:
        account = cli_ctx.account_manager.load("janeway")
        account.set_autosign(True)

    contract = cli_ctx.project_manager.Bank
    account.declare(contract)
    bank = contract.deploy(sender=account)

    # Initialize
    bank.initialize(sender=account)
