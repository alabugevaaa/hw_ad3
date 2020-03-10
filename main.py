# coding: utf-8


class Contact:

    def __init__(self, fname, lname, phone, favourite=False, **kwargs):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.favourite = favourite
        self.addition = kwargs

    def __str__(self):
        inf = ''
        for addition in self.addition.items():
            inf += f' {addition[0]}: {addition[1]}\n'
        return f'Имя: {self.fname}\nФамилия: {self.lname}\nТелефон: {self.phone}\n' \
               f'В избранных: {"Да" if self.favourite else "Нет"}\nДополнительная информация:\n{inf}'


class PhoneBook(Contact):

    def __init__(self, name):
        self.name = name
        self.abonents = []

    def __str__(self):
        return f'Список контактов {self.name}:\n-----\n' + '-----\n'.join(map(str, self.abonents))

    def add(self, contact):
        self.abonents.append(contact)

    def delete(self, phone):
        for i, contact in enumerate(self.abonents):
            if contact.phone == phone:
                del self.abonents[i]
                print(f'Номер {phone} удален из телефонной книги {self.name}\n')
                break
            if i == len(self.abonents)-1:
                print(f'Абонент с номером {phone} не найден\n')

    def favourites(self):
        fav_list = []
        for i, contact in enumerate(self.abonents):
            if contact.favourite:
                fav_list.append(self.abonents[i])
        print(f'Список избранных контактов:\n-----\n' + '-----\n'.join(map(str, fav_list)))

    def search(self, fname, lname):
        print('Результат поиска:')
        for i, contact in enumerate(self.abonents):
            if contact.fname == fname and contact.lname == lname:
                print(self.abonents[i])
                break
        if i == len(self.abonents) - 1:
            print(f'Абонент {fname} {lname} не найден\n')


my_phone_book = PhoneBook('Friends')

jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
peter = Contact('Peter', 'Parker', '+71235687898', True, instagram='@spiderman', site='spiderman.com')
james = Contact('James', 'Bond', '+71230000007', False, instagram='@007', facebook='JamesBond007', site='007.com')

my_phone_book.add(jhon)
my_phone_book.add(peter)
my_phone_book.add(james)

print(my_phone_book)

my_phone_book.delete('+71234567809')

my_phone_book.favourites()
my_phone_book.search('Peter', 'Parker')

