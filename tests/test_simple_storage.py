from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retreive()
    expected_value = 0
    # Assert
    assert expected_value == starting_value


def test_update():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    simple_storage.store(expected, {"from": account})
    actual = simple_storage.retreive()
    # Assert
    assert expected == actual
