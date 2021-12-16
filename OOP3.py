#Dekoratory w pythonie
#Dekoratory zmieniają zachowanie funkcji
#Dekoratory są to inne funkcje
#Robimy to po to aby zrobić różne warianty funkcji
#Dekorator pozwoli nam wpłynąć na dynamiczne zachowanie funkcji

def my_decorator(fn):
    def wrapper():
        print("Początkowe odliczanie")
        fn()
        print("Koniec odliczania")
    return wrapper

def get_5_values():
    for v in range(1,6):
        print(v)

get_5_values_decorator = my_decorator(get_5_values)

get_5_values_decorator()