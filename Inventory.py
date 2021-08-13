

player_inventory = {'rope' : 1, 'torch' : 6, 'gold coin' : 42, 'dagger' : 1, 'arrow' : 12}

def displayInventory(inventory):
	print('Inventory:')
	total=0
	for k, v in inventory.items():
		print(v,k)
		total=total+v
	print('The total number of items:',total)
displayInventory(player_inventory)