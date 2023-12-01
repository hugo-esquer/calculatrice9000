def calcul(ope):
    global num1
    global num2
    global resultat
    if ope == "/" and num2 == 0:
        print("Il est impossible de diviser par zéro.")
    elif ope == "+":
        print(f"{num1} + {num2} = {num1+num2}")
        resultat = f"{num1} + {num2} = {num1+num2}"
    elif ope == "-":
        print(f"{num1} - {num2} = {num1-num2}")
        resultat = f"{num1} - {num2} = {num1-num2}"
    elif ope == "x" or ope == "*":
        print(f"{num1} x {num2} = {num1*num2}")
        resultat = f"{num1} x {num2} = {num1*num2}"
    elif ope == "/":
        print(f"{num1} / {num2} = {num1/num2}")
        resultat = f"{num1} / {num2} = {num1/num2}"
    elif ope == "%":
        print(f"{num1} % {num2} = {num1%num2}")
        resultat = f"{num1} % {num2} = {num1%num2}"
    elif ope == "**":
        print(f"{num1} ** {num2} = {num1**num2}")
        resultat = f"{num1} ** {num2} = {num1**num2}"
    elif ope == "//":
        print(f"{num1} // {num2} = {num1//num2}")
        resultat = f"{num1} // {num2} = {num1//num2}"
    else:
        print("Entrer un opérateur valide.")


while True:
    historique = open("historique_texte.txt", "r")

    print("Tapper effacer pour effacer l'historique.")
    resultat = ""
    num1 = input("Entrer un chiffre: ")
    operateur = input("Entrer un opérateur: ")
    num2 = input("Entrer un deuxième chiffre : ")
    if num1 == "effacer" or operateur == "effacer" or num2 == "effacer":

        with open("historique_texte.txt", "w") as fichier:
            fichier.write("")
    else:
        try:
            num1 = float(num1)
            num2 = float(num2)
        except:
            print("Entrer des chiffres valides.")
            num1 = ""
            num2 = ""

        if num1 != "":
            calcul(operateur)

        if resultat != "":
            with open("historique_texte.txt", "a") as fichier:
                fichier.write(resultat + "\n")
    print("\n Historique:")
    print(historique.read())
    historique.close()