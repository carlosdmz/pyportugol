EBNF = {
    'KEYWORDS': {
        'desc': 'Palavras chaves',
        'PRINT': r'imprima',
        'READ': r'leia',
        'IF': r'se',
        'THEN': r'entao',
        'ELSE': r'senao',
        'END_IF': r'fim_se',
        'FOR': r'para',
        'UNTIL': r'ate',
        'STEP': r'passo',
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
        'equals': r'==',
        'less': r'<',
        'more': r'>',
        'less_or_equal': r'<=',
        'more_or_equal': r'>=',
    },
    'DATA': {
        'NUMBER': r'\d+',
        'STRING': r'".*?"'
    },
    'IDENT': r'\w+',
}
