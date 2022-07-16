DATA = [
    {
        "name": "Facundo",
        "age": 72,
        "organization": "Platzi",
        "position": "Technical Coach",
        "language": "python",
    },
    {
        "name": "Luisana",
        "age": 33,
        "organization": "Globant",
        "position": "UX Designer",
        "language": "javascript",
    },
    {
        "name": "Héctor",
        "age": 19,
        "organization": "Platzi",
        "position": "Associate",
        "language": "ruby",
    },
    {
        "name": "Gabriel",
        "age": 20,
        "organization": "Platzi",
        "position": "Associate",
        "language": "javascript",
    },
    {
        "name": "Isabella",
        "age": 30,
        "organization": "Platzi",
        "position": "QA Manager",
        "language": "java",
    },
    {
        "name": "Karo",
        "age": 23,
        "organization": "Everis",
        "position": "Backend Developer",
        "language": "python",
    },
    {
        "name": "Ariel",
        "age": 32,
        "organization": "Rappi",
        "position": "Support",
        "language": "",
    },
    {
        "name": "Juan",
        "age": 17,
        "organization": "",
        "position": "Student",
        "language": "go",
    },
    {
        "name": "Pablo",
        "age": 32,
        "organization": "Master",
        "position": "Human Resources Manager",
        "language": "python",
    },
    {
        "name": "Lorena",
        "age": 56,
        "organization": "Python Organization",
        "position": "Language Maker",
        "language": "python",
    },
]


def run():
    # python_workers = [
    #     worker["name"] for worker in DATA if worker["language"] == "python"
    # ]
    # print("Python Devs:")
    # for worker_name in python_workers:
    #     print(worker_name)

    # * RETO
    # python_workers = list(filter(lambda worker: worker["language"] == "python", DATA))
    # print("Platzi Workers:")
    # for worker in python_workers:
    #     print(worker["name"])

    # platzi_workers = [
    #     worker["name"] for worker in DATA if worker["organization"] == "Platzi"
    # ]
    # print("Platzi Workers:")
    # for worker_name in platzi_workers:
    #     print(worker_name)

    # * RETO
    # platzi_workers = list(
    #     filter(lambda worker: worker["organization"] == "Platzi", DATA)
    # )
    # for worker in platzi_workers:
    #     print(worker["name"])

    # adult_workers = list(filter(lambda worker: worker["age"] >= 18, DATA))
    # adult_workers = list(map(lambda worker: worker["name"], adult_workers))
    # print("Adults Workers:")
    # for worker_name in adult_workers:
    #     print(worker_name)

    # * RETO
    # adult_workers = [worker["name"] for worker in DATA if worker["age"] >= 18]
    # for worker_name in adult_workers:
    #     print(worker_name)

    # old_workers = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    # # * A partir de python 3.9 insertaron un nuevo operador llamado pipe (|).
    # # * Este operador permite unir un diccionario con otro
    # for worker in old_workers:
    #     print(worker)

    old_workers = [worker | {"old": worker["age"] > 70} for worker in DATA]
    for worker in old_workers:
        print(worker)


if __name__ == "__main__":
    run()
