from ape import networks
import ape

#Default network is starknet:local:starknet
print(ape.networks.provider.network.ecosystem.name)

with networks.parse_network_choice("ethereum:local:test"):
    print(ape.networks.provider.network.ecosystem.name)

    with networks.parse_network_choice("fantom:local:test"):
        print(ape.networks.provider.network.ecosystem.name)

        with networks.parse_network_choice("arbitrum:local:test"):
            print(ape.networks.provider.network.ecosystem.name)
        
        print(ape.networks.provider.network.ecosystem.name)

    print(ape.networks.provider.network.ecosystem.name)

print(ape.networks.provider.network.ecosystem.name)