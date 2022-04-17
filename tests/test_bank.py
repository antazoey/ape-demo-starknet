import ape


def test_increase_balance_when_not_initialized(bank):
    with ape.reverts():
        # Unitialized
        bank.increase_balance(100)


def test_initialize(bank):
    bank.initialize()

    with ape.reverts("Already initialized"):
        bank.initialize()


def test_balance(bank):
    assert bank.get_balance() == 0


def test_increase_balance(bank, account):
    bank.increase_balance(100, sender=account)
    assert bank.get_balance() == 100


def test_increase_balance_emits_event(bank, account):
    receipt = bank.increase_balance(200, sender=account)
    events = [e for e in receipt.decode_logs(bank.balance_increased)]
    assert len(events) == 1
    assert events[0].amount == 200
