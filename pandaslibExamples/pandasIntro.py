print("Introduccion a pandas")
import pandas as pd

#DataFrame es una estructura de datos
tabla = pd.DataFrame(columns=("nombre","edad"))
tabla.loc[1]= "John", 22
tabla.loc[2]= "James",100
print(tabla)
print(type(tabla))
print(tabla.columns)
