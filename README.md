# ape-demo-starknet

A demo Starknet project using Ape.
**Note**: This project uses the Starknet ecosystem as default instead of Ethereum.

To compile, run:

```bash
ape compile
```

To run the tests, do:

```bash
ape test
```

To deploy the `Bank` contract in a script or `ape console` session, do:

```python
from ape import accounts, project

account = accounts.containers["starknet"].test_accounts[0]
account.declare(project.Bank)
bank = project.Bank.deploy(sender=account)
```

Now, try to interact with it:

```python
bank.initialize(sender=account)
bank.increase_balance(200, sender=account)
```
