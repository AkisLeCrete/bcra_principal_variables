import datetime

hoy = datetime.datetime.today()
dia_hoy = hoy.day
mes_hoy = hoy.month
anio_hoy = hoy.year
fecha_hoy = [dia_hoy, mes_hoy, anio_hoy]

print(hoy + datetime.datetime.day('30''))
