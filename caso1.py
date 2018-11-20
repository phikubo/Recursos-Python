print("Caso 1")
inputfile="adn"
#referencia el archivo de nombre adn
archivo=open(inputfile,"r")
#sube el contenido a una variable
secuencia=archivo.read()
#Se reemplaza los caracteres en la nueva variable
secuencia2=secuencia.replace("\n","")
#secuencia2=secuencia.replace("\r","")
print(secuencia2)

tabla={
"ATA":"I","ATC":"I","ATT":"I","ATG":"M",
"ACA":"T","ACC":"T","ACG":"T","ACT":"T",
"AAC":"N","AAT":"N","AAA":"K","AAG":"K",
"AGC":"S","AGT":"S","AGA":"R","AGG":"R",
"CTA":"L","CTC":"L","CTG":"L","CTT":"L",
"CCA":"P","CCC":"P","CCG":"P","CCT":"P",
"CAC":"H","CAT":"H","CAA":"Q","CAG":"Q",
"CGA":"R","CGC":"R","CGG":"R","CGT":"R",
"GTA":"V","GTC":"V","GTG":"V","GTT":"V",
"GCA":"A","GCC":"A","GCG":"A","GCT":"A",
"GAC":"D","GAT":"D","GAA":"E","GAG":"E",
"GGA":"G","GGC":"G","GGG":"G","GGT":"G",
"TCA":"S","TCC":"S","TCG":"S","TCT":"S",
"TTC":"F","TTT":"F","TTA":"L","TTG":"L",
"TAC":"Y","TAT":"Y","TAA":"_","TAG":"_",
"TGC":"C","TGT":"C","TGA":"_","TGG":"W" }

#revisar que la secuencia sea divisible entre 3
if len(secuencia2) % 3 ==0:
	print("afirmativo")
else:
	print("negativo")
#loop sobre la secuencia

#extraer un codon

#revisar codon y guardarlo

print(len(secuencia2))
