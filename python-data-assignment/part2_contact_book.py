contacts = {
    "Raj": "9876543210",
    "Ankit": "9123456780",
    "Pritam": "9000011111"
}

print("All Contacts:")
for name, phone in contacts.items():
    print(name, ":", phone)

search_name = input("Enter name to search: ")

if search_name in contacts:
    print("Phone Number:", contacts[search_name])
else:
    print("Contact not found")
