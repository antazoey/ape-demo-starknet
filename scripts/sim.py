from ape import accounts, config, project, networks, project
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.logging import logger


def main():
    network = networks.provider.network.name

    if network == LOCAL_NETWORK_NAME:
        account = accounts.containers["starknet"].deploy_account("TEST")
        logger.info(f"Deploying {project.Bank.contract_type.name}...")
        bank = project.Bank.deploy()
    else:
        account = accounts.load("StarkMe2")
        deployment = config.deployments["starknet"][network][-1]
        contract_address = deployment["address"]
        logger.info(f"Use contract at address '{contract_address}'.")
        bank = project.Bank.at(contract_address)

    amount = 100
    logger.info(f"Increasing balance by {amount}...")

    bank.increase_balance(amount, sender=account)

    new_balance = bank.get_balance()
    logger.info(f"The balance has been updated to {new_balance}.")
