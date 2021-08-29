from lexer import Lexer
from parser import Parser


def run():
    text_input = """
        inteiro:x;
        inteiro:y;

        leia(x);

        leia(y);
        para x ate y passo 1 imprima(x); fim_para
    """
    evaluate(text_input)


def evaluate(code):
    lexer = Lexer().get_lexer()
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    for line in list(filter(None, code.split('\n'))):
        tokens = lexer.lex(line)
        parser.parse(tokens).eval()


if __name__ == '__main__':
    run()