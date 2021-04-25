import pytest
from name_normalizer import NameNormalizer, InvalidNameException


def test_empty_name_returns_empty_name():
    assert NameNormalizer('').normalize() == ''


def test_mononym_returns_same():
    assert NameNormalizer('Plato').normalize() == 'Plato'


def test_trims_whitespace():
    assert NameNormalizer('  Big    Boi  ').normalize() == 'Boi, Big'


def test_duonym_returns_last_first():
    assert NameNormalizer('Jeff Langr').normalize() == 'Langr, Jeff'

# do tests have to start with test_


def test_appends_suffixes():
    assert NameNormalizer('Martin Luther King, Jr.').normalize() == 'King, Martin L., Jr.'


# @pytest.mark.skip
def test_initializes_middle_name():
    assert NameNormalizer('Henry David Thoreau').normalize() == 'Thoreau, Henry D.'


def test_initializes_multiple_middle_names():
    assert NameNormalizer('Julia Scarlett Elizabeth Louis-Dreyfus').normalize() == 'Louis-Dreyfus, Julia S. E.'


def test_throws_on_excess_commas():
    with pytest.raises(InvalidNameException):
        NameNormalizer('howell, thurston, lovey')
