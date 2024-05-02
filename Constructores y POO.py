class Coche():
        #Codigo de la clase
        #Propiedades
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

        #Comportamiento=>  metodos Un metodo es una funcion que pertence a una Clase 
    def arrancar(self):
        self.enmarcha=True
    def estado(self):
        if(self.enmarcha):
            return "El coche está enmacha"
        
        else:

            return "El coche está parado"

miCoche=Coche()
    #con el codigo de arriba Creamos un objeto o instanciamos una clase
print(miCoche.largoChasis)
print("El largo de mi Coche es:", miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, "ruedas")
#miCoche.arrancar()

print(miCoche.estado())
