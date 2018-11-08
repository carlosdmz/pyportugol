EBNF = {
    'KEYWORDS': {
        'desc': 'Palavras chaves',
        'PRINT': r'imprima',
        'READ': r'leia',
        'IF': r'se',
        'ELSE': r'senao',
        'FOR': r'para',
        'UNTIL': r'ate',
        'PASS': r'passo',
        'INT': r'inteiro',
        'END_FOR': r'fim_para'
    },
    'DELIMITERS': {
        'open_paren': r'\(',
        'close_paren': r'\)',
        'end_statement': r'\;',
        'declare_type': r'\:'
    },
    'ARITHMETIC': {
        'add': r'\+',
        'sub': r'\-',
        'mult': r'\*',
        'div': r'\/'
    },
    'LOGIC': {
        'equals': r'='
    },
    'DATA': {
        'NUMBER': r'\d+',
        'STRING': r'".*"'
    },
    'IDENT': r'\w+',
}
