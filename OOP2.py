#Funkcja jako obiekt pierwszej klasy,
#Funkcje możemy w pythonie traktować jako wartości

def add(a,b):
    return a + b

def muliply(a,b):
    return a * b

def apply(fn,a,b):
    return fn(a,b)

oblicz1 = apply(add, 4, 10)
oblicz2 = apply(muliply, 4, 10)

print(oblicz1, " | ",oblicz2)