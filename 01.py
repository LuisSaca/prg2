# ejercicio 1
class NumeroEspecial:
  def __init__(self, x):
    self.x = int(x)
    
  def es_primo(self):
    # retorna 1 si es primo, y 0 si es falso
    if self.x < 2:
      return 0
    for i in range(2, self.x):
      if self.x % i == 0:
        return 0
    return 1

  def es_capicua(self):
    numero = self.x
    inv = 0
    aux = numero

    while aux > 0:
      inv = inv * 10 + aux % 10
      aux = aux // 10

    if numero == inv:
      return 1
    else:
      return 0

def main():
  # ingresar un lote de numeros en el intervalo de [x, y]. el algoritmo principal debe pedir la entrada de datos en x un valor igual o superior a 100 de lo contrario finaliza el algoritmo. en la entrada de datos en y debe ser un valor superios a la entrada de datos x, de lo contrario tambien finaliza el algoritmo. dentro el intervalo de lote de numero [x, y], hacer un barrido mostrando los numero sprimos y capicuas llamando a la clase NumeroEspecial y aplicando sus metodos
  
  x = int(input("Introduzca el valor de X: "))
  # x debe ser mayor a 100
  while x < 100:
    x = int(input("Introduzca el valor de X: "))
  y = int(input("Introduzca el valor de Y: "))
  # y debe ser mayor a x
  while y <= x:
    y = int(input("Introduzca el valor de Y: "))
  
  for i in range(x, y + 1):
    numero = NumeroEspecial(i)
    if numero.es_primo():
      print(f"PRIMO {i} ")
    if numero.es_capicua():
      print(f"CAPICUA {i}")
      
  
main()