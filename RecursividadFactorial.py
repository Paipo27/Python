def factorial(n):
    if n>1 :
        resultado=n*factorial(n-1)
    else:
        resultado=1
    return resultado

for i in range(1):
    print(factorial(5))


