import operations


# Function to print main menu
def DisplayMenu() -> None:
    print("1. List contacts")
    print("2. Search contact")
    print("3. Add a new contact")
    print("4. Delete a contact")
    print("5.exit")
    print()


# Loop for display menu
def MenuLoop() -> str:
    while True:
        DisplayMenu()
        option = input("Choose an option(1-5)")
        print("\n")
        try:
            if 1 <= int(option) <= 5:
                break
        except: ValueError
        print("ENTER ONLY NUMBERS(1-5)")
        

    return option


# Function to direct user a function which he chooses
def MainLoop() -> None:
    while True:
        option = MenuLoop()
        if option == "1":
            operations.ListContact()
        elif option == "2":
            operations.SearchContact()
        elif option == "3":
            operations.AddContact()
        elif option == "4":
            operations.DeleteContact()
        elif option.lower() == "5" or "exit":
            break


MainLoop()
