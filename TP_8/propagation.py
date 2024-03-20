# EX3_8_3: Simulation d'une suite de rencontres
def Simulation_Propagation():
    nb_personnes = int(input("Saisir le nb de personnes: "))
    statuts = {}
    for i in range(0,nb_personnes):
        if i == 0:
            statuts[i] = "C"
        else:
            statuts[i] = "I"
    print("jour","rencontre","nature",end="  ")
    jour = 0
    import random
    while "C" in statuts.values():
        X = random.randint(0,nb_personnes-1)
        Y = random.randint(0,nb_personnes-1)
        while Y == X:
            Y = random.randint(0,nb_personnes-1)  
        rencontre_pers = [X,Y]
        rencontre = [statuts[X],statuts[Y]]
        if rencontre == ["C","C"]:
            statuts[X] = "M"
            statuts[Y] = "M"
        elif rencontre == ["C","I"]:
            statuts[X] = "C"
            statuts[Y] = "C"
        elif rencontre == ["C","M"]:
            statuts[X] = "M"
            statuts[Y] = "M"
        elif rencontre == ["I","C"]:
            statuts[X] = "C"
            statuts[Y] = "C"
        elif rencontre == ["M","C"]:
            statuts[X] = "M"
            statuts[Y] = "M"
        jour += 1
        #print(jour)
        #print(rencontre_pers)
        #print(statuts)
    nb_ignorants = list(statuts.values()).count("I")
    nb_muets = list(statuts.values()).count("M")
Simulation_Propagation()
            
            


#Simulation_Propagation()

