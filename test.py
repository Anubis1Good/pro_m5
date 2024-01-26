from direct.showbase.ShowBase import ShowBase
# from direct


class Game(ShowBase):
    def __init__(self, fStartDirect=True, windowType=None):
        super().__init__(fStartDirect, windowType)
        
        # self.model = self.loader.loadModel('models/environment')
        self.model = self.loader.loadModel('./some_models/Boeing707.egg')
        self.texture = self.loader.loadTexture('./some_models/BoeingTexture.tif')
        self.model.setTexture(self.texture)
        self.model.setColor((0.0,0.7,0.0,1))
        self.model.reparentTo(self.render)
        self.model.setScale(0.1)
        self.model.setPos(-2,25,-3)
        self.camLens.setFov(90)

game = Game()
game.run()