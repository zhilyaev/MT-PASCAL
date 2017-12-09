// @autohr Dmitry Zhilyaev
grammar Pascal;

r: program ;
program : 'program ' ID ';'
            decl
            'begin'
                body
            'end.'
            #PROGRAM_NAME;
    decl:
        | var_decl decl
        | procedure_decl decl
        ;

    vars_decl:
        | var_decl vars_decl
        ;
        var_decl: 'var ' ID ':' STD_TYPE ';' #NEW_VAR;
    procedure_decl: 'procedure ' ID '(' args_decl ')' ';'
                    vars_decl
                    'begin'
                        body
                    'end;'
                    #NEW_PROCEDURE;
    args_decl:
        | arg_decl args_decl
        ;
        arg_decl: ID ':' STD_TYPE ;

body :
      | assign body {print($assign.text)}
      ;

assign : ID ':=' expression ';' #CHECK_ASSIGN;
      expression: simple_expression
                | simple_expression REL_OP simple_expression
                ;
                simple_expression: term
                    | simple_expression ADD_OP term
                    ;
                    term: not_el
                    | term MUL_OP not_el
                    ;
                    not_el: el
                        | 'not' el
                        ;
                        el: ID
                            | STD_VAL
                            | call
                            | '(' expression ')'
                            ;
                            call: ID '(' args_list ')';
                                args_list: arg args;
                                args:
                                    |',' arg args
                                    ;
                                    arg: expression;

// Tokens
STD_VAL : INTEGER | CHAR | BOOL;
MUL_OP : '*' | '/' | 'and';
ADD_OP : '+'|'-'|'or';
REL_OP : '<'| '>' | '=' | '<>' | '>=' | '<=';
STD_TYPE : 'integer' | 'boolean' | 'char' | 'real'    ;
INTEGER : '1'..'9' (DIGIT)*;
CHAR : '\'' LETTER '\'';
BOOL : 'true' | 'false';
ID : (LETTER | '_') ( '_' | LETTER | DIGIT)*;
DIGIT : '0'..'9';
LETTER : 'a' .. 'z' | 'A' .. 'Z';
WS : [ \t\r\n]+ -> skip;