
contador=0
def Fibonacci(n):
    global contador
    contador+=1
    if n>=2:
        resultado=Fibonacci(n-1) + Fibonacci(n-2)
    elif n==1:
        resultado=1
    else:
        resultado=0
    return resultado

print(Fibonacci(5))
print("El numero de llamados es :",contador)


