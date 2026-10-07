def sumar(a, b):
    return a + b

def restar (a, b):
    return a - b
    
def multiplicar(a,b):
    return a * b
  
def dividir (a,b):
    print("resultado")
    return a / b


if __name__ == "__main__":
    print(f"Resultado de la suma 2 + 3: {sumar(2, 3)}")
    print(f"resultado de la resta: {restar(2,3)}")
    print(f"resultado de la multiplacaion: {multiplicar(2,3)}")
    print(f"resultado de la multiplacaion: {dividir(2,3)}")