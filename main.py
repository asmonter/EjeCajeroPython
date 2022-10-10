from Validaciones import Validations

def printMenu():
    print("\n" ,"- " *100)
    return input("Menu: Enter\nSalir: q")

def printOptions():
    return input \
        ("1. Consultar Saldo\n2. Retirar Saldo\n3. Hisorico de Movimientos \n")

if __name__ == '__main__':
    val = Validations()
    password = False
    for x in range(0, 3):
        password = val.validPass()
        if password == True: break
        print("Contraseña erronea")
    if password:
        while True:
            res = printMenu()
            if res == "q": break
            res = printOptions()
            if val.validOption(res) :
                print("Opcion no valida")
                pass
            elif res == "1":
                val.currentBalance()
            elif res == "2":
                val.getMoney()
            elif res == "3":
                val.history()