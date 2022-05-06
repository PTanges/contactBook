from Contact import Contact
import pickle

def load_contacts():
   """ Unpickle the data on mydata.dat and save it to a dictionary
   Return an empty dictionary if the file doesn't exist """
   try:
      with open("mydata.dat", 'rb') as file:
         return pickle.load(file)
   except FileNotFoundError:
      return {}


def save_contacts(contacts):
   """ Serialize and save the data in the 'contacts' dictionary """
   with open("mydata.dat", 'wb') as file:
      pickle.dump(contacts, file)


def add(contacts):
   """ Ask the user to add a contact to the 'contacts' dictionary
   Do not allow duplicate names """
   name = input("Name: ")
   if name in contacts:
      print("An entry already exists for that contact!")
      return

   email = input("Email: ")
   entry = Contact(name, email)

   # Add phone numbers to the new Contact object until the user decides to stop
   while True:
      next_num = input("Enter a phone number (or -1 to stop): ")
      if next_num == "-1":
         break
      entry.add_number(next_num)

   # Add the new Contact object to the dictionary
   contacts[name] = entry


def look_up(contacts):
   """ Print the information related to the given name (if it exists in the dictionary) """
   name = input("Enter a name: ")
   if name in contacts:
      print(contacts[name])
   else:
      print("There is no contact with that name")


def delete(contacts):
   """ Delete the contact associated with the name the user enters (if it exists in the dictionary) """
   name = input("Enter a name to remove from your list of contacts: ")
   if name in contacts:
      print("Are you sure you want to delete the following contact? ")
      print(contacts[name])
      choice = input("'y' or 'n': ")
      if choice == 'y':
         del contacts[name]
      else:
         print("Contact saved in dictionary")
   else:
      print("There is no contact with that name")

def edit(contacts):
   """ Edit existing contact's name, add or delete phone numbers, edit email
       Remove key/value pair if name is edited """
   name = input("Enter a name: ")
   if name not in contacts:
      print("There is no contact with that name")
      return
   else:
      while True:
        choice = int(input("\nEnter\n6) edit existing name\n7) edit existing email\n8) add new phone numbers\n9) remove an existing phone number\n0) quit editing session\nCommand: "))
        if choice == 6:
           new_name = input("Enter the new name or 0 to quit: ")
           if new_name in contacts:
             print("That name already exists")
           elif new_name == "0":
             pass
           else:
             # Create a temp copy and transfer over data. Add entry. Then delete original key/value pair
             entry = Contact(new_name, contacts[name].email)
             phone_numbers = contacts[name].phone_numbers # Temp list to iterate from
             for phoneNum in phone_numbers:
               entry.add_number(phoneNum)
             contacts[new_name] = entry
             contacts.pop(name)
        elif choice == 7:
           email = input("Enter the new email: ")
           contacts[name].email = email
        elif choice == 8:
         while True:
          next_num = input("Enter a phone number (or -1 to stop): ")
          if next_num == "-1":
           break
          contacts[name].add_number(next_num) # Data validation already handled in add_number()
        elif choice == 9:
         while True:
          next_num = input("Enter a phone number (or -1 to stop): ")
          if next_num == "-1":
           break
          contacts[name].remove_number(next_num)
        elif choice == 0:
           break


def main():
   contacts = load_contacts()

   ### Ask the user what to do next each loop iteration
   while True:
      choice = int(input("\nEnter\n1) add a contact\n2) lookup a contact\n3) delete a contact\n4) edit a contact\n5) quit program\nCommand: "))
      if choice == 1:
         add(contacts)
      elif choice == 2:
         look_up(contacts)
      elif choice == 3:
         delete(contacts)
      elif choice == 4:
         edit(contacts)
      elif choice == 5:
         break

   save_contacts(contacts)
   print("Program shutting down...")


main()