#1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código 
# pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros 
# pero ¿qué pasa si se envía otro tipo de dato?


class prueba:
    def __init__(self,numero):
        self.numero = numero
    
        assert type(numero) == int, f"{numero} no es del tipo int"
        assert 0 < (numero) <= 50, f"{numero} no esta dentro del rango 1 a 50"


    def primo(self):


        cont = 0
        for j in range(1, self.numero +1):
            if self.numero %j == 0:
                cont += 1
    
        if cont <= 2:
            return f"El numero {self.numero} si es primo", True
        else:
            return f"El numero {self.numero} no es primo", False
    #2) En la función que hace la conversión de grados, validar 
    # que los parámetros enviados sean los esperados, de no serlo, 
    # informar cuáles son los valores esperados.        
    def conversion(self,origen,destino):

        assert origen == "C" or origen == "K" or origen == "F", f"{origen} no es una letra valida introduce 'C','k','F' "
        assert destino == "C" or destino == "K" or destino == "F", f"{destino} no es una letra valida introduce 'C','K','F' "

        if origen == "C" and destino == "K" or destino == "F":
            temperatura1 = f"{self.numero}°C equivalen a {self.numero + 273.15}K"
            temperatura2 = f"{self.numero}°C equivalen a {(self.numero*1.8) + 32}°F"
        elif origen == "F" and destino == "C" or destino == "K":
            temperatura1 = f"{self.numero}°F equivalen a {(self.numero-32)*(5/9)}°C"
            temperatura2 = f"{self.numero}°F equivalen a  {(self.numero+459.67)*(5/9)}°K"
        elif origen == "K" and destino == "C" or destino == "F":
            temperatura1 = f"{self.numero}°K equivalen a {self.numero - 273.15}°C"
            temperatura2 = f"{self.numero}°K equivalen a {1.8 * (self.numero-273) + 32}°F"
        return temperatura1,temperatura2
    
    def factorial(self):

        elemento = 1
        for i in range(1,self.numero+1):
            elemento = elemento * i
        return f"El factorial de {self.numero} es {elemento}"



n1 = prueba("25")