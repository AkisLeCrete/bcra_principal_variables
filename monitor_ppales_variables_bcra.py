import datos_bcra

print('-------------------------------------------')
print('PRINCIPALES INDICADORES DE LA WEB DEL BCRA:')
print('-------------------------------------------\n')
print('-'*10+'\t\t\t'+'-'*7+'\t\t'+'-'*7)
print('Indicador:\t\t\t Fecha:\t\t Valor:')
print('-'*10+'\t\t\t'+'-'*7+'\t\t'+'-'*7+'\n')

def print_rdo(nombre, funcion):
	arg_1 = funcion()[0]
	arg_2 = funcion()[1]
	if len(nombre) <= 8:
		return f'{nombre}\t\t\t\t{arg_1}\t{arg_2}'
	if len(nombre) >= 8 and len(nombre) < 16:
		return f'{nombre}\t\t\t{arg_1}\t{arg_2}'
	if len(nombre) >= 16 and len(nombre) <= 24:
		return f'{nombre}\t\t{arg_1}\t{arg_2}'
	if len(nombre) > 24:
		return f'{nombre}\t{arg_1}\t{arg_2}'

print(print_rdo('Dolar Minorista TCv Promedio:', datos_bcra.tc_min_prom_vendedor))
print(print_rdo('Tasa de Plazo Fijo:', datos_bcra.valor_pf))
print(print_rdo('UVA:', datos_bcra.valor_uva))
print(print_rdo('CER:', datos_bcra.valor_cer))	
print(print_rdo('Inflacion Mensual:', datos_bcra.valor_inflacion_mensual))
print(print_rdo('Inflacion Anualizada:', datos_bcra.valor_inflacion_interanual))
print(print_rdo('Tasa BADLAR:', datos_bcra.valor_badlar))
print(print_rdo('Base Monetaria:', datos_bcra.valor_bm))
print(print_rdo('Reservas (en millones de $):', datos_bcra.valor_reservas))

