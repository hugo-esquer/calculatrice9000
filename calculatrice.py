def calcul(ope):
    global num1
    global num2
    global resultat
    if ope == "+":
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

historique = []
while True:

    print("Tapper effacer pour effacer l'historique.")
    resultat = ""
    num1 = input("Entrer un chiffre: ")
    operateur = input("Entrer un opérateur: ")
    num2 = input("Entrer un deuxième chiffre : ")
    if num1 == "effacer" or operateur == "effacer" or num2 == "effacer":
        historique = []
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
            historique.append(resultat)
    print("\nHistorique:")
    for i in historique:
        print(i)
    print("\n")