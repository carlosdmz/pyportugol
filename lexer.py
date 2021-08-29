from rply import LexerGenerator

from ebnf import EBNF


class Lexer(object):
    """
        Adds tokens defined in EBNF to be built into the lexer.
        Lexer definitions matches EBNF definition.
    """
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Keywords tokens
        self.lexer.add('PRINT', EBNF['KEYWORDS']['PRINT'])
        self.lexer.add('READ', EBNF['KEYWORDS']['READ'])
        self.lexer.add('IF', EBNF['KEYWORDS']['IF'])
        self.lexer.add('THEN', EBNF['KEYWORDS']['THEN'])
        self.lexer.add('ELSE', EBNF['KEYWORDS']['ELSE'])
        self.lexer.add('END_IF', EBNF['KEYWORDS']['END_IF'])
        self.lexer.add('FOR', EBNF['KEYWORDS']['FOR'])
        self.lexer.add('UNTIL', EBNF['KEYWORDS']['UNTIL'])
        self.lexer.add('STEP', EBNF['KEYWORDS']['STEP'])
        self.lexer.add('INT', EBNF['KEYWORDS']['INT'])
        self.lexer.add('END_FOR', EBNF['KEYWORDS']['END_FOR'])

        # Delimiters tokens
        self.lexer.add('OPEN_PAREN', EBNF['DELIMITERS']['open_paren'])
        self.lexer.add('CLOSE_PAREN', EBNF['DELIMITERS']['close_paren'])
        self.lexer.add('END_STATEMENT', EBNF['DELIMITERS']['end_statement'])
        self.lexer.add('DECLARE_TYPE', EBNF['DELIMITERS']['declare_type'])

        # Arithmetic op's tokens
        self.lexer.add('ADD', EBNF['ARITHMETIC']['add'])
        self.lexer.add('SUB', EBNF['ARITHMETIC']['sub'])
        self.lexer.add('MULT', EBNF['ARITHMETIC']['mult'])
        self.lexer.add('DIV', EBNF['ARITHMETIC']['div'])

        # Logic tokens
        self.lexer.add('ATTR', EBNF['LOGIC']['equals'])
        self.lexer.add('LESS', EBNF['LOGIC']['less'])
        self.lexer.add('MORE', EBNF['LOGIC']['more'])
        self.lexer.add('LESS_EQ', EBNF['LOGIC']['less_or_equal'])
        self.lexer.add('MORE_EQ', EBNF['LOGIC']['more_or_equal'])

        # Data tokens
        self.lexer.add('NUMBER', EBNF['DATA']['NUMBER'])
        self.lexer.add('STRING', EBNF['DATA']['STRING'])
        self.lexer.add('IDENT', EBNF['IDENT'])

        # Spaces and new lines ignore rules in the parser
        self.lexer.ignore('\s+')
        self.lexer.ignore(r'\n')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
