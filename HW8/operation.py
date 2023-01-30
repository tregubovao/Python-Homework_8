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