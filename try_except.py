def divisors(num: int):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    try:
        num = int(input("Enter a positive number: "))

        if num < 0:
            raise ValueError
        else:
            print(divisors(num))
            print("Termino el programa.")
    except ValueError:
        print("Invalid number...")


if __name__ == "__main__":
    run()
