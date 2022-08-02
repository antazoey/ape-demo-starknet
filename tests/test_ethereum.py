import pytest


@pytest.fixture(autouse=True, scope="module")
def connection(networks):
    # Ensure uses Ethereum for tests in this module
    with networks.parse_network_choice("ethereum:local") as provider:
        yield provider


@pytest.fixture(scope="module")
def eth_contract(networks, project, eth_account):
    # Make a module-scoped Ethereum contract
    with networks.parse_network_choice("ethereum:local"):
        return eth_account.deploy(project.MyContract, sender=eth_account)


def test_ethereum_thing(eth_contract, eth_account):
    eth_contract.setNumber(123, sender=eth_account)
    assert eth_contract.myNumber() == 123
