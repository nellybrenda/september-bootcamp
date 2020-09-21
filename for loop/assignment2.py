firstName = input("Enter First Name ")
lastName = input("Enter Last Name ")
organization = input("Enter Organization Name ")

print("\n")
print('{0}, {1} works at {2}'.format(firstName, lastName, organization))
print('{1}, {0} works at {2}'.format(firstName, lastName, organization))
print('FirstName {0}, LastName {1} works at {2}'.format(firstName, lastName, organization))
print('{0}, {1} {0}, {1} works at {2}'.format(firstName, lastName, organization))