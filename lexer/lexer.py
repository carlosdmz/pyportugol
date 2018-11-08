from rply import LexerGenerator

from ebnf.ebnf import EBNF


class Lexer(object):

    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('PRINT', EBNF['KEYWORDS']['PRINT'])
        self.lexer.add('READ', EBNF['KEYWORDS']['READ'])
        self.lexer.add('IF', EBNF['KEYWORDS']['IF'])
        self.lexer.add('ELSE', EBNF['KEYWORDS']['ELSE'])
        self.lexer.add('FOR', EBNF['KEYWORDS']['FOR'])
        self.lexer.add('UNTIL', EBNF['KEYWORDS']['UNTIL'])
        self.lexer.add('PASS', EBNF['KEYWORDS']['PASS'])
        self.lexer.add('INT', EBNF['KEYWORDS']['INT'])
        self.lexer.add('END_FOR', EBNF['KEYWORDS']['END_FOR'])
        self.lexer.add('OPEN_PAREN', EBNF['DELIMITERS']['open_paren'])
        self.lexer.add('CLOSE_PAREN', EBNF['DELIMITERS']['close_paren'])
        self.lexer.add('END_STATEMENT', EBNF['DELIMITERS']['end_statement'])
        self.lexer.add('DECLARE_TYPE', EBNF['DELIMITERS']['declare_type'])
        self.lexer.add('ADD', EBNF['ARITHMETIC']['add'])
        self.lexer.add('SUB', EBNF['ARITHMETIC']['sub'])
        self.lexer.add('MULT', EBNF['ARITHMETIC']['mult'])
        self.lexer.add('DIV', EBNF['ARITHMETIC']['div'])
        self.lexer.add('ATTR', EBNF['LOGIC']['equals'])
        self.lexer.add('NUMBER', EBNF['DATA']['NUMBER'])
        self.lexer.add('STRING', EBNF['DATA']['STRING'])
        self.lexer.add('IDENT', EBNF['IDENT'])
        self.lexer.ignore('\s+')
        self.lexer.ignore(r'\n')

    def get_lexer(self):
        self._add_tokens()

        return self.lexer.build()
