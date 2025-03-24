# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def scanner(string):
    tokens = [ch for ch in string]
    print(tokens)
    i = -1
    while i < len(tokens) - 1:
        i += 1
        if tokens[i] == ' ' or tokens[i] == '\t' or tokens[i] == '\n':
            continue
        elif tokens[i] == '+':
            print("+ --> plus") 
        elif tokens[i] == '-':
            number = ""
            i += 1
            while tokens[i].isnumeric() or tokens[i] == ',': 
                number += tokens[i]
                i += 1
            if tokens[i] == 'e':
                number += tokens[i]
                i += 1
                while tokens[i].isnumeric(): 
                    number += tokens[i]
                    i += 1
                i -= 1
                number = '-' + number
                print(number, "--> scientific notation")
            elif tokens[i] == '(' or tokens[i].isnumeric():
                i -= 1
                print("- --> minus") 
            else:
                print("ERROR")
        elif tokens[i] == '*':
            print("* --> multiply") 
        elif tokens[i] == '/':
            print("/ --> division") 
        elif tokens[i] == '(':
            print("( --> left perenthesis") 
        elif tokens[i] == ')':
            print(") --> right parethesis")
        elif tokens[i].isnumeric():
            number = ""
            while tokens[i].isnumeric(): 
                number += tokens[i]
                i += 1
            print(number, "--> integer")
            i -= 1
        else:
            print("ERROR")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scanner("23+786-(87)/(-8,59e54)")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
