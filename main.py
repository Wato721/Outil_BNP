# --- DEFINITION DES SUBTESTS --- #
subtests_list = [
    "cub", "puz", "sim", "mat", "bal", "mch", "mim", "cod", "sym"
]


# --- CALCUL DES SCORES DES SUBTESTS --- #
def subtests_score():
    subtests = [
        "cube",
        "puzzle_visuel", 
        "vocabulaire",
        "similitudes",
        "matrices",
        "balances",
        "mémoire_chiffres",
        "mémoire_images",
        "code", 
        "symbole" 
    ]
    scores = {}
    
    for subtest in subtests:
        score = None
        while not score:
            try:
                score = int(input(f"Quel est la note standard au subtest {subtest} ?"))
            except ValueError:
                print("Veuillez entrer un nombre s'il vous plait")
        scores[subtest] = score
    return scores


scores_subtests = subtests_score()

# --- CALCUL DES INDICES --- #
subtests_result = list(scores_subtests.values())
    
total_IVS = scores_subtests["cube"] + scores_subtests["puzzle_visuel"]
total_ICV = scores_subtests["vocabulaire"] + scores_subtests["similitudes"] 
total_IRF = scores_subtests["matrices"] + scores_subtests["balances"]
total_IMT = scores_subtests["mémoire_chiffres"] + scores_subtests["mémoire_images"]
total_IVT = scores_subtests["code"] + scores_subtests["symbole"]

total_QIT = (total_ICV + total_IRF + total_IMT + scores_subtests["cube"] + scores_subtests["code"])
total_IAG = (total_IRF + total_ICV + scores_subtests["cube"])
total_ICC = (total_IVT + total_IMT)


# --- VERIFIER L'HOMOGENEITE AU SEIN DES INDICES --- #
IVS_difference = scores_subtests["cube"] - scores_subtests["puzzle_visuel"]
if IVS_difference < -3:
    print("Il existe un risque de dyspraxie")
elif IVS_difference > 3:
    print("La mémoire de travail est possiblement déficitaire")

IVT_difference = scores_subtests["code"] - scores_subtests["symbole"]
if IVT_difference < -3:
    print(
    "Il existe un risque de dyspraxie, demander un bilan ergothérapique"
)
pass


# --- CONVERSION NOTE COMPOSITE --- #
def calculate_ranks(indices):
    ranks = []
    for indice in indices:
        if indice in range(2, 39):
            ranks.append(range(2, 39).index(indice) + 1)

    return ranks

liste_ICV = [
    45, 50, 55, 59, 62, 65, 68, 70, 73, 76, 
    78, 81, 84, 86, 89, 92, 95, 98, 100, 103,
    106, 108, 111, 113, 116, 118, 121, 124, 127,
    130, 133, 136, 139, 142, 146, 150, 155
]

liste_IVS = [
    45, 49, 53, 57, 61, 64, 67, 69, 72, 75, 
    78, 81, 84, 86, 89, 92, 94, 97, 100, 102, 
    105, 111, 114, 117, 119, 122, 126, 129, 132, 
    135, 138, 141, 144, 147, 151, 155
]

liste_IVS = [
    45, 49, 53, 57, 61, 64, 67, 69, 72, 75, 
    78, 81, 84, 86, 89, 92, 94, 97, 100, 102, 
    105, 111, 114, 117, 119, 122, 126, 129, 132, 
    135, 138, 141, 144, 147, 151, 155
]

liste_IRF = [
    45, 51, 55, 58, 61, 64, 67, 69, 72, 74,
    76, 79, 82, 85, 88, 91, 94, 97, 100, 103, 106,
    109, 112, 115, 118, 121, 123, 126, 128, 131,
    134, 137, 140, 144, 147, 151, 155
]

liste_IMT = [
    45, 51, 55, 59, 62, 65, 67, 69, 72, 74, 76,
    79, 82, 85, 88, 91, 94, 97, 100, 107, 110, 112,
    115, 117, 120, 122, 125, 127, 130, 132, 135, 138,
    142, 146, 150, 155]

liste_IVT = [
    45, 49, 53, 56, 60, 63, 66, 69, 72, 75, 77, 80,
    83, 86, 89, 92, 95, 98, 100, 103, 105, 108, 111,
    114, 116, 119, 123, 126, 129, 132, 135, 138, 141, 144,
    148, 151, 155
]


measurement_names = [["ICV"], ["IVS"], ["IRF"], ["IMT"], ["IVT"]]
measurement_lists = [liste_ICV, liste_IVS, liste_IRF, liste_IMT, liste_IVT]
indice_value = {}

for i, measurement_list in enumerate(measurement_lists):
    measurement_name = measurement_names[i][0]  
    ranks = calculate_ranks(measurement_list)
    indice_value[measurement_name] = ranks

print(indice_value)

for measurement_list in measurement_lists:
    measurement_name = measurement_list[0].split()[0]  # Assuming name is first word
    ranks = calculate_ranks(measurement_list)
    indice_value[measurement_name] = ranks

print(indice_value)

# --- VERIFIER L'HOMOGENEITE DES INDICES --- #
def homogeneity_calcul():
    indice_resultats = [
        total_IVS, total_ICV, total_IRF, total_IMT, total_IVT
]
    profil = ""
    def maximum_liste():
        maxi = indice_resultats[0]
        for i in indice_resultats:
            if i >= maxi:
                maxi = i
        return maxi
    
    def minimum_liste():
        mini = indice_resultats[0]
        for i in indice_resultats:
            if i <= mini:
                mini = i
        return mini
    
    profil_indice = maximum_liste - minimum_liste
    if profil_indice >= 20:
        profil = "Hétérogène"
    else:
        profil = "Homogène" 
    return profil

print(f"Le profil de votre patient est {homogeneity_calcul()}")









#Afficher liste résultats associés aux indices
tableau_indices = list(zip(liste_indices, liste_resultats))

for trait in tableau_indices:
    print(trait)

#Déterminer si le profil est hétérogène
    #Déterminer l'indice le plus haut
maxi = liste_resultats[0]
for x in liste_resultats:
    if x >= maxi:
        maxi = x

    #Déterminer l'indice le plus bas
mini = liste_resultats[0]
for z in liste_resultats:
    if z <= mini:
        mini = z

Diffence_indices = maxi - mini
if Diffence_indices >= 20:
    print("Le profil est hétérogène. Ne pas tenir compte du QIT, mais de l'IAG")
else:
    print("Le profil est homogène")

#Calculer les forces et les faiblesses du profil
liste_point_fort = []
liste_point_faible = []

    #Calculer la moyenne des indices
Moyenne_indices = ((Resultat_ICV + Resultat_IMT + Resultat_IRF + Resultat_IVS + Resultat_IVT)/5)
print(f"La moyenne des indices est {Moyenne_indices}")

    #Regarder comment les résultats s'écartent de la moyenne
Difference_ICV_Moyenne = Resultat_ICV - Moyenne_indices
if Difference_ICV_Moyenne >= 10:
    liste_point_fort.append("ICV")
elif Difference_ICV_Moyenne <= -10:
    liste_point_faible.append("ICV")

Difference_IVS_Moyenne = Resultat_IVS - Moyenne_indices
if Difference_IVS_Moyenne >= 10:
    liste_point_fort.append("IVS")
elif Difference_IVS_Moyenne <= -10:
    liste_point_faible.append("IVS")

Difference_IRF_Moyenne = Resultat_IRF - Moyenne_indices
if Difference_IRF_Moyenne >= 10:
    liste_point_fort.append("IRF")
elif Difference_IRF_Moyenne <= -10:
    liste_point_faible.append("IRF")

Difference_IMT_Moyenne = Resultat_IMT - Moyenne_indices
if Difference_IMT_Moyenne >= 10:
    liste_point_fort.append("IMT")
elif Difference_IMT_Moyenne <= -10:
    liste_point_faible.append("IMT")

Difference_IVT_Moyenne = Resultat_IVT - Moyenne_indices
if Difference_IVT_Moyenne >= 10:
    liste_point_fort.append("IVT")
elif Difference_IVT_Moyenne <= -10:
    liste_point_faible.append("IVT")

print(f"Les points faibles sont {liste_point_faible}")
print(f"Les points forts sont {liste_point_fort}")

#Calculer le QIT 
liste_QIT = [40, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
            51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63,
            64, 65, 66, 67, 68, 69, 70, 70, 71, 72, 73, 73, 74, 
            75, 76, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87,
            88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101,
            102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112,
            113, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125,
            126, 127, 128, 129, 129, 130, 131, 132, 133, 134, 135, 136,
            137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148,
            149, 150, 151, 152, 153, 155, 156, 157, 158, 159, 160, 160,
            160, 160]

liste_addition_QIT = range(7, 134)

for w in liste_addition_QIT:
    if w == Echelle_total:
        Num_liste6 = liste_addition_QIT.index(w - 1)

Resultat_QIT = liste_QIT[Num_liste6]
print(f"La note composite du QIT est de {Resultat_QIT}")

if Resultat_QIT >= 130:
    print("Profil HPI")
elif 120 >= Resultat_QIT <130:
    print("Profil supérieur à la moyenne")
elif 110 >= Resultat_QIT <120:
    print("Profil moyenne haute")
elif 90 >= Resultat_QIT < 110:
    print("Profil moyen")
elif 80 >= Resultat_QIT < 90:
    print("Profil moyenne basse")
elif 70 >= Resultat_QIT < 80:
    print("Profil fragile")
else: 
    print("Déficience intellectuel")


#Calculer l'IAG
liste_IAG = [40, 44, 47, 49, 51, 53, 54, 55, 56, 57, 59, 60,
            61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
            74, 75, 76, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
            91, 92, 94, 95, 97, "abs", "abs", "abs", 100, 101, 103, 104, 105, 107, 108,
            109, 111, 112, 113, 115, 116, 117, 118, 120, 121, 123,
            124, 125, 126, 127, 128, 129, 130, 132, 133, 134, 136,
            137, 138, 140, 141, 143, 144, 145, 147, 148, 149, 151,
            152, 154, 155]

liste_addition_IAG = range(5, 93)

for a in liste_addition_QIT:
    if a == Echelle_IAG:
        Num_liste7 = liste_addition_IAG.index(a - 1)

Resultat_IAG = liste_IAG[Num_liste7]
print(f"La note composite de l'IAG est {Resultat_IAG}")

if Resultat_IAG >= 130:
    print("Profil HPI")
elif 120 >= Resultat_IAG <130:
    print("Profil supérieur à la moyenne")
elif 110 >= Resultat_IAG <120:
    print("Profil moyenne haute")
elif 90 >= Resultat_IAG < 110:
    print("Profil moyen")
elif 80 >= Resultat_IAG < 90:
    print("Profil moyenne basse")
elif 70 >= Resultat_IAG < 80:
    print("Profil fragile")
else: 
    print("Déficience intellectuel")