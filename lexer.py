# Harpreet Singh - 10282
# Install ply module for python to run this code

import sys,ply.lex

tokens = ('REALNUMBER','INT_CONST','HEXANUM','EXPONENTIALNUM','ADDITION','SUBTRACTION','MULTIPLICATION','DIVISION','POWER','EXPONENTIAL','PARENL','PARENR','SEMICOLON','BLOCK_BEGIN','BLOCK_END',)

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



def t_error(t):
    print "Unrecognized char skipped : '%s'" % t.value[0]
    t.lexer.skip(1)

lexer = ply.lex.lex()

#data = raw_input('Enter expression to evaluate: ')
#lexer.input(data)

def lex_output(raw_input):
    data = open(raw_input).read()
    lexer.input(data)

    for tok in lexer:
        # Open a file
	fo = open("foo.txt", "a")
	fo.write('('+tok.value+'\t\t\t\t\t"'+tok.type+'")\n')
	# Close opened file
	fo.close()

if __name__ == "__main__":
	from sys import argv
	filename, raw_input = argv
	lex_output(raw_input)
