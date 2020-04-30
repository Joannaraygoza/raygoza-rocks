"""
This is a simple accounting program in Spanish.
For each item, the user should enter the item name, cost, and date of purchase.
When the user is finished, they should type 'parar' for the name of the item.
The program will write each line item to a text file,
and at the end it will calculate the sales tax and grand total;
these will also be written to the text file.
"""

recuento = 0
entrada = 0
subtotal = 0
lista = []

with open('cuenta.txt', 'w') as archivo:
	archivo.write('Item          Cuesta        Fecha      Subtotal \n')
	
	while recuento < 10 and entrada != 'parar':
		print('''Por favor, entras el nombre, cuesta, y fecha de comprar por cada item. Si has terminado, entras 'parar'.''')
	
		nombre = (input("Nombre del item: ")).lower()
		if nombre == 'parar':
			break
		nombre = nombre[0].upper() + nombre[1:]
		cuesta = float(input("Cuesta del item: "))
		fecha = input("Fecha de comprar: ")
		subtotal += cuesta
		str_cuesta = f'{cuesta:.2f}'
		print('------------')
		
		#attempt to pretty up the text output by aligning it into columns
		espacios1 = 20 - (len(nombre) + len(str_cuesta))
		nombre_cuesta = nombre + (espacios1 * ' ') + str_cuesta
		archivo.write(nombre_cuesta)
		
		espacios2 = 13 - len(fecha)
		fecha_linda = espacios2*' ' + fecha
		archivo.write(fecha_linda)
		
		str_subtotal = f'{subtotal:.2f}'
		subtotal_linda = ' '*(14 - len(str_subtotal)) + str_subtotal + '\n'
		archivo.write(subtotal_linda)
		
		recuento += 1
		
	impuesto = subtotal * 0.1025
	gran_total = subtotal + impuesto
	archivo.write(f'\n\nTienes {recuento} items.\n')
	archivo.write(f'El impuesto a las ventas de tu compra es {impuesto}.\n')
	archivo.write(f'El gran total de tu cuenta es {gran_total}.\n')
	archivo.write(f'Gracias por comprar con nosotros.')
