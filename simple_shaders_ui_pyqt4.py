# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_shaders.ui'
#
# Created: Mon Sep 30 12:24:20 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SimpleShadersDlg(object):
    def setupUi(self, SimpleShadersDlg):
        SimpleShadersDlg.setObjectName(_fromUtf8("SimpleShadersDlg"))
        SimpleShadersDlg.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/cmiss_icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SimpleShadersDlg.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(SimpleShadersDlg)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(SimpleShadersDlg)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self._sceneviewerwidget = SceneviewerWidget(SimpleShadersDlg)
        self._sceneviewerwidget.setObjectName(_fromUtf8("_zincwidget"))
        self.gridLayout.addWidget(self._sceneviewerwidget, 0, 0, 1, 2)

        self.retranslateUi(SimpleShadersDlg)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), SimpleShadersDlg.close)
        QtCore.QMetaObject.connectSlotsByName(SimpleShadersDlg)

    def retranslateUi(self, SimpleShadersDlg):
        SimpleShadersDlg.setWindowTitle(_translate("SimpleShadersDlg", "Simple Shaders", None))
        self.pushButton.setText(_translate("SimpleShadersDlg", "&Quit", None))

from sceneviewerwidget import SceneviewerWidget
import icons_rc
