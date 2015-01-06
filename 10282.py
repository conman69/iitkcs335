# Harpreet Singh - 10282
# Install ply module for python to run this code

import sys,ply.lex

tokens = ('REALNUMBER','INTEGERNUMBER','HEXANUM','EXPONENTIALNUM','ADDITION','SUBTRACTION','MULTIPLICATION','DIVISION','POWER','EXPONENTIAL','PARENL','PARENR',)

t_ignore			= ' \t'
t_REALNUMBER		= r'(\d*\.\d+)|(\d+\.\d*)'
t_INTEGERNUMBER		= r'\d+'
t_HEXANUM			= r'0[xX][0-9a-fA-F]+'
t_EXPONENTIALNUM	= r'((\d*\.\d+)|(\d+\.\d*)|\d+)(e|E)(\+|-)?\d+'
t_ADDITION			= r'\+'
t_SUBTRACTION		= r'-'
t_MULTIPLICATION	= r'\*'
t_DIVISION			= r'/'
t_POWER				= r'\^'
t_EXPONENTIAL		= r'exp'
t_PARENL			= r'\('
t_PARENR			= r'\)'

def t_error(t):
    print "Unrecognized char skipped : '%s'" % t.value[0]
    t.lexer.skip(1)

lexer = ply.lex.lex()

data = raw_input('Enter expression to evaluate: ')
lexer.input(data)

for tok in lexer:
    print ('('+tok.type+', "'+tok.value+'")')