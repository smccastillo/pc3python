#Dividir números
def dividir(num1, num2):
    try:
        division = num1 / num2
        return division
    except ZeroDivisionError:
        print("Alerta: No se puede dividir por cero")
        return None