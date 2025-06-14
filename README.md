# Kompilator własnego języka Giava 🤌 do C
- Berenike Banek berenike@student.agh.edu.pl
- Mateusz Bielówka mbielowka@student.agh.edu.pl

## 🏆 Cel projektu
Celem projektu było stworzenie języka do nauki programowania z wykorzystaniem słów kluczowych w języku włoskim. Giava 🤌 łączy elementy języków wywodzących się z C, oraz Ady, co sprawia, że jest on bardziej intuicyjny i łatwiejszy do nauki dla osób początkujących.

## 🛠️ Sprawy techniczne
- Typ translatora - kompilator (Giava 🤌 🡒 C)
- Język implementacji - `Python`
- Generator skanerów i parserów - `ANTLR4`

## 📜 Wykaz tokenów

| Kod Tokena | Wartość Tokena | Opis |
|---|---|---|
| FUNCTION_KW | Funzione | Słowo kluczowe dla funkcji |
| BEGIN_KW | inizio | Rozpoczęcie bloku kodu |
| END_KW | fine | Zakończenie bloku kodu |
| IF_KW | se | Słowo kluczowe dla warunku |
| DO_KW | allora/fai | Słowo kluczowe użyte po warunku przed instrukcją warunkową |
| ELSE_KW | altrimenti | Alternatywna instrukcja w konstrukcji if-else |
| FOR_KW | per | Słowo kluczowe dla pętli typu FOR |
| TO_KW | a' | Słowo kluczowe dla warunku w pętli |
| WHILE_KW | mentre | Słowo kluczowe dla pętli typu WHILE |
| CONTINUE_KW | continua | Skok do początku pętli |
| BREAK_KW | ferma | Przerwanie pętli |
| RETURN_KW | ritorna | Zwracanie wartości |
| MAIN_KW | principale | Otwarcie funkcji Main |
| NO_KW | no | Słowo kluczowe do funkcji void |
| WRITE_KW | Scriviere | Wywołanie funkcji printf |
| READ_KW | Caricare | Wywołanie funkcji scanf |
| IDENTFIER | [a-zA-Z_][a-zA-Z0-9_]* | Identyfikator zmiennej |
| INTEGER_LIT | [0-9]+ | Literał dla liczby całkowitej |
| FLOAT_LIT | [0-9]+.[0-9]+ | Literał dla liczby zmiennoprzecinkowej |
| TCHAR_LIT | '[^']' | Literał dla znaku |
| QUOT_MARK | " | Symbol cudzysłowia |
| PARAMETER | $ | Symbol parametru |
| TEXT_IN_QUOTES | " ( '\\' [nt\\'";] \| ~["\\$;,] )* " | Tekst |
| LINE_COMMENT | !! | Komentarz jednoliniowy |
| BLOCK_COMMENT | '!!-' .*? '-!!' | Komentarz blokowy |
| W_S | [ \t\r\n]+ | Pusta przestrzeń |

### Typy zmiennych
| Kod Tokena | Wartość Tokena | Opis |
|---|---|---|
| SHORT_TP | Piccolo | Typ danych dla niewielkiej liczby całkowitej |
| INT_TP | Intero | Typ danych dla liczby całkowitej |
| FLOAT_TP | Flottante | Typ danych dla liczby zmiennoprzecinkowej |
| DOUBLE_TP | Doppio | Typ danych dla podwójnej precyzji |
| CHAR_TP | Carattere | Typ danych dla pojedynczego znaku |
| BOOL_TP | Booleano | Typ danych dla wartości logicznej |
| LONG_TP | Grande | Typ danych dla dużej liczby całkowitej |
| BOOLEAN_LIT_TRUE | vero | Literał dla wartości true |
| BOOLEAN_LIT_FALSE | falso | Literał dla wartości false |

### Operatory matematyczne
| Kod Tokena | Wartość Tokena | Opis |
|---|---|---|
| ADD_MATH_OP | \\+ | Operator dodawania |
| SUB_MATH_OP | - | Operator odejmowania |
| MUL_MATH_OP | \\* | Operator mnożenia |
| DIV_MATH_OP | / | Operator dzielenia |
| MOD_MATH_OP | % | Operator modulo |

### Operator przypisania
| Kod Tokena | Wartość Tokena | Opis |
|---|---|---|
| ASSIGN_OP | := | Operator przypisania |

### Operatory bitowe
| Kod Tokena | Wartość Tokena | Opis |
|---|---|---|
| OR_BIT_OP | '\|' | Operator bitowy lub |
| AND_BIT_OP | '&' | Operator bitowy i |
| RIGHT_SHIFT_BIT_OP | '>>' | Operator bitowy prawy shift |
| LEFT_SHIFT_BIT_OP | '<<' | Operator bitowy lewy shift |
| XOR_BIT_OP | '^' | Operator bitowy xor |

### Operatory boolean
| Kod Tokena | Wartość Tokena | Opis |
|---|---|---|
| EQUAL_BOOL_OP | '=' | Operator równne |
| LESS_EQ_BOOL_OP | '<=' | Operator mniejsze lub równe |
| GREATER_EQ_BOOL_OP | '>=' | Operator większe lub równe |
| NOT_EQ_BOOL_OP | '!=' | Operator różne |
| GREATER_BOOL_OP | '>' | Operator większe |
| LESS_BOOL_OP | '<' | Operator mniejsze |

### Operatory logiczne
| Kod Tokena | Wartość Tokena | Opis |
|---|---|---|
| AND_LOGICAL_OP | 'e\\'' | Operator logiczny AND |
| OR_LOGICAL_OP | 'o\\'' | Operator logiczny OR |
| NOT_LOGICAL_OP | non | Operator logiczny NOT |

### Nawiasy
| Kod Tokena | Wartość Tokena | Opis |
|---|---|---|
| LEFT_PAREN | \\( | Nawias'(' |
| RIGHT_PAREN | \\) | Nawias ')' |
| LEFT_SQUARE | \\[ | Nawias '[' |
| RIGHT_SQUARE | \\] | Nawias ']' |

### Separatory
| Kod Tokena | Wartość Tokena | Opis |
|---|---|---|
| COMMA | , | Separator ',' |
| SEMICOLON | ; | Separator ';' |

## 🅰️ Gramatyka

Spis tokenów jest zdefiniowany w pliku: [Expr/Expr.tokens](/Expr/Expr.tokens)

Gramatyka jest zdefiniowana w pliku: [Expr/Expr.g4](/Expr/Expr.g4)

Na jej podstawei ANTLR4 wygenerował pliki Parser i Lexer z tego samego folderu


## 💻 Przykładowy kod

```
Funzione principale()
inizio

    Intero array[100];
    Intero n;

    Scriviere("Inserisci il numero di elementi: ");
    Caricare("$n",Intero);
    Scriviere("Inserisci gli elementi: ");

    per i:= 0 a' n - 1 fai
    inizio
        Caricare("$array[i]",Intero);
    fine;

    quicksort(array, 0, n - 1);
    Scriviere("Array ordinato: ");

    per i:= 0 a' n - 1 fai
    inizio
        Scriviere("$array[i]",Intero);
        Scriviere(" ");
    fine;

fine;

Funzione quicksort(Intero array[], Intero inizio1 ,Intero fine1) no ritorna
inizio

    se inizio1 < fine1 fai
    inizio
        Intero pivot := array[fin];
        Intero indice := inizio1 - 1;
        per i := inizio1 a' fine1 - 1 fai
        inizio
            se array[i] < pivot fai
            inizio
                indice := indice + 1;
                swap(array[indice], array[i]);
            fine;
        fine;
            swap(array[indice + 1], array[fin]);
            Intero partizione := indice + 1;
            quicksort(array, inizio1, partizione - 1);
            quicksort(array, partizione + 1, fine1);
    fine;

fine;

Funzione swap(Intero a,Intero b) no ritorna
inizio
    Intero temp := a;
    a := b;
    b := temp;
fine;
```

## 🔎 Instrukcja obsługi
#### Wymagania:
- Python 3.12
- pip
#### Instalacja ANTLR4
- pobierz plik jar https://www.antlr.org/download/antlr-4.13.1-complete.jar
- `pip install antlr4-tools`
- `pip install antlr4-python3-runtime==4.7`
- możliwe, że musisz dodać c:\Users\...\AppData\Local\...\LocalCache\local-packages\Python312\Scripts do PATH zmiennych systemowych
#### Uruchomienie ANTLR4
- `git clone https://github.com/YourHumbleNarrator/TKiK.git`
- `cd TKiK`
- `antlr4 -Dlanguage=Python3 Expr/Expr.g4 -visitor -o Expr` (po dokonaniu zmian w pliku Expr/Expr.g4)
- `python -m venv \ścieżka\do\nowego\wirtualnego\środowiska`
- `...\<środowisko>\Scripts\activate`
#### Uruchomienie GUI
- `python webapp.py`