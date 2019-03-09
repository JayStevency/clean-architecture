import copy
from clean_architecture.entity import Entity
from dataclasses import dataclass


@dataclass
class NestedMock(Entity):
    x: int


@dataclass
class Mock(Entity):
    x: int
    y: int
    l: list
    t: tuple
    d: dict
    n: NestedMock


class UnDataClassMock(Entity):
    def __init__(self, x):
        self.x = x


def test_to_dict_unsupport_when_no_data_class():
    m = UnDataClassMock(x=10)

    expected = {}

    assert m.to_dict() == expected


def test_entity_to_dict_when_data_class():
    m = Mock(x=10,
             y=20,
             l=[1, 2],
             t=('abc', 123),
             d={'x': 10, 'y': 20},
             n=NestedMock(x=1))

    expected = {
        'x': 10,
        'y': 20,
        'l': [1, 2],
        't': ('abc', 123),
        'd': {'x': 10, 'y': 20},
        'n': {'x': 1}
    }

    assert m.to_dict() == expected


def test_entity_eq():
    m1 = Mock(x=10,
              y=20,
              l=[1, 2],
              t=('abc', 123),
              d={'x': 10, 'y': 20},
              n=NestedMock(x=1))

    m2 = copy.deepcopy(m1)

    assert m1 == m2


def test_entity_not_eq():
    m1 = Mock(x=10,
              y=20,
              l=[1, 2],
              t=('abc', 123),
              d={'x': 10, 'y': 20},
              n=NestedMock(x=1))

    m2 = copy.deepcopy(m1)
    m2.l[0] = 20

    assert m1 != m2
