import random

dix=[1,2,3,4,5,6,7,8]

print(dix[7:])

for i in range(10):

    inicio_masked=random.randint(1,len(dix)-2)
    fin_masked=inicio_masked+max(1,round(random.gauss(int(len(dix)/4),1)))

    if(inicio_masked==len(dix)-2): fin_masked=len(dix)-1

    prefijo=dix[0:inicio_masked]
    masked_content=dix[inicio_masked:fin_masked]
    sufijo=dix[fin_masked:]

    #print(dix[inicio_masked:fin_masked])
    print(prefijo,masked_content,sufijo)
#
