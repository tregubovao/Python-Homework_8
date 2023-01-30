"""Задача 2.
Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром
Цезаря и возвращает его. Шифр Цезаря заменяет каждую букву в тексте на букву, которая
отстоит в алфавите на некоторое фиксированное число позиций.
В функцию передается сообщение и сдвиг алфавита. Если сдвиг не указан, то пусть ваша
функция кодирует сдвиг алфавита на 3 позиции:
А→Г,А→Г,
Б→Д,Б→Д,
В→Е,В→Е,
……
Э→А,Э→А,
Ю→Б,Ю→Б,
Я→ВЯ→В
Все символы, кроме русских букв должны остаться неизменными. Маленькие буквы должны
превращаться в маленькие, большие — в большие.
Напишите также функцию декодирования decrypt_caesar(msg, shift), также
использующую сдвиг по умолчанию. При написании функции декодирования используйте
вашу функцию кодирования.

Да здравствует салат Цезарь!
Зг кзугефхецих фгогх Щикгуя!"""

def  encrypt_caesar(msg, shift):
    encrypted = ''
    for el in msg:
        if el.isalpha():
            a = ord(el)
            if 1072 <= a <= 1103:                   # маленькие буквы
                while (a + shift) > 1103:        
                    a -= 32
                en = a + shift
                encrypted += chr(en)
            else:                                   # БОЛЬШИЕ БУКВЫ
                while (a + shift) > 1071:        
                    a -= 32
                en = a + shift
                encrypted += chr(en)
        else:
            encrypted += el
    return(encrypted)


def  decrypt_caesar(msg, shift):
    decrypted = ''
    for el in msg:
        if el.isalpha():
            a = ord(el)
            if 1072 <= a <= 1103:               # маленькие буквы
                while (a - shift) < 1072:        
                    a += 32
                en = a - shift
                decrypted += chr(en)
            else:                               # БОЛЬШИЕ БУКВЫ
                while (a - shift) < 1040:        
                    a += 32
                en = a - shift
                decrypted += chr(en)
        else:
            decrypted += el
    return(decrypted)

m = (input('Введите SHIFT:'))
if m.isdigit():
    s = int(m)
else:
    s = 3
msg = 'Да здравствует салат Цезарь!'
print(encrypt_caesar(msg, s))
print(decrypt_caesar(encrypt_caesar(msg, s), s))






# mmssg = 'АБВГДЕЖЗИЭЮЯ'
# for el in mmssg:
#     print(el, ord(el)) 

# mmssg = 'абвгдежзиэюя'
# for el in mmssg:
#     print(el, ord(el))

   



