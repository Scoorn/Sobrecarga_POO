#Importamos la libreria numpy para hacer los calculos
import numpy as np
#Creamos una clase que permita calcular la norma de un vector 2D y 3D
class Vector:  
    def calculo_norma(self, vector):
         return np.linalg.norm(vector)

    

