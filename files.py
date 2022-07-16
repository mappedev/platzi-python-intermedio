def read():
    numbers = []
    # file = open("./files/numbers.txt", "r", encoding="utf-8")
    # for line in file:
    #     numbers.append(int(line))
    # file.close()

    # * Forma ideal:
    """
    With se usa para trabajr con recursos no administrados cómo archivos (file streams).
    Este permite asegurarse de que un recurso se "limpie"
    cuando el código que lo usa termina de ejecutarse, incluso si se lanzan excepciones.
    Proporciona 'azúcar sintáctico' para try/finallybloques.
    """
    with open("./files/numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            numbers.append(int(line))

    # * el parámetro encoding indica cuál será la codificación a usar
    # * utf-8 acepta acentos y caracteres especiales

    print(numbers)


def write():
    names = ["Mario", "Jesús", "Jose", "Carlos", "Peña"]

    with open("./files/names.txt", "w", encoding="utf-8") as file:
        for name in names:
            file.write(name + "\n")


def append():
    name = "Carla"

    with open("./files/names.txt", "a", encoding="utf-8") as file:
        file.write(name + "\n")


def run():
    append()


if __name__ == "__main__":
    run()
