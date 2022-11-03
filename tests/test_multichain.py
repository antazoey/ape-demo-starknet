import pytest


@pytest.fixture(scope="module")
def eth_contract(networks, project, eth_account):
    # Make a module-scoped Ethereum contract.
    # NOTE: Can also yield here to retain connection
    with networks.parse_network_choice("ethereum:local"):
        yield eth_account.deploy(project.MyContract, sender=eth_account)


@pytest.fixture(scope="module")
def stark_contract(networks, project, stark_account):
    with networks.parse_network_choice("starknet:local"):
        contract = project.Bank.deploy()
        contract.initialize(sender=stark_account)
        yield contract


def test_ethereum_thing(eth_contract, eth_account):
    eth_contract.setNumber(123, sender=eth_account)
    assert eth_contract.myNumber() == 123


def test_starknet_thing(stark_account, stark_contract):
    initial_balance = stark_contract.get_balance()
    stark_contract.increase_balance(100, sender=stark_account)
    assert stark_contract.get_balance() == initial_balance + 100


def test_multichain_in_same_test(
    networks, stark_account, stark_contract, eth_account, eth_contract
):
    initial_balance = stark_contract.get_balance()
    stark_contract.increase_balance(100, sender=stark_account)
    assert stark_contract.get_balance() == initial_balance + 100

    # Switch to Ethereum mid test
    with networks.parse_network_choice("ethereum:local"):
        eth_contract.setNumber(123, sender=eth_account)
        assert eth_contract.myNumber() == 123

    initial_balance = stark_contract.get_balance()
    stark_contract.increase_balance(100, sender=stark_account)
    assert stark_contract.get_balance() == initial_balance + 100
