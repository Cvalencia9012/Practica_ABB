class Incidente:
    def __init__(self, idIncidente, direccionIP, tipoAtaque, nivelRiesgo, estado):
        self.idIncidente = idIncidente
        self.direccionIP = direccionIP
        self.tipoAtaque = tipoAtaque
        self.nivelRiesgo = nivelRiesgo
        self.estado = estado

    def __str__(self):
        return (f"ID: {self.idIncidente} | IP: {self.direccionIP} | "
                f"Ataque: {self.tipoAtaque} | Riesgo: {self.nivelRiesgo} | "
                f"Estado: {self.estado}")


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijoIzquierdo = None
        self.hijoDerecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, incidente):
        nuevo = Nodo(incidente)

        if self.raiz is None:
            self.raiz = nuevo
            return True

        actual = self.raiz
        while True:
            if incidente.idIncidente == actual.dato.idIncidente:
                print(f"El incidente con ID {incidente.idIncidente} ya existe.")
                return False

            if incidente.idIncidente < actual.dato.idIncidente:
                if actual.hijoIzquierdo is None:
                    actual.hijoIzquierdo = nuevo
                    return True
                actual = actual.hijoIzquierdo
            else:
                if actual.hijoDerecho is None:
                    actual.hijoDerecho = nuevo
                    return True
                actual = actual.hijoDerecho

    def buscar(self, idIncidente):
        actual = self.raiz
        while actual is not None:
            if idIncidente == actual.dato.idIncidente:
                return actual.dato
            elif idIncidente < actual.dato.idIncidente:
                actual = actual.hijoIzquierdo
            else:
                actual = actual.hijoDerecho
        return None

    def recorridoInorden(self):
        def recorrer(nodo):
            if nodo is not None:
                recorrer(nodo.hijoIzquierdo)
                print(nodo.dato)
                recorrer(nodo.hijoDerecho)
        recorrer(self.raiz)

    def recorridoPreorden(self):
        def recorrer(nodo):
            if nodo is not None:
                print(nodo.dato)
                recorrer(nodo.hijoIzquierdo)
                recorrer(nodo.hijoDerecho)
        recorrer(self.raiz)

    def recorridoPostorden(self):
        def recorrer(nodo):
            if nodo is not None:
                recorrer(nodo.hijoIzquierdo)
                recorrer(nodo.hijoDerecho)
                print(nodo.dato)
        recorrer(self.raiz)

    def imprimirArbol(self):
        if self.raiz is None:
            print("El arbol esta vacio.")
            return

        def imprimir(nodo, prefijo="", etiqueta="Raiz: "):
            if nodo is None:
                return
            print(prefijo + etiqueta + str(nodo.dato.idIncidente))
            imprimir(nodo.hijoIzquierdo, prefijo + "    ", "Izq: ")
            imprimir(nodo.hijoDerecho, prefijo + "    ", "Der: ")

        imprimir(self.raiz)

    def contarNodos(self):
        def contar(nodo):
            if nodo is None:
                return 0
            return 1 + contar(nodo.hijoIzquierdo) + contar(nodo.hijoDerecho)
        return contar(self.raiz)

    def obtenerMenor(self):
        actual = self.raiz
        if actual is None:
            return None
        while actual.hijoIzquierdo is not None:
            actual = actual.hijoIzquierdo
        return actual.dato

    def obtenerMayor(self):
        actual = self.raiz
        if actual is None:
            return None
        while actual.hijoDerecho is not None:
            actual = actual.hijoDerecho
        return actual.dato

    def buscarPorNivelRiesgo(self, nivel):
        encontrados = []

        def recorrer(nodo):
            if nodo is not None:
                recorrer(nodo.hijoIzquierdo)
                if nodo.dato.nivelRiesgo.lower() == nivel.lower():
                    encontrados.append(nodo.dato)
                recorrer(nodo.hijoDerecho)

        recorrer(self.raiz)
        for incidente in encontrados:
            print(incidente)
        return encontrados


def main():
    arbol = ArbolBinarioBusqueda()

    incidentes = [
        Incidente(150, "192.168.1.25", "Fuerza bruta", "Alto", "En investigacion"),
        Incidente(100, "192.168.1.30", "Malware", "Crítico", "Pendiente"),
        Incidente(200, "10.0.0.15", "Escaneo de puertos", "Medio", "Resuelto"),
        Incidente(75, "192.168.1.45", "Phishing", "Alto", "En investigacion"),
        Incidente(125, "10.0.0.20", "Acceso no autorizado", "Crítico", "Pendiente"),
        Incidente(175, "192.168.1.80", "Ransomware", "Crítico", "En investigacion"),
        Incidente(250, "10.0.0.50", "Denegación de servicio", "Alto", "Pendiente")
    ]

    for incidente in incidentes:
        arbol.insertar(incidente)

    print("\n=== ARBOL BINARIO ===")
    arbol.imprimirArbol()

    # Actividad 4
    print("\n=== RECORRIDO INORDEN ===")
    arbol.recorridoInorden()
    print("\n=== RECORRIDO PREORDEN ===")
    arbol.recorridoPreorden()
    print("\n=== RECORRIDO POSTORDEN ===")
    arbol.recorridoPostorden()

    # Actividad 5
    print("\n=== BUSCAR ID 125 ===")
    encontrado = arbol.buscar(125)
    print(encontrado if encontrado is not None else "Incidente no encontrado")

    # Actividad 6
    print("\n=== BUSCAR ID 300 ===")
    encontrado = arbol.buscar(300)
    print(encontrado if encontrado is not None else "El incidente con ID 300 no fue encontrado")

    # Actividad 7
    print("\n=== CONTAR INCIDENTES ===")
    print("Cantidad de incidentes:", arbol.contarNodos())

    # Actividad 8
    print("\n=== IDENTIFICADORES EXTREMOS ===")
    menor = arbol.obtenerMenor()
    mayor = arbol.obtenerMayor()
    print("Menor:", menor if menor is not None else "Sin incidentes")
    print("Mayor:", mayor if mayor is not None else "Sin incidentes")

    # Actividad 9
    print("\n=== PRUEBA DE ID DUPLICADO ===")
    arbol.insertar(Incidente(150, "10.0.0.99", "Prueba", "Bajo", "Pendiente"))

    # Actividad 10
    print("\n=== INCIDENTES CON RIESGO CRITICO ===")
    criticos = arbol.buscarPorNivelRiesgo("Crítico")
    print("Total de incidentes críticos:", len(criticos))
    print("IDs:", [incidente.idIncidente for incidente in criticos])


if __name__ == "__main__":
    main()
