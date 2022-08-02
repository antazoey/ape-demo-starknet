import pytest
import ape


"""Accounts can still be session-scoped"""


@pytest.fixture(scope="session")
def eth_account(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def stark_account():
    return ape.accounts.containers["starknet"].test_accounts[0]
