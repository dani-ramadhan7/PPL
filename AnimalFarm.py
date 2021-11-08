class HewanTernak:
    def __init__(self, name, jenisHewan, jenisMakanan):
        self.name = name
        self.jenisHewan = jenisHewan
        self.jenisMakanan = jenisMakanan
    
    def printDescription(self):
        print(self.name, self.jenisHewan, self.jenisMakanan)

Ayam = HewanTernak("Ayam", "unggas", "omnivora")
Kambing = HewanTernak("Kambing", "mamalia", "herbivora")

Ayam.printDescription()
Kambing.printDescription()