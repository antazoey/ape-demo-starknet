from ape import networks, project
from click import echo


def main():
    class_hash = networks.provider.declare(project.BigCairo)
    echo(class_hash)
