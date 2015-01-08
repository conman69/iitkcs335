# Harpreet Singh - 10282
# Install ply module for python to run this code

import sys,ply.lex




keywords = {'if':'IF','else':'ELSE','return':'RETURN'}


tokens = ['EQUALS','REALNUMBER','INT_CONST','HEXANUM','EXPONENTIALNUM','ADDITION','SUBTRACTION','MULTIPLICATION','DIVISION','POWER','EXPONENTIAL','PARENL','PARENR','SEMICOLON','IDENTIFIER','BLOCK_BEGIN','BLOCK_END',]+list(keywords.values())



t_ignore		= ' \t\n'
t_REALNUMBER		= r'(\d*\.\d+)|(\d+\.\d*)'
t_INT_CONST		= r'\d+'
#t_HEXANUM		= r'0[xX][0-9a-fA-F]+'
#t_EXPONENTIALNUM	= r'((\d*\.\d+)|(\d+\.\d*)|\d+)(e|E)(\+|-)?\d+'
#t_ADDITION		= r'\+'
#t_SUBTRACTION		= r'-'
#t_MULTIPLICATION	= r'\*'
#t_DIVISION		= r'/'
#t_POWER		= r'\^'
#t_EXPONENTIAL		= r'exp'
t_PARENL		= r'\('
t_PARENR		= r'\)'
t_SEMICOLON             = r'\;'
t_BLOCK_BEGIN   	= r'\{'
t_BLOCK_END 		= r'\}'
t_EQUALS  		= r'=='



def t_error(t):
    print "Unrecognized char skipped : '%s'" % t.value[0]
    t.lexer.skip(1)

def t_IDENTIFIER(t):
    r"[a-zA-Z$_][\w$]*"
    t.type = keywords.get(t.value,'IDENTIFIER')
    return t

lexer = ply.lex.lex()

#data = raw_input('Enter expression to evaluate: ')
#lexer.input(data)

def lex_output(raw_input):
    data = open(raw_input).read()
    lexer.input(data)

    fo = open("foo.txt","w")

    for tok in lexer:
	fo.write('('+tok.value+'\t\t\t\t\t"'+tok.type+'")\n')

    fo.close()

if __name__ == "__main__":
	from sys import argv
	filename, raw_input = argv
	lex_output(raw_input)
