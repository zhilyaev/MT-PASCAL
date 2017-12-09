// © zhiylaev@github.com
grammar Pascal;

@members {
globalVars = {}  # ID : TYPE
lastType = ''
}

r: program ;
program : 'program ' ID mb
            decl
            'begin'
                body
            'end.'
          ;
    decl:
        | var_decl decl
        | procedure_decl decl
        ;

    vars_decl:
        | var_decl vars_decl
        ;
        var_decl: 'var ' ID ':'  STD_TYPE_NAME mb
{
if $ID.text not in self.globalVars:
    self.globalVars[$ID.text] = $STD_TYPE_NAME.text
else:
    sys.stderr.write('Строка №'+str($ID.line)+': Палехче ID='+$ID.text+' уже исползуется\n');
};

    procedure_decl: 'procedure ' ID '(' args_decl ')' mb
                    vars_decl
                    'begin'
                        body
                    'end' mb
{
self.globalVars[$ID.text] = 'VOID'
};
    args_decl:
        | arg_decl args_decl
        ;
        arg_decl: ID ':' STD_TYPE_NAME
        ;

body :
     | 'begin' body 'end' mb
     | simple_body
     ;
      simple_body: assign body
                 | b_for
                 | b_while
                 | call
                 | b_if
                 ;

      b_if: 'if' expression 'then' body 'else' body;
      b_for: 'for' assign 'to' expression 'do' body;
      b_while: 'while' expression 'do' body;

assign : ID ':=' expression mb
{
if $ID.text in self.globalVars:
    if (self.globalVars[$ID.text] != self.lastType):
        sys.stderr.write('Строка №'+str($ID.line)+': Неверный тип '+$ID.text+'\n')
else:
    sys.stderr.write('Строка №'+str($ID.line)+': Необъявленный ID='+$ID.text+'\n');
};
call: ID '(' args_list ')' mb;
    args_list: arg args;
             args:
             |',' arg args
             ;
             arg: expression;

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
                            | INTEGER {self.lastType = 'integer'}
                            | CHAR {self.lastType = 'character'}
                            | BOOL {self.lastType = 'boolean'}
                            //| if u wanna func -> place here
                            | '(' expression ')'
                            ;

mb :
    | ';'
    ;
// Tokens
//STD_VAL : INTEGER | CHAR | BOOL;
MUL_OP : '*' | '/' | 'and';
ADD_OP : '+'|'-'|'or';
REL_OP : '<'| '>' | '=' | '<>' | '>=' | '<=';
STD_TYPE_NAME : 'integer' | 'boolean' | 'real' | 'string' | 'character' ;
INTEGER : ('1'..'9' (DIGIT)*) | '0';
CHAR : '\'' LETTER '\'';
BOOL : 'true' | 'false';
STRING :'"' .*? '"' ;
ID : (LETTER | '_') ( '_' | LETTER | DIGIT)*;
DIGIT : '0'..'9';
LETTER : 'a' .. 'z' | 'A' .. 'Z';
WS : [ \t\r\n]+ -> skip;
COMMENT_1: '(*' .*? '*)' -> skip;
COMMENT_2: '{' .*? '}' -> skip;
COMMENT_3: '/*' .*? '*/' -> skip;