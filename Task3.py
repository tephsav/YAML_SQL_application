# Task 3

import sys
import yaml
import mysql.connector
from mysql.connector import Error, OperationalError, IntegrityError


def read_yaml(path):
    try:
        with open(path, 'r') as f:
            data = yaml.load(f, Loader=yaml.Loader)
        return data
    except FileNotFoundError as error:
        print(error)
        sys.exit(0)


def get_list_games(dict_games):
    list_games = []
    list_dict_games = dict_games.get("games")

    for game_structure in list_dict_games:
        dict_game = []
        dict_game.extend(game_structure.values())
        list_games.append(dict_game)

    return list_games


def get_list_toys(dict_toys):
    list_toys = []
    list_dict_toys = dict_toys.get("toys")

    for toy_structure in list_dict_toys:
        dict_toy = []
        dict_toy.extend(toy_structure.values())
        list_toys.append(dict_toy)

    return list_toys


if __name__ == '__main__':
    games = read_yaml('a.yaml')
    toys = read_yaml('b.yaml')
    toys_note = read_yaml('c.yaml')

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(host='localhost', database='toys_games', charset='utf8', user='root',
                                             password='root')
        cursor = connection.cursor()

        for game in get_list_games(games):  # Task 3.a
            query_insert_games = f"INSERT INTO games(game_id, name, date) VALUES ('{game[0]}','{game[1]}','{game[2]}')"
            cursor.execute(query_insert_games)

        for toy in get_list_toys(toys):  # Task 3.b
            query_insert_toys = f"INSERT INTO toys(toy_id, name, status, status_updated) VALUES ('{toy[0]}','{toy[1]}','{toy[2]}','{toy[3]}') "
            cursor.execute(query_insert_toys)

            for game in toy[4]:
                query_insert_toy_games = f"INSERT INTO toys_games(game_id, toy_id, note) VALUES ('{game['id']}','{toy[0]}','{game['note']}')"
                cursor.execute(query_insert_toy_games)

        for toy in get_list_toys(toys_note):  # Task 3.c
            for note in toy[1]:
                query_insert_toys_note = f"INSERT INTO toys_repair(toy_id, issue_description) VALUES ('{toy[0]}','{note}')"
                cursor.execute(query_insert_toys_note)

    except (OperationalError, IntegrityError) as e:
        print(e)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
