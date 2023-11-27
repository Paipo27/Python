from ClassGrafo import Grafo

g = Grafo()
for i in range(6):
    g.agregarVertice(i)
g.listaVertices
g.agregarArista(0, 1, 5)
g.agregarArista(0, 5, 2)
g.agregarArista(1, 2, 4)
g.agregarArista(2, 3, 9)
g.agregarArista(3, 4, 7)
g.agregarArista(3, 5, 3)
g.agregarArista(4, 0, 1)
g.agregarArista(5, 4, 8)
g.agregarArista(5, 2, 1)
for v in g:  # type: ignore
    for w in v.obtenerConexiones():
        print("( %s , %s )" % (v.obtenerId(), w.obtenerId()))