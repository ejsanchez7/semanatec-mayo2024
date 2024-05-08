def promedio(numeros) :
  suma = 0
  for num in numeros :
    suma += num
  return suma / len(numeros)

print(f"El promedio de {1, 2, 3}: {promedio([1, 2, 3])}")
