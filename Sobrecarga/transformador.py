#Creo una clase que me permita transformar datos en este caso sumarlos y multiplicarlos por un factor
class Transformador:
    def transformar(self,datos,factor):
        suma=sum(datos)
        resultado=suma*factor
        return suma,resultado




