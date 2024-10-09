import pickle
import tabulate

def addRecord():
  f1=open('emp.dat', 'ab')
  while True:
    emp=[]
    print('\n\tAdding New Employee')
    eno=int(input('Enter Employee Number: '))
    emp.append(eno)
    ename=input('Enter Employee Name: ')
    emp.append(ename)
    subject=input('Enter Subject: ')
    emp.append(subject)
    dept=input('Enter Department Name: ')
    emp.append(dept)
    salary=float(input('Enter Employee Salary: '))
    emp.append(salary)
    pickle.dump(emp,f1)
    ch1=input('Do you want to add more employee(y/n)? ')
    if ch1.lower()=='y':
      continue
    else:
      break
  f1.close()

def displayAllRecords():
  emp=[]
  with open('emp.dat', 'rb') as f1:
    #print(tabulate.tabulate(header))
    while True:
      try:
        emp.append(pickle.load(f1))
      except:
        print('Read all records.')
        break
  print(tabulate.tabulate(emp, headers=['Emp. No.', 'Employee Name', 'Subject', 'Department', 'Salary'],tablefmt="pretty"))

def SearchRecord():
  id_search = input("Enter the ID of the employee to search : ")
  with open ('emp.dat','rb+') as fl:
    emp = []
    while True:
      try:emp.append(pickle.load(fl))
      except:break
    for i in emp:
      if i[0] == int(id_search):print("\nEmployee Found.\n",tabulate.tabulate(emp, headers=['Emp. No.', 'Employee Name', 'Subject', 'Department', 'Salary']))       
      else:print("\nEmployee Not Found.")

while True:
  print('\n\tBinary File Management Using Pickle')
  print('\n1. Add new record.')
  print('\n2. Display all records.')
  print('\n3. Search for a record.')
  print('\n4. Modify a record.')
  print('\n5. Delete a record.')
  ch=int(input('\nEnter your choice (0. to exit): '))
  if ch==1:
    addRecord()
  elif ch==2:
    displayAllRecords()
  elif ch==3:
    SearchRecord()
  elif ch==4:
    ModifyRecord()
  elif ch==5:
    deleteRecord()
  elif ch==0:
    break
  else:
    print('\nInvalide Choice!!\nPlease Try Again')

