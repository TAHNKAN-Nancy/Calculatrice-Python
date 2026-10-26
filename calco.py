import math

def operations_base(choix):
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxieme nombre : "))
    resultat= None

    if choix == 1 :
        resultat = a + b
    elif choix == 2:
          resultat = a - b
    elif choix == 3:
           resultat = a * b
    elif choix == 4:
          if b != 0:
                 resultat = a / b
          else:
                 print("Division impossible.")

    return resultat

def trigonometrie(choix):
      angle = float(input("Entrez l angle en degre :"))
      angle_rad = math.radians(angle)
      resultat = 0
      
      if choix == 5:
           resultat = math.cos(angle_rad)
      elif choix == 6:
           resultat = math.sin(angle_rad)
      elif choix == 7:
           if abs(math.cos(angle_rad)) != 0:
               resultat = math.sin(angle_rad)/ math.cos(angle_rad)
           else:
                print("Tangente non definie pour cette angle.")
      return resultat 

def tri_insertion(T):
     N = len(T)

     for i in range(1, N):
          x = T[i]
          j = i - 1

          while j >= 0 and T[j] > x:
               T[j + 1] = T[j]
               j = j - 1

          T[j + 1] = x
          
def max_min():
     N = int(input("combien de nombres voulez vous saisir? "))
     T = []

     for i in range(N):
          nombre = float(input(f"entrez le nombre {i + 1}: "))
          T.append(nombre)

     tri_insertion(T)
     print("Minimum:", T[0])
     print("Maximum:", T[N - 1])

def main():
     choix = -1

     while choix != 0:
          print("\n BIENVENU DANS LA CALCULATRICE DE NANCY")
          print("1. Addition")
          print("2. Soustraction")
          print("3. Multiplication")
          print("4. Division")
          print("5. Cosinus")
          print("6. Sinus")
          print("7. Tangente")
          print("8. Maximum et Minimum")
          print("0. Quitter")

          choix = int(input("choisissez une operation : "))

          if choix in (1, 2, 3, 4):
               resultat = operations_base(choix)
               if resultat is not None:
                  print("Resultat :" , resultat)
          elif choix in (5, 6, 7):
               resultat = trigonometrie(choix)
               if resultat is not None:
                  print("Resultat :" , resultat)
          elif choix == 8:
               max_min()
          elif choix == 0:
                 print("Fin du programme.")
          else: 
                 print("choix invalide.")

main()