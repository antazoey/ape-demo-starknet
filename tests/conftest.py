import pytest
from ape import accounts


@pytest.fixture(scope="session")
def account():
    container = accounts.containers["starknet"]
    return container.deploy_account("TEST")


@pytest.fixture(scope="session")
def bank_contract_type(project):
    return project.Bank


@pytest.fixture(scope="session")
def bank(bank_contract_type):
    return bank_contract_type.deploy()
