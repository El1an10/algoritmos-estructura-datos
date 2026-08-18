class Empty(Exception):
  pass

class _Node:
  __slots__ = 'element', 'prev', 'next'
  def __init__(self, element, prev=None, next=None):
    self.element = element
    self.prev = prev
    self.next = next
  

class LinkedTreque(): # Se permite heredar de otra clase
  """La clase LinkeTreque representa una estructura de datos ficticia que consiste
  en una cola con tres lados para insertar y remover elementos que son: el inicio,
  el final y el medio. En el caso del medio, si el número de elementos es par
  se refiere al último elemento de la primera mitad de la cola, Ejemplos:

  [ 6, 7, 8, 1 ], el medio sería el número 7, si se inserta el número 2 al medio
  la cola queda así:
  [ 6, 7, 2, 8, 1 ] 
  y ahora si se inserta un 10 al medio el orden es el siguiente:
  [ 6, 7, 10, 2, 8, 1 ]
  si se elimina nuevamente el de enmedio:
  [ 6, 7, 2, 8, 1 ]

  Observe que según esta definición, el elemento de en medio varía si 
  se insertan o eliminan elementos al frente o al final de la cola. Por ejemplo,
  en el estado anterior el elemento de en medio es 2, pero si se elimina el 1,
  ahora el de en medio es 7.
  [ 6, 7, 2, 8 ]

  Se requiere que la complejidad de las operaciones de inserción y eliminación al 
  inicio y al final sea O(1), no así con la complejidad de la operación de
  inserción y eliminación al medio, que puede ser O(n) en el peor de los casos.
  """

  def __init__(self):
    self._head = None
    self._tail = None
    self._size = 0

  def __len__(self):
    return self._size
  
  def is_empty(self):
    return self._size == 0


  def first(self):
    """Devuelve (pero no elimina) el elemento en el frente del treque.

    Lanza una excepción Empty si el treque está vacío.
    """
    if self.is_empty():
      raise Empty("Treque is empty")
    return self._head.element
  

  def last(self):
    """Devuelve (pero no elimina) el elemento en la parte trasera del treque.

    Lanza una excepción Empty si el treque está vacío.
    """
    
    if self.is_empty():
      raise Empty("treque is empty")
    return self._tail.element
  

  def middle(self):
    """Devuelve (pero no elimina) el elemento en la parte media del treque.

    Lanza una excepción Empty si el treque está vacío.
    """
    if self.is_empty():
      raise Empty("Treque is empty")
    mid = (self._size - 1) // 2
    node = self._head
    for _ in range(mid):
      node = node.next
    return node.element


  def insert_first(self, e):
    """Agrega un elemento al frente del treque."""
    new = _Node(e, None, self._head)
    if self.is_empty():
      self._tail = new
    else: 
      self._head.prev = new
    self._head = new
    self._size += 1
  

  def insert_last(self, e):
    """Agrega un elemento a la parte trasera del treque."""
    new = _Node(e, self._tail, None)
    if self.is_empty():
      self._head = new
    else:
      self._tail.next = new
    self._tail = new
    self._size += 1
  


  def insert_middle(self, e):
    """Agrega un elemento a la parte media del treque."""

    if self.is_empty():
      self.insert_first(e)
      return
    
    mid = (self._size - 1) // 2
    node = self._head
    for _ in range(mid):
      node = node.next

    if self._size % 2 == 0:
        new = _Node(e, node, node.next)
        if node.next:
          node.next.prev = new
        else:
          self._tail = new
        node.next = new
    else:
        new = _Node(e, node.prev, node)
        if node.prev:
            node.prev.next = new
        else:
            self._head = new
        node.prev = new

    self._size += 1


  def delete_first(self):
    """Elimina y devuelve el elemento del frente del treque.

    Lanza una excepción Empty si el treque está vacío.
    """
    if self.is_empty():
      raise Empty("Treque is empty")
    value = self._head.element
    self._head = self._head.next
    if self._head is None:
      self._tail = None
    else: 
      self._head.prev = None
    self._size -= 1
    return value
  
       
  def delete_last(self):
    """Elimina y devuelve el elemento de la parte trasera del treque.

    Lanza una excepción Empty si el treque está vacío.
    """
    if self.is_empty():
      raise Empty("Treque is empty")
    value = self._tail.element
    self._tail = self._tail.prev
    if self._tail is None:
      self._head = None
    else:
      self._tail.next = None
    self._size -= 1
    return value


  def delete_middle(self):
    """Elimina y devuelve el elemento de la parte media del treque.

    Lanza una excepción Empty si el treque está vacío.
    """
    
    if self.is_empty():
      raise Empty("Treque is empty")
    mid = (self._size - 1) // 2
    node = self._head
    for _ in range(mid):
      node = node.next
    value = node.element
    if node.prev:
      node.prev.next = node.next
    else:
      self._head = node.next
    if node.next:
      node.next.prev = node.prev
    else:
      self._tail = node.prev
    self._size -= 1
    return value


  def items(self):
    """Devuelve un interable de los elementos en el treque.
    Desde el frente hasta la parte trasera.
    """
    node = self._head
    while node:
      yield node.element
      node = node.next



    
