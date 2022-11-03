from ape import accounts, config, networks, project
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.logging import logger


def main():
    network = networks.provider.network.name

    if network == LOCAL_NETWORK_NAME:
        account = accounts.containers["starknet"].test_accounts[0]
        bank = project.Bank.deploy()
        bank.initialize(sender=account)
    else:
        account = accounts.load("argentx")
        deployment = config.deployments["starknet"][network][-1]
        contract_address = deployment["address"]
        logger.info(f"Use contract at address '{contract_address}'.")
        bank = project.Bank.at(contract_address)

    # Fails here
    bank.initialize(sender=account)
