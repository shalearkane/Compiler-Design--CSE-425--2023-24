# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('ANONYMOUS_IDENTIFIER', 'CHARACTER', 'COMMENT', 'ELLIPSIS', 'FLOAT', 'INTEGER', 'LOWERCASE_IDENTIFIER', 'MAJOR_KEYWORD', 'MINOR_KEYWORD', 'OPERATORS', 'PUNCTUATION', 'STRING', 'UPPERCASE_IDENTIFIER'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_COMMENT>(%.*)|(/\\*(.*(\\n)*)*\\*/))|(?P<t_newline>\\n+)|(?P<t_MAJOR_KEYWORD>\\b(class|clauses|constants|constructors|delegate|domains|end|facts|goal|implement|inherits|interface|monitor|namespace|open|predicates|properties|resolve|supports|where)\\b)|(?P<t_MINOR_KEYWORD>\\b(align|and|anyflow|as|bitsize|catch|determ|digits|div|do|else|elseif|erroneous|externally|failure|finally|foreach|from|guard|if|in|language|mod multi|nondeterm|otherwise|or|orelse|procedure|quot|rem|single|then|to|try)\\b)|(?P<t_ELLIPSIS>\\.\\.\\.)|(?P<t_FLOAT>[-+]?[0-9]+(\\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+))|(?P<t_PUNCTUATION>:-|::|[;!,.#\\[\\]\\|(){}:])|(?P<t_INTEGER>[-]?((0o[0-7]+)|(0x[0-9a-fA-F]+)|([0-9]+)))|(?P<t_LOWERCASE_IDENTIFIER>\\b[a-z][a-zA-Z0-9_]*\\b)|(?P<t_UPPERCASE_IDENTIFIER>\\b[_A-Z][a-zA-Z0-9_]*\\b)|(?P<t_ANONYMOUS_IDENTIFIER>_)|(?P<t_OPERATORS>~~|\\+\\+|\\*\\*|\\^\\^|>>|<<|<>|><|<=|>=|:=|==|\\^|/|\\*|\\+|-|=|<|>)|(?P<t_CHARACTER>\'.\')|(?P<t_STRING>\'.+\'|\\".*\\")', [None, ('t_COMMENT', 'COMMENT'), None, None, None, None, ('t_newline', 'newline'), ('t_MAJOR_KEYWORD', 'MAJOR_KEYWORD'), None, ('t_MINOR_KEYWORD', 'MINOR_KEYWORD'), None, ('t_ELLIPSIS', 'ELLIPSIS'), ('t_FLOAT', 'FLOAT'), None, None, None, ('t_PUNCTUATION', 'PUNCTUATION'), ('t_INTEGER', 'INTEGER'), None, None, None, None, ('t_LOWERCASE_IDENTIFIER', 'LOWERCASE_IDENTIFIER'), ('t_UPPERCASE_IDENTIFIER', 'UPPERCASE_IDENTIFIER'), ('t_ANONYMOUS_IDENTIFIER', 'ANONYMOUS_IDENTIFIER'), ('t_OPERATORS', 'OPERATORS'), ('t_CHARACTER', 'CHARACTER'), ('t_STRING', 'STRING')])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
