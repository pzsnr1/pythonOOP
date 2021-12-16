def my_decorator(fn):
    def wrapper():
        print("Początkowe odliczanie")
        fn()
        print("Koniec odliczania")
    return wrapper

@my_decorator
def get_5_values():
    for v in range(1,6):
        print(v)

get_5_values()