

player_inventory = {'rope' : 1, 'torch' : 6, 'gold coin' : 42, 'dagger' : 1, 'arrow' : 12}

def displayInventory(inventory):
	print('Inventory:')
	total=0
	for k, v in inventory.items():
		print(v,k)
		total=total+v
	print('\nThe total number of items:',total)
displayInventory(player_inventory)

print('\n' + ('=' * 60))

def displayInventory(inventory):
	print('\nInventory:')
	total=0
	for k, v in inventory.items():
		print(k.ljust(len(k)), str(v).rjust(25-len(k), '-'))
		total=total+v
	print('\nThe total number of items:',total)
displayInventory(player_inventory)