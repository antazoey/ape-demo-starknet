import ape
import pytest

"""Accounts can still be session-scoped"""


@pytest.fixture(scope="session")
def eth_account(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def stark_account():
    with ape.networks.starknet.local.use_provider("starknet"):
        return ape.accounts.containers["starknet"].test_accounts[0]
