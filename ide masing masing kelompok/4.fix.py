# update
class pegawai:
    def __init__(self,nama,bagian):
        self.nama = nama
        self.bagian = bagian

class manajer(pegawai):
    def __init__(self,nama, bagian, gaji, bonus):
        super().__init__(nama,bagian)
        self.gaji = gaji
        self.bonus = bonus

    def hasil(self):
        print("-"*50)
        print("Nama     : ",self.nama)
        print("Bagian   : ",self.bagian)
        print("Gaji     : ",self.gaji)
        print("Bonus    : ",self.bonus)
        print("Total    : ",self.gaji + self.bonus)
        

class programer(pegawai):
    def __init__(self,nama, bagian, gaji, bonus, intensif):
        super().__init__(nama,bagian)
        self.Gaji = gaji
        self.bonus = bonus
        self.intensif = intensif

    def hasil(self):
        print("-" * 50)
        print("Nama     : ", self.nama)
        print("Bagian   : ", self.bagian)
        print("Gaji     : ", self.Gaji)
        print("Bonus    : ", self.bonus)
        print("Intensif : ", self.intensif)
        print("Total    : ", self.Gaji + self.bonus + self.intensif)
        

Pegawai_list = [

    manajer("dimas","manajer",300, 400),
    programer("ripal","pr",300,200, 100),
    manajer("yuda", "manager", 700, 500)
]

for pegawai in Pegawai_list:
    pegawai.hasil()




