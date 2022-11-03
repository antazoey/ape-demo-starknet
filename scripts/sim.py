from ape import accounts, config, networks, project
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.logging import logger
from rich import print


def main():
    network = networks.provider.network.name

    if network == LOCAL_NETWORK_NAME:
        account = accounts.containers["starknet"].test_accounts[0]
        logger.info(f"Deploying {project.Bank.contract_type.name}...")
        bank = project.Bank.deploy()
        bank.initialize(sender=account)
    else:
        account = accounts.load("argentx")
        deployment = config.deployments["starknet"][network][-1]
        contract_address = deployment["address"]
        logger.info(f"Use contract at address '{contract_address}'.")
        bank = project.Bank.at(contract_address)

    amount = 100
    logger.info(f"Increasing balance by {amount}...")
    receipt = bank.increase_balance(amount, sender=account)

    # There should not be any transfer logs
    transfer_logs = list(receipt.decode_logs(bank.Transfer))
    print(f"\n***********\nFound {len(transfer_logs)} Transfer logs:")
    for log in transfer_logs:
        print(f"\n\tSender={log.from_},\n\tReceiver={log.to},\n\tValue={log.value}.\n")
    print("\n***********\n")

    amount = 20
    logger.info(f"Increasing balance by {amount}...")
    bank.increase_balance(amount, sender=account)

    new_balance = bank.get_balance()
    logger.info(f"The balance has been updated to {new_balance}.")


if __name__ == "__main__":
    with networks.starknet.local.use_provider("starknet"):
        main()
