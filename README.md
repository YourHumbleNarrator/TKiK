# Kompilator własnego języka Giava 🤌 do C
- Berenike Banek berenike@student.agh.edu.pl
- Mateusz Bielówka mbielowka@student.agh.edu.pl

## 🏆 Cel projektu
Celem projektu było stworzenie języka do nauki programowania z wykorzystaniem słów kluczowych w języku włoskim. Giava 🤌 łączy elementy języków wywodzących się z C, oraz Ady, co sprawia, że jest on bardziej intuicyjny i łatwiejszy do nauki dla osób początkujących.

## 🛠️ Sprawy techniczne
- Typ translatroa - kompilator (Giava 🤌 🡒 C)
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
| TEXT_IN_QUOTES | " ( '\\' [nt\\'";] | ~["\\$;,] )* " | Tekst |
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
work in progress

## 💻 Przykładowy kod

```
Funzione principale()
inizio

    Intero array[100];
    Intero n;
    Booleano temp := Vero;
    Booleano temp2 := (3>2) o' (2<3);

    Scriviere("Inserisci il numero di elementi: ");
    Caricare("$n",Intero);
    Scriviere("Inserisci gli elementi: ");

    per i:= 0 a' n - 1 fai
    inizio
        Scriviere("$array[i]",Intero);
    fine;

    quicksort(array, 0, n - 1);
    Scriviere("Array ordinato: ");

    per i:= 0 a' n - 1 fai
    inizio
        Scriviere("$array[i]",Intero);
        Scriviere(" ");
    fine;

    Intero i := 10;
    mentre i < 14
    inizio
        Grande additionResult := add(60, i);
        Scriviere("$additionResult", Grande);
        Piccolo subtractionResult := subtract(60, i);
        Scriviere("$subtractionResult", Piccolo);
        Flottante multiplicationResult := multiply(60, i);
        Scriviere("$multiplicationResult", Flottante);
        Doppio divisionResult := divideByTwo(i);
        Scriviere("$divisionResult", Doppio);
        i := i + 1;
    fine;

    Carattere symbol;
    Caricare("$symbol", Carattere);

    se symbol = '#' fai
    inizio
        Scriviere("You chose the # symbol :D");
    fine;
    altrimenti
    inizio
        Scriviere("$symbol", Carattere);
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

Funzione add(Grande a, Grande b) ritorna Grande
inizio
    Grande result := a+b;
    ritorna result;
fine;

Funzione subtract(Piccolo a, Piccolo b) ritorna Piccolo
inizio
    Piccolo result := a-b;
    ritorna result;
fine;

Funzione multiply(Flottante a, Flottante b) ritorna Flottante
inizio
    Flottante result := a*b;
    ritorna result;
fine;

Funzione divideByTwo(Doppio a) ritorna Doppio
inizio
    Doppio result := a/2;
    ritorna result;
fine;

Funzione printEvenNumbersUpTo18() no ritorna
inizio
    per i := 0 a' 100 fai
    inizio
        se i % 2 = 1 fai
        inizio
            continua;
        fine;
        altrimenti
        inizio
            ferma;
        fine;
        Scriviere("$i", Intero);
    fine;
fine;
```

## 🔎 Instrukcja obsługi
work in progress
