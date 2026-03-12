from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40))

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        
    def elementsToDisplay(self):
        self.elements = [
            Image((50 , 50), 100, 100, './imgs/battlescreen.jpg')
        ]

        # y = 0
        # #two rows of three
        # for trainer in self.trainers:
        #     x = 0
        #     y += 100/3
        #     for poke in trainer.pokemon:
        #         x += 100/4
        #         self.elements.append(Image((x, y), 20, 20, poke.img))
        #         self.elements.append(Label((x, y + 10), 20, 10, poke.name))
                
 #place closest active pokmeon
        p1Active = self.trainers[0].pokemon[0]
        x = 30
        y = 25
        self.elements.append(Image((x,y), 20, 20, p1Active.img))


        #place furthest active pokmeon
        p2Active = self.trainers[1].pokemon[0]
        x = 70
        y = 50
        self.elements.append(Image((x,y), 20, 20, p2Active.img))
               



