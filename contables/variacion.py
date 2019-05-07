#
import math
import txtt

print("inicio")
#p1 debe ser mayor a p2

def variacion(p1, p2):
	res=p1-p2
	#print(res)
	result= ((res*100.0)/p1)
	print(p1, "y", p2, "...",result)
	print("---")

def restar(p1,p2):
	print(p1, "y", p2, "...",p1-p2)
	print("---")
	
def variacion1(p1, p2):
	res=p1-p2
	#print(res)
	result= ((res*100.0)/p1)
	#print(p1, "y", p2, "...",result)
	#print("---")
	return result

def restar1(p1,p2):
	#print(p1, "y", p2, "...",p1-p2)
	#print("---")
	return p1-p2
		

mayor=601172
menor=543400
#variacion(mayor,menor)

lista_2018=[44518800,
22259400,
2473315,
970313,
601172,
3375000,

21259000,
12401000,
10858800,

14839600,
6739800,
680000]

lista_2017=[39555750,
15213750,
1500000,
917100,
543400,
3125000,

19777875,
11866725,
7911150,

8367563,
6085500,
6085500]


l2018=["51.938.600",
"36.357.020",
"15.581.580",
"22.259.400",
"11.129.700",
"7.790.790",
"3.338.910",

"21.259.000",
"13.818.000",
"7.441.000",
"12.401.000",
"4.960.400",
"7.440.600",
"10.858.800",

"14.839.600",
"10.387.720",
"4.451.880",
"6.739.800",
"5.391.840",
"1.347.960",
"680.000",

"2.473.315",
"989.326",
"1.483.989"]

l2017=["36.513.000",
"21.907.800",
"14.605.200",
"24.342.000",
"14.605.200",
"7.302.600",
"2.434.200",

"19.777.875",
"11.866.725",
"7.911.150",
"11.866.725",
"4.746.690",
"7.120.035",
"7.911.150",

"8.367.563",
"4.183.782",
"4.183.781",
"6.085.500",
"3.651.300",
"2.434.200",
"6.085.500",
"1.500.000",
"224.200",
"1.275.800"]



l2017_int=[]
l2018_int=[]
for i, j in zip(l2017, l2018):
	ext=i.replace(".","")
	ext2=j.replace(".","")
	l2017_int.append(int(ext))
	l2018_int.append(int(ext2))
	
print(l2018_int, l2017_int)


	
diferencia_lista=[]
variacion_lista=[]


print("Diferencia")
for i, j in zip(l2017_int, l2018_int):
	print(j, "--y-- " ,i)
	#print(restar(j,i))
	diferencia_lista.append(restar1(j,i))
	txtt.guardar_listas("diferen",diferencia_lista)

print("variacion horizontal")
for i, j in zip(l2017_int, l2018_int):
	print(j, "--y-- " ,i)
	#print(variacion(j,i))
	variacion_lista.append(variacion1(j,i))
	txtt.guardar_listas("variacion",variacion_lista)
 
'''
print("Diferencia")
for i, j in zip(lista_2017, lista_2018):
	#print(j, "--y-- " ,i)
	restar(j,i)
	diferencia_lista.append(restar1(j,i))
	txtt.guardar_listas("diferen",diferencia_lista)

print("variacion horizontal")
for i, j in zip(lista_2017, lista_2018):
	#print(j, "--y-- " ,i)
	variacion(j,i)
	variacion_lista.append(variacion1(j,i))
	txtt.guardar_listas("variacion",variacion_lista)
	
print("variación vertical")
'''
