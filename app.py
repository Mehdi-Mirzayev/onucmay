class BankHesabi:
    def __init__(self, hesab_nomresi: int, balans: float):
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans

    def depozit(self, mebleg: float):
        self.balans += mebleg
        print(f"{mebleg} AZN pul elave olundu. Yeni balans: {self.balans} AZN")

    def cixar(self, mebleg: float):
        if mebleg <= self.balans:
            self.balans -= mebleg
            print(f"{mebleg} AZN pul cixarildi. Yeni balans: {self.balans} AZN")
        else:
            print("Kifayet qeder vesait yoxdur")

    def balansi_goster(self):
        print(f"Hesab Nomresi: {self.hesab_nomresi} Balans: {self.balans} AZN")


class KreditHesabi(BankHesabi):
    def __init__(self, hesab_nomresi: int, balans: float, kredit_meblegi: float):
        super().__init__(hesab_nomresi, balans)
        self.kredit_meblegi = kredit_meblegi

    def kredit_ver(self):
        self.balans += self.kredit_meblegi
        print(f"{self.kredit_meblegi} AZN kredit hesabina elave olundu. Yeni balans: {self.balans} AZN")

    def kredit_ode(self):
        ayliq_odenis = self.kredit_meblegi / 12
        if ayliq_odenis <= self.balans:
            self.balans -= ayliq_odenis
            self.kredit_meblegi -= ayliq_odenis
            print(f"Kredit odenisi olan {ayliq_odenis} AZN ugurla odenildi. Yeni balans: {self.balans} AZN")
        else:
            print("Kredit odemek ucun kifayet qeder vesait yoxdur.")
