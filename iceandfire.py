import requests
import requests_cache

requests_cache.install_cache('api_of_ice_and_fire')

BASE_URL = 'https://anapioficeandfire.com/api'


class Character(object):

    def __init__(self, dictionary):
        ...
        for k, v in dictionary.items():
            setattr(self, k, v)

    def __contains__(self, param1):
        return param1 in self.__dict__.keys()


class House(object):

    def __init__(self, dictionary):
        ...
        for k, v in dictionary.items():
            setattr(self, k, v)

    def __contains__(self, param1):
        return param1 in self.__dict__.keys()


class Books(object):

    def __init__(self, dictionary):
        ...
        for k, v in dictionary.items():
            setattr(self, k, v)

    def __contains__(self, param1):
        return param1 in self.__dict__.keys()


def get_house(name: str):
    json = requests.get(f"{BASE_URL}/houses/?name={'+'.join(name.split())}").json()
    if not json:
        raise ValueError('Cannot find House on anapioficeandfire')
    return House(json[0])


def get_character(name: str):
    json = requests.get(f"{BASE_URL}/characters/?name={'+'.join(name.split())}").json()
    if not json:
        raise ValueError('Cannot find Character on anapioficeandfire')
    return Character(json[0])


def get_book(name: str):
    json = requests.get(f"{BASE_URL}/books/?name={'+'.join(name.split())}").json()
    if not json:
        raise ValueError('Cannot find Character on anapioficeandfire')
    return Books(json[0])
