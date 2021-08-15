class estudiante:
  def __init__ (self, carne, nombre, edad, direccion, telefono, email, carrera, puesto):
    self.carne = carne
    self.nombre = nombre
    self.edad = edad
    self.direccion = direccion
    self.telefono = telefono
    self.email = email
    self.carrera = carrera
    self.puesto = puesto

class nodo:
  def __init__ (self, estudiante=None, siguiente=None):
    self.estudiante = estudiante
    self.siguiente = siguiente


class lista_enlazada:
  def __init__(self):
    self.primero = None

  def insertar(self, estudiante):
    if self.primero is None:
      self.primero = nodo(estudiante=estudiante)
      return
    actual = self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo(estudiante=estudiante)

  def recorrer(self):
    actual = self.primero
    while actual != None:
      print("carne", actual.estudiante.carne, "nombre:", actual.estudiante.nombre, "email:", actual.estudiante.email,
            "->")
      actual = actual.siguiente

  def eliminar(self, carne):
    actual = self.primero
    anterior = None

    while actual and actual.estudiante.carne != carne:
      anterior = actual
      actual = actual.siguiente

    if anterior is None:
      self.primero = actual.siguiente
      actual.siguiente = None
    elif actual:
      anterior.siguiente = actual.siguiente
      actual.siguiente = None

  def buscar(self, carne):
    actual = self.primero

    while actual != None:
      if actual and actual.estudiante.carne == carne:
        print(f"Carne {actual.estudiante.carne} Nombre: {actual.estudiante.nombre} Correo{actual.estudiante.carne} Professión: {actual.estudiante.carrera}")
      actual = actual.siguiente




e1 = estudiante(202010312,"Gerson ortiz","20", "Guatemala",20202010312,"a@gmail.com","Sistemas","Programador Jr")
e2 = estudiante(202110312,"Karen ortiz","21", "Guatemala",54730080,"b@gmail.com","Sistemas","Programador Jr")
e3 = estudiante(202210312,"Luis ortiz","22", "Guatemala",52218573,"c@gmail.com","Sistemas","Programador Jr")


lista_e = lista_enlazada()
lista_e.insertar(e1)
lista_e.insertar(e2)
lista_e.insertar(e3)

lista_e.recorrer()

lista_e.eliminar(202110312)
lista_e.recorrer()

lista_e.buscar(202210312)