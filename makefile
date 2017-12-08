
all:
	antlr4 -Dlanguage=Python3 antlr/Hello.g4
	python main.py
	

clean: rm -f *.tokens