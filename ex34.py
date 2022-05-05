from math import sqrt

def hipotenusa(catetoA, catetoB):
    catetoA, catetoB = float(catetoA), float(catetoB)
    print(f"Cateto A: {catetoA}\nCateto B: {catetoB}\nHipotenusa: {sqrt(catetoA**2 + catetoB**2)}" if catetoA != 0 and catetoB != 0 else "Algum cateto igual a 0")
    
        
hipotenusa(3, 4)
