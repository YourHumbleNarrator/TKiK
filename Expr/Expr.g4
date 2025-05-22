grammar Expr;

program
    : main_function_definition
     function_definition*
     EOF
    ;

main_function_definition
    : FUNCTION_KW
    MAIN_KW
    LEFT_PAREN parameter_list? RIGHT_PAREN
    BEGIN_KW
    function_body
    END_KW SEMICOLON
    ;

function_definition
    : FUNCTION_KW
    IDENTIFIER
    LEFT_PAREN parameter_list? RIGHT_PAREN
    (RETURN_KW type_specifier | NO_KW RETURN_KW)
    BEGIN_KW
    function_body
    END_KW SEMICOLON
    ;

parameter_list
    : parameter ( COMMA parameter )*
    ;

parameter
    : type_specifier ( LEFT_SQUARE RIGHT_SQUARE )* IDENTIFIER
    ;

type_specifier
    : BOOL_TP
    | SHORT_TP
    | INT_TP
    | FLOAT_TP
    | DOUBLE_TP
    | CHAR_TP
    | LONG_TP
    ;

function_body
    : statement+
    ;


write_function
    : WRITE_KW LEFT_PAREN TEXT_IN_QUOTES RIGHT_PAREN SEMICOLON
    | WRITE_KW LEFT_PAREN QUOT_MARK (PARAMETER expression)* QUOT_MARK (COMMA type_specifier)* RIGHT_PAREN SEMICOLON
    ;

read_function
    : READ_KW
    LEFT_PAREN
    QUOT_MARK PARAMETER lvalue QUOT_MARK COMMA type_specifier
    RIGHT_PAREN SEMICOLON
    ;

statement
    : simple_statement
    | complex_statement
    ;

simple_statement
    : local_variable_declaration
    | assignment_statement
    | function_call
    | return_statement
    | write_function
    | read_function
    ;

complex_statement
    : if_statement
    | for_statement
    | while_statement
    ;

statement_in_loop
    : simple_statement_in_loop
    | complex_statement_in_loop
    ;

simple_statement_in_loop
    : simple_statement
    | BREAK_KW SEMICOLON
    | CONTINUE_KW SEMICOLON
    ;

complex_statement_in_loop
    : if_statement_in_loop
    | for_statement
    | while_statement
    ;

local_variable_declaration
    : type_specifier lvalue ( ASSIGN_OP expression )? SEMICOLON
    ;

assignment_statement
    : lvalue ASSIGN_OP (expression | lvalue) SEMICOLON
    ;

function_call
    : IDENTIFIER LEFT_PAREN RIGHT_PAREN SEMICOLON
    | IDENTIFIER LEFT_PAREN expression (COMMA expression)* RIGHT_PAREN SEMICOLON
    ;

if_statement
    : IF_KW
    logical_expression
    DO_KW BEGIN_KW
    statement+
    END_KW SEMICOLON
    else_statement?
    ;

else_statement
    : ELSE_KW
    BEGIN_KW
    statement+
    END_KW
    SEMICOLON
    ;

if_statement_in_loop
    : IF_KW
    logical_expression
    DO_KW BEGIN_KW
    statement_in_loop+
    END_KW SEMICOLON
    else_statement_in_loop?
    ;

else_statement_in_loop
    : ELSE_KW
    BEGIN_KW
    statement_in_loop+
    END_KW
    SEMICOLON
    ;

for_statement
    : FOR_KW
    lvalue ASSIGN_OP math_expression
    TO_KW
    math_expression
    DO_KW
    BEGIN_KW
    statement_in_loop+
    END_KW SEMICOLON
    ;

while_statement
    : WHILE_KW
    logical_expression
    BEGIN_KW
    statement_in_loop+
    END_KW SEMICOLON
    ;

return_statement
    : RETURN_KW
    expression
    SEMICOLON
    ;


lvalue
    : IDENTIFIER (LEFT_SQUARE math_expression RIGHT_SQUARE)*
    ;


expression
    : math_expression
    | logical_expression
    | CHAR_LITERAL
    ;

math_expression
    : SUB_MATH_OP? term (math_operator math_expression)*
    | LEFT_PAREN math_expression RIGHT_PAREN
    ;

term
    : literal | lvalue
    ;

math_operator
    : ADD_MATH_OP
    | SUB_MATH_OP
    | MUL_MATH_OP
    | DIV_MATH_OP
    | MOD_MATH_OP
    | OR_BIT_OP
    | AND_BIT_OP
    | RIGHT_SHIFT_BIT_OP
    | LEFT_SHIFT_BIT_OP
    | XOR_BIT_OP
    ;

comparison_expression
    : math_expression boolean_operator math_expression
    | LEFT_PAREN math_expression boolean_operator math_expression RIGHT_PAREN
    ;

boolean_value
    : (comparison_expression | BOOLEAN_TRUE_LIT | BOOLEAN_FALSE_LIT)
    ;

  //NAWIASOWANIE!!!!
logical_expression
    : boolean_value ((AND_LOGICAL_OP | OR_LOGICAL_OP) logical_expression)*
    | LEFT_PAREN logical_expression RIGHT_PAREN
    ;

boolean_operator
    : EQUAL_BOOL_OP
    | NOT_EQ_BOOL_OP
    | GREATER_BOOL_OP
    | GREATER_EQ_BOOL_OP
    | LESS_BOOL_OP
    | LESS_EQ_BOOL_OP
    ;

literal
    : INTEGER_LITERAL
    | FLOAT_LITERAL
    | BOOLEAN_TRUE_LIT
    | BOOLEAN_FALSE_LIT
    ;

// Types
SHORT_TP: 'Piccolo';
INT_TP: 'Intero';
FLOAT_TP: 'Flottante';
DOUBLE_TP: 'Doppio';
CHAR_TP: 'Carattere';
BOOL_TP: 'Booleano';
LONG_TP: 'Grande';
BOOLEAN_TRUE_LIT: 'Vero';
BOOLEAN_FALSE_LIT: 'Falso';

FUNCTION_KW : 'Funzione';
BEGIN_KW : 'inizio';
END_KW : 'fine';
IF_KW: 'se';
DO_KW: 'allora' | 'fai';
ELSE_KW: 'altrimenti';
FOR_KW: 'per';
TO_KW: 'a\'';
WHILE_KW: 'mentre';
CONTINUE_KW: 'continua';
BREAK_KW: 'ferma';
RETURN_KW: 'ritorna';
EXCEPTION_KW: 'eccezione';
MAIN_KW: 'principale';
NO_KW: 'no';
WRITE_KW: 'Scriviere';
READ_KW: 'Caricare';
IDENTIFIER: [a-z_] [a-zA-Z0-9_]* ;
INTEGER_LITERAL: [0-9]+ ;
FLOAT_LITERAL : [0-9]+.[0-9]+ ;
CHAR_LITERAL: '\'' ( '\\' [nt\\'"] | ~['\\] ) '\'' ;
LINE_COMMENT: '!!' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '!!-' .*? '-!!' -> skip ;
TEXT_IN_QUOTES: QUOT_MARK ( '\\' [nt\\'";] | ~["\\$;,] )* QUOT_MARK;
QUOT_MARK: '"';
WS: [ \t\r\n]+ -> skip;
PARAMETER: '$';



// Math operators
ADD_MATH_OP: '+';
SUB_MATH_OP: '-';
MUL_MATH_OP: '*';
DIV_MATH_OP: '/';
MOD_MATH_OP: '%';

// Assign operator
ASSIGN_OP: ':=';

// Boolean operators
EQUAL_BOOL_OP: '=';
LESS_EQ_BOOL_OP: '<=';
GREATER_EQ_BOOL_OP: '>=';
NOT_EQ_BOOL_OP: '!=';
GREATER_BOOL_OP: '>';
LESS_BOOL_OP: '<';

// Bit operators
OR_BIT_OP: '|';
AND_BIT_OP: '&';
RIGHT_SHIFT_BIT_OP: '>>';
LEFT_SHIFT_BIT_OP: '<<';
XOR_BIT_OP: '^';

// Logical operators
AND_LOGICAL_OP: 'e\'';
OR_LOGICAL_OP: 'o\'';
NOT_LOGICAL_OP: 'non';

// Brackets
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
LEFT_SQUARE: '[';
RIGHT_SQUARE: ']';

// Separators
COMMA: ',';
SEMICOLON: ';';
