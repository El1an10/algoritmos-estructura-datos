from datetime import datetime


class AVLTreeMap:
    """Implementación básica de un mapa ordenado usando árbol AVL."""

    class _Node:
        __slots__ = "key", "value", "left", "right", "parent", "height"

        def __init__(self, key, value, parent=None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.parent = parent
            self.height = 1

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    # ------------- utilidades internas -------------
    def _update_height(self, node):
        lh = node.left.height if node.left is not None else 0
        rh = node.right.height if node.right is not None else 0
        node.height = max(lh, rh) + 1

    def _balance_factor(self, node):
        lh = node.left.height if node.left is not None else 0
        rh = node.right.height if node.right is not None else 0
        return lh - rh

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self._root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        self._update_height(x)
        self._update_height(y)
        return y

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self._root = x
        elif y is y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x
        self._update_height(y)
        self._update_height(x)
        return x

    def _rebalance(self, node):
        while node is not None:
            self._update_height(node)
            bf = self._balance_factor(node)

            if bf > 1:
                if self._balance_factor(node.left) < 0:
                    self._rotate_left(node.left)
                node = self._rotate_right(node)
            elif bf < -1:
                if self._balance_factor(node.right) > 0:
                    self._rotate_right(node.right)
                node = self._rotate_left(node)
            else:
                node = node.parent

    def _subtree_search(self, node, key):
        """Devuelve el nodo donde está key o el último visitado en la búsqueda."""
        while node is not None and node.key != key:
            if key < node.key:
                if node.left is not None:
                    node = node.left
                else:
                    break
            else:
                if node.right is not None:
                    node = node.right
                else:
                    break
        return node

    def _subtree_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def _subtree_max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def _transplant(self, u, v):
        if u.parent is None:
            self._root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    # ------------- API de mapa -------------
    def __getitem__(self, key):
        node = self._subtree_search(self._root, key) if self._root is not None else None
        if node is None or node.key != key:
            raise KeyError("Key Error: " + repr(key))
        return node.value

    def __setitem__(self, key, value):
        if self._root is None:
            self._root = self._Node(key, value)
            self._size = 1
            return

        node = self._subtree_search(self._root, key)
        if node.key == key:
            node.value = value
            return

        new = self._Node(key, value, parent=node)
        if key < node.key:
            node.left = new
        else:
            node.right = new

        self._size += 1
        self._rebalance(node)

    def __delitem__(self, key):
        if self._root is None:
            raise KeyError("Key Error: " + repr(key))
        node = self._subtree_search(self._root, key)
        if node is None or node.key != key:
            raise KeyError("Key Error: " + repr(key))
        self._delete_node(node)

    def _delete_node(self, node):
        rebalance_start = node.parent

        if node.left is None:
            self._transplant(node, node.right)
        elif node.right is None:
            self._transplant(node, node.left)
        else:
            y = self._subtree_min(node.right)
            if y.parent is not node:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            rebalance_start = y

        self._size -= 1
        if rebalance_start is not None:
            self._rebalance(rebalance_start)

    # ------------- consultas ordenadas -------------
    def find_min(self):
        if self._root is None:
            return None
        n = self._subtree_min(self._root)
        return (n.key, n.value)

    def find_max(self):
        if self._root is None:
            return None
        n = self._subtree_max(self._root)
        return (n.key, n.value)

    def _find_le_node(self, key):
        node = self._root
        res = None
        while node is not None:
            if key < node.key:
                node = node.left
            else:
                res = node
                node = node.right
        return res

    def _find_lt_node(self, key):
        node = self._root
        res = None
        while node is not None:
            if key <= node.key:
                node = node.left
            else:
                res = node
                node = node.right
        return res

    def _find_ge_node(self, key):
        node = self._root
        res = None
        while node is not None:
            if key > node.key:
                node = node.right
            else:
                res = node
                node = node.left
        return res

    def _find_gt_node(self, key):
        node = self._root
        res = None
        while node is not None:
            if key >= node.key:
                node = node.right
            else:
                res = node
                node = node.left
        return res

    def find_le(self, key):
        node = self._find_le_node(key)
        return (node.key, node.value) if node is not None else None

    def find_lt(self, key):
        node = self._find_lt_node(key)
        return (node.key, node.value) if node is not None else None

    def find_ge(self, key):
        node = self._find_ge_node(key)
        return (node.key, node.value) if node is not None else None

    def find_gt(self, key):
        node = self._find_gt_node(key)
        return (node.key, node.value) if node is not None else None

    def _inorder_from(self, node, start_key, stop_key):
        if node is None:
            return
        if start_key is None or node.key >= start_key:
            # lado izquierdo
            for kv in self._inorder_from(node.left, start_key, stop_key):
                yield kv
        if (start_key is None or node.key >= start_key) and (
            stop_key is None or node.key < stop_key
        ):
            yield (node.key, node.value)
        if stop_key is None or node.key < stop_key:
            # lado derecho
            for kv in self._inorder_from(node.right, start_key, stop_key):
                yield kv

    def find_range(self, start, stop):
        """Itera sobre las entradas con start <= key < stop."""
        return self._inorder_from(self._root, start, stop)

    # iterador in-order de todas las claves, por si lo necesitas
    def __iter__(self):
        stack = []
        node = self._root
        while stack or node is not None:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.key
                node = node.right

    def items(self):
        for k in self:
            yield (k, self[k])


class LogMap(AVLTreeMap):
    """Mapa de logs basado en árbol AVL.

    Restricciones:
    - claves: datetime
    - valores: string
    """

    # ------------- validaciones de tipos -------------
    def _validate_key(self, k):
        if not isinstance(k, datetime):
            raise TypeError("Las claves de LogMap deben ser de tipo datetime")

    def _validate_value(self, v):
        if not isinstance(v, str):
            raise TypeError("Los valores de LogMap deben ser de tipo string")

    # ------------- métodos sobrescritos -------------
    def __setitem__(self, k, v):
        self._validate_key(k)
        self._validate_value(v)
        super().__setitem__(k, v)

    def __getitem__(self, k):
        self._validate_key(k)
        return super().__getitem__(k)

    def __delitem__(self, k):
        self._validate_key(k)
        super().__delitem__(k)

    def find_min(self):
        return super().find_min()

    def find_max(self):
        return super().find_max()

    def find_le(self, k):
        self._validate_key(k)
        return super().find_le(k)

    def find_lt(self, k):
        self._validate_key(k)
        return super().find_lt(k)

    def find_ge(self, k):
        self._validate_key(k)
        return super().find_ge(k)

    def find_gt(self, k):
        self._validate_key(k)
        return super().find_gt(k)

    def find_range(self, start, stop):
        if start is not None:
            self._validate_key(start)
        if stop is not None:
            self._validate_key(stop)
        return super().find_range(start, stop)
