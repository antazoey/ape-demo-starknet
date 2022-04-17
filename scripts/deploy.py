import click
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.cli import NetworkBoundCommand, ape_cli_context
from ape.logging import logger


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
    _ = network  # Used by NetworkBoundCommand
    contract = cli_ctx.project_manager.Bank
    #logger.info(f"Deploying {contract.name} ...")
    bank = contract.deploy()
    click.echo(bank)
