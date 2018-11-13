from lexer.lexer import Lexer
from parser.parser import Parser


text_input = """
    inteiro:x;
    inteiro:y;

    leia(x);

    leia(y);
    para x ate y passo 1 imprima(x); fim_para
"""

lexer = Lexer().get_lexer()

pg = Parser()
pg.parse()
parser = pg.get_parser()

for line in list(filter(None, text_input.split('\n'))):
    tokens = lexer.lex(line)
    parser.parse(tokens).eval()
