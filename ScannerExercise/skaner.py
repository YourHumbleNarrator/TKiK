# This is a sample Python script.
import sys


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def scanner(string):
    tokens = [ch for ch in string]
    result = []
    print(tokens)
    i = -1
    while i < len(tokens) - 1:
        i += 1
        if tokens[i] in [' ', '\t', '\n']:
            continue
        elif tokens[i] == '+':
            result.append((tokens[i], 'plus', 'OPERATOR'))
            print(f"{tokens[i]} --> plus")
        elif tokens[i] == '-':
            number = "-"
            i += 1
            if i >= len(tokens) or result[-1][1] in ['scientific notation', 'real number', 'right parenthesis'] or tokens[i] in ['+', '*', '/', '(', ')']:
                result.append(('-', 'minus', 'OPERATOR'))
                print(f"- --> minus")
                i -= 1
                continue
            while i < len(tokens) and (tokens[i].isnumeric() or tokens[i] == ','):
                number += tokens[i]
                i += 1
            if i < len(tokens) and tokens[i] == 'e':
                number += tokens[i]
                i += 1
                if i < len(tokens) and tokens[i] == '-':
                    number += tokens[i]
                    i += 1
                while i < len(tokens) and tokens[i].isnumeric():
                    number += tokens[i]
                    i += 1
                i -= 1
                result.append((number, 'scientific notation', 'NUMBER'))
                print(f"{number} --> scientific notation")
            else:
                i -= 1
                result.append((number, 'real number', 'NUMBER'))
                print(f"{number} --> real number")
        elif tokens[i].isnumeric() or tokens[i] == ',':
            number = ""
            while i < len(tokens) and (tokens[i].isnumeric() or tokens[i] == ','):
                number += tokens[i]
                i += 1
            if i < len(tokens) and tokens[i] == 'e':
                number += tokens[i]
                i += 1
                if i < len(tokens) and tokens[i] == '-':
                    number += tokens[i]
                    i += 1
                while i < len(tokens) and tokens[i].isnumeric():
                    number += tokens[i]
                    i += 1
                i -= 1
                result.append((number, 'scientific notation', 'NUMBER'))
                print(f"{number} --> scientific notation")
            else:
                i -= 1
                result.append((number, 'real number', 'NUMBER'))
                print(f"{number} --> real number")
        elif tokens[i] == '*':
            result.append((tokens[i], 'multiply', 'OPERATOR'))
            print(f"{tokens[i]} --> multiply")
        elif tokens[i] == '/':
            result.append((tokens[i], 'division', 'OPERATOR'))
            print(f"{tokens[i]} --> division")
        elif tokens[i] == '(':
            result.append((tokens[i], 'left parenthesis', 'PARENTHESIS'))
            print(f"{tokens[i]} --> left parenthesis")
        elif tokens[i] == ')':
            result.append((tokens[i], 'right parenthesis', 'PARENTHESIS'))
            print(f"{tokens[i]} --> right parenthesis")
        else:
            result.append((tokens[i], 'ERROR', 'ERROR'))
            print(f"{tokens[i]} --> ERROR")
    return result


def highlight_code(scanned_expression):
    token_colors = {
        'NUMBER': 'blue',
        'OPERATOR': 'red',
        'PARENTHESIS': 'green',
        'ERROR': 'black'
    }
    highlighted_text = ""
    for token, _, category in scanned_expression:
        color = token_colors.get(category, 'black')
        highlighted_text += f'<span style="color: {color};">{token}</span>'
    return highlighted_text


def process_line(lines, output_file):
    highlighted_lines = "".join([highlight_code(scanner(input_line)) + '\n' for input_line in lines])
    html_content = """
    <html>
    <head>
        <title>Highlighted Code</title>
    </head>
    <body>
        <pre>
""" + highlighted_lines + """
        </pre>
    </body>
    </html>
    """

    with open(output_file, 'w', encoding='utf-8') as file1:
        file1.write(html_content)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("input.txt", 'r', encoding='utf-8') as f:
        process_line(f.readlines(), "output1.html")

    process_line(["23+786-(87)/(-8,59e-54)","567g","*+-"], "output2.html")


    print(f"Kolorowany kod zapisano w output[1-2].html")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
