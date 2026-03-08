class Parc:
    def __init__(self,id,adresse,capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.liste_voiture = []

    def entrer_voiture(self, voiture):
        if voiture in self.liste_voiture:
            print("La voiture existe déjà dans le parc.")
        elif len(self.liste_voiture) >= self.capacite:
            print("Le parc est plein.")
        else:
            self.liste_voiture.append(voiture)
            print("La voiture est entrée dans le parc.")
