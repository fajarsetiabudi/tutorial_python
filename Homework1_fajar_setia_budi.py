class Hewan:
    nama_latin = 'Anggora' #class atributes

     #instance atributes
    def __init__(self, name, age):     
        self.name = name
        self.age = age
        

    #instance method
    def bangun(self):
        print("Nama hewan : {} \nUmur : {} tahun ".format(
            self.name,
            self.age,
            
        ))

    #class method
    def changeNamaLatin(self):
        
        print ("Nama latin : " +self.nama_latin)

class Kucing(Hewan):
    kecepatan = 5

    #instance attribute
    def __init__(self,name,age, warna, asal):
        super().__init__(name,age)
        self.warna = warna
        self.asal = asal
        
        
    #instance method
    def bangun(self):
        
        
       print("Nama hewan : {} \nUmur : {} tahun \nWarna : {} \nAsal : {} ".format(
            self.name,
            self.age,
            self.warna,
            self.asal

            
        ))
    #class method
    def changeNamaLatin(self, nama_latin = 'Felis Catus'):
        print("Nama Latin : ",nama_latin)
    
    def lari(self):
        kecepatan = getattr(Kucing, 'kecepatan')
    
        print('Kecepatan lari : {} Km/jam'.format(self.kecepatan))

        if  kecepatan > 10   :
            print('Kategori : cepat sekali') 
        else:
            print('Kategori : lambat')


cat1 = Kucing('Ciko', 2, 'Putih', 'Amerika')
cat1.bangun()
cat1.changeNamaLatin()
cat1.lari()






    
        





