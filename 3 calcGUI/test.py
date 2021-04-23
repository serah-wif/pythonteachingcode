names = []
phone_numbers = []
num = 3

for i in range(num):
    name = input("Name:")
    phone_number = input("phone_number: ")
names.append(name)
phone_numbers.append(phone_number)
#print(names)
#print(phone_numbers)

print("\nName\t\t\tphone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[0], phone_numbers[0]))
    #print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

search_term = input("\nEnter search Term: ")
print("Search Results")
if search_term in names:
   index = names.index(search_term)
   phone_number = phone_numbers[index]
   print("Name {}, phone Number: {}". format(search_term, phone_number))

else:
    print("Name not found")
    