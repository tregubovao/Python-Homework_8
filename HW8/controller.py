
import view
import process
import operation

def button_click():
    m = view.inp_shift()
    s = process.intepr_shift(m)
    msg = 'Да здравствует салат Цезарь!'
    print(operation.encrypt_caesar(msg, s))
    print(operation.decrypt_caesar(operation.encrypt_caesar(msg, s), s))