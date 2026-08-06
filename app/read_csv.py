import csv


def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)  # une los elementos de dos listas en tuplas

            country_dict = dict(
                iterable
            )  # convierte las tuplas en diccionarios y los imprime

            # Segunda forma con comprensión de diccionarios
            # country_dict = {key: value for key, value in iterable}
            data.append(country_dict)  # Agrega la fila clave  valor a la lista
        return data


if __name__ == "__main__":
    data = read_csv("./app/world_population.csv")
    print(data)
