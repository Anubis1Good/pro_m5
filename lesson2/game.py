# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager(self)
        self.land.loadLand("land.txt")

        self.hero = Hero(self, (1, 21, 2), self.land)

        self.camLens.setFov(90)


game = Game()
game.run()
