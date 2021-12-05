# -*- coding: utf-8 -*-
#importando bibliotecas

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from pytube import YouTube
from pytube.cli import on_progress
import os

#criando a janela do GUI
class Ui_Youtuber_Download(object):
    def setupUi(self, Youtuber_Download):
        Youtuber_Download.setObjectName("Youtuber_Download")
        Youtuber_Download.resize(466, 450)
        Youtuber_Download.setMinimumSize(QtCore.QSize(466, 450))
        Youtuber_Download.setMaximumSize(QtCore.QSize(466, 450))
        self.centralwidget = QtWidgets.QWidget(Youtuber_Download)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_download = QtWidgets.QPushButton(self.centralwidget)
        self.bt_download.setGeometry(QtCore.QRect(270, 300, 186, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        #definindo botão para download
        self.bt_download.setFont(font)
        self.bt_download.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 51, 51);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}")
        self.bt_download.setObjectName("bt_download")

        #definindo labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 20, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 10, 191, 101))
        self.label_4.setStyleSheet("image: url(:/yt/Youtube-PNG.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 310, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 380, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        #definindo os LineEdit
        self.txt_link = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_link.setGeometry(QtCore.QRect(120, 120, 301, 20))
        self.txt_link.setObjectName("txt_link")
        self.txt_link.setPlaceholderText('Digite a URL do video')
        self.txt_titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_titulo.setGeometry(QtCore.QRect(120, 160, 301, 20))
        self.txt_titulo.setObjectName("txt_titulo")
        self.txt_titulo.setPlaceholderText('Digite o nome do arquivo que deseja salvar')
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 300, 62, 56))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_dir.setGeometry(QtCore.QRect(180, 220, 251, 20))
        self.txt_dir.setObjectName("txt_dir")
        self.txt_dir.setPlaceholderText('Diretório')

        #Definindo o radio button
        self.rd_mp3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.rd_mp3.setFont(font)
        self.rd_mp3.setChecked(True)
        self.rd_mp3.setObjectName("rd_mp3")
        self.verticalLayout.addWidget(self.rd_mp3)
        self.rd_mp4 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.rd_mp4.setFont(font)
        self.rd_mp4.setObjectName("rd_mp4")
        self.verticalLayout.addWidget(self.rd_mp4)

        #Definindo barra de progresso
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 410, 301, 23))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.progressBar.setFont(font)
        self.progressBar.setObjectName("progressBar")

        #Definindo combobox
        self.cb_res = QtWidgets.QComboBox(self.centralwidget)
        self.cb_res.setGeometry(QtCore.QRect(90, 310, 69, 22))
        self.cb_res.setObjectName("cb_res")
        self.cb_res.addItem("")
        self.cb_res.addItem("")
        self.cb_res.addItem("")
        self.cb_res.addItem("")
        self.cb_res.addItem("")

        #definindo botão para diretorio
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 210, 121, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 10px;\n"
"    min-width: 6em;\n"
"    padding: 6px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        
        Youtuber_Download.setCentralWidget(self.centralwidget)

        self.retranslateUi(Youtuber_Download)
        QtCore.QMetaObject.connectSlotsByName(Youtuber_Download)

        self.pushButton.clicked.connect(self.salvar)
        self.bt_download.clicked.connect(self.download_l)
       


    def retranslateUi(self, Youtuber_Download):
        _translate = QtCore.QCoreApplication.translate
        Youtuber_Download.setWindowTitle(_translate("Youtuber_Download", "MainWindow"))
        self.bt_download.setText(_translate("Youtuber_Download", "DOWNLOAD"))
        self.label.setText(_translate("Youtuber_Download", "Título:"))
        self.label_2.setText(_translate("Youtuber_Download", "Link:"))
        self.label_3.setText(_translate("Youtuber_Download", "Download"))
        self.rd_mp3.setText(_translate("Youtuber_Download", "MP3"))
        self.rd_mp4.setText(_translate("Youtuber_Download", "MP4"))
        self.cb_res.setItemText(0, _translate("Youtuber_Download", "720p"))
        self.cb_res.setItemText(1, _translate("Youtuber_Download", "480p"))
        self.cb_res.setItemText(2, _translate("Youtuber_Download", "360p"))
        self.cb_res.setItemText(3, _translate("Youtuber_Download", "240p"))
        self.cb_res.setItemText(4, _translate("Youtuber_Download", "144p"))
        self.label_5.setText(_translate("Youtuber_Download", "Resolução:"))
        self.label_6.setText(_translate("Youtuber_Download", "Download progress"))
        self.pushButton.setText(_translate("Youtuber_Download", "Pasta para download"))

    #função para salvar o diretório
    def salvar(self):
        arquivo =QtWidgets.QFileDialog.getExistingDirectory()
        self.txt_dir.setText(arquivo)

    #função para atualização da progressbar
    def progressbar(self, streamm, chunk, byte_remaining):
        size = round(((streamm.filesize - byte_remaining) / streamm.filesize)*100.0)
        self.progressBar.setValue(size)
        QApplication.processEvents()
        if size == 100.0:
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setText('Download Concluido') 
            x = msg.exec_()

    #função para realizar o download        
    def download_l(self):
        #download no formato mp3
        if self.rd_mp3.isChecked() == True:
            try:
                self.progressBar.setValue(0)
                self.url = self.txt_link.text()
                titulo = self.txt_titulo.text()
                self.my_video = YouTube(self.url, on_progress_callback= self.progressbar)   
                           
                self.my_video = self.my_video.streams.get_audio_only()
                self.out_file = self.my_video.download(self.txt_dir.text(),filename=self.txt_titulo.text())
                self.base, self.ext = os.path.splitext(self.out_file)  # para baixar mp3
                self.new_file = self.base + '.mp3'  # para baixar mp3
                os.rename(self.out_file, self.new_file) 
        
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText('Link Inválido')  

                x = msg.exec_()

        #download no formato mp4
        elif self.rd_mp4.isChecked() == True:
            try:
                self.progressBar.setValue(0)
                self.url = self.txt_link.text()
                titulo = self.txt_titulo.text()
                self.my_video = YouTube(self.url, on_progress_callback= self.progressbar)              
                self.my_video = self.my_video.streams.get_by_resolution(self.cb_res.currentText()) 
                self.download_dir = self.txt_dir.text()
                self.my_video.download(self.download_dir,filename=self.txt_titulo.text())
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText('Link Inválido')   
                x = msg.exec_()


#importando imagens
import yt
#executando a aplicação
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Youtuber_Download = QtWidgets.QMainWindow()
    ui = Ui_Youtuber_Download()
    ui.setupUi(Youtuber_Download)
    Youtuber_Download.show()
    sys.exit(app.exec_())

