from ColaDoble import ColaDoble1

p=ColaDoble1()

print(p.estaVacia())
p.agregarFinal(4)
p.agregarFinal('perro')
p.agregarFrente("gato")
p.agregarFrente(True)
print(p.inspeccionarFinal())
print(p.inspeccionarFrente())
p.agregarFinal(8.4)
print(p.tamano())
print(p.estaVacia())
p.agregarFinal(8.4)
p.removerfinal()
p.removerFrente
