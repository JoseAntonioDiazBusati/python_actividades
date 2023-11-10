num=int(input("Introduce un numero: "))
num_cont=2
if num==1:
    print("El numero 1 no es primo")
else:
    while num==num_cont:
        num/num_cont
        num_cont+=1
    if num%num_cont==0 and num_cont!=num:
        print("No es primo") 
    else:
        print("Es primo")  