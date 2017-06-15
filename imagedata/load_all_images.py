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
mat02.addSpectrumValue(0.0,color(0.0,0.0,0.0,1.0))
mat02.addSpectrumValue(1.0,color(1.0,1.0,1.0,1.0))

##CO obj sax_slice <class 'eidolon.ImageObject.ImageSceneObject'>
obj = MetaImg.loadObject(scriptdir+'HEALTHY/sax_slice.mhd','sax_slice')
mgr.addSceneObject(obj)

##CO obj01 tags_slice <class 'eidolon.ImageObject.ImageSceneObject'>
obj01 = MetaImg.loadObject(scriptdir+'HEALTHY/tags_slice1.mhd','tags_slice')
mgr.addSceneObject(obj01)

##CO obj02 4dflow_mag_slice <class 'eidolon.ImageObject.ImageSceneObject'>
obj02 = MetaImg.loadObject(scriptdir+'HEALTHY/4dflow_mag_slice.mhd','4dflow_mag_slice')
mgr.addSceneObject(obj02)

##CO obj03 4dflow_phase_slice <class 'eidolon.ImageObject.ImageSceneObject'>
obj03 = MetaImg.loadObject(scriptdir+'HEALTHY/4dflow_phase_slice.mhd','4dflow_phase_slice')
mgr.addSceneObject(obj03)

##CO obj04 sax_slice_01 <class 'eidolon.ImageObject.ImageSceneObject'>
obj04 = MetaImg.loadObject(scriptdir+'DCM/sax_slice.mhd','sax_slice_01')
mgr.addSceneObject(obj04)

##CO obj05 tags_slice1 <class 'eidolon.ImageObject.ImageSceneObject'>
obj05 = MetaImg.loadObject(scriptdir+'DCM/tags_slice1.mhd','tags_slice1')
mgr.addSceneObject(obj05)

##CO obj06 4dflow_phase_slice_01 <class 'eidolon.ImageObject.ImageSceneObject'>
obj06 = MetaImg.loadObject(scriptdir+'DCM/4dflow_phase_slice.mhd','4dflow_phase_slice_01')
mgr.addSceneObject(obj06)

##CO obj07 4dflow_mag_slice_01 <class 'eidolon.ImageObject.ImageSceneObject'>
obj07 = MetaImg.loadObject(scriptdir+'DCM/4dflow_mag_slice.mhd','4dflow_mag_slice_01')
mgr.addSceneObject(obj07)

##CO obj08 sax_slice_02 <class 'eidolon.ImageObject.ImageSceneObject'>
obj08 = MetaImg.loadObject(scriptdir+'ATHLETE/sax_slice.mhd','sax_slice_02')
mgr.addSceneObject(obj08)

##CO obj09 tags_slice1_01 <class 'eidolon.ImageObject.ImageSceneObject'>
obj09 = MetaImg.loadObject(scriptdir+'ATHLETE/tags_slice1.mhd','tags_slice1_01')
mgr.addSceneObject(obj09)

##CO obj10 4dflow_mag_slice_02 <class 'eidolon.ImageObject.ImageSceneObject'>
obj10 = MetaImg.loadObject(scriptdir+'ATHLETE/4dflow_mag_slice.mhd','4dflow_mag_slice_02')
mgr.addSceneObject(obj10)

##CO obj11 4dflow_phase_slice_02 <class 'eidolon.ImageObject.ImageSceneObject'>
obj11 = MetaImg.loadObject(scriptdir+'ATHLETE/4dflow_phase_slice.mhd','4dflow_phase_slice_02')
mgr.addSceneObject(obj11)

##CO obj12 sax_slice_03 <class 'eidolon.ImageObject.ImageSceneObject'>
obj12 = MetaImg.loadObject(scriptdir+'FONTAN/sax_slice.mhd','sax_slice_03')
mgr.addSceneObject(obj12)

##CO obj13 tags_slice1_02 <class 'eidolon.ImageObject.ImageSceneObject'>
obj13 = MetaImg.loadObject(scriptdir+'FONTAN/tags_slice1.mhd','tags_slice1_02')
mgr.addSceneObject(obj13)

##CO obj14 sax_slice_04 <class 'eidolon.ImageObject.ImageSceneObject'>
obj14 = MetaImg.loadObject(scriptdir+'HCM/sax_slice.mhd','sax_slice_04')
mgr.addSceneObject(obj14)

##SO obj sax_slice <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj01 tags_slice <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj02 4dflow_mag_slice <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj03 4dflow_phase_slice <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj04 sax_slice_01 <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj05 tags_slice1 <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj06 4dflow_phase_slice_01 <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj07 4dflow_mag_slice_01 <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj08 sax_slice_02 <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj09 tags_slice1_01 <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj10 4dflow_mag_slice_02 <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj11 4dflow_phase_slice_02 <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj12 sax_slice_03 <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj13 tags_slice1_02 <class 'eidolon.ImageObject.ImageSceneObject'>


##SO obj14 sax_slice_04 <class 'eidolon.ImageObject.ImageSceneObject'>


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

##CR rep04 Timed Image Stack 04 <sax_slice_01> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep04=obj04.createRepr(ReprType._imgtimestack,imgmat=mat)
mgr.addSceneObjectRepr(rep04)

##CR rep05 Timed Image Stack 05 <tags_slice1> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep05=obj05.createRepr(ReprType._imgtimestack,imgmat=mat)
mgr.addSceneObjectRepr(rep05)

##CR rep06 Timed Image Stack 06 <4dflow_phase_slice_01> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep06=obj06.createRepr(ReprType._imgtimestack,imgmat=mat01)
mgr.addSceneObjectRepr(rep06)

##CR rep07 Timed Image Stack 07 <4dflow_mag_slice_01> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep07=obj07.createRepr(ReprType._imgtimestack,imgmat=mat01)
mgr.addSceneObjectRepr(rep07)

##CR rep08 Timed Image Stack 08 <sax_slice_02> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep08=obj08.createRepr(ReprType._imgtimestack,imgmat=mat)
mgr.addSceneObjectRepr(rep08)

##CR rep09 Timed Image Stack 09 <tags_slice1_01> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep09=obj09.createRepr(ReprType._imgtimestack,imgmat=mat)
mgr.addSceneObjectRepr(rep09)

##CR rep10 Timed Image Stack 10 <4dflow_mag_slice_02> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep10=obj10.createRepr(ReprType._imgtimestack,imgmat=mat01)
mgr.addSceneObjectRepr(rep10)

##CR rep11 Timed Image Stack 11 <4dflow_phase_slice_02> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep11=obj11.createRepr(ReprType._imgtimestack,imgmat=mat01)
mgr.addSceneObjectRepr(rep11)

##CR rep12 Timed Image Stack 12 <sax_slice_03> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep12=obj12.createRepr(ReprType._imgtimestack,imgmat=mat)
mgr.addSceneObjectRepr(rep12)

##CR rep13 Timed Image Stack 13 <tags_slice1_02> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep13=obj13.createRepr(ReprType._imgtimestack,imgmat=mat)
mgr.addSceneObjectRepr(rep13)

##CR rep14 Timed Image Stack 14 <sax_slice_04> <class 'eidolon.ImageObject.ImageSeriesRepr'>
rep14=obj14.createRepr(ReprType._imgtimestack,imgmat=mat)
mgr.addSceneObjectRepr(rep14)

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
mgr.setReprProps(rep03,trans=transform(980.0,3.690706,1961.7812,-1.0,1.0,-1.0,0.0,0.0,0.0,False),parent=None)

##SR rep04 Timed Image Stack 04 <sax_slice_01> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep04,False)
mgr.showHandle(rep04,False)
mgr.setReprProps(rep04,trans=transform(-608.0,95.0,593.0,-1.0,1.0,1.0,0.0,0.0,1.570795,False),parent=None)

##SR rep05 Timed Image Stack 05 <tags_slice1> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep05,False)
mgr.showHandle(rep05,False)
mgr.setReprProps(rep05,trans=transform(-764.0,96.0,574.0,-1.0,1.0,1.0,0.0,0.0,1.570795,False),parent=None)

##SR rep06 Timed Image Stack 06 <4dflow_phase_slice_01> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep06,False)
mgr.showHandle(rep06,False)
mgr.setReprProps(rep06,trans=transform(395.0,75.800167,1038.0,-1.0,1.0,-1.0,0.0,0.0,0.0,False),parent=None)

##SR rep07 Timed Image Stack 07 <4dflow_mag_slice_01> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep07,False)
mgr.showHandle(rep07,False)
mgr.setReprProps(rep07,trans=transform(113.809857,75.748728,1037.0,-1.0,1.0,-1.0,0.0,0.0,0.0,False),parent=None)

##SR rep08 Timed Image Stack 08 <sax_slice_02> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep08,False)
mgr.showHandle(rep08,False)
mgr.setReprProps(rep08,trans=transform(-295.0,32.0,884.0,-1.0,1.0,1.0,0.0,0.0,0.0,False),parent=None)

##SR rep09 Timed Image Stack 09 <tags_slice1_01> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep09,False)
mgr.showHandle(rep09,False)
mgr.setReprProps(rep09,trans=transform(-437.0,32.0,890.0,-1.0,1.0,1.0,0.0,0.0,0.0,False),parent=None)

##SR rep10 Timed Image Stack 10 <4dflow_mag_slice_02> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep10,False)
mgr.showHandle(rep10,False)
mgr.setReprProps(rep10,trans=transform(125.0,-7.0,985.0,-1.0,1.0,-1.0,0.0,0.0,0.0,False),parent=None)

##SR rep11 Timed Image Stack 11 <4dflow_phase_slice_02> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep11,False)
mgr.showHandle(rep11,False)
mgr.setReprProps(rep11,trans=transform(423.0,-7.0,985.0,-1.0,1.0,-1.0,0.0,0.0,0.0,False),parent=None)

##SR rep12 Timed Image Stack 12 <sax_slice_03> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep12,False)
mgr.showHandle(rep12,False)
mgr.setReprProps(rep12,trans=transform(-538.0,44.0,537.0,1.0,1.0,1.0,0.0,0.0,0.0,False),parent=None)

##SR rep13 Timed Image Stack 13 <tags_slice1_02> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep13,False)
mgr.showHandle(rep13,False)
mgr.setReprProps(rep13,trans=transform(-685.0,44.0,554.0,1.0,1.0,1.0,0.0,0.0,0.0,False),parent=None)

##SR rep14 Timed Image Stack 14 <sax_slice_04> <class 'eidolon.ImageObject.ImageSeriesRepr'>
mgr.showBoundBox(rep14,False)
mgr.showHandle(rep14,False)
mgr.setReprProps(rep14,trans=transform(-524.0,99.0,601.0,-1.0,1.0,1.0,0.0,0.0,1.57079,False),parent=None)

## Scene Setup
mgr.setSingleFreeCamera()
mgr.setCameraOrtho(False)
mgr.setBackgroundColor(color(0.0,0.0,0.0,1.0))
mgr.setAmbientLight(color(0.5,0.5,0.5,1.0))
mgr.setTimeFPS(25)
mgr.setTimeStepsPerSec(500)

mgr.setCameraSeeAll()
