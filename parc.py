class Parc:
    def __init__(self,id,adresse,capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.liste_voiture = []
    def entrer_voiture(self,voiture):
          self.liste_voiture.append(voiture)
