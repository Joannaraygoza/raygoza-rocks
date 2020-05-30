"""
This is a simple accounting program in Spanish.
For each item, the user should enter the item name, cost, and date of purchase.
When the user is finished, they should type 'parar' for the name of the item.
The program will write each line item to a text file,
and at the end it will calculate the sales tax and grand total;
these will also be written to the text file.
"""

count = 0
item_name = None
subtotal = 0
item_list = []

with open('cuenta.txt', 'w') as outfile:
    outfile.write('Item      Cuesta del item         Fecha          Subtotal \n')
    
    while count < 10 and item_name != 'parar':
        print("Por favor, entras el nombre, cuesta, y fecha"
              " de comprar por cada item. Si has terminado, entras 'parar'.")
    
        item_name = (input("Nombre del item: ")).lower()
        if item_name == 'parar':
            break

        #Capitalize first letter of the item for the output file
        item_name = item_name[0].upper() + item_name[1:]

        try:    #Cost entry: Check to be sure they enter a number for cost
            cost = float(input("Cuesta del item: "))
        except ValueError:
            print("Lo siento, necesitas entrar un numero por la cuesta.")
            exit()

        purchase_date = input("Fecha de comprar: ")

        subtotal += cost
        str_cost = f'{cost:.2f}'
        print('------------')
        
        #Print the item details to a text file, with column alignment
        spaces1 = 23 - (len(item_name) + len(str_cost))
        nameandcost = f'{item_name}{spaces1 * " "} ${str_cost}'
        outfile.write(nameandcost)
        
        spaces2 = 13 - len(purchase_date)
        print_date = f'{spaces2*" "} {purchase_date}'
        outfile.write(print_date)
        
        str_subtotal = f'{subtotal:.2f}'
        print_subtotal = f'{" "*(16 - len(str_subtotal))} ${str_subtotal}\n'
        outfile.write(print_subtotal)
        
        count += 1
        
    tax = subtotal * 0.1025
    grand_total = subtotal + tax
    outfile.write(f'\n{"-"*57}\n')
    outfile.write(f'\nTienes {count} items.\n')
    outfile.write(f'El impuesto a las ventas de tu compra es ${tax:.2f}.\n')
    outfile.write(f'El gran total de tu cuenta es ${grand_total:.2f}.\n')
    outfile.write(f'Gracias por comprar con nosotros.')
