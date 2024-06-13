questions_list = [
    "Tripote ou ronge certaines choses",
    "Insolent avec les grandes personnes",
    "A du mal à se faire des amis et à les garder",
    "Très irritable, impulsif",
    "Veut tout commander",
    "Suce ou mâchonne (pouce, vêtement, etc",
    "Pleure facilement",
    "Se sent attaqué, est toujours sur la défencive",
    "Rêvasse",
    "A des difficultés pour l’apprentissage de la lecture, calcul, écriture",
    "Se « tortille » ne tient pas en place",
    "A peur de nouvelles situations, d’endroits, de personnes, d’aller à l’école",
    "Agité, a toujours besoin de faire quelque chose",
    "Destructeur",
    "Ment ou raconte des histoires qui ne sont pas vraies",
    "Timide",
    "S’attire plus d’ennuis (se fait plus attraper que les autres enfants de son âge)",
    "Ne parle pas comme les autres enfants de son âge (bégaye, difficile à comprendre, parle bébé)",
    "Nie ses erreurs ou accuse toujours les autres",
    "Querelleur",
    "Fait la moue et boude",
    "Prend des choses qui ne lui appartiennent pas",
    "Est désobéissant ou obéit à contre-coeur",
    "S’inquiète plus que les autres de la maladie, mort, solitude",
    "Ne termine pas ce qu’il a commencé",
    "Se sent facilement froissé",
    "Brutalise, agresse ou intimide ses camarades",
    "Ne peut pas s’arrêter lors d’une activité répétitive",
    "Cruel",
    "Comportement « bébé », immature, collant, puéril, constamment besoin d’être rassuré, demande de l'aide pour des choses qu'il peut faire seul",
    "Problème d’attention, fixation, concentration ou distractibilité",
    "Maux de tête",
    "Changements d’humeur rapides et marqués",
    "N’aime pas obéir aux règles ou interdits",
    "Se bagarre constamment",
    "Ne s’entend pas avec ses frères et/ou soeurs",
    "Se décourage facilement devant l’effort",
    "Dérange les autres enfants",
    "Enfant foncièrement malheureux",
    "Problème d’alimentation sans appétit se lève après chaque bouchée",
    "Maux d’estomac",
    "Sommeil perturbé (difficulté à s’endormir et lève tôt) se réveille pendant la nuit",
    "Autres plaintes physiques et douleurs",
    "Vomissements, nausées",
    "Se sent lésé à la maison, à l’école",
    "Se vante, fanfaronne",
    "Se laisse écraser, manipuler",
    "Problème d’évacuation intestinale irrégulier, selles molles, constipation etc"
    ]


def questionnaire_answer_parent_version():
    answer_list = []
    for question in questions_list:
        print(question)
        print(
           "0 : not at all", "1 : a little bit",
           "2 : many", "3 : enormously"
        )
        answer = None
        while answer is None:
            try:
                answer = int(input("What's your answer ?"))
                if 0 < answer > 3:
                    print("Please enter a number between 0 and 3")
                    answer = None
            except ValueError:
                print("Please enter a number")
        answer_list.append(answer)

    return answer_list


questionnaire_answer = questionnaire_answer_parent_version()


def hyperactivity_profile():
    questions = [
        4, 7, 11, 13, 14,
        25, 31, 33, 37, 38
    ]
    questions_scores = []
    for question in questions:
        question_score = questionnaire_answer[question + 1]
        questions_scores.append(question_score)
    index_hyperactivity = sum(questions_scores)/len(questions)

    return index_hyperactivity


index_hyperactivity = hyperactivity_profile()

print(index_hyperactivity)
