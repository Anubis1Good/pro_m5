from direct.showbase.ShowBase import ShowBase
# import panda3d.core
# from panda3d.core import NodePath
from mapmanager import Mapmanager

    
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager(loader=self.loader,render=self.render)
        self.camLens.setFov(90)

game = Game()
game.run()