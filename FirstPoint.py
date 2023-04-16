numbers = []
try:
    while True:
        a= int(input('Enter an integer: '))
        numbers.append(a)
        print(a)
        print(numbers)
except ValueError:
    if len(numbers) >0:
        print('Se ordenarán los numeros de acuerdo al criterio del ejercicio.')
    else:
        print('No se agregaron numeros a la lista, se terminará el ejercicio.')
        print(numbers)
    zeros=0


    for i in numbers:
      if i==0:
        zeros+=1
        numbers.remove(i)
    for i in range(0, zeros,1):
        numbers.append(0)
print('El orden de los numeros quedó tal que: ')
print(numbers)
