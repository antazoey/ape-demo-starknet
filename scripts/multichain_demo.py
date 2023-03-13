import ape
from ape import networks
from click import echo


def main():
    # Default network is starknet:local:starknet
    echo(ape.networks.provider.network.ecosystem.name)

    with networks.parse_network_choice("ethereum:local:test"):
        echo(ape.networks.provider.network.ecosystem.name)

        with networks.parse_network_choice("fantom:local:test"):
            echo(ape.networks.provider.network.ecosystem.name)

            with networks.parse_network_choice("arbitrum:local:test"):
                echo(ape.networks.provider.network.ecosystem.name)

            echo(ape.networks.provider.network.ecosystem.name)

        echo(ape.networks.provider.network.ecosystem.name)

    echo(ape.networks.provider.network.ecosystem.name)
