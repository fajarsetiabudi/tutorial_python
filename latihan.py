#parent class
class Mobil():
    def __init__(self, color):
        self.color = color
    def desc(self):
        print('this is mobil', self.color)

#child class
class Honda(Mobil):
    def __init__(self, color, model):
        super().__init__(color)
        self.model = model

    def desc(self):
        print ('this is honda', self.color, self.model)

vc = Mobil('merah')
ho = Honda('hitam', 'hcgc')
vc.desc()
ho.desc()