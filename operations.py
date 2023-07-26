import WorksWIthFIle

"""
Module for working with files
"""


def __dir__():
    return []


# Function to list existing contacts
def ListContact() -> None:
    contactsList = WorksWIthFIle.ReadFile()
    print(f"There are {len(contactsList)} contacts.\n")
    print(f"{'name':^10} {'Surname':^10} {'Number':^10}")
    for contact in contactsList:
        print(f"{contact.get('name', ' '):10.10} {contact.get('surName', ' '):10.10} \
{contact.get('telNumber', ' '):11.11}")
    print()


# Function to search existing contact
def SearchContact() -> None:
    print("SEARCH A CONTACT: ")
    name = input("Name: ")
    surName = input("Surname: ")
    contactsList = WorksWIthFIle.SearchContactFromFile(name, surName)
    print("Phone number is: ", end="")
    for contact in contactsList:
        print(f"{contact.get('telNumber'):11.11}")
    print()


# Function to add a new contact
def AddContact() -> None:
    print("ADD NEW RECORD:")
    while True:
        name = input("Name: ")
        surName = input("Surname: ")
        telNumber = input("Telephone number: ")
        if 3 <= len(name) <= 10 and 3 <= len(surName) <= 15 and 3 <= len(telNumber) <= 11:
            print(f"New record: {name} {surName} {telNumber}")
            if AreYouSure():
                WorksWIthFIle.AddContactToFile(name, surName, telNumber)
                print("SAVED!\n")
            break
        else:
            print("ENTER AGAIN!")
            continue


# Function to delete an existing contact
def DeleteContact() -> None:
    print("DELETE RECORD:")
    name: str = input("Name: ")
    surName = input("Surname: ")
    contactsList = WorksWIthFIle.SearchContactFromFile(name, surName)
    print("Phone number is: ", end="")
    for contact in contactsList:
        print(f"{contact.get('telNumber'):11.11}")
    if AreYouSure():
        WorksWIthFIle.DeleteContactFromFile(contactsList)
        print("DELETED!")


# This function prompts the user to confirm the operation
def AreYouSure() -> bool:
    while True:
        answer = input("Are you sure? (Y)es/(N)o: ")
        print()
        if answer.upper() == "Y":
            return True
        elif answer.upper() == "N":
            return False
