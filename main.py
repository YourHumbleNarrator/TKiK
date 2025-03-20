# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


tokens = {
    "plus": "+",
    "minus": "-",
    "multiply": "*",
    "divide": "/",
    "left_parenthesis": "(",
    "right_left_parenthesis": ")"
}


tokens2 = {
    "+": "plus",
    "_": "minus",
    "*": "multiply",
    "/": "divide",
    "(": "left_parenthesis",
    ")": "right_left_parenthesis",
    "[0-9]+": "integer"
}

tokens3 = [
    ('+', 'plus'),
    ('-', 'minus'),
    ('*', 'multiply'),
    ('/', 'divide'),
    ('(', 'left_parenthesis'),
    (')', 'right_parenthesis'),
    ('[0-9]', 'integer'),
]


tokens4 = {
    "+": "plus",
    "-": "minus",
    "*": "multiply",
    "/": "divide",
    "(": "left_parenthesis",
    ")": "right_parenthesis",
    "0": "digit",
    "1": "digit",
    "2": "digit",
    "3": "digit",
    "4": "digit",
    "5": "digit",
    "6": "digit",
    "7": "digit",
    "8": "digit",
    "9": "digit"
}


def scanner(string):
    for i in range(len(string)):
        if string[i] == " " or string[i] == "\t" or string[i] == "\n":
            continue
        elif string[i] in tokens4.keys():
            integer = ""
            while tokens4[string[i]] == "digit":
                integer += string[i]
                print("vefore ", integer, i)
                i += 1
                print("after ", integer, i)
            if integer != "":

                print(integer)
            else:
                print(tokens4[string[i]], i)
        else:
            print("Cannot recognize ", string[i], " as a token. The string is invalid. The column of the wrong char: ", i)


def scanner2(string):
    tokens = [ch for ch in string]
    print(tokens)
    column = 0
    while len(tokens) > column:
        next_symbol = tokens[column]
        if next_symbol == " " or next_symbol == "\t" or next_symbol == "\n":
            continue
        elif next_symbol in tokens4.keys():
            if tokens4[next_symbol] != "digit":
                print(next_symbol, "==>", tokens4[next_symbol])
            else:
                integer = ""
                while tokens4[next_symbol] == "digit":
                    integer += next_symbol
                    column += 1
                    next_symbol = tokens[column]
                print(integer, "==>", "integer")
                column -= 1
        else:
            print("Cannot recognize ", next_symbol, " as a token. The string is invalid.",
                  "The column of the wrong char: ", column)
        column += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scanner2("23+786-(87)")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
