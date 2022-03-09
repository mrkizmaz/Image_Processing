"""
Ersel Kızmaz - ersel.kizmaz@gmail.com
Robotik Görme Temelleri
"""

# gerekli olan kütüphanelerin import edilmesi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import numpy as np
import math
import cv2
import os
import sys


class Ui_Form(object):
    
    # arayüz tasarım islemleri
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(449, 369)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 233, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 250, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 241, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 116, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 155, 52))
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
        brush = QtGui.QBrush(QtGui.QColor(252, 233, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 244, 167))
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
        brush = QtGui.QBrush(QtGui.QColor(252, 233, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 250, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 241, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 116, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 155, 52))
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
        brush = QtGui.QBrush(QtGui.QColor(252, 233, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 244, 167))
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
        brush = QtGui.QBrush(QtGui.QColor(126, 116, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 233, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 250, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 241, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 116, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 155, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 116, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 116, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 233, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 233, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 233, 79))
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
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 441, 71))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 80, 301, 131))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 90, 151, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sagButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sagButton.setObjectName("sagButton")
        self.horizontalLayout.addWidget(self.sagButton)
        self.solButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.solButton.setObjectName("solButton")
        self.horizontalLayout.addWidget(self.solButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 120, 151, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.yansimaButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.yansimaButton.setObjectName("yansimaButton")
        self.verticalLayout.addWidget(self.yansimaButton)
        self.negatifButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.negatifButton.setObjectName("negatifButton")
        self.verticalLayout.addWidget(self.negatifButton)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 210, 311, 51))
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 260, 371, 23))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.logAc = QtWidgets.QPushButton(self.layoutWidget)
        self.logAc.setObjectName("logAc")
        self.horizontalLayout_4.addWidget(self.logAc)
        self.logSlider = QtWidgets.QSlider(self.layoutWidget)
        self.logSlider.setOrientation(QtCore.Qt.Horizontal)
        self.logSlider.setObjectName("logSlider")
        self.horizontalLayout_4.addWidget(self.logSlider)
        self.logLabel = QtWidgets.QLabel(self.layoutWidget)
        self.logLabel.setObjectName("logLabel")
        self.horizontalLayout_4.addWidget(self.logLabel)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 290, 281, 41))
        self.label_3.setObjectName("label_3")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 330, 381, 23))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.powerAc = QtWidgets.QPushButton(self.layoutWidget_2)
        self.powerAc.setObjectName("powerAc")
        self.horizontalLayout_3.addWidget(self.powerAc)
        self.powerSlider = QtWidgets.QSlider(self.layoutWidget_2)
        self.powerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.powerSlider.setObjectName("powerSlider")
        self.horizontalLayout_3.addWidget(self.powerSlider)
        self.powerLabel = QtWidgets.QLabel(self.layoutWidget_2)
        self.powerLabel.setObjectName("powerLabel")
        self.horizontalLayout_3.addWidget(self.powerLabel)
        
        # butonlara basıldıgında calıstırılacak olan fonksiyonlar
        self.sagButton.clicked.connect(self.sagaIslem)
        self.solButton.clicked.connect(self.solaIslem)
        self.yansimaButton.clicked.connect(self.yansimaIslem)
        self.negatifButton.clicked.connect(self.negatifIslem)
        self.logAc.clicked.connect(self.logIslem)
        self.powerAc.clicked.connect(self.powerIslem)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "EEE 420 / Odev - 2"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#204a87;\"> ROBOTİK GÖRME TEMELLERİ <br/>ERSEL KIZMAZ - ersel.kizmaz@gmail.com<br/>-------------------------------------------------</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#204a87;\">1. Görüntüyü sağa veya sola döndürme <br/>işlemleri için yandaki butonlara tıklayınız. </span></p><p align=\"center\"><span style=\" font-weight:600; color:#204a87;\">2. Görüntünün y eksenine göre yansıması için <br/>yansıma butonuna tıklayınız.</span></p><p align=\"center\"><span style=\" font-weight:600; color:#204a87;\">3. Görüntünün negatifini görüntülemek için <br/>negatif butonuna tıklayınız.</span></p></body></html>"))
        self.sagButton.setText(_translate("Form", "Sağ"))
        self.solButton.setText(_translate("Form", "Sol"))
        self.yansimaButton.setText(_translate("Form", "Yansıma"))
        self.negatifButton.setText(_translate("Form", "Negatif"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#204a87;\">4. Görüntüye logaritma işlemi uygulamak için<br/> önce dosya açın ardından \'log slider\'ı kaydırın.</span></p></body></html>"))
        self.logAc.setText(_translate("Form", "Dosya Aç"))
        self.logLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#a40000;\">Log</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#204a87;\">5. Görüntüye power işlemi uygulamak için <br>önce dosya açın ardından \'power slider\'ı kaydırın.</span></p></body></html>"))
        self.powerAc.setText(_translate("Form", "Dosya Aç"))
        self.powerLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#a40000;\">Power</span></p></body></html>"))


    # görüntüyü saga döndürme islemi
    def sagaIslem(self):
        dosya_ismi = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter= '(*.png *.jpeg *.jpg)') # sadece resim dosyalı alır
        resim = cv2.imread(dosya_ismi[0]) # dosyanın dizini alır ve okur
        resim = cv2.resize(resim, (500,500)) # görüntünün boyutunu ayarlar
        cv2.imshow("OrjinalGoruntu", resim) # görüntüyü acar
        
        h,w,c = resim.shape # görüntünün yükseklik, genislik ve katman degerlerini alır
        sagImage = np.zeros([h,w,c], dtype=np.uint8) # görüntü degerlerine bos bir array
        
        # döngü islemi   
        for i in range(h):
            for j in range(w):
                sagImage[i,j] = resim[h-j-1,w-i-1]
               # sagImage = sagImage[0:h,0:w]

        # görüntüyü basarılı sekilde acar ve sonlanırır
        cv2.imshow("SagaDonenGoruntu", sagImage) 
        cv2.waitKey(0)
        cv2.destroyAllWindows()
      
    # görüntüyü sola döndürme islemi     
    def solaIslem(self):
        dosya_ismi = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter= '(*.png *.jpeg *.jpg)')
        resim = cv2.imread(dosya_ismi[0]) # dosyanın dizini alır ve okur
        resim = cv2.resize(resim, (500, 500))
        cv2.imshow("OrjinalGoruntu", resim) # görüntüyü acar
        
        h,w,c = resim.shape
        solImage = np.zeros([h,w,c], dtype=np.uint8)

        for i in range(h):
            for j in range(w):
                solImage[i,j] = resim[j-1,i-1]
                solImage = solImage[0:h,0:w]

        cv2.imshow("SolaDonenGoruntu", solImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
     
    # görüntüye yansıma uygulama islemi    
    def yansimaIslem(self):
        dosya_ismi = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter= '(*.png *.jpeg *.jpg)')
        resim = cv2.imread(dosya_ismi[0])
        resim = cv2.resize(resim, (500,300))
        cv2.imshow("OrjinalGoruntu", resim)
      
        rows, cols, dim = resim.shape
        M = np.float32([[-1, 0, cols],
                        [ 0, 1, 0],
                        [ 0, 0, 1]])

        yansimaImage = cv2.warpPerspective(resim,M,(int(cols),int(rows)))
        
        cv2.imshow("YansimaGoruntu", yansimaImage) 
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    # görüntüye negatif uygulama islemi    
    def negatifIslem(self):
        dosya_ismi = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter= '(*.png *.jpeg *.jpg)')
        resim = cv2.imread(dosya_ismi[0])
        resim = cv2.resize(resim, (500,300))
        cv2.imshow("OrjinalGoruntu", resim)
        
        negatifImage = np.invert(resim)
        
        cv2.imshow("NegatifGoruntu", negatifImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    # görüntüye log uygulama islemi    
    def logIslem(self):
        dosya_ismi = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter= '(*.png *.jpeg *.jpg)')
        resim = cv2.imread(dosya_ismi[0])
        resim = cv2.resize(resim, (500,300))
        cv2.imshow("OrjinalGoruntu", resim)
        
        self.logSlider.valueChanged.connect(self.sliderLogIslem) # log slider fonskiyonu
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    # log slider islemi
    def sliderLogIslem(self): 
        path = '/home/mrkizmaz/Desktop/resimler-eee420/maserati.jpg'
        resim = cv2.imread(path)
        resim = cv2.resize(resim, (500,300))
        
        value = str(self.logSlider.value())
        self.logLabel.setText(value)
        
        c = 255 / np.log(1 + int(value))
        logImage = c * (np.log10(resim + 1))
        logImage = np.array(logImage, dtype=np.uint8)
        cv2.imshow("LogGoruntu", logImage)
        
    # görüntüye power uygulama islemi
    def powerIslem(self):
        dosya_ismi = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter= '(*.jpeg *.xpm *.jpg)')
        resim = cv2.imread(dosya_ismi[0])
        resim = cv2.resize(resim, (500,300))
        cv2.imshow("OrjinalGoruntu", resim) 
        
        self.powerSlider.valueChanged.connect(self.sliderPowerIslem) # power slider fonksiyonu
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # power slider islemi
    def sliderPowerIslem(self):
        path = '/home/mrkizmaz/Desktop/resimler-eee420/doga.jpg'
        resim = cv2.imread(path)
        resim = cv2.resize(resim, (500,300))
        
        value = str(self.powerSlider.value())
        self.powerLabel.setText(value)
        powerImage = np.power(resim, int(value))
        cv2.imshow("PowerGoruntu", powerImage)
        
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