from app import db, create_app
from app.model import Question

def populate_database():
    questions = [
        Question(
            text="Quel est le principe de la partie double en comptabilité ?",
            answer_a="Chaque transaction affecte au moins deux comptes",
            answer_b="Chaque transaction n'affecte qu'un seul compte",
            answer_c="Les transactions sont enregistrées deux fois",
            answer_d="Les comptes sont toujours équilibrés",
            correct_answer="A"
        ),
        Question(
            text="Qu'est-ce que le bilan en comptabilité ?",
            answer_a="Un rapport des revenus et dépenses",
            answer_b="Un état des actifs, passifs et capitaux propres à une date donnée",
            answer_c="Un résumé des flux de trésorerie",
            answer_d="Une liste des transactions de l'année",
            correct_answer="B"
        ),
        Question(
            text="Quelle est la principale différence entre l'audit interne et l'audit externe ?",
            answer_a="L'audit interne est effectué par des employés, l'externe par des tiers indépendants",
            answer_b="L'audit interne est obligatoire, l'externe est facultatif",
            answer_c="L'audit interne concerne les finances, l'externe les opérations",
            answer_d="Il n'y a pas de différence significative",
            correct_answer="A"
        ),
        Question(
            text="Qu'est-ce que le principe de continuité d'exploitation en comptabilité ?",
            answer_a="Les états financiers sont préparés en supposant que l'entreprise cessera ses activités",
            answer_b="Les états financiers sont préparés en supposant que l'entreprise poursuivra ses activités",
            answer_c="Les états financiers sont préparés uniquement pour une période définie",
            answer_d="Les états financiers sont préparés sans tenir compte de l'avenir de l'entreprise",
            correct_answer="B"
        ),
        Question(
            text="Quel est le but principal d'un audit financier ?",
            answer_a="Détecter toutes les fraudes possibles",
            answer_b="Améliorer l'efficacité opérationnelle de l'entreprise",
            answer_c="Exprimer une opinion sur la fidélité des états financiers",
            answer_d="Préparer les déclarations fiscales de l'entreprise",
            correct_answer="C"
        ),
        Question(
            text="Qu'est-ce que le seuil de signification en audit ?",
            answer_a="Le montant maximum des honoraires d'audit",
            answer_b="Le niveau d'erreur considéré comme significatif dans les états financiers",
            answer_c="Le nombre minimum de transactions à vérifier",
            answer_d="Le pourcentage de profit minimum pour une entreprise",
            correct_answer="B"
        ),
        Question(
            text="Quelle est la définition du compte de résultat ?",
            answer_a="Un document qui montre les actifs et passifs de l'entreprise",
            answer_b="Un rapport qui présente les revenus, dépenses et bénéfices sur une période donnée",
            answer_c="Une liste de tous les comptes bancaires de l'entreprise",
            answer_d="Un résumé des flux de trésorerie de l'entreprise",
            correct_answer="B"
        ),
        Question(
            text="Qu'est-ce que l'amortissement en comptabilité ?",
            answer_a="Une méthode pour augmenter la valeur des actifs",
            answer_b="Un prêt à long terme",
            answer_c="La répartition du coût d'un actif sur sa durée de vie utile",
            answer_d="Une forme de revenu",
            correct_answer="C"
        ),
        Question(
            text="Quel est le rôle principal du grand livre en comptabilité ?",
            answer_a="Enregistrer les transactions quotidiennes",
            answer_b="Calculer les impôts",
            answer_c="Contenir tous les comptes de l'entreprise",
            answer_d="Préparer les rapports financiers",
            correct_answer="C"
        ),
        Question(
            text="Qu'est-ce qu'une provision en comptabilité ?",
            answer_a="Un type de revenu",
            answer_b="Une estimation d'une dépense ou d'une perte future probable",
            answer_c="Un type d'actif",
            answer_d="Un dividende payé aux actionnaires",
            correct_answer="B"
        ),
        Question(
            text="Quel est le principe de prudence en comptabilité ?",
            answer_a="Surévaluer les actifs et sous-évaluer les passifs",
            answer_b="Ne pas tenir compte des risques potentiels",
            answer_c="Comptabiliser les pertes potentielles mais pas les gains potentiels",
            answer_d="Maximiser les profits à court terme",
            correct_answer="C"
        ),
        Question(
            text="Qu'est-ce que le contrôle interne dans une entreprise ?",
            answer_a="Un département chargé de l'audit interne",
            answer_b="Un ensemble de procédures pour assurer l'efficacité et la conformité des opérations",
            answer_c="Un logiciel de comptabilité",
            answer_d="Un rapport financier interne",
            correct_answer="B"
        ),
        Question(
            text="Quelle est la différence entre les charges et les dépenses ?",
            answer_a="Il n'y a pas de différence, ces termes sont synonymes",
            answer_b="Les charges sont comptabilisées quand elles sont engagées, les dépenses quand elles sont payées",
            answer_c="Les charges sont pour les grandes entreprises, les dépenses pour les petites",
            answer_d="Les charges sont déductibles fiscalement, les dépenses ne le sont pas",
            correct_answer="B"
        ),
        Question(
            text="Qu'est-ce que le cycle comptable ?",
            answer_a="La durée de vie d'une entreprise",
            answer_b="La période entre deux audits",
            answer_c="La séquence des étapes comptables de l'enregistrement à la préparation des états financiers",
            answer_d="Le temps nécessaire pour former un comptable",
            correct_answer="C"
        ),
        Question(
            text="Quel est le but principal de la comptabilité analytique ?",
            answer_a="Préparer les états financiers pour les actionnaires",
            answer_b="Calculer les impôts à payer",
            answer_c="Fournir des informations détaillées sur les coûts pour la prise de décision",
            answer_d="Enregistrer les transactions quotidiennes",
            correct_answer="C"
        ),
        Question(
            text="Qu'est-ce que le rapprochement bancaire ?",
            answer_a="Un prêt bancaire",
            answer_b="La comparaison entre le relevé bancaire et le livre de caisse de l'entreprise",
            answer_c="Une méthode de paiement",
            answer_d="Un type de compte bancaire",
            correct_answer="B"
        ),
        Question(
            text="Qu'est-ce que la certification des comptes ?",
            answer_a="L'enregistrement des transactions comptables",
            answer_b="La préparation des déclarations fiscales",
            answer_c="L'opinion émise par un auditeur sur la régularité et la sincérité des comptes",
            answer_d="L'approbation des comptes par les actionnaires",
            correct_answer="C"
        ),
        Question(
            text="Quel est le rôle du commissaire aux comptes ?",
            answer_a="Préparer les états financiers de l'entreprise",
            answer_b="Gérer les opérations quotidiennes de l'entreprise",
            answer_c="Certifier la régularité et la sincérité des comptes annuels",
            answer_d="Décider de la politique de dividendes de l'entreprise",
            correct_answer="C"
        ),
        Question(
            text="Qu'est-ce que le fonds de roulement ?",
            answer_a="L'argent disponible dans la caisse de l'entreprise",
            answer_b="La différence entre les actifs à court terme et les passifs à court terme",
            answer_c="Le total des dettes de l'entreprise",
            answer_d="Le montant des ventes annuelles",
            correct_answer="B"
        ),
        Question(
            text="Quel est le principe de séparation des exercices en comptabilité ?",
            answer_a="Chaque transaction doit être enregistrée séparément",
            answer_b="Les revenus et les dépenses doivent être comptabilisés dans la période à laquelle ils se rapportent",
            answer_c="Les comptes personnels et professionnels doivent être séparés",
            answer_d="Chaque département de l'entreprise doit avoir ses propres comptes",
            correct_answer="B"
        ),
        Question(
            text="Qu'est-ce que la comptabilité en partie simple ?",
            answer_a="Un système où chaque transaction n'affecte qu'un seul compte",
            answer_b="Un système utilisé uniquement pour les petites entreprises",
            answer_c="Un système où les transactions sont enregistrées une seule fois",
            answer_d="Un système obsolète non utilisé en comptabilité moderne",
            correct_answer="A"
        ),
        Question(
            text="Quel est le rôle principal du plan comptable ?",
            answer_a="Définir les règles de l'audit",
            answer_b="Fournir une structure standardisée pour l'organisation des comptes",
            answer_c="Calculer les impôts de l'entreprise",
            answer_d="Déterminer le salaire des comptables",
            correct_answer="B"
        ),
        Question(
            text="Qu'est-ce que le principe de permanence des méthodes en comptabilité ?",
            answer_a="Utiliser toujours les mêmes méthodes comptables d'une période à l'autre",
            answer_b="Changer de méthodes comptables chaque année",
            answer_c="Utiliser uniquement des méthodes approuvées par les autorités fiscales",
            answer_d="Appliquer les méthodes les plus récentes à chaque exercice",
            correct_answer="A"
        ),
        Question(
            text="Qu'est-ce que le seuil de rentabilité ?",
            answer_a="Le niveau de profit maximum qu'une entreprise peut atteindre",
            answer_b="Le point où les revenus totaux égalent les coûts totaux",
            answer_c="Le montant minimum de ventes pour éviter la faillite",
            answer_d="Le pourcentage de profit par rapport au chiffre d'affaires",
            correct_answer="B"
        ),
        Question(
            text="Quelle est la différence entre un coût fixe et un coût variable ?",
            answer_a="Les coûts fixes changent avec le niveau de production, les coûts variables restent constants",
            answer_b="Les coûts fixes restent constants, les coûts variables changent avec le niveau de production",
            answer_c="Les coûts fixes sont payés mensuellement, les coûts variables annuellement",
            answer_d="Il n'y a pas de différence significative entre les deux",
            correct_answer="B"
        ),
        Question(
            text="Qu'est-ce que le principe d'entité en comptabilité ?",
            answer_a="Chaque entreprise doit avoir sa propre comptabilité, séparée de celle de ses propriétaires",
            answer_b="Toutes les entités d'un groupe doivent utiliser le même système comptable",
            answer_c="Les entités gouvernementales et privées doivent utiliser des systèmes comptables différents",
            answer_d="Chaque département d'une entreprise doit avoir sa propre comptabilité",
            correct_answer="A"
        ),
        Question(
            text="Qu'est-ce que la comptabilité de gestion ?",
            answer_a="La préparation des états financiers pour les autorités fiscales",
            answer_b="L'enregistrement des transactions quotidiennes",
            answer_c="La fourniture d'informations financières pour la prise de décision interne",
            answer_d="La vérification des comptes par un auditeur externe",
            correct_answer="C"
        ),
        Question(
            text="Quel est le rôle principal du tableau de flux de trésorerie ?",
            answer_a="Montrer les profits et pertes de l'entreprise",
            answer_b="Présenter les entrées et sorties de trésorerie de l'entreprise",
            answer_c="Lister tous les actifs et passifs de l'entreprise",
            answer_d="Calculer les impôts à payer",
            correct_answer="B"
        ),
        Question(
            text="Qu'est-ce que le principe de non-compensation en comptabilité ?",
            answer_a="Les dettes et les créances ne peuvent pas être compensées",
            answer_b="Les revenus et les dépenses doivent toujours être égaux",
            answer_c="Les actifs et les passifs doivent être présentés séparément sans compensation",
            answer_d="Les profits d'un département ne peuvent pas compenser les pertes d'un autre",
            correct_answer="C"
        ),
        Question(
            text="Qu'est-ce que la méthode FIFO en gestion des stocks ?",
            answer_a="First In, First Out - les premiers articles entrés sont les premiers sortis",
            answer_b="Fast Inventory, Fast Output - gestion rapide des stocks",
            answer_c="Financial Inventory for Fiscal Operations - inventaire financier pour opérations fiscales",
            answer_d="Final Inventory, Final Outcome - inventaire final pour résultat final",
            correct_answer="A"
        ),
        Question(
            text="Quel est le but principal de l'analyse financière ?",
            answer_a="Préparer les déclarations fiscales",
            answer_b="Enregistrer les transactions quotidiennes",
            answer_c="Évaluer la santé financière et la performance d'une entreprise",
            answer_d="Auditer les comptes de l'entreprise",
            correct_answer="C"
        ),
        Question(
            text="Qu'est-ce que le goodwill en comptabilité ?",
            answer_a="La valeur des biens immobiliers d'une entreprise",
            answer_b="La différence entre la valeur d'acquisition d'une entreprise et la juste valeur de ses actifs nets identifiables",
            answer_c="Le montant des profits non distribués",
            answer_d="La valeur des brevets et marques déposées",
            correct_answer="B"
            ),
        Question(
            text="Qu'est-ce que le ratio de liquidité générale ?",
            answer_a="Le rapport entre les actifs à court terme et les passifs à court terme",
            answer_b="Le rapport entre les dettes totales et les capitaux propres",
            answer_c="Le rapport entre le bénéfice net et le chiffre d'affaires",
            answer_d="Le rapport entre les stocks et les créances clients",
            correct_answer="A"
        ),
        Question(
            text="Quel est le principe de matérialité en audit ?",
            answer_a="Tous les éléments doivent être audités, quelle que soit leur importance",
            answer_b="Seuls les éléments importants qui pourraient influencer les décisions des utilisateurs des états financiers sont pris en compte",
            answer_c="Seuls les éléments matériels comme les immobilisations sont audités",
            answer_d="Les auditeurs doivent utiliser uniquement des preuves matérielles",
            correct_answer="B"
        ),
        Question(
            text="Qu'est-ce que la méthode du coût moyen pondéré en gestion des stocks ?",
            answer_a="Une méthode où le coût de chaque article est calculé individuellement",
            answer_b="Une méthode où le coût des stocks est la moyenne pondérée de tous les articles similaires achetés ou produits au cours de la période",
            answer_c="Une méthode où le coût le plus élevé est toujours utilisé",
            answer_d="Une méthode où le coût le plus bas est toujours utilisé",
            correct_answer="B"
        ),
        Question(
            text="Qu'est-ce que le principe de l'image fidèle en comptabilité ?",
            answer_a="Les états financiers doivent présenter une image exacte de la situation financière de l'entreprise",
            answer_b="Les états financiers doivent être présentés de manière esthétique",
            answer_c="Les états financiers doivent être approuvés par un photographe professionnel",
            answer_d="Les états financiers doivent inclure des images de tous les actifs de l'entreprise",
            correct_answer="A"
        ),
        Question(
            text="Quel est le rôle du journal en comptabilité ?",
            answer_a="Enregistrer chronologiquement toutes les transactions financières",
            answer_b="Publier les résultats financiers de l'entreprise",
            answer_c="Calculer les impôts à payer",
            answer_d="Préparer les budgets pour l'année suivante",
            correct_answer="A"
        ),
        Question(
            text="Qu'est-ce que la méthode de l'amortissement linéaire ?",
            answer_a="Une méthode où l'amortissement augmente chaque année",
            answer_b="Une méthode où l'amortissement diminue chaque année",
            answer_c="Une méthode où l'amortissement reste constant chaque année",
            answer_d="Une méthode où l'amortissement est calculé de manière aléatoire",
            correct_answer="C"
        ),
        Question(
            text="Qu'est-ce que le principe de non-compensation en comptabilité ?",
            answer_a="Les actifs et les passifs doivent être présentés séparément sans être compensés",
            answer_b="Les revenus et les dépenses doivent toujours être égaux",
            answer_c="Les dettes et les créances doivent être compensées",
            answer_d="Les profits d'un département doivent compenser les pertes d'un autre",
            correct_answer="A"
        ),
        Question(
            text="Quel est le but principal du grand livre auxiliaire ?",
            answer_a="Enregistrer les transactions en détail pour des comptes spécifiques",
            answer_b="Remplacer le grand livre général",
            answer_c="Calculer les impôts à payer",
            answer_d="Préparer les états financiers",
            correct_answer="A"
        ),
        Question(
            text="Qu'est-ce que le seuil de rentabilité ?",
            answer_a="Le point où les revenus totaux égalent les coûts totaux",
            answer_b="Le niveau de profit maximum qu'une entreprise peut atteindre",
            answer_c="Le montant minimum de ventes pour éviter la faillite",
            answer_d="Le pourcentage de profit par rapport au chiffre d'affaires",
            correct_answer="A"
        ),
        Question(
            text="Qu'est-ce que la comptabilité d'engagement ?",
            answer_a="Une méthode où les transactions sont enregistrées uniquement lorsque l'argent est reçu ou payé",
            answer_b="Une méthode où les revenus et les dépenses sont enregistrés lorsqu'ils sont gagnés ou encourus, indépendamment du flux de trésorerie",
            answer_c="Une méthode utilisée uniquement pour les grandes entreprises",
            answer_d="Une méthode où toutes les transactions sont enregistrées à la fin de l'année fiscale",
            correct_answer="B"
        ),
        Question(
            text="Quel est le rôle principal de l'état des variations des capitaux propres ?",
            answer_a="Montrer les changements dans la position financière de l'entreprise",
            answer_b="Présenter les revenus et les dépenses de l'entreprise",
            answer_c="Illustrer les changements dans l'avoir des actionnaires au cours d'une période",
            answer_d="Calculer les dividendes à payer aux actionnaires",
            correct_answer="C"
        ),
        Question(
            text="Qu'est-ce que le principe de l'importance relative en comptabilité ?",
            answer_a="Tous les éléments doivent être traités de la même manière, quelle que soit leur taille",
            answer_b="Seuls les éléments de grande valeur sont importants en comptabilité",
            answer_c="Les éléments significatifs qui pourraient influencer les décisions des utilisateurs des états financiers doivent être présentés séparément",
            answer_d="L'importance d'un élément est déterminée uniquement par sa valeur monétaire",
            correct_answer="C"
        ),
        Question(
            text="Qu'est-ce que le ratio d'endettement ?",
            answer_a="Le rapport entre les actifs totaux et les passifs totaux",
            answer_b="Le rapport entre les dettes totales et les capitaux propres",
            answer_c="Le rapport entre le bénéfice net et les ventes",
            answer_d="Le rapport entre les actifs courants et les passifs courants",
            correct_answer="B"
        ),
        Question(
            text="Quel est le but principal de la comptabilité de trésorerie ?",
            answer_a="Enregistrer les transactions uniquement lorsque l'argent est effectivement reçu ou payé",
            answer_b="Calculer les impôts à payer",
            answer_c="Préparer le bilan",
            answer_d="Évaluer la rentabilité de l'entreprise",
            correct_answer="A"
        ),
        Question(
            text="Qu'est-ce que le principe de la comptabilité d'exercice ?",
            answer_a="Les transactions sont enregistrées uniquement à la fin de l'exercice fiscal",
            answer_b="Les revenus et les dépenses sont comptabilisés lorsqu'ils sont gagnés ou encourus, indépendamment du moment du paiement",
            answer_c="Toutes les transactions doivent être enregistrées en espèces",
            answer_d="Les transactions sont enregistrées uniquement lorsque l'argent est reçu ou payé",
            correct_answer="B"
        ),
        Question(
            text="Qu'est-ce que le coût d'opportunité en comptabilité de gestion ?",
            answer_a="Le coût réel d'un bien ou d'un service",
            answer_b="Le coût de production d'un produit",
            answer_c="La valeur de la meilleure alternative abandonnée lorsqu'un choix est fait",
            answer_d="Le coût total de tous les produits d'une entreprise",
            correct_answer="C"
        ),
        Question(
            text="Quel est le rôle principal du compte de résultat prévisionnel ?",
            answer_a="Enregistrer les transactions passées",
            answer_b="Prévoir les revenus et les dépenses futurs",
            answer_c="Calculer les impôts à payer",
            answer_d="Déterminer la valeur des actifs de l'entreprise",
            correct_answer="B"
        ),
        Question(
            text="Qu'est-ce que la méthode des coûts standard en comptabilité de gestion ?",
            answer_a="Une méthode où les coûts réels sont toujours utilisés",
            answer_b="Une méthode où des coûts prédéterminés sont utilisés pour évaluer la performance",
            answer_c="Une méthode où les coûts les plus élevés sont toujours utilisés",
            answer_d="Une méthode où les coûts sont déterminés à la fin de la période comptable",
            correct_answer="B"
        ),
        Question(
            text="Quel est le but principal de l'analyse du point mort ?",
            answer_a="Déterminer le niveau de production où l'entreprise ne fait ni profit ni perte",
            answer_b="Calculer le profit maximum possible",
            answer_c="Évaluer la valeur de l'entreprise",
            answer_d="Déterminer le montant des impôts à payer",
            correct_answer="A"
        ),
        Question(
            text="Qu'est-ce que le principe de la permanence des méthodes en comptabilité ?",
            answer_a="Changer de méthodes comptables chaque année",
            answer_b="Utiliser toujours les mêmes méthodes comptables d'une période à l'autre, sauf si un changement est justifié",
            answer_c="Utiliser uniquement des méthodes approuvées par les autorités fiscales",
            answer_d="Appliquer les méthodes les plus récentes à chaque exercice",
            correct_answer="B"
        ),
        Question(
            text="Qu'est-ce que le concept de substance over form en comptabilité ?",
            answer_a="La forme juridique d'une transaction est plus importante que sa substance économique",
            answer_b="La substance économique d'une transaction est plus importante que sa forme juridique",
            answer_c="Seule la forme juridique des transactions doit être considérée",
            answer_d="Les transactions doivent être ignorées si leur forme juridique n'est pas claire",
            correct_answer="B"
        ),
    ]

    db.session.add_all(questions)
    db.session.commit()
    print("Base de données remplie avec succès avec 60 questions!")
    

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        populate_database()