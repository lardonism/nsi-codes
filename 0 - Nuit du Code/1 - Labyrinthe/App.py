import pyxel

class App:
    """ Application graphique - Pyxel """
    def __init__(self):
        """ App -> None """
        # initialisation de la fenêtre graphique
        pyxel.init(128, 128, title="La Nuit du Code")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ App -> None
        Met à jour l'application """

    def draw(self):
        """ App -> None
        Affiche les éléments dans la fenêtre graphique """

    
    
    def deplacer(self, perso, direction):
        """ App, Personnage, (int, int) -> None
        Déplace le personnage dans la direction indiquée si cela est possible """
        pass

App()
