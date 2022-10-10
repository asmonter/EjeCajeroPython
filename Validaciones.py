class Validations:
    def __init__(self):
        self.saldo = 1000
        self.movimientos = ["Saldo de 1000"]
        self.contrasenia = "1235"

    def validPass(self):
        res = input("Ingresa contraseña: ")
        return res == self.contrasenia

    def validOption(self, entrada):
        return not(entrada == "1" or entrada == "2" or entrada == "3")

    def currentBalance(self):
        print("Tu saldo es de {}".format(self.saldo))

    def isAvailable(self, money):
        try:
            if int(money) < 1: raise Exception
            valor = self.saldo - int(money)
        except:
            valor = -1
        finally:
            if valor < 0:
                print("**No es posible ese valor**")
                return False
            else:
                return True

    def getMoney(self):
        res =  input("Cuanto deceas retirar: \n")
        if self.isAvailable(res):
            self.saldo = self.saldo - int(res)
            print("Retirando {}, te queda {}".format(res, self.saldo))
            self.movimientos.append("Saldo Retirado de {}".format(res))

    def history(self):
        for x in range(0, len(self.movimientos)):
            print("Movimiento {}. {}".format(x, self.movimientos[x]))

    def cambios(self):
        print("Este es el cambio")