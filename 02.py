# ejercicio 2

class OperacionBasica:
  def __init__(self, x, y):
    self.x = float(x)
    self.y = float(y)
    
  def suma(self):
    return float(self.x + self.y)
    
  def resta(self):
    return float(self.x - self.y)
  
  def multiplicacion(self):
    return float(self.x * self.y)
  
  def division(self):
    if self.y != 0:
      return float(self.x / self.y)
    else:
      return 0
    
def main():
  n = int(input("Intro N: "))
  for i in range(n):
    x = float(input("Introduzca el valor de A: "))
    y = float(input("Introduzca el valor de B: "))
    operacion = OperacionBasica(x, y)
    if i % 2 != 0:
      print(f"la resta de {x} - {y} es: ", operacion.resta())
    if i % 2 == 0:
      print(f"la division de {x} / {y} es: ", operacion.division())
      
main()  
