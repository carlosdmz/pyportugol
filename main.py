from lexer.lexer import Lexer
from parser.parser import Parser


text_input = """
    inteiro:x;
    inteiro:y;

    imprima("Digite o valor de X...");
    leia(x);
    imprima("Digite o valor de Y...");
    leia(y);

    imprima(x);
    imprima(y);
"""

lexer = Lexer().get_lexer()

pg = Parser()
pg.parse()
parser = pg.get_parser()

for line in list(filter(None, text_input.split('\n'))):
    tokens = lexer.lex(line)
    parser.parse(tokens).eval()
