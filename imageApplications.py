"""
EEE 420 - ROBOTİK GÖRME TEMELLERİ / ÖDEV - 3
ERSEL KIZMAZ - 31018008
ATEŞ TAŞ - 31017068
KEMAL GEYLANİ YUKİ - 31017024
"""

# gerekli kütüphanelerin dahil edilmesi
import os, sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
import numpy as np

# arayüz tasarım islemleri
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(331, 242)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 147, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 94, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 27, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 148, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 147, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 94, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 27, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 148, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 147, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 94, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 27, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        Form.setPalette(palette)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 0, 291, 91))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 90, 291, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        # self.dosyaAc = QtWidgets.QPushButton(self.verticalLayoutWidget)
        # self.dosyaAc.setObjectName("dosyaAc")
        # self.verticalLayout.addWidget(self.dosyaAc)
        self.grayScale = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.grayScale.setObjectName("grayScale")
        self.verticalLayout.addWidget(self.grayScale)
        self.histogram = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.histogram.setObjectName("histogram")
        self.verticalLayout.addWidget(self.histogram)
        self.histEqualization = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.histEqualization.setObjectName("histEqualization")
        self.verticalLayout.addWidget(self.histEqualization)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "EEE 420 / Odev - 3"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#eeeeec;\">EEE 420 - ROBOTİK GÖRME TEMELLERİ / ÖDEV - 3 <br/>ERSEL KIZMAZ - 31018008 <br/>ATEŞ TAŞ - 31017068 <br/>KEMAL GEYLANİ YUKİ - 31017024</span></p></body></html>"))
        # self.dosyaAc.setText(_translate("Form", "Dosya Aç"))
        self.grayScale.setText(_translate("Form", "Gray Scale"))
        self.histogram.setText(_translate("Form", "Histogram"))
        self.histEqualization.setText(_translate("Form", "Histogram Equalization"))


        # butonlara basıldıgında calıstırılacak olan fonksiyonlar
        # self.dosyaAc.clicked.connect(self.dosyaAcIslem)
        self.grayScale.clicked.connect(self.grayScaleIslem)
        self.histogram.clicked.connect(self.histogramIslem)
        self.histEqualization.clicked.connect(self.histEqualizationIslem)

    # dosya acma islemi
    """def dosyaAcIslem(self):
        dosya_ismi = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter= '(*.png *.jpeg *.jpg)') # sadece resim dosyalı alır
        resim = cv2.imread(dosya_ismi[0]) # dosyanın dizini alır ve okur
        resim = cv2.resize(resim, (500,500)) # görüntünün boyutunu ayarlar
        cv2.imshow("OrjinalGoruntu", resim) # görüntüyü acar

        cv2.waitKey(0)
        cv2.destroyAllWindows()"""

    # gray scale islemi
    def grayScaleIslem(self):
        dosya_ismi = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter= '(*.png *.jpeg *.jpg)') # sadece resim dosyalı alır
        resim = cv2.imread(dosya_ismi[0]) # dosyanın dizini alır ve okur
        resim = cv2.resize(resim, (500,500)) # görüntünün boyutunu ayarlar
        cv2.imshow("OrjinalGoruntu", resim) # görüntüyü acar

        red = resim[:, :, 0]
        green = resim[:, :, 1]
        blue = resim[:, :, 2]

        imgGray = 0.2989 * red + 0.5870 * green + 0.1140 * blue
        plt.imshow(imgGray, cmap='gray')
        plt.show()

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def histogramIslem(self):
        dosya_ismi = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter= '(*.png *.jpeg *.jpg)') # sadece resim dosyalı alır
        resim = cv2.imread(dosya_ismi[0]) # dosyanın dizini alır ve okur
        resim = cv2.resize(resim, (500,500)) # görüntünün boyutunu ayarlar
        cv2.imshow("OrjinalGoruntu", resim) # görüntüyü acar

        R = np.zeros((256), dtype=int)
        G = np.zeros((256), dtype=int)
        B = np.zeros((256), dtype=int)
        I=  np.zeros((256), dtype=int)
        k = 0

        while k<256:
            R[k] = np.count_nonzero(resim[:, :, 2] == k)    # img=0 0 ların sayısı, img=1 1 lerin sayısı...
            G[k] = np.count_nonzero(resim[:, :, 1] == k)
            B[k] = np.count_nonzero(resim[:, :, 0] == k)
            I[k] = np.count_nonzero(resim[:, :] == k)
            k = k+1

        intensity = np.arange(0,256,1)      #grafikteki intensity çubuğu 0-255 arası 1 er artıyor.

        plt.figure(figsize=(10,20))

        #RED
        plt.subplot(411)
        plt.bar(intensity, R, color="red", width=0.5)
        #plt.xlabel("Intensity")
        plt.ylabel("Frequency")
        plt.title("RED")

        #BLUE
        plt.subplot(412)
        plt.bar(intensity, G, color="green", width=0.5)
        #plt.xlabel("Intensity")
        plt.ylabel("Frequency")
        plt.title("GREEN")

        #GREEN
        plt.subplot(413)
        plt.bar(intensity, B, color="blue", width=0.5)
        #plt.xlabel("Intensity")
        plt.ylabel("Frequency")
        plt.title("BLUE")

        #Intensity
        plt.subplot(414)
        plt.bar(intensity, I, color="black", width=0.5)
        plt.xlabel("Intensity")
        plt.ylabel("Frequency")
        plt.title("Intensity")

        plt.show()
        cv2.waitKey(0)

    # histogram equalize islemi
    def histEqualizationIslem(self):
        dosya_ismi = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter= '(*.png *.jpeg *.jpg)') # sadece resim dosyalı alır
        resim = cv2.imread(dosya_ismi[0]) # dosyanın dizini alır ve okur
        resim = cv2.resize(resim, (500,500)) # görüntünün boyutunu ayarlar
        cv2.imshow("OrjinalGoruntu", resim) # görüntüyü acar

        a = np.zeros((256,),dtype=np.float16)
        b = np.zeros((256,),dtype=np.float16)

        height, width, cols = resim.shape

        #Histogramın alınması ve indisin 1 arttırılması
        for i in range(width):
            for j in range(height):
                g = resim[j,i]        # g renkleri tutar
                a[g] = a[g]+1       # 0,255 değerlerinin piksel sayıları

        #print(a)

        b = np.zeros((256,),dtype=np.float16)

        #Histogram eşitleme işleminin yapılması
        for i in range(256):
            for j in range(i+1):
                b[i] += a[j]/(height*width);
            b[i] = round(b[i] * 255);        # yuvarlama komutu

        b=b.astype(np.uint8)        #tüm elemanları int yap

        #print(b)
        #Sonucun atanması
        for i in range(width):
            for j in range(height):
                g = resim[j,i]
                resim[j,i]= b[g]

        cv2.imshow('image',resim)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
