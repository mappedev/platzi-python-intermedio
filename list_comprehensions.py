def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    """
    [element for element in iterable if condition]
    * element: cada uno de los elementos a poner en la nueva lista.
    * for: ciclo a partir del cuál se extraen los elementos de cualquier iterable.
    * condition: condición opcional para filtrar los elementos del ciclo.
    De forma general se lee así: para cada elemento del iterable, guardame el elemento si la condición se cumple.
    El ejemplo se lee así: para cada elemento de una lista desde el 1 al 100, guardame los elementos elevados al cuadrado si el elemento no es divisible entre 3
    """
    print(squares)

    # list = [i for i in range(1, 100000) if i % 36 == 0]
    list = [i for i in range(1, 100000) if i % 36 == 0]
    print(list)


if __name__ == "__main__":
    run()
