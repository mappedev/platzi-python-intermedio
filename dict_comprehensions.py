def run():
    # dict = {}
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         dict[i] = i**3

    # dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # """
    # [key:value for element in iterable if condition]
    # * key:value: cada una de las llaves y valores a poner en el nuevo objeto.
    # * for: ciclo a partir del cuál se extraen los elementos de cualquier iterable.
    # * condition: condición opcional para filtrar los elementos del ciclo.
    # De forma general se lee así: para cada elemento del iterable, guardame dicha llave y valor del elemento si la condición se cumple.
    # El ejemplo se lee así: para cada elemento de una lista desde el 1 al 100, guardame el elemento cómo llave y el elemento elevado a la 3 cómo valor si el elemento no es divisible entre 3
    # """
    # print(dict)

    new_dict = {i: round(i**0.5, 2) for i in range(1, 1001)}
    print(new_dict)


if __name__ == "__main__":
    run()
