def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Mario", "lastname": "Peña"}

    super_list = [
        {"firstname": "Mario", "lastname": "Peña"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martínez"},
        {"firstname": "José", "lastname": "García"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "float_nums": [1.1, 2.2, 3.3, 4.4, 5.5],
    }

    for i in super_list:
        print(i)

    for key, value in super_dict.items():
        print(key + ":", value)


if __name__ == "__main__":
    run()
