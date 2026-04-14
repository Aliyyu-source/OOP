from file_handler import FileHandler
from item import Item
filename = "inventory.csv"
inventory_file = FileHandler(filename)
rows= inventory_file.read() 
print(f'#####{filename}####')
for row in rows:
    item = Item.deserialize(row)
    item.display_price()

print(f'#####End of {filename}#####')