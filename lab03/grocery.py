grocery_list = []
print("Welcome to Your Shopping List!")
print()
print("Please make a selection from one of the following options:")
print()
print("1. Add an item to the shopping list.")
print("2. Display the shopping list.")
print("3. Display the item count.")
print("4. Display the first item in the shopping list.")
print("5. Display the last item in the shopping list.")
print("6. Clear the shopping list.")
print()
selection = input("Selection: ")
if selection == "1":
    item = input("Item to add: ")
    grocery_list.append(item)
elif selection == "2":
    print(grocery_list)
elif selection == "3":
    print (f"ITEM COUNT: {len(grocery_list)}")
elif selection == "4":
    print(f"FIRST ITEM: {grocery_list[0]}")
elif selection == "5":
    print(f"LAST ITEM: {grocery_list[-1]}")
elif selection == "6":
    grocery_list = []
else:
    print("You entered an invalid option.")
    print("Goodbye!")

