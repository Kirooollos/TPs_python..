def capital(nb_annees,capital_debut):
    i = 1
    cap = capital_debut
    while i <= nb_annees:
        cap = cap*1.05 - 11
        i += 1
    return cap

def gagne_argent(nb_annees,capital_debut):
    return (capital(nb_annees,capital_debut) - capital_debut) >= 0


def placement_min(nb_annees,but):
    cap_debut = but
    while nb_annees > 0:
        cap_debut = (cap_debut + 11)/1.05
        nb_annees -= 1
    return cap_debut

def duree_min(capital,but):
    i = 0
    if capital <= 220:
        i = "erreur"
    else:
        while but > capital:
            but = (but + 11)/1.05
            i += 1
    return i 

def fonction_principal():
    print(capital(10,1000))
    print(gagne_argent(10,1000))
    print(placement_min(10,10000))
    print(duree_min(1000,10000))


