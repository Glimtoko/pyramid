import ply.lex as lex
import ply.yacc as yacc

import pyramid

# pyramid of token names
tokens = (
    'NUMBER',
    'PRINT'
)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
t_PRINT = 'p'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# YACC
def p_expression_pyramid(p):
    'expression : pyramid'
    p[0] = p[1]


def p_pyramid_number(p):
    'pyramid : NUMBER'
    p[0] = pyramid.Pyramid(p[1])


def p_pyramid_pyramid_number(p):
    'pyramid : pyramid NUMBER'
    p[0] = p[1]
    p[0].add(p[2])


def p_intermediate_print(p):
    'pyramid : pyramid PRINT'
    p[0] = p[1]
    print(p[0])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    print("Token was:", p)


lexer = lex.lex()
parser = yacc.yacc()
