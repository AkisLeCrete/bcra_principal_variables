#pylint:disable=E0602
#pylint:disable=W0101
import requests
from bs4 import BeautifulSoup


# Creo una funcion que devuelve los datos que este buscando dentro de la web de principales variables del bcra
# para luego volver a llamarla a traves de otras funciones]
def extractor_principales_variables(argumento):
	# Variables resultado_provisorio y resultado
	resultado = []
	
	# Request a URL de las principales variables del BCRA más su Soup que ingreso en una lista]
	principales_variables_bcra = requests.get('https://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables.asp')
	soup_principales_variables_bcra = BeautifulSoup(principales_variables_bcra.text, 'lxml')
	filtro = 'tbody>tr>td'
	lista =  soup_principales_variables_bcra.select(filtro)
	
	# Recorro la lista con un For buscando el texto donde se encuentra la tasa del plazo fijo en pesos y almaceno
	# en la lista resultado los dos lugares posteriores que son los que devuelven la fecha y la tasa
	contador = 0
	for element in lista:
		if argumento in str(element):
			resultado.append(str(lista[contador + 1].getText()))
			resultado.append(str(lista[contador + 2].getText()))
		contador += 1
	
	return resultado
	

# Valor de la tasa de PF
def valor_pf():
	return extractor_principales_variables('Tasa mínima para plazos fijos de personas humanas hasta $10 millones (en % n.a.)')


# Valor del UVA
def valor_uva():
	return extractor_principales_variables('Unidad de Valor Adquisitivo (UVA)')


# Valor de las Reservas Internacionales
def valor_reservas():
	return extractor_principales_variables('Reservas Internacionales del BCRA')
	

# Valor del tipo de cambio minorista Promedio Vendedor
def tc_min_prom_vendedor():
	return extractor_principales_variables('Tipo de Cambio Minorista ($ por US$) Comunicación B 9791')
	

# Valor de tasa BADLAR
def valor_badlar():
	return extractor_principales_variables('BADLAR en pesos de bancos privados (en % n.a.)')

	
# Valor de la Base monetaria
def valor_bm():
	return extractor_principales_variables('Base monetaria')
	

# Valor de 
def valor_inflacion_mensual():
	return extractor_principales_variables('Inflación mensual')
	

# Valor de 
def valor_inflacion_interanual():
	return extractor_principales_variables('Inflación interanual')
	

# Valor de 
def valor_cer():
	return extractor_principales_variables('CER')