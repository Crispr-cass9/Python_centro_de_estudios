my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
copy_list = my_list[:]
j=0


for i in my_list:
    print("Valor de i=",i,"Valor de j=",j)
    if i in copy_list[j+1:]:
        del copy_list[j]
        j-=1
    j+=1 

print("La lista con elementos únicos:")
print(copy_list)

##Nueva formamás comprensible para lograr el laboratorio

my_list = set(my_list) ##Set elimina los elementos duplicados de una lista pero no respeta el orden

print(my_list)
