# herhangi bir görüntünün koordinat, RGB ve HSV degerlerini gösteren program

"""
Bu uygulama Linux isletim siteminde gelistirilmistir.
Windows ortamında calıstırılırsa hata verebilir!
"""

# gerekli olan kütüphanelerin import edilmesi
import sys 
import os
import cv2
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout

# arayüz tasarlamak icin kullanılan class
class Isleme(QWidget):
    # arayüz tasarlamak icin gerekli olan kalıtım islemleri
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(400,200,300,150) # arayüzün konumu ve boyutu
        text1 = """
\t\tGörüntü İşleme Programı \n
Bilgisayarınızdan istediğiniz resim dosyayısını secerek 
dosyanın koordinat, RGB ve HSV degerlerini göreceksiniz.

"""
        text2 = "(Bu uygulama sadece .png ve .jpg uzantılı dosyalarda çalışır.)"
        self.yazi_alani = QLabel(text1 + text2)
        self.yazi_alani.move(10,10)
        
        self.open = QPushButton("Dosya Aç") # acma butonu

        h_box = QHBoxLayout() # horizontal box
        h_box.addWidget(self.open) # butonu pencere üzerine ekler

        v_box = QVBoxLayout() # vertical box
        v_box.addWidget(self.yazi_alani) # vbox üzerine label ekler
        v_box.addLayout(h_box)

        self.setLayout(v_box) # pencere üzerinde vbox ekler
        self.setWindowTitle("Görüntü İşleme Uygulaması") # pencere ismi
        
        self.open.clicked.connect(self.openFile) # butona basıldıgı zaman fonksiyona gider
        self.show()  # pencereyi gösterir
        
    # butona basıldıgında dosya acma fonksiyonu
    def openFile(self):
        dosya_ismi = QFileDialog.getOpenFileName(self, "Dosya Aç", os.getenv("HOME")) # dizin, tuple seklinde alır
        
        # görüntü isleme fonksiyonu
        def TiklamaOlayi(olay, x, y, flags, param):
            if olay == cv2.EVENT_LBUTTONDOWN:
                h = hsv[y, x, 0]
                s = hsv[y, x, 1]
                v = hsv[y, x, 2]
                hsvUzayi = 'HSI: ' + str(h) + ' ' + str(s) + ' ' + str(v)
                cv2.putText(goruntu, hsvUzayi, (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (100,20,0),1) # görüntü degerleri
                cv2.imshow("Goruntu", goruntu) # görüntüyü acar

        goruntu = cv2.imread(dosya_ismi[0]) # dosyanın dizini alır ve okur
        hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV) # RGB'den HSV dönüstürme fonksiyonu ve renklendirme
        cv2.imshow("Goruntu", goruntu) # resim ismi ve görüntüyü acar
        cv2.setMouseCallback('Goruntu',TiklamaOlayi) # mouse tıkladıgında HSV degerlerini gösterir

        cv2.waitKey(0)
        cv2.destroyAllWindows() # uygulamayı basarılı sekilde calıstırır ve sonlandırır
    
app = QApplication(sys.argv) # arayüz uygulamasının bulundugu dosyayı okur

Isleme = Isleme() # uygulama classını calıstırır
sys.exit(app.exec_()) # pencerede x tusuna basıldıgında uygulamayı sonlandırır