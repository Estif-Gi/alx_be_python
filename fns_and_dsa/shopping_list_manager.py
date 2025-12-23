def display_menu():
    print("\n" + "="*20)
    print("Shopping List Manager")
    print("="*20)
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("="*20)


def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"✓ '{item}' has been added to your shopping list.")
    else:
        print("No item entered. Nothing was added.")


def remove_item(shopping_list):
    if not shopping_list:
        print("Your shopping list is already empty!")
        return
    
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"✓ '{item}' has been removed from your shopping list.")
    else:
        print(f"✗ '{item}' was not found in your shopping list.")


def view_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty.")
        return
    
    print("\nYour Current Shopping List:")
    print("-" * 30)
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")
    print("-" * 30)


def main():
    shopping_list = []
    print("Welcome to the Shopping List Manager!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_item(shopping_list)
        
        elif choice == '2':
            remove_item(shopping_list)
        
        elif choice == '3':
            view_list(shopping_list)
        
        elif choice == '4':
            print("\nGoodbye! Happy shopping! 🛒")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()