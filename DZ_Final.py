            
def input_error(func):
    def integ(n):
        try:                        
            result = func(n)
            return result
        
        except KeyError:
            print(KeyError)

        except ValueError:
            print(ValueError)

        except IndexError:
            if n == 'change':
                return 'Give me name and phone please'
            elif n == 'add':
                return 'Give me name and phone please'
            elif n == 'phone':
                return 'Give me phone please'
            
    return integ

@input_error
def add(n):   
    print(n)
    nick = n[1]
    phone_n = n[2]    
    if book_phone.get(nick) is None:
        book_phone.update({nick: phone_n})
        return f"додан контакт {nick} з номером {phone_n}"
    else:
        phone = book_phone.get(nick)
        return f"контакт {nick} вже існує, номер {phone}"

@input_error
def change(n):
    nick = n[1]
    phone_n = n[2]
    if nick in book_phone.values():
        for dic in book_phone:
            if nick == dic:
                book_phone.update({nick: phone_n})
                return f'для контакту {nick} змінено номер на {phone_n}'
    else:
        return f'Контакт {nick} відсутній у телефоній книзі'

@input_error
def phone(n):
    nick = n[1]
    phone_n = n[2]

    if nick in book_phone.keys():
        for item, value in book_phone.items():
            if nick == item:
                return value
    else:
        return f'контакт {nick} відсутній у телефоній книзі'

@input_error
def show_all(n):
    # nick = n[1]
    # phone_n = n[2]
    book = ''
    #print(len(book_phone.values()))
    if len(book_phone.values()) != 0:
        for items, values in book_phone.items():
            book += str(items) + ' ' + str(values) + '\n'                
        return book
    else:
        return 'телефонна книга пуста'

def main():
    global book_phone
    book_phone = {}
    while True:
        n = input("Чекаю команди ")                
        n = n.split(' ')
        if n[0] in ("good bye", "close", "exit"):
            print("Good bye!")
            break

        elif n[0] == 'hello':
            print("How can I help you?")

        elif n[0] == 'show_all':
            print(show_all(n))
        
        elif n[0] == 'change':
            print(change(n))
        
        elif n[0] == 'phone':
            print(phone(n))

        elif n[0] == 'add':
            print(add(n))           
        else:
            print("доступні команди add, change, phone, show_all, good bye, close, exit")

if __name__ == "__main__":
    main()