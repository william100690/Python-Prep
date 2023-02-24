class prueba:
    def __init__(self,numero):
        self.numero = numero

    def primo(self):
        cont = 0
        for j in range(1, self.numero +1):
            if self.numero %j == 0:
                cont += 1
    
        if cont <= 2:
            return True
        else:
            return False
        
    def conversion(self,origen,destino):
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