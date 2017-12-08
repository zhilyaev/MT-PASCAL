
all:
	antlr4 -Dlanguage=Python3 antlr/Pascal.g4

test:
	python main.py tests/true/1.pas
	python main.py tests/true/2.pas
	python main.py tests/true/3.pas
	python main.py tests/true/4.pas
	python main.py tests/true/5.pas

clean: rm -f Pascal*.*