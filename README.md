# Kompilator C do własnego języka
- Berenike Banek berenike@student.agh.edu.pl
- Mateusz Bielówka mbielowka@student.agh.edu.pl

## Opis
- Język wykorzystuje elementy języka włoskiego języku C-like i Ady, co sprawia, że jest bardziej zrozumiały dla osób znających te języki.
- Język implementacji - `Python`
- Generator skanerów i parserów - `ANTLR4`

## Wykaz tokenów

| Kod Tokena | Wartość Tokena | Opis |
|---|---|---|
| kw_FUNCTION | Funzione | Słowo kluczowe dla funkcji |
| kw_BEGIN | inizio | Rozpoczęcie bloku kodu |
| kw_END | fine | Zakończenie bloku kodu |
| kw_IF | se | Słowo kluczowe dla warunku |
| kw_DO | allora/fai | Słowo kluczowe użyte po warunku przed instrukcją warunkową |
| kw_ELSE | altrimenti | Alternatywna instrukcja w konstrukcji if-else |
| kw_FOR | per | Słowo kluczowe dla pętli typu FOR |
| kw_WHILE | mentre | Słowo kluczowe dla pętli typu WHILE |
| kw_CONTINUE | continua | Skok do początku pętli |
| kw_BRAKE | ferma | Przerwanie pętli |
| kw_TRY | prova | Słowo kluczowe dla bloku try |
| kw_CATCH | cattura | Słowo kluczowe dla bloku catch |
| kw_THROW | lancia | Słowo kluczowe do rzucania wyjątków |
| kw_RETURN | ritorna | Zwracanie wartości |
| kw_NEW | nuovo | Słowo kluczowe do tworzenia nowych obiektów |
| tp_SHORT | Piccolo | Typ danych dla niewielkiej liczby całkowitej |
| tp_INT | Intero | Typ danych dla liczby całkowitej |
| tp_FLOAT | Flottante | Typ danych dla liczby zmiennoprzecinkowej |
| tp_DOUBLE | Doppio | Typ danych dla podwójnej precyzji |
| tp_CHAR | Carattere | Typ danych dla pojedynczego znaku |
| tp_BOOL | Booleano | Typ danych dla wartości logicznej |
| tp_LONG | Grande | Typ danych dla dużej liczby całkowitej |
| lit_BOOLEAN_TRUE | vero | Literał dla wartości true |
| lit_BOOLEAN_FALSE | falso | Literał dla wartości false |
| IDENTFIER | [a-zA-Z_][a-zA-Z0-9_]* | Identyfikator zmiennej |
| lit_INTEGER | [0-9]+ | Literał dla liczby całkowitej |
| lit_FLOAT | [0-9]+.[0-9]+ | Literał dla liczby zmiennoprzecinkowej |
| lit_CHAR | '[^']' | Literał dla znaku |
| math_operators | [\\+ - \\* / %] | Operatory matematyczne |
| bool_operators | ['=' '<=' '>=' '!=' '>''<'] | Operatory logiczne |
| bit_operators | ['\|''&''>>''<<''^'] | Operatory bitowe |
| logical_operators | ['e\\'' 'o\\''] | Operatory logiczne AND i OR (np. vero o' falso) |
| br_L_PAREN | \\( | Nawias'(' |
| br_R_PAREN | \\) | Nawias ')' |
| br_L_SQ | \\[ | Nawias '[' |
| br_R_SQ | \\] | Nawias ']' |
| separator_COMMA | , | Separator ',' |
| separator_SEMICOLON | ; | Separator ';' |
| kw_COMMENT_LINE | !! | Komentarz jednoliniowy |

## Wstępne uwagi:
- `inizio` - `fine` oddzielają ciąg poleceń wykonywany wramach danej pętli/funkcji/instrukcji warunkowej
- Funzione - definiuje nową funkcję.
- Scrivi - funkcja do wypisywania.
- Typ funkcji określony jest przy zwracaniu wartości i musi być użyty konsekwentnie przy każdym ritorna (np. ritorna Intero 5;) jeśli to słowo nie wystąpi funkcja jest typu void.
