## Header
from eidolon import *

## Material Setup
mat=mgr.createMaterial("mat")
mat.setAmbient(color(1.0,1.0,1.0,1.0))
mat.setDiffuse(color(1.0,1.0,1.0,1.0))
mat.setSpecular(color(0.0,0.0,0.0,1.0))
mat.setEmissive(color(0.0,0.0,0.0,1.0))
mat.setShininess(0.0)
mat.setPointSize(0.0,0.0)
mat.setPointSizeAbs(2.0)
mat.setPointAttenuation(False)
mat.useVertexColor(False)
mat.useDepthCheck(True)
mat.useDepthWrite(True)
mat.useTexFiltering(True)
mat.clampTexAddress(False)
mat.useFlatShading(False)
mat.useLighting(True)
mat.cullBackfaces(True)
mat.usePointSprites(False)
mat.setAlpha(1.0)
mat.useInternalAlpha(True)
mat.setGPUProgram('BaseImage',PT_FRAGMENT)
mat.addSpectrumValue(0.0,color(0.0,0.0,0.0,1.0))
mat.addSpectrumValue(1.0,color(1.0,1.0,1.0,1.0))

##CO obj sax_slice <class 'eidolon.ImageObject.ImageSceneObject'>
obj = MetaImg.loadObject(scriptdir+'sax_slice.mhd','sax_slice')
mgr.addSceneObject(obj)

##SO obj sax_slice <class 'eidolon.ImageObject.ImageSceneObject'>


##CR rep Timed Image Stack <sax_slice> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep=obj.createRepr(ReprType._imgtimestack,imgmat=mat)
mgr.addSceneObjectRepr(rep)

##SR rep Timed Image Stack <sax_slice> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep,False)
mgr.showHandle(rep,False)
mgr.setReprProps(rep,trans=transform(0.0,0.0,0.0,-1.0,1.0,1.0,0.0,0.0,1.57079,False),parent=None)

## Scene Setup
mgr.setSingleFreeCamera()
mgr.setCameraOrtho(False)
mgr.setBackgroundColor(color(0.0,0.0,0.0,1.0))
mgr.setAmbientLight(color(0.5,0.5,0.5,1.0))
mgr.setTimeFPS(25)
mgr.setTimeStepsPerSec(500)

mgr.setCameraSeeAll()
