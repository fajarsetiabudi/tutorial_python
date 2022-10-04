class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan health: {}".format(
            self.name,
            self.health))

class Hero_mage(Hero):
    def __init__(self,name):
        super().__init__(name, 100)

    def showInfo(self):
        print("{} \n\tTipe: mage, \n\thealth: {}".format(
            self.name,
            self.health))
       
        

class Hero_support(Hero):
    def __init__(self,name):
        super().__init__(name, 200)
        

shinta = Hero_mage('shinta')
jilong = Hero_support('jilong')

shinta.showInfo()
jilong.showInfo()