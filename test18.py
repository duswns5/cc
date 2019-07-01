hab = 0
i =0

for i in range (1,101,1) :
    if i % 3 == 0 :
        continue
    hab = hab + i
print ("3의배수가 아닌것의 합 : %d"%hab)