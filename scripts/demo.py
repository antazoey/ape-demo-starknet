import click

from ape.api.networks import LOCAL_NETWORK_NAME
from ape.cli import ape_cli_context, NetworkBoundCommand


def starknet_network_option():
    def callback(ctx, param, value):
        return f"starknet:{value}"

    options = ["testnet", "mainnet", LOCAL_NETWORK_NAME]
    return click.option(
        "--network",
        type=click.Choice(options),
        callback=callback,
        default=LOCAL_NETWORK_NAME
    )


@click.command(cls=NetworkBoundCommand)
@ape_cli_context()
@starknet_network_option()
def cli(cli_ctx, network):
    """Demo Starknet"""

    if cli_ctx.provider.name != "starknet":
        click.echo("Please use Starknet when executing this script.")

    # Demo that we can compile + access the contract
    bank = cli_ctx.project_manager.Bank
    click.echo(f"The Cairo contract in this project: {bank}")

    # Demo that we can get a block
    block = cli_ctx.provider.get_block(0)
    click.echo(block)

