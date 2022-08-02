import pytest


@pytest.fixture(autouse=True, scope="module")
def connection(networks):
    # Ensure uses Starknet for tests in this module
    with networks.parse_network_choice("starknet:local") as provider:
        yield provider


@pytest.fixture(scope="module")
def stark_contract(project, stark_account):
    contract = project.Bank.deploy()
    contract.initialize(sender=stark_account)
    return contract


def test_increase_balance(stark_contract, stark_account):
    initial_balance = stark_contract.get_balance()
    stark_contract.increase_balance(100, sender=stark_account)
    assert stark_contract.get_balance() == initial_balance + 100


def test_increase_balance_emits_event(stark_contract, stark_account):
    receipt = stark_contract.increase_balance(200, sender=stark_account)
    events = [e for e in receipt.decode_logs(stark_contract.balance_increased)]
    assert len(events) == 1
    assert events[0].amount == 200
