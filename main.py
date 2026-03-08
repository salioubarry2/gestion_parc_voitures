from voiture import Voiture
from parc import Parc

parc1= Parc(1 , "Toronto", 3)

voiture1 = Voiture("11", "NISAN","NOIR")
voiture2 = Voiture("12", "TOYOTA", "GRIS")
voiture3 = Voiture("13", "HUNDA", "BLANC")


voiture1.afficher_information()
voiture2.afficher_information()
voiture3.afficher_information()


parc1.entrer_voiture(voiture1)
parc1.entrer_voiture(voiture2)
parc1.entrer_voiture(voiture3)


print("Places disponibles est:",parc1.calculer_nbr_place_dispo())

parc1.sortir_voiture(voiture2)


print("Places disponible apres la sortie est:",parc1.calculer_nbr_place_dispo())

