menu = {"cheeseburger": 5.99,
        "chicken sandwich": 3.44,
        "veggie wrap": 2.55,
        "beef tacos": 5.60
}

running = False

keys = menu.keys()
menuKeys = []
startShop = input('Press s to order: ')
total = 0.0
       
if startShop == 's':
    
        for i, key in enumerate(keys):
                print(f'{i}. {key}')
        running = True
                
while running == True:
        for key in keys:
                menuKeys.append(key)

        select = int(input('\n' + 'Select food from the menu(10 to quit): '))
        if select == 10:
                break
        else:
                print(f'Order for {menuKeys[select]} has been placed.')
                total += menu.get(menuKeys[select])

print('---------------------')
print(f'Total: ${total}')

     
        


