grammar GPlanguage;

IF : 'if' ;
LOOP : 'loop' ;

INTEGER_VALUE : [0-9]+ ;
FLOAT_VALUE : [0-9]+ '.' [0-9]* | '.' [0-9]+ ;
STRING_VALUE : '"' (~["\\\n\r])* '"' ;

BLOCK_START : '{' ;
BLOCK_END: '}' ;
OUT: 'out';
IN: 'in';
ARRAY: 'array';

LPAREN : '(' ;
RPAREN : ')' ;
LSQUARE : '[' ;
RSQUARE : ']' ;

PLUS : '+' ;
MINUS : '-' ;
MULT : '*' ;
DIV : '/' ;
EQ : '==' ;
NEQ : '!=' ;
LT : '<' ;
LTE : '<=' ;
GT : '>' ;
GTE : '>=' ;

AND : 'and' ;
OR : 'or' ;

ASSIGN : '=' ;
SEMI : ';' ;
COMMA : ',' ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ;

WS : [ \t\r\n]+ -> skip ;

program : statement+;

statement : if_statement | assignment SEMI | loop_statement | output_statement | input_statement;

if_statement : IF LPAREN expression RPAREN code_block;

array_create : ARRAY LPAREN arithmetic_expression RPAREN ;

array_initialization : LSQUARE (arithmetic_expression? | arithmetic_expression (COMMA arithmetic_expression)*) RSQUARE | STRING_VALUE;

assignment : ID (LSQUARE arithmetic_expression RSQUARE)? ASSIGN (expression | array_create | array_initialization);

loop_statement : LOOP LPAREN expression RPAREN code_block ;

output_statement : OUT LPAREN expression RPAREN SEMI;

input_statement : ID ASSIGN IN LPAREN RPAREN SEMI;

expression: boolean_expression | arithmetic_expression;

code_block : BLOCK_START statement+ BLOCK_END ;

boolean_expression
    : relational_expression (OR boolean_expression)? |
    relational_expression (AND boolean_expression)?
    ;

relational_expression
    : (variable_reference | value | arithmetic_expression | array_index) op=(EQ | NEQ | LT | LTE | GT | GTE) (variable_reference | value | arithmetic_expression | array_index)
    ;

arithmetic_expression: arithmetic_expression op=(PLUS | MINUS | MULT | DIV) arithmetic_expression | value | variable_reference | array_index;

array_index : variable_reference LSQUARE arithmetic_expression RSQUARE ;

value :
    INTEGER_VALUE |
    FLOAT_VALUE
    ;

variable_reference : ID ;






