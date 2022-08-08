import json


def PrintData(data):
    with open(data, 'r') as file:
        BD = json.load(file)
        for i in BD:
            for key, value in i.items():
                print("{}: {}".format(key, value))
            print('\n')