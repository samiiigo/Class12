size_of_rec = 20
with open ('names.dat','wb') as fl:
    print('\n\n     ----------MENU-DRIVEN-PROGRAM----------\n')
    print('''1. Total no of records
2. Add a record
3. Display all records
4. Search for a Record
0. Quit''')
    choice = int(input('Enter Choice: '))
    if choice == 1:
        ans = 'y'
        while ans.lower() == 'y':
            name = input ("Enter Name : ")
            l = len(name)
            name = name+(size_of_rec-l)*' '
            fl.write(name.encode())
            fl.flush()
            ans = input("Add More ?")
    elif choice == 2:
        

    

