def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"Added '{item}' to shopping list.")
            else:
                print("Item cannot be empty.")
                
        elif choice == '2':
            # Prompt for and remove an item
            if shopping_list:
                item = input("Enter item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"Removed '{item}' from shopping list.")
                else:
                    print(f"'{item}' not found in shopping list.")
            else:
                print("Shopping list is empty!")
                
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nYour Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
                print(f"Total: {len(shopping_list)} items")
            else:
                print("Your shopping list is empty.")
                
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()