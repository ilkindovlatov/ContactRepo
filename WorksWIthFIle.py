import pickle
import os

"""
Module for working with files
"""


def __dir__():
    return []


# Function to delete a record from the binary record file
def DeleteContactFromFile(contactsListPar: list) -> None:
    contactsList = ReadFile()
    for contact in contactsList:
        for contactForDelete in contactsListPar:
            if contact.get("name") == contactForDelete.get("name") and contact.get("surName") == contactForDelete.get(
                    "surName"):
                contactsList.remove(contactForDelete)
                continue
    WriteFile(contactsList)


# Function to add a new contact to the binary record file
def AddContactToFile(namePar: str, surNamePar: str, telNumberPar: str):
    contactsList = ReadFile()
    contactDict = dict(name=namePar, surName=surNamePar, telNumber=telNumberPar)
    contactsList.append(contactDict)
    WriteFile(contactsList)


# Function to search a record from the binary record file
def SearchContactFromFile(namePar: str, surNamePar: str) -> list:
    contactsList = ReadFile()
    responseList = list()
    for contact in contactsList:
        if contact.get("name").upper() == namePar.upper() and contact.get("surName").upper() == surNamePar.upper():
            responseList.append(contact)
        else:
            print('"NO MATCHING CONTACT FOUND!"')

    return responseList


# Function to write records to the binary record file
def WriteFile(contactsListPar: list) -> None:
    with open("data.bin", "wb") as fileObject:
        pickle.dump(contactsListPar, fileObject)


# Function to read records from the binary record file
def ReadFile() -> list:
    if os.path.isfile("data.bin"):
        with open("data.bin", "rb") as fileObject:
            contactsList = pickle.load(fileObject)
    else:
        contactsList = list()
    return contactsList
