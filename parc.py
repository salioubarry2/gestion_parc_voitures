class Parc:
    def __init__(self,id,adresse,capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.liste_voiture = []
    def entrer_voiture(self,voiture):
          self.liste_voiture.append(voiture)
    def sortir_voiture(self , voiture):
        if voiture in self.liste_voiture:
            self.liste_voiture.remove(voiture)
            print("la voiture est sortie du parc.")
        else :
            print("la voiture n'est pas dans le parc.")

    def calculer_nbr_place_dispo(self):
        return self.liste_capacite -len(self.liste_voiture)

