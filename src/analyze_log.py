import csv
from os.path import exists
from typing import Counter


def analyze_log(path_to_file):
    if path_to_file.endswith(".csv") is False:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    if not exists(path_to_file):
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
    with open(path_to_file, mode='r') as file:
        data = list(csv.DictReader(file, fieldnames=["name", "food", "day"]))
        maria = maria_foods(data)
        arnaldo = arnaldo_hamburgues(data)
        joao_r = joao_request(data)
        joao_d = joao_days(data)
        array = [maria, arnaldo, joao_r, joao_d]
        write_file(array)


def write_file(array):
    with open("data/mkt_campaign.txt", mode='w') as file:
        for rows in array:
            file.write(f"{rows}\n")


def maria_foods(data):
    food_of_maria = []
    for rows in data:
        if rows["name"] == "maria":
            food_of_maria.append(rows["food"])
    return Counter(food_of_maria).most_common(1)[0][0]


def arnaldo_hamburgues(data):
    count = 0
    for rows in data:
        if rows["name"] == "arnaldo":
            if rows["food"] == "hamburguer":
                count += 1

    return count


def joao_request(data):
    foods_in_general = set()
    foods_of_joao = set()
    for rows in data:
        foods_in_general.add(rows["food"])
        if rows["name"] == "joao":
            foods_of_joao.add(rows["food"])
    return foods_in_general.difference(foods_of_joao)


def joao_days(data):
    days_in_general = set()
    days_of_joao = set()
    for rows in data:
        days_in_general.add(rows["day"])
        if rows["name"] == "joao":
            days_of_joao.add(rows["day"])
    return days_in_general.difference(days_of_joao)
