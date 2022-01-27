import pstats
from brownie import accounts, SimpleStorage, config


def read_contract():
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retreive())


def main():
    read_contract()
