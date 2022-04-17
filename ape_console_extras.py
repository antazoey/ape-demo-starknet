from ape.api.networks import LOCAL_NETWORK_NAME


def ape_init_extras(networks, project):
    extras = {}
    # if networks.provider.network.name == LOCAL_NETWORK_NAME:
    #     bank = project.Bank.deploy()
    #     extras["bank"] = bank

    return extras
