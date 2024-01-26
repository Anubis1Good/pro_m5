# напиши свой код здесь


class Hero:
    def __init__(self, base, pos, land) -> None:
        self.base = base
        self.land = land
        self.hero = self.base.loader.loadModel("smiley")
        self.hero.setColor(1, 0.5, 0, 1)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(self.base.render)
        self.mode = True
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        self.base.disableMouse()
        self.base.camera.setH(180)
        self.base.camera.reparentTo(self.hero)
        self.base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        self.base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        self.base.camera.reparentTo(self.base.render)
        self.base.enableMouse()
        self.cameraOn = False

    def accept_events(self):
        self.base.accept("c", self.changeView)

        self.base.accept("m", lambda: self.turn(-5))
        self.base.accept("m" + "-repeat", lambda: self.turn(-5))
        self.base.accept("n", lambda: self.turn(5))
        self.base.accept("n" + "-repeat", lambda: self.turn(5))

        self.base.accept("w",lambda:self.move_dir(0))
        self.base.accept("w"+'-repeat',lambda:self.move_dir(0))
        self.base.accept("s",lambda:self.move_dir(180))
        self.base.accept("s"+'-repeat',lambda:self.move_dir(180))
        self.base.accept("a",lambda:self.move_dir(90))
        self.base.accept("a"+'-repeat',lambda:self.move_dir(90))
        self.base.accept("d",lambda:self.move_dir(270))
        self.base.accept("d"+'-repeat',lambda:self.move_dir(270))

    def changeView(self):
        self.cameraUp() if self.cameraOn else self.cameraBind()

    def turn(self, delta):
        self.hero.setH((self.hero.getH() + delta) % 360)

    def look_at(self, angle):
        from_x = round(self.hero.getX())
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)

        return from_x + dx, from_y + dy, from_z

    def check_dir(self, angle):
        speed = 1
        if angle >= 0 and angle <= 20:
            return (0, -speed)
        elif angle <= 65:
            return (speed, -speed)
        elif angle <= 110:
            return (speed, 0)
        elif angle <= 155:
            return (speed, speed)
        elif angle <= 200:
            return (0, speed)
        elif angle <= 245:
            return (-speed, speed)
        elif angle <= 290:
            return (-speed, 0)
        elif angle <= 335:
            return (-speed, -speed)
        else:
            return (0, -speed)


    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def try_move(self, angle):
        pass

    def move_to(self, angle):
        self.just_move(angle) if self.mode else self.try_move(angle)

    # def forward(self):
    #     pass

    # def back(self):
    #     angle =(self.hero.getH()+180) % 360
    #     self.move_to(angle)

    # def left(self):
    #    ...
    # def right(self):
    #    ...
    def move_dir(self,dir):
        angle =(self.hero.getH()+dir) % 360
        self.move_to(angle)
