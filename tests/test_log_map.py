import random
from datetime import datetime

import pytest

from estructuras_de_datos.log_map.log_map import AVLTreeMap, LogMap


def _height(node):
    if node is None:
        return 0
    return 1 + max(_height(node.left), _height(node.right))


def _assert_avl(node):
    """Verifica balance, alturas guardadas y punteros a padre en todo el arbol."""
    if node is None:
        return
    assert abs(_height(node.left) - _height(node.right)) <= 1
    assert node.height == _height(node)
    for child in (node.left, node.right):
        if child is not None:
            assert child.parent is node
    _assert_avl(node.left)
    _assert_avl(node.right)


def test_insert_and_get():
    m = AVLTreeMap()
    for k in [5, 3, 8, 1, 4]:
        m[k] = str(k)
    assert len(m) == 5
    assert m[4] == "4"
    assert list(m) == [1, 3, 4, 5, 8]


def test_missing_key_raises():
    m = AVLTreeMap()
    with pytest.raises(KeyError):
        m[1]
    with pytest.raises(KeyError):
        del m[1]


def test_overwrite_does_not_change_size():
    m = AVLTreeMap()
    m[1] = "a"
    m[1] = "b"
    assert len(m) == 1
    assert m[1] == "b"


def test_delete_two_children_keeps_balance():
    # Caso que antes dejaba el arbol desbalanceado: el sucesor de 9
    # no es hijo directo y el rebalanceo empezaba en el nodo equivocado.
    m = AVLTreeMap()
    for k in [5, 4, 12, 6, 9, 13, 1, 11, 14, 10]:
        m[k] = k
    del m[9]
    _assert_avl(m._root)
    assert list(m) == [1, 4, 5, 6, 10, 11, 12, 13, 14]


def test_random_operations_match_dict():
    rng = random.Random(42)
    for _ in range(50):
        m, ref = AVLTreeMap(), {}
        for _ in range(300):
            k = rng.randint(0, 100)
            if rng.random() < 0.6:
                m[k] = k
                ref[k] = k
            elif k in ref:
                del m[k]
                del ref[k]
            _assert_avl(m._root)
        assert list(m) == sorted(ref)
        assert len(m) == len(ref)


def test_ordered_queries():
    m = AVLTreeMap()
    for k in [10, 20, 30, 40]:
        m[k] = k
    assert m.find_min() == (10, 10)
    assert m.find_max() == (40, 40)
    assert m.find_le(25) == (20, 20)
    assert m.find_lt(20) == (10, 10)
    assert m.find_ge(25) == (30, 30)
    assert m.find_gt(40) is None
    assert [k for k, _ in m.find_range(15, 40)] == [20, 30]


def test_logmap_range_example_from_readme():
    m = LogMap()
    m[datetime(2026, 1, 5)] = "login failed"
    m[datetime(2026, 1, 9)] = "disk warning"
    m[datetime(2026, 1, 12)] = "server restart"
    result = list(m.find_range(datetime(2026, 1, 6), datetime(2026, 1, 13)))
    assert [v for _, v in result] == ["disk warning", "server restart"]


def test_logmap_validates_types():
    m = LogMap()
    with pytest.raises(TypeError):
        m["2026-01-01"] = "texto"
    with pytest.raises(TypeError):
        m[datetime(2026, 1, 1)] = 123
