#!/usr/bin/python
"""
PyZinc examples

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

import sys
try:
    from PySide import QtGui, QtCore
    from simple_shaders_ui_pyside import Ui_SimpleShadersDlg
except ImportError:
    from PyQt4 import QtGui, QtCore
    from simple_shaders_ui_pyqt4 import Ui_SimpleShadersDlg

# opencmiss.zinc.imports start
from opencmiss.zinc.context import Context as ZincContext
from opencmiss.zinc.glyph import Glyph
import time
# opencmiss.zinc.imports end

# SimpleShadersDlg start
class SimpleShadersDlg(QtGui.QWidget):
    '''
    Create a subclass of QWidget for our application.  We could also have derived this 
    application from QMainWindow to give us a menu bar among other things, but a
    QWidget is sufficient for our purposes.
    '''
    
    def __init__(self, parent=None):
        '''
        Initiaise the SimpleShadersDlg first calling the QWidget __init__ function.
        '''
        QtGui.QWidget.__init__(self, parent)
 
        # create instance of Zinc Context from which all other objects are obtained
        self._context = ZincContext("Simple Shaders")
        self._defaultRegion = self._context.getDefaultRegion()
        self._shaderuniforms = None
        logger = self._context.getLogger()
        # set up standard materials and glyphs so we can use them elsewhere
        # define standard materials first as some coloured glyphs use them
        materialmodule = self._context.getMaterialmodule()
        materialmodule.defineStandardMaterials()
        # this example uses a standard axes glyph hence need the following:
        glyphmodule = self._context.getGlyphmodule()
        glyphmodule.defineStandardGlyphs()

        # Using composition to include the visual element of the GUI.
        self.ui = Ui_SimpleShadersDlg()
        self.ui.setupUi(self)
        # Must pass the context to the ZincWidget to set it up
        self.ui._sceneviewerwidget.setContext(self._context)
        self.setWindowIcon(QtGui.QIcon(":/cmiss_icon.ico"))
        self.resize(620, 440)
        self._start = time.time()
        self._material = None
        # set up content for this application
        self.readMesh()
        #display the mesh
        self.drawSurfaces()
        self.updateUniforms()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateUniforms)
        self.timer.start(1000/60)        
        number = logger.getNumberOfMessages()
        for i in range(number):
            print(logger.getMessageTextAtIndex(i))
            
    def updateUniforms(self):
        elapsed = time.time() - self._start
        self._shaderuniforms.setUniformDouble("time", [elapsed])
        
    def readMesh(self):
    	self._defaultRegion.readFile("models/cheese.exnode")
    	self._defaultRegion.readFile("models/cheese.exelem")
    	
    def setShader(self, material):
        vs = open("shader.vs","r") 
        fs = open("shader.fs", "r")
        shadermodule = self._context.getShadermodule()
        shaderprogram = shadermodule.createShaderprogram()
        shaderprogram.setVertexString(vs.read())
        shaderprogram.setFragmentString(fs.read())
        vs.close()
        fs.close()
        self._shaderuniforms = shadermodule.createShaderuniforms()
        self._shaderuniforms.addUniformDouble("time", [0.0])
        self._shaderuniforms.addUniformInteger("shadingMode", [0])
        self.updateUniforms()
        material.setShaderuniforms(self._shaderuniforms)
        material.setShaderprogram(shaderprogram)
        
    # SimpleShadersDlg.setupAxes start
    def drawSurfaces(self):
        region = self._defaultRegion
        # Graphics for visualising a region belong to its scen
        scene = region.getScene()
        
        fieldmodule = region.getFieldmodule()
        imageField = fieldmodule.createFieldImage()
        imageField.readFile("models/background.jpg")
        imageField.setTextureCoordinateSizes([1.0, 1.0, 1.0])
        imageField.setWrapMode(imageField.WRAP_MODE_MIRROR_REPEAT)
        coordinates = fieldmodule.findFieldByName("coordinates")
        xi = fieldmodule.findFieldByName("xi")
        # Call beginChange() to stop scene change messages being sent while
        # making multiple changes to scene or its graphics.
        # It's very important to call endChange() at the end!
        scene.beginChange()
        
        # Create Points graphics in scene and visualise with unit-sized solid 3-D axes
        surface = scene.createGraphicsSurfaces()
        surface.setCoordinateField(coordinates)
        surface.setTextureCoordinateField(coordinates)
        material = surface.getMaterial()
        material.setTextureField(1, imageField)

        self._material = material
        self.setShader(material)
       	
        # Restart scene messaging and inform clients of changes.
        # This ultimately triggers a redraw in the Zinc Widget.
        scene.endChange()
        # SimpleShadersDlg.setupAxes end
        #self.ui._sceneviewerwidget._scene_viewer.viewAll()

# main start
def main(argv):
    '''
    The entry point for the application, handle application arguments and initialise the 
    GUI.
    '''
    
    app = QtGui.QApplication(argv)

    w = SimpleShadersDlg()
    w.show()
    sys.exit(app.exec_())
# main end

if __name__ == '__main__':
    main(sys.argv)
