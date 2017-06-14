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

mat01=mgr.createMaterial("mat01")
mat01.setAmbient(color(1.0,1.0,1.0,1.0))
mat01.setDiffuse(color(1.0,1.0,1.0,1.0))
mat01.setSpecular(color(0.0,0.0,0.0,1.0))
mat01.setEmissive(color(0.0,0.0,0.0,1.0))
mat01.setShininess(0.0)
mat01.setPointSize(0.0,0.0)
mat01.setPointSizeAbs(2.0)
mat01.setPointAttenuation(False)
mat01.useVertexColor(False)
mat01.useDepthCheck(True)
mat01.useDepthWrite(True)
mat01.useTexFiltering(True)
mat01.clampTexAddress(False)
mat01.useFlatShading(False)
mat01.useLighting(True)
mat01.cullBackfaces(True)
mat01.usePointSprites(False)
mat01.setAlpha(1.0)
mat01.useInternalAlpha(True)
mat01.setGPUProgram('BaseImage',PT_FRAGMENT)
mat01.addSpectrumValue(0.0,color(0.0,0.0,0.0,1.0))
mat01.addSpectrumValue(1.0,color(1.0,1.0,1.0,1.0))

mat02=mgr.createMaterial("mat02")
mat02.setAmbient(color(1.0,1.0,1.0,1.0))
mat02.setDiffuse(color(1.0,1.0,1.0,1.0))
mat02.setSpecular(color(0.0,0.0,0.0,1.0))
mat02.setEmissive(color(0.0,0.0,0.0,1.0))
mat02.setShininess(0.0)
mat02.setPointSize(0.0,0.0)
mat02.setPointSizeAbs(2.0)
mat02.setPointAttenuation(False)
mat02.useVertexColor(False)
mat02.useDepthCheck(True)
mat02.useDepthWrite(True)
mat02.useTexFiltering(True)
mat02.clampTexAddress(False)
mat02.useFlatShading(False)
mat02.useLighting(True)
mat02.cullBackfaces(True)
mat02.usePointSprites(False)
mat02.setAlpha(1.0)
mat02.useInternalAlpha(True)
mat02.setGPUProgram('BaseImage',PT_FRAGMENT)
mat02.addSpectrumValue(0.2,color(0.0,0.0,0.0,1.0))
mat02.addSpectrumValue(0.8,color(1.0,1.0,1.0,1.0))

##CO obj sax_slice <class 'eidolon.ImageObject.ImageSceneObject'>
obj = MetaImg.loadObject(scriptdir+'sax_slice.mhd','sax_slice')
mgr.addSceneObject(obj)

##CO obj01 tags_slice <class 'eidolon.ImageObject.ImageSceneObject'>
obj01 = MetaImg.loadObject(scriptdir+'tags_slice1.mhd','tags_slice')
mgr.addSceneObject(obj01)

##CO obj02 4dflow_mag_slice <class 'eidolon.ImageObject.ImageSceneObject'>
obj02 = MetaImg.loadObject(scriptdir+'4dflow_mag_slice.mhd','4dflow_mag_slice')
mgr.addSceneObject(obj02)

##CO obj03 4dflow_phase_slice <class 'eidolon.ImageObject.ImageSceneObject'>
obj03 = MetaImg.loadObject(scriptdir+'4dflow_phase_slice.mhd','4dflow_phase_slice')
mgr.addSceneObject(obj03)

##SO obj sax_slice <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj01 tags_slice <class 'eidolon.ImageObject.ImageSceneObject'>
#obj01.setTimestepList([32.869565,  64.608696,  96.347826,  128.086957,  159.826087,  191.565217,  223.304348,  255.043478,  286.782609,  318.521739,  350.260870,  382.000000,  413.739130,  445.478261,  477.217391,  508.956522,  540.695652,  572.434783,  604.173913,  635.913043,  667.652174,  699.391304,  731.130435,  762.869565])

##SO obj02 4dflow_mag_slice <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj03 4dflow_phase_slice <class 'eidolon.ImageObject.ImageSceneObject'>


##CR rep Timed Image Stack <sax_slice> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep=obj.createRepr(ReprType._imgtimestack,imgmat=mat)
mgr.addSceneObjectRepr(rep)

##CR rep01 Timed Image Stack 01 <tags_slice> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep01=obj01.createRepr(ReprType._imgtimestack,imgmat=mat)
mgr.addSceneObjectRepr(rep01)

##CR rep02 Timed Image Stack 02 <4dflow_mag_slice> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep02=obj02.createRepr(ReprType._imgtimestack,imgmat=mat01)
mgr.addSceneObjectRepr(rep02)

##CR rep03 Timed Image Stack 03 <4dflow_phase_slice> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep03=obj03.createRepr(ReprType._imgtimestack,imgmat=mat02)
mgr.addSceneObjectRepr(rep03)

##SR rep Timed Image Stack <sax_slice> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep,False)
mgr.showHandle(rep,False)
mgr.setReprProps(rep,trans=transform(-217.555986,0.0,200.16079,1.0,1.0,1.0,0.0,0.0,0.0,False),parent=None)

##SR rep01 Timed Image Stack 01 <tags_slice> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep01,False)
mgr.showHandle(rep01,False)
mgr.setReprProps(rep01,trans=transform(-232.481062,0.0,200.166145,1.0,1.0,1.0,0.0,0.0,0.0,False),parent=None)

##SR rep02 Timed Image Stack 02 <4dflow_mag_slice> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep02,False)
mgr.showHandle(rep02,False)
mgr.setReprProps(rep02,trans=transform(1020.764664,-0.183632,3730.137349,-1.0,1.0,-1.0,0.0,0.0,0.0,False),parent=None)

##SR rep03 Timed Image Stack 03 <4dflow_phase_slice> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep03,False)
mgr.showHandle(rep03,False)
mgr.setReprProps(rep03,trans=transform(980.0,-8.313213,1961.7812,-1.0,1.0,-1.0,0.0,0.0,0.0,False),parent=None)

## Scene Setup
mgr.setSingleFreeCamera()
mgr.setCameraOrtho(False)
mgr.setBackgroundColor(color(0.0,0.0,0.0,1.0))
mgr.setAmbientLight(color(0.5,0.5,0.5,1.0))
mgr.setTimeFPS(25)
mgr.setTimeStepsPerSec(500)

mgr.setCameraSeeAll()
