# напиши здесь код создания и управления картой
# from direct.showbase.ShowBase import ShowBase


class Mapmanager:
    """Управление картой"""

    def __init__(self, base):
        # super().__init__()
        self.model = "block"  # модель кубика лежит в файле block.egg
        # # используются следующие текстуры:
        self.texture = "block.png"
        self.base = base
        # создаём строительные блоки
        self.color = (0.2, 0.2, 0.35, 1)  # rgba
        self.colors = [
            (0.5, 0.3, 0.0, 1),
            (0.2, 0.2, 0.3, 1),
            (0.5, 0.5, 0.2, 1),
            (0.0, 0.6, 0.0, 1),
        ]
        self.block = self.base.loader.loadModel(self.model)
        self.block.setTexture(self.base.loader.loadTexture(self.texture))

        # создаём основной узел карты:
        self.startNew()
        self.addBlock((0, 0, 0))

    def startNew(self):
        """создаёт основу для новой карты"""
        self.land = self.base.render.attachNewNode(
            "Land"
        )  # узел, к которому привязаны все блоки карты

    def getColor(self,z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]
        

    def addBlock(self, position):
        self.block = self.base.loader.loadModel(self.model)
        self.block.setTexture(self.base.loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.getColor(position[2]))
        self.block.reparentTo(self.land)

    def clear(self):
        self.land.removeNode()
        self.startNew()

    def loadLand(self, filename: str):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(" ")
                for z in line:
                    for z0 in range(int(z) + 1):
                        self.addBlock((x, y, z0))
                    x += 1
                y += 1
