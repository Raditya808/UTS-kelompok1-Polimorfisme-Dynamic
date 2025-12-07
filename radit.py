# ide pertama (raditya membuat class yang di isi masing masing function dan pewaris)
# dan membuat masing masing gaji manager dan  programmer beserta bonus yang diwariskan class pekerja

class pekerja:
    def gaji(self):
        return 1000000

class manager(pekerja):
    def gaji(self):
        return 5000000
        
class programmer(pekerja):
    def gaji(self):
        return 3000000
        
class manager_bonus(pekerja):
    def gaji(self):
        return 3500000
        
class bonus_programmer(pekerja):
    def gaji(self):
        return 3500000


def gaji(a):
   return a.gaji()

tes1 = manager()
print(f"Gaji Manager adalah =",gaji(tes1))
tes2 = programmer()
print(f"Gaji Programmer adalah = {tes2.gaji()}")
tes3 = bonus_programmer()
print(f"Gaji bonus untuk Programmer adalah = {tes3.gaji()}")
tes4 = manager_bonus()
print(f"Gaji Bonus Manager adalah = {tes4.gaji()}")

