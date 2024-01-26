# from direct.showbase.ShowBase import ShowBase

class Mapmanager():
    """ Управление картой """
    def __init__(self,loader,render):
        # super().__init__()
        self.model = 'block' # модель кубика лежит в файле block.egg
        # # используются следующие текстуры: 
        self.texture = 'block.png'
        self.loader = loader
        self.render = render
        # создаём строительные блоки   
        self.color = (0.2, 0.2, 0.35, 1) #rgba
        self.block = self.loader.loadModel(self.model)
        self.block.setTexture(self.loader.loadTexture(self.texture))           

        # создаём основной узел карты:
        self.startNew() 
        self.addBlock((0,0, 0))

    def startNew(self):
        """создаёт основу для новой карты""" 
        self.land = self.render.attachNewNode("Land") # узел, к которому привязаны все блоки карты
    
    def addBlock(self, position):
        self.block = self.loader.loadModel(self.model)
        self.block.setTexture(self.loader.loadTexture(self.texture)) 
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
