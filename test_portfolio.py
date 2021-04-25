import pytest
from portfolio import Portfolio


@pytest.fixture
def portfolio():
    return Portfolio()


def test_is_empty_when_created(portfolio):
    assert portfolio.is_empty is True


def test_is_not_empty_after_purchase(portfolio):
    portfolio.purchase('AAPL', 10)

    result = portfolio.is_empty

    assert result is False


def test_symbol_count_zero_when_created(portfolio):
    assert portfolio.unique_symbol_count == 0


def test_symbol_count_one_after_purchase(portfolio):
    portfolio.purchase('IBM', 1)

    result = portfolio.unique_symbol_count

    assert result == 1


def test_symbol_count_increments_on_unique_symbol_purchase(portfolio):
    portfolio.purchase('IBM', 1)
    portfolio.purchase('AAPL', 1)

    result = portfolio.unique_symbol_count

    assert result == 2


def test_symbol_count_does_not_increment_on_same_symbol_purchase(portfolio):
    portfolio.purchase('IBM', 1)
    portfolio.purchase('IBM', 1)

    result = portfolio.unique_symbol_count

    assert result == 1


def test_returns_shares_for_symbol(portfolio):
    portfolio.purchase('IBM', 42)

    result = portfolio.shares_of('IBM')

    assert result == 42


def test_separates_shares_by_symbol(portfolio):
    portfolio.purchase('IBM', 13)
    portfolio.purchase('AAPL', 42)

    result = portfolio.shares_of('IBM')

    assert result == 13


def test_returns_0_for_unpurchased_shares(portfolio):
    assert portfolio.shares_of('IBM') == 0


def test_sums_shares_for_symbol(portfolio):
    portfolio.purchase('IBM', 13)
    portfolio.purchase('IBM', 42)

    result = portfolio.shares_of('IBM')

    assert result == 55


def test_throws_on_purchase_non_positive_shares(portfolio):
    with pytest.raises(ValueError):
        portfolio.purchase('AAPL', 0)


def test_throws_oversell(portfolio):
    with pytest.raises(ValueError) as exception_info:
        portfolio.purchase('IBM', 50)
        portfolio.sell('IBM', 50 + 1)
    assert 'attempt to sell more shares than owned' == str(exception_info.value)


def test_reduces_shares_on_sell(portfolio):
    portfolio.purchase('IBM', 50)
    portfolio.sell('IBM', 20)

    result = portfolio.shares_of('IBM')

    assert result == 30


def test_reduces_symbol_count_on_symbol_selloff(portfolio):
    portfolio.purchase('IBM', 50)
    portfolio.sell('IBM', 50)

    result = portfolio.unique_symbol_count

    assert result == 0
