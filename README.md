# Kompilator własnego języka do C
- Berenike Banek berenike@student.agh.edu.pl
- Mateusz Bielówka mbielowka@student.agh.edu.pl

## Opis
- Język wykorzystuje elementy języka włoskiego, języków C-like i Ady, co sprawia, że będzie on bardziej zrozumiały dla osób znających te języki.
- Język implementacji - `Python`
- Generator skanerów i parserów - `ANTLR4`

## Wykaz tokenów

| Kod Tokena | Wartość Tokena | Opis |
|---|---|---|
| FUNCTION_KW | Funzione | Słowo kluczowe dla funkcji |
| BEGIN_KW | inizio | Rozpoczęcie bloku kodu |
| END_KW | fine | Zakończenie bloku kodu |
| IF_KW | se | Słowo kluczowe dla warunku |
| DO_KW | allora/fai | Słowo kluczowe użyte po warunku przed instrukcją warunkową |
| ELSE_KW | altrimenti | Alternatywna instrukcja w konstrukcji if-else |
| FOR_KW | per | Słowo kluczowe dla pętli typu FOR |
| WHILE_KW | mentre | Słowo kluczowe dla pętli typu WHILE |
| CONTINUE_KW | continua | Skok do początku pętli |
| BRAKE_KW | ferma | Przerwanie pętli |
| TRY_KW | prova | Słowo kluczowe dla bloku try |
| CATCH_KW | cattura | Słowo kluczowe dla bloku catch |
| THROW_KW | lancia | Słowo kluczowe do rzucania wyjątków |
| RETURN_KW | ritorna | Zwracanie wartości |
| NEW_KW | nuovo | Słowo kluczowe do tworzenia nowych obiektów |
| SHORT_TP | Piccolo | Typ danych dla niewielkiej liczby całkowitej |
| INT_TP | Intero | Typ danych dla liczby całkowitej |
| FLOAT_TP | Flottante | Typ danych dla liczby zmiennoprzecinkowej |
| DOUBLE_TP | Doppio | Typ danych dla podwójnej precyzji |
| CHAR_TP | Carattere | Typ danych dla pojedynczego znaku |
| BOOL_TP | Booleano | Typ danych dla wartości logicznej |
| LONG_TP | Grande | Typ danych dla dużej liczby całkowitej |
| BOOLEAN_LIT_TRUE | vero | Literał dla wartości true |
| BOOLEAN_LIT_FALSE | falso | Literał dla wartości false |
| IDENTFIER | [a-zA-Z_][a-zA-Z0-9_]* | Identyfikator zmiennej |
| INTEGER_LIT | [0-9]+ | Literał dla liczby całkowitej |
| FLOAT_LIT | [0-9]+.[0-9]+ | Literał dla liczby zmiennoprzecinkowej |
| TCHAR_LIT | '[^']' | Literał dla znaku |
| L_PAREN_BR | \\( | Nawias'(' |
| R_PAREN_BR | \\) | Nawias ')' |
| L_SQ_BR | \\[ | Nawias '[' |
| R_SQ_BR | \\] | Nawias ']' |
| COMMA_SEP | , | Separator ',' |
| SEMICOLON_SEP | ; | Separator ';' |
| COMMENT_LINE | !! | Komentarz jednoliniowy |

| Kod Tokena | Wartość Tokena | Opis |
|---|---|---|
| MATH_ADD_OP | \\+ | Operator dodawania |
| MATH_SUB_OP | - | Operator odejmowania |
| MATH_MUL_OP | \\* | Operator mnożenia |
| MATH_DIV_OP | / | Operator dzielenia |
| MATH_MOD_OP | % | Operator modulo |

| Kod Tokena | Wartość Tokena | Opis |
|---|---|---|
| BOOL_EQ_OP | '=' | Operator równne |
| BOOL_LESS_EQ_OP | '<=' | Operator mniejsze lub równe |
| BOOL_GREATER_EQ_OP | '>=' | Operator większe lub równe |
| BOOL_NOT_EQ_OP | '!=' | Operator różne |
| BOOL_GREATER_OP | '>' | Operator większe |
| BOOL_LESS_OP | '<' | Operator mniejsze |

| Kod Tokena | Wartość Tokena | Opis |
|---|---|---|
| BIT_OR_OP | '\|' | Operator bitowy lub |
| BIT_AND_OP | '&' | Operator bitowy i |
| BIT_RIGHT_SHIFT_OP | '>>' | Operator bitowy prawy shift |
| BIT_LEFT_SHIFT_OP | '<<' | Operator bitowy lewy shift |
| BIT_XOR_OP | '^' | Operator bitowy xor |

| Kod Tokena | Wartość Tokena | Opis |
|---|---|---|
| LOGICAL_AND_OP | 'e\\'' | Operator logiczny AND i OR (np. vero o' falso) |
| LOGICAL_OR_OP | 'o\\'' | Operator logiczny AND i OR (np. vero o' falso) |

## Wstępne uwagi:
- `inizio` - `fine` oddzielają ciąg poleceń wykonywany wramach danej pętli/funkcji/instrukcji warunkowej
- Funzione - definiuje nową funkcję.
- Scrivi - funkcja do wypisywania.
- Typ funkcji określony jest przy zwracaniu wartości i musi być użyty konsekwentnie przy każdym ritorna (np. ritorna Intero 5;) jeśli to słowo nie wystąpi funkcja jest typu void.
