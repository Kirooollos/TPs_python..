def est_ce_carac(carac):
    if ord("A")<=ord(carac)<= ord("Z") or  ord("a")<=ord(carac)<= ord("z"):
        return True
    else:
        return False

def maj_minus(carac):
    if "A"<=carac<="Z":
        return "majuscule"
    elif "a"<=carac<="z":
        return "minuscule"
    else:
        return None

def voy_con(carac):
    if carac in "ueoaiy":
        return "voyelle"
    elif carac not in "ueoaiy":
        return "minuscule"
    else:
        return None

def position(carac):
    if maj_minus(carac) == "majuscule":
        pos = ord(carac) - ord("A") + 1
    elif maj_minus(carac)== "minuscule":
        pos = ord(carac) - ord("a") +1
    else:
        pos = None
    return pos

def main():
    kiro= "1.miniscule ou majuscule taper:m\n2.Est-ce_caractère taper:c\n3.voyelle/consonne taper:vc\n4.quitter taper:q\n"
    option = input(kiro)
    while option not in ["m","vc","c","q"]:
        option = input(kiro)
    while option != "q":
        carac = input("saisir un caractere: ")
        if option == "m":
            print(maj_minus(carac))
        elif option == "c":
            print(est_ce_carac(carac))
        else:
            print(voy_con(carac))
        option = input(kiro)
main()
        