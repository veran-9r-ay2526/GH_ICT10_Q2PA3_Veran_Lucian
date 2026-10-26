# Working with Dictionaries
from pyscript import display, document


def game_details(e):
    document.getElementById('resulta').innerHtml = " "
    favorite_game = document.getElementById('dict').value.lower().strip()

    # Specifying Dictionaries
    game_devs = {
        'minecraft': "Notch",
        'fnaf': "Scott Cawthon",
        'roblox': "David Baszucki",
        'codm': "TiMi Studio"
    }

    game_check = favorite_game in game_devs

    # Message to be displayed
    display_message = ('Sorry, your game is not in the list!', f'{game_devs.get([favorite_game])}')

    display(display_message[game_check], target="resulta")

    # Adding New Elements
    game_devs['genshin impact'] = 'Hoyoverse'
    display(game_devs, target="resulta")

    list_with_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
    tuple_with_strings = ("ab", "cd", "ef")
    list_with_strings = ["ax", 'by', 'cz']

    display(dict(list_with_tuples), target="resulta")
    display(dict(tuple_with_strings), target="resulta")
    display(dict(list_with_strings), target="resulta")

    keywords = ['say', 'jm', 'jay', 'mace']
    values = ['esguerra', 'piansay', 'estrada', 'panela']

    students_nicknames = dict(zip(keywords, values))

    display(students_nicknames, target="resulta")

    # Replacing and Deleting elements
    philadelphia = {
        'c':'Joel Embiid',
        'pf':'Lebron James',
        'sf':'Jaylen Brown',
        'sg':'VJ Edgecomb',
        'pg':'Tyrese Maxey'
    }

    philadelphia['pg'] = 'Stephen Curry'
    del philadelphia['sg']
    display(philadelphia, target="resulta")

    dict1 = {'x': 1, 'y': 2, 'z':3}
    dict2 = {'a': 4, 'b': 5, 'c': 6}

    # combining and multiplying
    display(dict1|dict2, target="resulta")
    merged_dictionary = {**dict1, **dict2}
    display(merged_dictionary, target="resulta")

    # counting
    display(len(merged_dictionary), target="resulta")

    ai = {
        'tony stark': "creator",
        'JARVIS': "AI1",
        'FRIDAY': "AI2",
        'Edith': "AI3",
        'Vision': "AI4"
    }

    # checking if in dictionary
    display('Vision' in ai, target="resulta")
    display(ai.get('JARVIS'), target="resulta")
    display(ai.keys(), target="resulta")
    display(ai.values(), target="resulta")
    display(ai['tony stark'], target="resulta")
