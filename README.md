# Анализатор языка паскаль
Данная программа написана в рамках курса ❤ Методы Трансляции

## Семантические ошибки, подлежащие обнаружению 
1. Использование необъявленного идентификатора 
    * [x] Необъявленные процедуры
2. Повторное объявление идентификатора 
    * [x] Повторное объявление процедуры
    * [x] Повторное объявление аргументов
3. Использование переменной не в соответствии с объявлением
   * [x] Примитивное обнаружение: 
    ```Pascal 
    n:=0;
    c:='c'
    s:="string"
    ```
    * [x] Примитивное обнаружение c переменной:
    ```Pascal 
    program vars;
    var n:integer;
    var k:string;
    begin
        n:=k;
    end.
    ```
    
## Поддерживаемые конструкции Pascal
* [x] for
* [x] while
* [x] if
* [x] if-else-if*
* [x] if-else
* [x] procedure
* [x] assign

Были убраны обязательные **';'**

## Install
0. install python3
1. Install [antlr4](https://tomassetti.me/antlr-mega-tutorial)
    ```Bash
    $ cd /usr/local/lib
    $ sudo curl -O http://www.antlr.org/download/antlr-4.7-complete.jar
    $ export CLASSPATH=".:/usr/local/lib/antlr-4.7-complete.jar:$CLASSPATH"
    $ alias antlr4='java -jar /usr/local/lib/antlr-4.7-complete.jar'
    $ alias grun='java org.antlr.v4.gui.TestRig'
    ```
2. install runtime for python3
    ```bash
    $ pip install antlr4-python3-runtime
    ```
3. git clone this repo
    ```bash
    $ git clone https://github.com/zhilyaev/MT-PASCAL.git
    ```
4. Generate grammar
    ```bash
    $ antlr4 -Dlanguage=Python3 antlr/Pascal.g4
    or
    $ make
    ```
5. run example
    ```bash
    main tests/syntax/vars_decl.pas
    or
    main.py tests/syntax/vars_decl.pas
    or
    python main.py tests/syntax/vars_decl.pas
    ```
6. use make for tests demo
    ```bash
    $ make test
    ```
