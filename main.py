import pandas as pd 

#ORGANIZAR LOS DATOS 

tabla1=pd.read_csv("./data/empleados.csv")

from data.comidas import comidas

tabla2=pd.DataFrame(comidas)

from data.medicos import crearMedicos

medicos=crearMedicos()

tabla3=pd.DataFrame(medicos)

# tabla1Modificada=tabla1.head(50)

# tabla1Modificada=tabla1.tail(50)

tabla1Modificada=tabla1['salario']

print(tabla1Modificada)


