# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_shaders.ui'
#
# Created: Mon Sep 30 12:24:06 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SimpleShadersDlg(object):
    def setupUi(self, SimpleShadersDlg):
        SimpleShadersDlg.setObjectName("SimpleShadersDlg")
        SimpleShadersDlg.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cmiss_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SimpleShadersDlg.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(SimpleShadersDlg)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtGui.QPushButton(SimpleShadersDlg)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self._sceneviewerwidget = SceneviewerWidget(SimpleShadersDlg)
        self._sceneviewerwidget.setObjectName("_sceneviewerwidget")
        self.gridLayout.addWidget(self._sceneviewerwidget, 0, 0, 1, 2)

        self.retranslateUi(SimpleShadersDlg)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), SimpleShadersDlg.close)
        QtCore.QMetaObject.connectSlotsByName(SimpleShadersDlg)

    def retranslateUi(self, SimpleShadersDlg):
        SimpleShadersDlg.setWindowTitle(QtGui.QApplication.translate("SimpleShadersDlg", "Simple Shaders", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("SimpleShadersDlg", "&Quit", None, QtGui.QApplication.UnicodeUTF8))

from sceneviewerwidget import SceneviewerWidget
import icons_rc
