import prettytable as pt
#Creating a prettytable object.
table = pt.PrettyTable()
table.add_column("Name",['Yethishwar','Chintu','Siddhartha','Sai kiran','Preethi'])
table.add_column('Marks',[98,89,100,99,70])
table.align = 'l' #Alligned data to the left
print(table)
