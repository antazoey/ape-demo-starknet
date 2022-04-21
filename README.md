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

To interact with the Bank contract in the `console`, first launch the console:

```bash
ape console
```

The default network provider is `starknet-devnet`, so accounts you deploy will not persist.

Deploy an ephemeral account by doing the following:

```python
In [1]: account = accounts.containers["starknet"].deploy_account("Temp")
```

Then, deploy the Bank contract:

```python
In [2]: bank = project.Bank.deploy(sender=account)
SUCCESS: Contract 'Bank' deployed to: 0x5685DCE3F9c319B7B62F80421eB9db19C5DbC878616af504f825377Ce973e7f
```

Now, try to interact with it:

```python

```
