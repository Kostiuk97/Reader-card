qwer={'ID':'10','last name':'Kostjuk','Name':'Yurii','group':'ІПЗс23-2','course':'1','books':[],'book statistics':[] }
print("ID = " + qwer['ID'])
print("last name' = " + qwer['last name'])
print("'Name = " + qwer['Name'])
print("group = " + qwer['group'])
print("course = " + qwer['course'])
print("books(debts) = " , qwer['books'])
print("book statistics = ", qwer['book statistics'] )


while True:
    ss = input("0 - вийти з програми -\n1- видати карту читача \n2 - вибрати книгу яку бажаєте взяти\n3- повернути книгу\n Введіть потрібну цифру-")
    if ss =='1':
        print("ID = " + qwer['ID'])
        print("last name' = " + qwer['last name'])
        print("'Name = " + qwer['Name'])
        print("group = " +  qwer['group'])
        print("course = " + qwer['course'])
        print("books (debts) = " , qwer['books'])
        print("book statistics = ", qwer['book statistics'] )
    elif ss == '2':
        s1 = input('Введіть назву книги яку хочете взяти: ')
        qwer['books'].append(s1) 
    elif ss == '3':
        s2= input ('введіть назву книги яку хочете повернути:')
        qwer['books'].remove(s2) 
        qwer['book statistics'].append(s2)      
    elif ss =='0': 
        print('Ви вийшли з програми ') 
        break 