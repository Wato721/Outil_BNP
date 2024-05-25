#Liste des différentes épreuves et des résultats obtenus (NS)
liste_subtest = [
    "cub", "puz", "voc", "sim", "mat", "bal", "mch", "mim", "cod", "sym"
    ]
liste_profil = []

#Entré des scores par le praticien
Cube = int(input("Quelle est la note standard au subtest cube ?"))
liste_profil.append(Cube)
Puzzle_visuel = int(input("Quelle est la note standard au subtest puzzles-visuel ?"))
liste_profil.append(Puzzle_visuel)
Vocabulaire = int(input("Quelle est la note standard au subtest vocabulaire ?"))
liste_profil.append(Vocabulaire)
Similitudes = int(input("Quelle est la note standard au subtest similitudes ?"))
liste_profil.append(Similitudes)
Matrices = int(input("Quelle est la note standard au subtest matrices ?"))
liste_profil.append(Matrices)
Balances = int(input("Quelle est la note standard au subtest balances ?"))
liste_profil.append(Balances)
Memoire_chiffres = int(input("Quelle est la note standard au subtest mémoire de chiffres ?"))
liste_profil.append(Memoire_chiffres)
Memoire_images = int(input("Quelle est la note standard au subtest mémoire des images ?"))
liste_profil.append(Memoire_images)
Code = int(input("Quelle est la note standard au subtest code ?"))
liste_profil.append(Code)
Symbole = int(input("Quelle est la note standard au subtest symbole ?"))
liste_profil.append(Symbole)

#Afficher le tableau récapitulatif des résultats
tableau_NS = list(zip(liste_subtest, liste_profil))

for ligne in tableau_NS:
    print(ligne)


#Calcul des indices:
Total_ICV = Vocabulaire + Similitudes
Total_IVS = Cube + Puzzle_visuel
Total_IRF = Matrices + Balances
Total_IMT = Memoire_chiffres + Memoire_images
Total_IVT = Code + Symbole
Echelle_total = (Cube + Similitudes + Matrices + Memoire_chiffres +
                Memoire_images + Code + Vocabulaire + Balances)
Echelle_IAG = (Cube + Similitudes + Matrices + Vocabulaire + Balances)
Echelle_ICC = (Memoire_chiffres + Memoire_images + Code + Symbole)

#Vérifier l'homogénéité au sein des indices
Difference_IVS = Cube - Puzzle_visuel
if Difference_IVS >= 4:
    print("Vérifier les compétences en mémoire de travail. Le subtest Puzzle-Visuel sollicitant davantage ce processus.")
elif Difference_IVS <= -4:
    print("Vérifier la coordination visuo-motrice. Risque de dyspraxie +++")

Difference_IVT = Code - Symbole
if Difference_IVT >= 4:
    print("Verifier l'attention sélective")
elif Difference_IVT <= -4:
    print("Fragilité des compétences graphomotrices. Nécessité bilan ergo +++")

#Lien entre total indice et la note composite
    #J'avais commencé en faisant un range pour somme_NS mais ça 
    #n'avait pas marché
Somme_NS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
            24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 
            34, 35, 36, 37, 38]

liste_indices = ["ICV", "IVS", "IRF", "IMT", "IVT"]
liste_resultats = []

#Calcul ICV : Indice de Compréhension Verbale
liste_ICV = [45, 50, 55, 59, 62, 65, 68, 70, 73, 76, 
            81, 84, 86, 89, 92, 95, 98, 100, 103, 106,
            108, 111, 113, 116, 118, 121, 124, 127, 130,
            133, 136, 139, 142, 146, 150, 155]

for i in Somme_NS:
    if i == Total_ICV:
        Num_liste1 = Somme_NS.index(i - 1)

Resultat_ICV = liste_ICV[Num_liste1]
liste_resultats.append(Resultat_ICV)

#Calcul IVS : Indice Visuo-Spatial
liste_IVS = [45, 49, 53, 57, 61, 64, 67, 69, 72, 75, 78,
            81, 84, 86, 89, 92, 94, 97, 100, 102, 105, 111,
            114, 117, 119, 122, 126, 129, 132, 135, 138, 141,
            144, 147, 151, 155]

for j in Somme_NS:
    if j == Total_IVS:
        Num_liste2 = Somme_NS.index(j - 1)

Resultat_IVS = liste_IVS[Num_liste2]
liste_resultats.append(Resultat_IVS)

#Calcul IRF : Indice de Raisonnement Fluide
liste_IRF = [45, 51, 55, 58, 61, 64, 67, 69, 72, 74,
            76, 79, 82, 85, 88, 91, 94, 97, 100, 103, 106,
            109, 112, 115, 118, 121, 123, 126, 128, 131,
            134, 137, 140, 144, 147, 151, 155]

for s in Somme_NS:
    if s == Total_IRF:
        Num_liste3 = Somme_NS.index(s - 1)

Resultat_IRF = liste_IRF[Num_liste3]
liste_resultats.append(Resultat_IRF)

#Calcul IMT : Indice de Mémoire de Travail
liste_IMT = [45, 51, 55, 59, 62, 65, 67, 69, 72, 74, 76,
            79, 82, 85, 88, 91, 94, 97, 100, 107, 110, 112,
            115, 117, 120, 122, 125, 127, 130, 132, 135, 138,
            142, 146, 150, 155]

for t in Somme_NS:
    if t == Total_IMT:
        Num_liste4 = Somme_NS.index(t - 1)

Resultat_IMT = liste_IMT[Num_liste4]
liste_resultats.append(Resultat_IMT)

#Calcul IVT : Indice de Vitesse de Traitement
liste_IVT = [45, 49, 53, 56, 60, 63, 66, 69, 72, 75, 77, 80,
            83, 86, 89, 92, 95, 98, 100, 103, 105, 108, 111,
            114, 116, 119, 123, 126, 129, 132, 135, 138, 141, 144,
            148, 151, 155]

for u in Somme_NS:
    if u == Total_IVT:
        Num_liste5 = Somme_NS.index(u - 1)

Resultat_IVT = liste_IVT[Num_liste5]
liste_resultats.append(Resultat_IVT)

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