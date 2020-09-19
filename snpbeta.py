#!/usr/bin/env python
import sys
import math






#definição da função beta
def function_beta(p,n,z):
    beta=z/(math.sqrt(2*p*(1-p)*(n+z**2)))
    return beta
#definição da função se
def function_se(p,n,z):
    se=1/(math.sqrt(2*p*(1-p)*(n+z**2)))
    return se

#aviso inicial
print("SNPBeta v1.0")
print("This software is distributed under: The GNU General Public License v3.0")
print("Githup repository: https://github.com/alessandrobof/snpbeta")
print("Authors:")
print("A. B. Oliveira, B. S. Silva, C. S. Gusmão, J. K. N. Ramos, D. L. Rovaris")


#criando leitura de argumento com sys
#lendo arquivo de entrada

find=sys.argv[1]

#lendo arquivo de saida
foutd=sys.argv[2]

fo=open(foutd,'w')
print("Processing file: ",find)
print("This might take some minutes...")
#lendo arquivo
with open(find) as fp:
    #line=fp.readline()
    lc=0
    for line in fp:
        if lc==0:
            cab=line.strip().split(' ')
            cab.append('BETA')
            cab.append('SE')
            #print(cab)
            #print(" ".join(cab))
            fo.write(" ".join(cab))
            fo.write("\n")
        else:
            col=line.strip().split(' ')
            z=float(col[8])
            n=float(col[7])
            p=float(col[6])
            beta=function_beta(p,n,z)
            se=function_se(p,n,z)
            col.append(str(beta))
            col.append(str(se))
            #print(" ".join(col))
            fo.write(" ".join(col))
            fo.write("\n")
        lc=lc+1
    
#mensagem final    
print("Processing finished.")
print("Number of snp processed: ",lc)
#fechando os arquivos
fp.close()
fo.close()



#if __name__ =="__main__":
