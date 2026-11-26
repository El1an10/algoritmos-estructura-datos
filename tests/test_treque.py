import pytest

from estructuras_de_datos.treque import Empty, LinkedTreque


def _treque(values):
    t = LinkedTreque()
    for v in values:
        t.insert_last(v)
    return t


def test_ends():
    t = LinkedTreque()
    t.insert_last(1)
    t.insert_last(2)
    t.insert_first(0)
    assert t.first() == 0
    assert t.last() == 2
    assert t.delete_first() == 0
    assert t.delete_last() == 2
    assert list(t.items()) == [1]


def test_middle_matches_docstring_example():
    t = _treque([6, 7, 8, 1])
    assert t.middle() == 7
    t.insert_middle(2)
    assert list(t.items()) == [6, 7, 2, 8, 1]
    t.insert_middle(10)
    assert list(t.items()) == [6, 7, 10, 2, 8, 1]
    assert t.delete_middle() == 10
    assert list(t.items()) == [6, 7, 2, 8, 1]
    t.delete_last()
    assert t.middle() == 7


def test_insert_middle_readme_example():
    t = LinkedTreque()
    t.insert_last(1)
    t.insert_last(2)
    t.insert_first(0)
    t.insert_middle(99)
    assert list(t.items()) == [0, 99, 1, 2]


def test_single_element_middle():
    t = LinkedTreque()
    t.insert_middle(5)
    assert t.delete_middle() == 5
    assert t.is_empty()


@pytest.mark.parametrize(
    "method", ["first", "last", "middle", "delete_first", "delete_last", "delete_middle"]
)
def test_empty_raises(method):
    with pytest.raises(Empty):
        getattr(LinkedTreque(), method)()
