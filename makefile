
all:
	antlr4 -Dlanguage=Python3 antlr/Pascal.g4

test:
	python main.py

clean: rm -f Pascal*.*