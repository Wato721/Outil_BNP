def calculating_subtests_score():
    subtests = [
        "cube",
        "visual_puzzle",
        "vocabulary",
        "similarities",
        "matrices",
        "scales",
        "number_memory",
        "images_memory",
        "code", 
        "symbol"
    ]
    scores = {}
    
    for subtest in subtests:
        score = None
        while not score:
            try:
                score = int(input(f"What is the standard score for the {subtest} subtest?"))
            except ValueError:
                print("Please enter a number")
        scores[subtest] = score
    return scores


standard_subtest_scores = calculating_subtests_score()


# check homogeneity within indices
IVS_difference = standard_subtest_scores["cube"] - standard_subtest_scores["visual_puzzle"]
if IVS_difference < -3:
    print("there is a risk of visual-motor coordination disorders")
elif IVS_difference > 3:
    print("working memory may be impaired")

IVT_difference = standard_subtest_scores["code"] - standard_subtest_scores["symbol"]
if IVT_difference < -3:
    print("there is a risk of visual-motor coordination disorders, go to ergotherapy")
pass


# calculating indices from subtests scores
subtests_result = list(standard_subtest_scores.values())
    
sums_standard_notes_IVS = standard_subtest_scores["cube"] + standard_subtest_scores["visual_puzzle"]
sums_standard_notes_ICV = standard_subtest_scores["vocabulary"] + standard_subtest_scores["similarities"]
sums_standard_notes_IRF = standard_subtest_scores["matrices"] + standard_subtest_scores["scales"]
sums_standard_notes_IMT = standard_subtest_scores["number_memory"] + standard_subtest_scores["images_memory"]
sums_standard_notes_IVT = standard_subtest_scores["code"] + standard_subtest_scores["symbol"]

sums_standard_notes_QIT = (
        sums_standard_notes_ICV + sums_standard_notes_IRF +
        sums_standard_notes_IMT + standard_subtest_scores["cube"] +
        standard_subtest_scores["code"]
    )

sums_standard_notes_IAG = sums_standard_notes_IRF + sums_standard_notes_ICV + standard_subtest_scores["cube"]
sums_standard_notes_ICC = sums_standard_notes_IVT + sums_standard_notes_IMT


# converting index ratings into composite ratings
index_ratings = range(2, 39)


def composite_rating_icv():
    icv_value = [
        45, 50, 55, 59, 62,
        65, 68, 70, 73, 76,
        78, 81, 84, 86, 89,
        92, 95, 98, 100, 103,
        106, 108, 111, 113, 116,
        118, 121, 124, 127, 130,
        133, 136, 139, 142, 146,
        150, 155
    ]
    for i in index_ratings:
        if i == sums_standard_notes_ICV:
            rating_icv = index_ratings.index(i)
    icv_score = icv_value[rating_icv]

    return icv_score


def composite_rating_ivs():
    ivs_value = [
        45, 49, 53, 57, 61,
        64, 67, 69, 72, 75,
        78, 81, 84, 86, 89,
        92, 94, 97, 100, 102,
        105, 108, 111, 114, 117,
        119, 122, 126, 129, 132,
        135, 138, 141, 144, 147,
        151, 155
    ]
    for i in index_ratings:
        if i == sums_standard_notes_IVS:
            rating_ivs = index_ratings.index(i)
    ivs_score = ivs_value[rating_ivs]

    return ivs_score


def composite_rating_irf():
    irf_value = [
        45, 51, 55, 58, 61,
        64, 67, 69, 72, 74,
        76, 79, 82, 85, 88,
        91, 94, 97, 100, 103,
        106, 109, 112, 115, 118,
        121, 123, 126, 128, 131,
        134, 137, 140, 144, 147,
        151, 155
    ]
    for i in index_ratings:
        if i == sums_standard_notes_IRF:
            rating_irf = index_ratings.index(i)
    irf_score = irf_value[rating_irf]

    return irf_score


def composite_rating_imt():
    imt_value = [
        45, 51, 55, 59, 62,
        65, 67, 69, 72, 74,
        76, 79, 82, 85, 88,
        91, 94, 97, 100, 103,
        107, 110, 112, 115, 117,
        120, 122, 125, 127, 130,
        132, 135, 138, 142, 146,
        150, 155
    ]
    for i in index_ratings:
        if i == sums_standard_notes_IMT:
            rating_imt = index_ratings.index(i)
    imt_score = imt_value[rating_imt]

    return imt_score


def composite_rating_ivt():
    ivt_value = [
        45, 49, 53, 56, 60,
        63, 66, 69, 72, 75,
        77, 80, 83, 86, 89,
        92, 95, 98, 100, 103,
        105, 108, 111, 114, 116,
        119, 123, 126, 129, 132,
        135, 138, 141, 144, 148,
        151, 155
    ]
    for i in index_ratings:
        if i == sums_standard_notes_IVT:
            rating_ivt = index_ratings.index(i)
    ivt_score = ivt_value[rating_ivt]

    return ivt_score


composite_scale_icv = composite_rating_icv()
composite_scale_ivs = composite_rating_ivs()
composite_scale_irf = composite_rating_irf()
composite_scale_imt = composite_rating_imt()
composite_scale_ivt = composite_rating_ivt()

composite_scale_scores = [
    composite_scale_icv, composite_scale_ivs,
    composite_scale_irf, composite_scale_imt,
    composite_scale_ivt
]

print(composite_scale_scores)

# check index homogeneity


def homogeneity_calcul():
    standard_deviation = max(composite_scale_scores) - min(composite_scale_scores)
    if standard_deviation >= 20:
        profile = "heterogeneous"
    else:
        profile = "Homogeneous"
    return profile


profile_wisc = homogeneity_calcul()

print(f"your patient's profile is {profile_wisc}")

# calculate the patient's strengths/weak points
highlights_list_patient = []
weaknesses_list_patient = []
average_composite_score = sum(composite_scale_scores) / len(composite_scale_scores)

for composite_scale_score in composite_scale_scores:
    difference = composite_scale_score - average_composite_score
    if difference >= 10:
        highlights_list_patient.append(composite_scale_score)
    elif difference <= 10:
        weaknesses_list_patient.append(composite_scale_score)
    else:
        pass

print(highlights_list_patient)
print(weaknesses_list_patient)


# calculating QIT


def composite_rating_qit():
    index_ratings_qit = range(7, 134)
    qit_value = [
        40, 40, 41, 42, 43,
        44, 45, 46, 47, 48,
        49, 50, 51, 52, 53,
        54, 55, 56, 57, 58,
        59, 60, 61, 62, 63,
        64, 65, 66, 67, 68,
        69, 70, 70, 71, 72,
        73, 73, 74, 75, 76,
        76, 77, 78, 79, 80,
        81, 82, 83, 84, 85,
        86, 87, 88, 89, 91,
        92, 93, 94, 95, 96,
        97, 98, 99, 100, 101,
        102, 103, 104, 105, 106,
        107, 108, 109, 110, 111,
        112, 113, 115, 116, 117,
        118, 119, 120, 121, 122,
        123, 124, 125, 126, 127,
        128, 129, 129, 130, 131,
        132, 133, 134, 135, 136,
        137, 138, 139, 140, 141,
        142, 143, 144, 145, 146,
        147, 148, 149, 150, 151,
        152, 153, 155, 156, 157,
        158, 159, 160, 160, 160,
        160
    ]

    for i in index_ratings_qit:
        if i == sums_standard_notes_QIT:
            rating_qit = index_ratings_qit.index(i)
    qit_score = qit_value[rating_qit]

    return qit_score


composite_scale_qit = composite_rating_qit()



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