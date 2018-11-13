from rply import ParserGenerator

from ast.ast import (
    Numero,
    Nulo,
    String,
    Tipo,
    Identificador,
    Add,
    Sub,
    Mult,
    Div,
    Less,
    More,
    LessEqual,
    MoreEqual,
    Imprime,
    Atribuicao,
    Leia,
    ForLoop
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
                'IF',
                'THEN',
                'ELSE',
                'END_IF',
                'FOR',
                'UNTIL',
                'STEP',
                'END_FOR',
                'OPEN_PAREN',
                'CLOSE_PAREN',
                'END_STATEMENT',
                'DECLARE_TYPE',
                'ADD',
                'SUB',
                'MULT',
                'DIV',
                'LESS',
                'MORE',
                'LESS_EQ',
                'MORE_EQ',
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
            'expression : IF expression THEN expression END_IF'
        )
        @self.pg.production(
            'expression : IF expression THEN expression ELSE expression END_IF'
        )
        def expression_conditional_complete(p):
            if len(p) > 5:
                return p[3] if p[1].eval() else p[5]
            return p[3] if p[1].eval() else Nulo()

        @self.pg.production(
            'expression : FOR expression UNTIL expression STEP expression expression END_FOR'
        )
        def expression_control_loop(p):
            if isinstance(p[1], Identificador):
                if p[1].nome in self.vars.keys():
                    base = self.vars[p[1].nome]

            if isinstance(p[3], Identificador):
                if p[3].nome in self.vars.keys():
                    limite = self.vars[p[3].nome]

            if isinstance(base, Identificador) and isinstance(limite, Identificador):
                return ForLoop(base, limite, p[5], p[6])

            return ForLoop(p[1], p[3], p[5], p[6])

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

        @self.pg.production('expression : expression LESS expression')
        @self.pg.production('expression : expression MORE expression')
        @self.pg.production('expression : expression LESS_EQ expression')
        @self.pg.production('expression : expression MORE_EQ expression')
        def expression_bool(p):
            left = p[0]
            right = p[2]
            operator = p[1]

            if isinstance(p[0], Identificador):
                if p[0].nome in self.vars.keys():
                    left = self.vars[p[0].nome]

            if isinstance(p[2], Identificador):
                if p[2].nome in self.vars.keys():
                    right = self.vars[p[2].nome]

            if operator.gettokentype() == 'LESS':
                return Less(left, right)
            elif operator.gettokentype() == 'MORE':
                return More(left, right)
            elif operator.gettokentype() == 'LESS_EQ':
                return LessEqual(left, right)
            elif operator.gettokentype() == 'MORE_EQ':
                return MoreEqual(left, right)


        @self.pg.production('expression : expression ADD expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MULT expression')
        @self.pg.production('expression : expression DIV expression')
        def expression_arg(p):
            left = p[0]
            right = p[2]
            operator = p[1]

            if isinstance(p[0], Identificador):
                if p[0].nome in self.vars.keys():
                    left = self.vars[p[0].nome]

            if isinstance(p[2], Identificador):
                if p[2].nome in self.vars.keys():
                    right = self.vars[p[2].nome]

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
