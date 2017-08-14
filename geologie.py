# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'general.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Geologie_donnees as geologie_data
import math as mathematiques

class Ui_Accueil(object):

    ###################### Déclaration des tableaux ######################################

    donnees_x = list()
    donnees_x_initiale = list()
    donnees_y = list()
    donnees_z = list()
    donnees_converties = False
    echelle = 0.0
    equidistance = 0
    fascicule = 0

    ################## les fonctions appliquées aux différents boutons ###################
    def quitterApplication(self):
        sys.exit()

    def afficherSaisie(self):
        self.tableWidget.setVisible(1)
        self.label_table.setVisible(1)
        self.btn_convertir.setVisible(1)
        self.btn_calcul_equ.setVisible(1)
        self.btn_courbe.setVisible(1)
        self.btn_profil.setVisible(1)
        self.label_val_equi.setVisible(1)
        self.val_equi.setVisible(1)
        self.val_echelle.setVisible(1)
        self.label_val_echelle.setVisible(1)
        self.btn_calcul_echelle.setVisible(1)
        self.btn_ann_quit.setVisible(1)
        self.label_saisie_donnee.setVisible(1)
        self.btn_moins.setVisible(1)
        self.btn_plus.setVisible(1)
        self.line_separateur.setVisible(1)
        self.label_long_papier.setVisible(1)
        self.lineEdit_long_papier.setVisible(1)
        self.label_long_cm.setVisible(1)
        self.label_Long_papier.setVisible(1)
        self.lineEdit_Long_papier.setVisible(1)
        self.label_Long_km.setVisible(1)
        self.label_val_fascicule.setVisible(1)
        self.lineEdit_val_fascicule.setVisible(1)
        self.label_val_cm.setVisible(1)

    def cacherElts(self):
        self.tableWidget.setVisible(0)
        self.label_table.setVisible(0)
        self.btn_convertir.setVisible(0)
        self.btn_calcul_equ.setVisible(0)
        self.btn_courbe.setVisible(0)
        self.btn_profil.setVisible(0)
        self.label_val_equi.setVisible(0)
        self.val_equi.setVisible(0)
        self.val_echelle.setVisible(0)
        self.label_val_echelle.setVisible(0)
        self.btn_calcul_echelle.setVisible(0)
        self.btn_ann_quit.setVisible(0)
        self.label_saisie_donnee.setVisible(0)
        self.btn_moins.setVisible(0)
        self.btn_plus.setVisible(0)
        self.line_separateur.setVisible(0)
        self.label_long_papier.setVisible(0)
        self.lineEdit_long_papier.setVisible(0)
        self.label_long_cm.setVisible(0)
        self.label_Long_papier.setVisible(0)
        self.lineEdit_Long_papier.setVisible(0)
        self.label_Long_km.setVisible(0)
        self.label_val_fascicule.setVisible(0)
        self.lineEdit_val_fascicule.setVisible(0)
        self.label_val_cm.setVisible(0)
        self.lineEdit_long_papier.clear()
        self.lineEdit_Long_papier.clear()
        self.lineEdit_val_fascicule.clear()
        self.tableWidget.clearContents()
        self.val_echelle.clear()
        self.val_equi.clear()
        self.donnees_converties = False
        self.donnees_x.clear()
        self.donnees_x_initiale.clear()
        self.donnees_y.clear()
        self.donnees_z.clear()

   ################### Ajout d'une ligne au tableau #################################
    def ajouterLigne(self):
        self.tableWidget.insertRow(self.tableWidget.rowCount())

   ################### Rétrait d'une ligne au tableau #################################
    def retirerLigne(self):
        self.tableWidget.removeRow(self.tableWidget.rowCount() - 1)

    ################### CAalcul de l'éechelle ########################################
    def calculEchelle(self):
        if(len(self.lineEdit_Long_papier.text()) == 0 or len(self.lineEdit_Long_papier.text()) == 0):
            QtWidgets.QMessageBox.information(self.tableWidget, "Calcul de l'échelle", "Veuillez renseigner les champs longueur et Longueur sur papier !")
        else:
            long_papier = self.lineEdit_long_papier.text()
            Long_papier = self.lineEdit_Long_papier.text()
            self.echelle = geologie_data.calculerEchelle(long_papier, Long_papier)
            self.val_echelle.setText("1 : "+str(self.echelle))

            ############ la fonction qui saisit les données ##########
            def saisieDonnees(self, nb_lignes, nb_colonnes):
                i, j = 0, 0
                for i in range(0, nb_lignes):
                    for i in range(0, nb_lignes):
                        for j in range(0, nb_colonnes):
                            value = self.tableWidget.item(i, j)
                            if value is not None and len(value.text()) != 0:
                                value = value.text()
                                if j == 0:
                                    #if(QtWidgets.QTableWidget.cellChanged(self.tableWidget, i, j)):
                                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(geologie_data.convertirX(int(value)))))
                                    self.donnees_y.append(geologie_data.convertirY(int(value), self.echelle))
                                    self.tableWidget.setItem(i, j + 1, QtWidgets.QTableWidgetItem(
                                        str(geologie_data.convertirY(int(value), self.echelle))))
                                    self.donnees_z.append(geologie_data.convertirY(int(value), self.echelle))
                                    self.tableWidget.setItem(i, j + 2, QtWidgets.QTableWidgetItem(
                                        str(geologie_data.convertirY(self.fascicule, self.echelle))))
                                print("The current is ", i, ", ", j)
                                print("In this cell we have ", value)

    ################### Conversion des données du tableau #############################
                   ############ la fonction qui convertit les données ##########
    def conversionDonnees(self, nb_lignes, nb_colonnes):
        self.calculEchelle()
        self.fascicule = int(self.lineEdit_val_fascicule.text())
        i, j = 0, 0
        for i in range (0, nb_lignes):
            for j in range(0, nb_colonnes):
                value = self.tableWidget.item(i, j)
                if value is not None and len(value.text()) != 0:
                    value = value.text()
                    if j == 0:
                        self.donnees_x_initiale.append((int(value)))
                        self.donnees_x.append(geologie_data.convertirX(int(value)))
                        self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(geologie_data.convertirX(int(value)))))
                        self.donnees_y.append(geologie_data.convertirY(int(value), self.echelle))
                        self.tableWidget.setItem(i, j+1, QtWidgets.QTableWidgetItem(str(geologie_data.convertirY(int(value), self.echelle))))
                        self.donnees_z.append(geologie_data.convertirY(self.fascicule, self.echelle))
                        self.tableWidget.setItem(i, j+2, QtWidgets.QTableWidgetItem(str(geologie_data.convertirY(self.fascicule, self.echelle))))
                    print("The current is ", i, ", ", j)
                    print("In this cell we have ", value)
        self.donnees_converties = True

    ########################## L'action qui declenche la conversion ###################

    def boutonConvertir(self):
        if(len(self.lineEdit_Long_papier.text()) == 0 or len(self.lineEdit_Long_papier.text()) == 0 or len(self.lineEdit_val_fascicule.text()) == 0):
            QtWidgets.QMessageBox.information(self.tableWidget, "Conversion des données",
                                              "Veuillez d'abord renseigner les champs longueur, Longueur et fascicule !")
        else:
            nbLignes = self.tableWidget.rowCount()
            nbColonnes = self.tableWidget.columnCount()
            if self.donnees_converties is not True:
                self.conversionDonnees(nbLignes, nbColonnes)
                QtWidgets.QMessageBox.information(self.tableWidget, "Conversion des données",
                                                  "Les données ont été converties. Retrouvez les données dans le tableau !")
            else:
                QtWidgets.QMessageBox.information(self.tableWidget, "Conversion des données",
                                                  "Les données ont déjà été converties !")

        print(self.donnees_converties)
        print("======== X init  =======")
        print(self.donnees_x_initiale)
        print("======== X =======")
        print(self.donnees_x)
        print("======== Y =======")
        print(self.donnees_y)
        print("======== Z =======")
        print(self.donnees_z)

########--------------------- Calcul de l'équidistance --------------------#########
    def calculEquidistance(self):
        if self.donnees_converties is True:
            tableau_vals_equi = [x_item for x_item in self.donnees_x_initiale if x_item % 10 == 0]
            if len(tableau_vals_equi) == 2:
                self.equidistance = geologie_data.calculerEquidistance(tableau_vals_equi[0], tableau_vals_equi[1])
                self.val_equi.setText(str(int(self.equidistance)))
            else:
                QtWidgets.QMessageBox.information(self.tableWidget, "Calcul de l'équidistance",
                                                  "Il faut deux (02) points non côtés (sur la courbe) pour calculer l'équidistance !")
        else:
            QtWidgets.QMessageBox.information(self.tableWidget, "Courbe Géologique",
                                              "Veuillez d'abord convertir les données !")

########---------------- Tracé de la courbe géologique ----------------##################
    def courbeGeologique(self):
        if self.donnees_converties is True:
            geologie_data.tracerCourbeGeologique(self.donnees_x, self.donnees_y)
        else:
            QtWidgets.QMessageBox.information(self.tableWidget, "Courbe Géologique",
                                              "Veuillez d'abord convertir les données !")

########---------------- Tracé du profil topographique ----------------##################
    def profilTopographique(self):
        if self.donnees_converties is True:
            geologie_data.tracerProfilTopographique(self.donnees_x, self.donnees_y, self.donnees_z)
        else:
            QtWidgets.QMessageBox.information(self.tableWidget, "Profil topographique",
                                              "Veuillez d'abord convertir les données !")

##################### Fin des fonctions #################################################

    def setupUi(self, Accueil):
        Accueil.setObjectName("Accueil")
        Accueil.resize(1000, 600)
        Accueil.setMinimumSize(QtCore.QSize(1000, 600))
        Accueil.setMaximumSize(QtCore.QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(Accueil)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1000, 581))
        self.label.setMinimumSize(QtCore.QSize(1000, 0))
        self.label.setMaximumSize(QtCore.QSize(1000, 16777215))
        pixmap = QtGui.QPixmap("images/img.jpg")
        self.label.setPixmap(pixmap)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_table = QtWidgets.QLabel(self.centralwidget)
        self.label_table.setGeometry(QtCore.QRect(0, 0, 1001, 601))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_table.setFont(font)
        self.label_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_table.setObjectName("label_table")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 371, 441))
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(12)
        self.tableWidget.setColumnCount(3)
        col_headers = ['Xm', 'Ymm = X/E', 'EPmm = Val/E']
        self.tableWidget.setHorizontalHeaderLabels(col_headers)
        self.tableWidget.setObjectName("tableWidget")
        self.btn_convertir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_convertir.setGeometry(QtCore.QRect(560, 100, 171, 41))
        self.btn_convertir.setObjectName("btn_convertir")

        ############# Action du bouton Tout annuler ####################
        self.btn_convertir.clicked.connect(self.boutonConvertir)
        ################################################################

        self.btn_calcul_equ = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calcul_equ.setGeometry(QtCore.QRect(560, 190, 171, 41))
        self.btn_calcul_equ.setObjectName("btn_calcul_equ")

        ############# Action du bouton Tout annuler ####################
        self.btn_calcul_equ.clicked.connect(self.calculEquidistance)
        ################################################################

        self.btn_courbe = QtWidgets.QPushButton(self.centralwidget)
        self.btn_courbe.setGeometry(QtCore.QRect(770, 100, 171, 41))
        self.btn_courbe.setObjectName("btn_courbe")

        ############# Action du bouton Tout annuler ####################
        self.btn_courbe.clicked.connect(self.courbeGeologique)
        ################################################################

        self.btn_profil = QtWidgets.QPushButton(self.centralwidget)
        self.btn_profil.setGeometry(QtCore.QRect(770, 190, 171, 41))
        self.btn_profil.setObjectName("btn_profil")

        ############# Action du bouton Tout annuler ####################
        self.btn_profil.clicked.connect(self.profilTopographique)
        ################################################################

        self.label_val_equi = QtWidgets.QLabel(self.centralwidget)
        self.label_val_equi.setGeometry(QtCore.QRect(570, 380, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_val_equi.setFont(font)
        self.label_val_equi.setObjectName("label_val_equi")
        self.val_equi = QtWidgets.QLabel(self.centralwidget)
        self.val_equi.setGeometry(QtCore.QRect(770, 380, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.val_equi.setFont(font)
        self.val_equi.setText("")
        self.val_equi.setObjectName("val_equi")
        self.val_echelle = QtWidgets.QLabel(self.centralwidget)
        self.val_echelle.setGeometry(QtCore.QRect(780, 460, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.val_echelle.setFont(font)
        self.val_echelle.setText("")
        self.val_echelle.setObjectName("val_echelle")
        self.label_val_echelle = QtWidgets.QLabel(self.centralwidget)
        self.label_val_echelle.setGeometry(QtCore.QRect(590, 460, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_val_echelle.setFont(font)
        self.label_val_echelle.setObjectName("label_val_echelle")
        self.btn_calcul_echelle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calcul_echelle.setGeometry(QtCore.QRect(560, 270, 171, 41))
        self.btn_calcul_echelle.setObjectName("btn_calcul_echelle")

        ############# Action du bouton Tout annuler ####################
        self.btn_calcul_echelle.clicked.connect(self.calculEchelle)
        ################################################################

        self.btn_ann_quit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ann_quit.setGeometry(QtCore.QRect(770, 270, 171, 41))
        self.btn_ann_quit.setObjectName("btn_ann_quit")

        ############# Action du bouton Tout annuler ####################
        self.btn_ann_quit.clicked.connect(self.cacherElts)
        ################################################################

        self.label_saisie_donnee = QtWidgets.QLabel(self.centralwidget)
        self.label_saisie_donnee.setGeometry(QtCore.QRect(10, 0, 981, 71))
        self.label_saisie_donnee.setStyleSheet("color: rgb(255, 85, 0);\n"
"background-color: rgb(85, 255, 127);\n"
"font: 75 28pt \"MS Reference Sans Serif\";")
        self.label_saisie_donnee.setObjectName("label_saisie_donnee")
        self.btn_moins = QtWidgets.QPushButton(self.centralwidget)
        self.btn_moins.setGeometry(QtCore.QRect(40, 540, 21, 21))
        self.btn_moins.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/moins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_moins.setIcon(icon)
        self.btn_moins.setObjectName("btn_moins")

        ############# Action du bouton Moins ####################
        self.btn_moins.clicked.connect(self.retirerLigne)
        #########################################################

        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(10, 540, 21, 21))
        font = QtGui.QFont()
        font.setKerning(False)
        self.btn_plus.setFont(font)
        self.btn_plus.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_plus.setIcon(icon1)
        self.btn_plus.setObjectName("btn_plus")

        ############# Action du bouton Plus ####################
        self.btn_plus.clicked.connect(self.ajouterLigne)
        #########################################################

        self.line_separateur = QtWidgets.QFrame(self.centralwidget)
        self.line_separateur.setGeometry(QtCore.QRect(533, 70, 41, 511))
        self.line_separateur.setLineWidth(3)
        self.line_separateur.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_separateur.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_separateur.setObjectName("line_separateur")
        self.label_long_papier = QtWidgets.QLabel(self.centralwidget)
        self.label_long_papier.setGeometry(QtCore.QRect(390, 80, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_long_papier.setFont(font)
        self.label_long_papier.setObjectName("label_long_papier")
        self.lineEdit_long_papier = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_long_papier.setGeometry(QtCore.QRect(390, 110, 121, 31))
        self.lineEdit_long_papier.setObjectName("lineEdit_long_papier")
        self.label_long_cm = QtWidgets.QLabel(self.centralwidget)
        self.label_long_cm.setGeometry(QtCore.QRect(520, 115, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_long_cm.setFont(font)
        self.label_long_cm.setObjectName("label_long_cm")
        self.label_Long_km = QtWidgets.QLabel(self.centralwidget)
        self.label_Long_km.setGeometry(QtCore.QRect(520, 210, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Long_km.setFont(font)
        self.label_Long_km.setObjectName("label_Long_km")
        self.lineEdit_Long_papier = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Long_papier.setGeometry(QtCore.QRect(390, 205, 121, 31))
        self.lineEdit_Long_papier.setObjectName("lineEdit_Long_papier")
        self.label_Long_papier = QtWidgets.QLabel(self.centralwidget)
        self.label_Long_papier.setGeometry(QtCore.QRect(390, 175, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_Long_papier.setFont(font)
        self.label_Long_papier.setObjectName("label_Long_papier")
        self.label_val_cm = QtWidgets.QLabel(self.centralwidget)
        self.label_val_cm.setGeometry(QtCore.QRect(520, 320, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_val_cm.setFont(font)
        self.label_val_cm.setObjectName("label_val_cm")
        self.lineEdit_val_fascicule = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_val_fascicule.setGeometry(QtCore.QRect(390, 315, 121, 31))
        self.lineEdit_val_fascicule.setObjectName("lineEdit_val_fascicule")
        self.label_val_fascicule = QtWidgets.QLabel(self.centralwidget)
        self.label_val_fascicule.setGeometry(QtCore.QRect(390, 280, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_val_fascicule.setFont(font)
        self.label_val_fascicule.setObjectName("label_val_fascicule")
        Accueil.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Accueil)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 25))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        Accueil.setMenuBar(self.menubar)
        self.actionNouveau = QtWidgets.QAction(Accueil)
        self.actionNouveau.setObjectName("actionNouveau")

        ############# Action du menu Nouveau ####################
        self.actionNouveau.triggered.connect(self.afficherSaisie)
        #########################################################

        self.actionQuitter = QtWidgets.QAction(Accueil)
        self.actionQuitter.setObjectName("actionQuitter")

        ############# Action du menu Quitter ####################
        self.actionQuitter.triggered.connect(self.quitterApplication)
        #########################################################

        self.actionManuel_d_utilisation = QtWidgets.QAction(Accueil)
        self.actionManuel_d_utilisation.setObjectName("actionManuel_d_utilisation")
        self.actionA_propos_de_G_oGraph = QtWidgets.QAction(Accueil)
        self.actionA_propos_de_G_oGraph.setObjectName("actionA_propos_de_G_oGraph")
        self.menuFichier.addAction(self.actionNouveau)
        self.menuFichier.addAction(self.actionQuitter)
        self.menuAide.addAction(self.actionManuel_d_utilisation)
        self.menuAide.addAction(self.actionA_propos_de_G_oGraph)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(Accueil)
        QtCore.QMetaObject.connectSlotsByName(Accueil)

        #################### cacher les widgets au lancement ############################
        self.cacherElts()
        #################################################################################

    def retranslateUi(self, Accueil):
        _translate = QtCore.QCoreApplication.translate
        Accueil.setWindowTitle(_translate("Accueil", "GéoGraph"))
        self.btn_convertir.setText(_translate("Accueil", "Convertir les données"))
        self.btn_calcul_equ.setText(_translate("Accueil", "Calculer l\'équidistance"))
        self.btn_courbe.setText(_translate("Accueil", "Courbe géologique"))
        self.btn_profil.setText(_translate("Accueil", "Profile topographique"))
        self.label_val_equi.setText(_translate("Accueil", "Valeur de l\'équidistance :"))
        self.label_val_echelle.setText(_translate("Accueil", "Valeur de l\'échelle :"))
        self.btn_calcul_echelle.setText(_translate("Accueil", "Calculer l\'échelle"))
        self.btn_ann_quit.setText(_translate("Accueil", "Tout annuler"))
        self.label_saisie_donnee.setText(_translate("Accueil", " Saisie et traitement des donées de calcul"))
        self.label_long_papier.setText(_translate("Accueil", "<html><head/><body><p>longueur (<span style=\" font-size:10pt; font-weight:600;\"> l </span>) sur papier</p></body></html>"))
        self.label_long_cm.setText(_translate("Accueil", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">cm</span></p></body></html>"))
        self.label_Long_km.setText(_translate("Accueil", "<html><head/><body><p><span style=\" font-weight:600;\">km</span></p></body></html>"))
        self.label_Long_papier.setText(_translate("Accueil", "<html><head/><body><p>Longueur (<span style=\" font-size:10pt; font-weight:600;\"> L </span>) sur papier</p></body></html>"))
        self.label_val_cm.setText(_translate("Accueil", "<html><head/><body><p><span style=\" font-weight:600;\">cm</span></p></body></html>"))
        self.label_val_fascicule.setText(_translate("Accueil", "<html><head/><body><p>valeur(<span style=\" font-size:10pt; font-weight:600;\"> Val </span>) du fascicule</p></body></html>"))
        self.menuFichier.setTitle(_translate("Accueil", "Fichier"))
        self.menuAide.setTitle(_translate("Accueil", "Aide ?"))
        self.actionNouveau.setText(_translate("Accueil", "Nouveau"))
        self.actionNouveau.setShortcut(_translate("Accueil", "Ctrl+N"))
        self.actionQuitter.setText(_translate("Accueil", "Quitter"))
        self.actionQuitter.setShortcut(_translate("Accueil", "Ctrl+Q"))
        self.actionManuel_d_utilisation.setText(_translate("Accueil", "Manuel d\'utilisation"))
        self.actionManuel_d_utilisation.setShortcut(_translate("Accueil", "Ctrl+U"))
        self.actionA_propos_de_G_oGraph.setText(_translate("Accueil", "A propos de GéoGraph"))
        self.actionA_propos_de_G_oGraph.setShortcut(_translate("Accueil", "Ctrl+A"))

#import test_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Accueil = QtWidgets.QMainWindow()
    ui = Ui_Accueil()
    ui.setupUi(Accueil)
    Accueil.show()
    sys.exit(app.exec_())

