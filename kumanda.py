import time


class Kumanda():


    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanal_listesi= ["Trt"], kanal="Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_on(self):
        if self.tv_durum == "Açık":
            print("Tv zaten açık...")
        else:
            print("Tv açılıyor...")
            time.sleep(2)
            self.tv_durum = "Açık"
            print("Tv açıldı...")

    def tv_off(self):
        if self.tv_durum == "Kapalı":
            print("Tv zaten kapalı..")
        else:
            print("Tv kapanıyor")
            time.sleep(2)
            self.tv_durum = "Kapalı"

    def voice_settings(self):
        while True:
            if self.tv_durum == "Açık":
                cevap = input("Sesi açmak için: +\nSesi azaltmak için: -\nİşlem seçiniz : ")
                if cevap == "+":
                    self.tv_ses += 1
                    print("Tv artırıldı:", self.tv_ses)
                elif cevap == "-":
                    self.tv_ses -= 1
                    print("Tv sesi azaltılıyor", self.tv_ses)
                else:
                    return
            else:
                print("Tv kapalıyken bu işlem gerçekleştirelemez Tv açılıyor lütfen bekleyin...")
                time.sleep(3)
                kumanda.tv_on()
                return

    def kanal_ekle(self, kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)



kumanda = Kumanda()
print("""
********************************************
******     TV KUMANDA UYGULAMASI      ******

******       1-Tv aç                  ******
 
******       2-Tv kapa                ******  

******       3-Ses ayarları           ******  

******       4-Kanal ekleme           ******  

******       5-Exit                   ******  
********************************************

""")
while True:
    process = int(input("İşlem seçiniz :"))
    if process == 1:
        kumanda.tv_on()
    elif process == 2:
        kumanda.tv_off()
    elif process == 3:
        kumanda.voice_settings()
    elif process == 4:
        kanal_isimleri = input("Eklemek istediniz kanalları arasında','koyarak giriniz\n")
        kanal_listesi = kanal_isimleri.split(",")
        for ekle in kanal_listesi:
            kumanda.kanal_ekle(ekle)
        print("Kanal listeniz güncellendi", kanal_listesi)
    elif process == 5:
        print("İşlem sonlandırılıyor")
        break
