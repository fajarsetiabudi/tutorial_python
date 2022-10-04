class Hero:
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):

        #instance attributes
        self.nama = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

    #void function method tanpa return
    def siapa(self):
        print('nama ku adalah ' + self.nama)

hero1 = Hero('Barat', 100, 500,300)
hero1.siapa()





    