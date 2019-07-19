#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	19/07/2019 23:31:19
#+ Editado:	19/07/2019 23:43:19
#------------------------------------------------------------------------------------------------
import sys
#------------------------------------------------------------------------------------------------
def code(integer):
	chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	sign = '-' if integer < 0 else ''
	integer = abs(integer)
	result = ''

	while integer > 0:
		integer, remainder = divmod(integer, 36)
		result = chars[remainder]+result

	return sign+result
#------------------------------------------------------------------------------------------------
def decode(number):
	return int(number, 36)
#------------------------------------------------------------------------------------------------
def menu(args):
	if '-c' in args:
		return code(int(args[args.index('-c')+1]))

	if '-d' in args:
		return decode(args[args.index('-d')+1])
#------------------------------------------------------------------------------------------------
if __name__=="__main__":
	if len(sys.argv)>1:
		if sys.argv[1]=='-?':
			print('axuda')
		
		elif sys.argv[1]=='-h':
			print('axuda')
		
		else:
			print(menu(sys.argv[1:]))
	else:
		print('Erro: Faltan argumentos')
#------------------------------------------------------------------------------------------------