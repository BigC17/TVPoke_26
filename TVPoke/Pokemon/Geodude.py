from TVPoke.BaseClasses.PokeTypes import Ground
from TVPoke.BaseClasses.Move import Move

class Geodude(Ground):
    def __init__(self):
        moves = [
            Move("Body Slam", "NORMAL", 60),
            Move("Punch", "NORMAL", 80),
            Move("", "WATER", 80),
            Move("Crunch", "NORMAL", 0)
        ]
        super().__init__("Geodude", 140, moves, "./TVPoke/Pokemon/imgs/Geodude.png")