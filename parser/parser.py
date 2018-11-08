from rply import ParserGenerator

from ast.ast import (
    Numero,
    String,
    Tipo,
    Identificador,
    Add,
    Sub,
    Mult,
    Div,
    Imprime,
    Atribuicao,
    Leia
)

class Parser():

    def __init__(self):
        self.pg = ParserGenerator(
            [
                'NUMBER',
                'STRING',
                'IDENT',
                'PRINT',
                'READ',
                'INT',
                'OPEN_PAREN',
                'CLOSE_PAREN',
                'END_STATEMENT',
                'DECLARE_TYPE',
                'ADD',
                'SUB',
                'MULT',
                'DIV',
            ],
            precedence= [
                ('left', ['ADD', 'SUB']),
                ('left', ['MUL', 'DIV'])
            ]
        )
        self.vars = {}
        self.flags = {
            "for": False,
            "while": False,
            "if": False
        }

    def parse(self):
        @self.pg.production("main : expression")
        def main(p):

            return p[0]

        @self.pg.production(
            "expression : PRINT OPEN_PAREN expression CLOSE_PAREN END_STATEMENT"
        )
        def imprime(p):
            if isinstance(p[2], Identificador):
                if p[2].nome in self.vars.keys():
                    return Imprime(self.vars[p[2].nome])

            return Imprime(p[2])


        @self.pg.production(
            "expression : READ OPEN_PAREN expression CLOSE_PAREN END_STATEMENT"
        )
        def read_input(p):
            new_ident, new_value = Leia(p[2]).eval()
            self.vars[new_ident.nome].value = new_value

            return new_ident

        @self.pg.production(
            'expression : expression DECLARE_TYPE expression END_STATEMENT'
        )
        def expression_attr(p):
            type_ident = p[0]
            ident = p[2]

            atrib = Atribuicao(type_ident, ident)
            ident_to_be_stored = atrib.right.tipo.value

            self.vars[ident_to_be_stored] = atrib.right

            return atrib

        @self.pg.production('expression : expression ADD expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MULT expression')
        @self.pg.production('expression : expression DIV expression')
        def expression_arg(p):
            left = p[0]
            right = p[2]
            operator = p[1]

            if operator.gettokentype() == 'ADD':
                return Add(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MULT':
                return Mult(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)

        @self.pg.production('expression : IDENT')
        def identifier(p):

            return Identificador(p[0].value, p[0])

        @self.pg.production('expression : NUMBER')
        def number(p):

            return Numero(p[0].value)

        @self.pg.production('expression : STRING')
        def string(p):

            return String(p[0].value)

        @self.pg.production('expression : INT')
        def tipo(p):

            return Tipo(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):

        return self.pg.build()
