// © zhiylaev@github.com
grammar Pascal;

@members {
globalVars = {}  # ID : TYPE
procedures = {}
local = False
localVars = {}
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
        var_decl: 'var ' ID ':'  STD_TYPE_NAME ';'
{
map = {}
if self.local:
    map = self.localVars
else:
    map = self.globalVars

if ($ID.text not in map):
    map[$ID.text] = $STD_TYPE_NAME.text
else:
    sys.stderr.write('Строка №'+str($ID.line)+': ID='+$ID.text+' объявлен повторно\n');
};

    procedure_decl:
{
self.local = True
}
                    'procedure ' ID '(' arg_list_decl ')' mb
                    vars_decl
                    'begin'
                        body
                    'end' ';'
{
if ($ID.text not in self.globalVars) and ($ID.text not in self.procedures):
    self.procedures[$ID.text] = $ID.line
else:
    sys.stderr.write('Строка №'+str($ID.line)+': Палехче ID='+$ID.text+' уже исползуется\n');

self.localVars.clear()
self.local = False
};
arg_list_decl:
    | arg_decl
    | arg_decl mult_arg_decl
    ;
    mult_arg_decl: ';' arg_list_decl;
    arg_decl: ID ':' STD_TYPE_NAME
{
if $ID.text not in self.localVars:
    self.localVars[$ID.text] = $STD_TYPE_NAME.text
else:
    sys.stderr.write('Строка №'+str($ID.line)+': Аргумент ID='+$ID.text+' уже исползуется\n');
};

body :
     | 'begin' body 'end' mb body
     | simple_body mb
     | simple_body mb body
     ;
      simple_body: assign
                 | b_for
                 | b_while
                 | call
                 | b_if
                 | s_if
                 ;
      s_if: 'if' expression 'then' body;
      b_if: 'if' expression 'then' body 'else' body;
      b_for: 'for' assign 'to' expression 'do' body;
      b_while: 'while' expression 'do' body;

assign : ID ':=' expression
{
map = {}
if self.local:
    map = self.localVars
else:
    map = self.globalVars

if $ID.text in map:
    if map[$ID.text] != self.lastType:
        sys.stderr.write('Строка №'+str($ID.line)+': Неверный тип ID='+$ID.text+' '+map[$ID.text]+' => '+ self.lastType +'\n')

else:
    sys.stderr.write('Строка №'+str($ID.line)+': Необъявленный ID='+$ID.text+'\n');

self.lastType = ''
};
call: ID '(' arg_list ')'
{
if $ID.text not in self.procedures:
    sys.stderr.write('Строка №'+str($ID.line)+': Необъявленная Процедура\n');
};
    arg_list:
            |arg args
            ;
            args:
            | ',' arg args
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
{
map = {}
if self.local:
    map = self.localVars
else:
    map = self.globalVars
if $ID.text in map:
    self.lastType = map[$ID.text]
else:
    sys.stderr.write('Строка №'+str($ID.line)+': Необъявленный ID\n');
}
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