import csv
import sys

def main(argv):
    fich_csv = open(argv[1], "r") #define o nome do ficheiro
    csv_reader = csv.reader(fich_csv, delimiter=",")#copia o ficheiro para uma variável
    
    soma = 0
    n = 0
    minimo = sys.float_info.max
    maximo = -sys.float_info.max
    
    #descartar a primeira linha
    next(csv_reader)

    for row in csv_reader:
        try:
            temp = float(row[3])
        except:
            continue
    
        n += 1
        soma += temp
        if temp < minimo :
            minino = temp
        if temp > maximo :
            maximo = temp
    
    if n != 0 :
        media = soma / n
        print ("temperatura minima = " + str(minino))
        print ("temperatura maxima = " + str(maximo))
        print ("temperatura media = " + str(media))
    else :
        print("ficheiro vazio\n")

    fich_csv.close()

main(sys.argv)
