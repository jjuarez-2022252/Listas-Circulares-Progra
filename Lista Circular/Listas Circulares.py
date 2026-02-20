class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = Nodo(dato)

        if not self.head:
            self.head = nuevo
            nuevo.siguiente = self.head
            return

        actual = self.head
        while actual.siguiente != self.head:
            actual = actual.siguiente

        actual.siguiente = nuevo
        nuevo.siguiente = self.head

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        actual = self.head
        while True:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
            if actual == self.head:
                break
        print("(vuelve al inicio)")

    def buscar(self, valor):
        if not self.head:
            return "Lista vacía"

        actual = self.head
        posicion = 0

        while True:
            if actual.dato == valor:
                return f"Valor {valor} encontrado en posición {posicion}"

            actual = actual.siguiente
            posicion += 1

            if actual == self.head:
                break

        return f"Valor {valor} no encontrado"

    def eliminar(self, valor):
        if not self.head:
            return "Lista vacía"

        actual = self.head
        anterior = None

        # Caso: eliminar head
        if actual.dato == valor:
            if actual.siguiente == self.head:
                self.head = None
                return f"Valor {valor} eliminado"

            ultimo = self.head
            while ultimo.siguiente != self.head:
                ultimo = ultimo.siguiente

            self.head = actual.siguiente
            ultimo.siguiente = self.head
            return f"Valor {valor} eliminado"

        # Caso general
        while True:
            anterior = actual
            actual = actual.siguiente

            if actual.dato == valor:
                anterior.siguiente = actual.siguiente
                return f"Valor {valor} eliminado"

            if actual == self.head:
                break

        return f"Valor {valor} no encontrado"


# ========================
# MENÚ INTERACTIVO
# ========================

lista = ListaCircular()

while True:
    print("\n--- MENÚ ---")
    print("1. Insertar")
    print("2. Eliminar")
    print("3. Buscar")
    print("4. Mostrar")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            numero = int(input("Ingrese número a insertar: "))
            lista.insertar_final(numero)
            print("Número insertado correctamente")
        except ValueError:
            print("Ingrese un número válido")

    elif opcion == "2":
        try:
            numero = int(input("Ingrese número a eliminar: "))
            print(lista.eliminar(numero))
        except ValueError:
            print("Ingrese un número válido")

    elif opcion == "3":
        try:
            numero = int(input("Ingrese número a buscar: "))
            print(lista.buscar(numero))
        except ValueError:
            print("Ingrese un número válido")

    elif opcion == "4":
        lista.mostrar()

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida")