
all:
	antlr4 -Dlanguage=Python3 antlr/Pascal.g4

test:
	python main.py tests/logic/vars.pas
	python main.py tests/syntax/for-while_once.pas
	python main.py tests/syntax/if.pas
	python main.py tests/syntax/for-while.pas
	python main.py tests/syntax/vars_decl.pas
	python main.py tests/syntax/for_once.pas
	python main.py tests/syntax/comments.pas
	python main.py tests/syntax/procedure_single.pas
	python main.py tests/syntax/procedure_option.pas
	python main.py tests/logic/k.pas
	python main.py tests/logic/procedures.pas

clean: rm -f Pascal*.*