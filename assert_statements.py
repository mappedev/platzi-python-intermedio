def divisors(num: int):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    num = input("Enter a positive number: ")

    assert num.isnumeric(), "Only positive numbers..."
    print(divisors(int(num)))
    print("Termino el programa.")

    """
    BUENAS PRÁCTICAS:
    se recomienda usar los asserts solo para el testing...
    No mezclar assert y try catch
    """


if __name__ == "__main__":
    run()
