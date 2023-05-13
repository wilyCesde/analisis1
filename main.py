import pandas as pd 

#ORGANIZAR LOS DATOS 

tabla1=pd.read_csv("./data/empleados.csv")

from data.comidas import comidas

tabla2=pd.DataFrame(comidas,columns=['nombrePlato','precioPlato'])

from data.medicos import crearMedicos

medicos=crearMedicos()

tabla3=pd.DataFrame(medicos)

# tabla1Modificada=tabla1.head(50)

# tabla1Modificada=tabla1.tail(50)

# tabla1Modificada=tabla1['salario',]

# tabla1Modificada=tabla1[['nombres','salario']].head(10)

tabla1Modificada=tabla3['nombre'].head(10)



print(tabla1Modificada)


