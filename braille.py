#Author-Benjamin Braun
#Description- braille fusion360 Python 

import adsk.core, adsk.fusion, adsk.cam, traceback, math, string
app = adsk.core.Application.get()
ui  = app.userInterface
design = app.activeProduct
rootComp = design.rootComponent
revolves = rootComp.features.revolveFeatures
combine = rootComp.features.combineFeatures
sketches = rootComp.sketches;
extrudes = rootComp.features.extrudeFeatures
xyPlane = rootComp.xYConstructionPlane;
xzPlane = rootComp.xZConstructionPlane;


def vonal(n,ca):
    xy = sketches.add(xyPlane)
    korxy = xy.sketchCurves.sketchCircles
    vonalxy = xy.sketchCurves.sketchLines
    pozx=n*6+3
    pozx2=n*6+5.3
    pozz=3
    pozz2=3+2.3
    pozz3=3+4.6
    alap=0
    alap2=2
    mag=2.9
    #b1/l1
    egy1=vonalxy.addByTwoPoints(adsk.core.Point3D.create(pozx, alap , -pozz3), adsk.core.Point3D.create(pozx, mag, -pozz3))
    korxy.addByCenterRadius(adsk.core.Point3D.create(pozx, alap2 , -pozz3), 0.9)
    #b2/l2
    egy2=vonalxy.addByTwoPoints(adsk.core.Point3D.create(pozx, alap , -pozz2), adsk.core.Point3D.create(pozx, mag, -pozz2))
    korxy.addByCenterRadius(adsk.core.Point3D.create(pozx, alap2 , -pozz2), 0.9)
    #b3/l3
    egy3=vonalxy.addByTwoPoints(adsk.core.Point3D.create(pozx, alap , -pozz), adsk.core.Point3D.create(pozx, mag, -pozz))
    korxy.addByCenterRadius(adsk.core.Point3D.create(pozx, alap2 , -pozz), 0.9)
    #j1/r1
    keto1=vonalxy.addByTwoPoints(adsk.core.Point3D.create(pozx2, alap , -pozz3), adsk.core.Point3D.create(pozx2, mag, -pozz3))
    korxy.addByCenterRadius(adsk.core.Point3D.create(pozx2, alap2 , -pozz3), 0.9)
    #r2/j2
    keto2=vonalxy.addByTwoPoints(adsk.core.Point3D.create(pozx2, alap , -pozz2), adsk.core.Point3D.create(pozx2, mag, -pozz2))
    korxy.addByCenterRadius(adsk.core.Point3D.create(pozx2, alap2 , -pozz2), 0.9)   
    #j3/r3
    keto3=vonalxy.addByTwoPoints(adsk.core.Point3D.create(pozx2, alap , -pozz), adsk.core.Point3D.create(pozx2, mag, -pozz))
    korxy.addByCenterRadius(adsk.core.Point3D.create(pozx2, alap2 , -pozz), 0.9)
    if ca == 'a':
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)  

    elif ca == 'b':
        profa = xy.profiles.item(0)
        revInput = revolves.createInput(profa, egy2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
            
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
    elif ca == 'c':
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        
        profa = xy.profiles.item(6)
        revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'd':
        
        profa = xy.profiles.item(2)
        revInput = revolves.createInput(profa, keto2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
       
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)

        profa = xy.profiles.item(6)
        revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'e':
       
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)

        profa = xy.profiles.item(2)
        revInput = revolves.createInput(profa, keto2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'f':
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)

        profa = xy.profiles.item(0)
        revInput = revolves.createInput(profa, egy2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)

        profa = xy.profiles.item(6)
        revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'g':
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)

        profa = xy.profiles.item(0)
        revInput = revolves.createInput(profa, egy2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)

        profa = xy.profiles.item(2)
        revInput = revolves.createInput(profa, keto2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)

        profa = xy.profiles.item(6)
        revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'h':

        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)

        profa = xy.profiles.item(0)
        revInput = revolves.createInput(profa, egy2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)

        profa = xy.profiles.item(2)
        revInput = revolves.createInput(profa, keto2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'i':
        profa = xy.profiles.item(0)
        revInput = revolves.createInput(profa, egy2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)

        profa = xy.profiles.item(6)
        revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'j':
        profa = xy.profiles.item(0)
        revInput = revolves.createInput(profa, egy2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(2)
        revInput = revolves.createInput(profa, keto2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(6)
        revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'k':
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        #hiper hiper
        profa = xy.profiles.item(10)
        revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'l':
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(0)
        revInput = revolves.createInput(profa, egy2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(10)
        revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'm':
        #mitesznek a méhekek?
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    
        profa = xy.profiles.item(10)
        revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(6)
        revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'n':
        
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(10)
        revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(2)
        revInput = revolves.createInput(profa, keto2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(6)
        revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'o':
        
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(10)
        revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(2)
        revInput = revolves.createInput(profa, keto2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    
    elif ca == 'p':
        
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(0)
        revInput = revolves.createInput(profa, egy2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(10)
        revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(6)
        revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    
    elif ca == 'q':
        
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(0)
        revInput = revolves.createInput(profa, egy2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(10)
        revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
       
        profa = xy.profiles.item(2)
        revInput = revolves.createInput(profa, keto2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(6)
        revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'r':
       
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
       
        profa = xy.profiles.item(0)
        revInput = revolves.createInput(profa, egy2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(10)
        revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(2)
        revInput = revolves.createInput(profa, keto2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 's':
       
        profa = xy.profiles.item(0)
        revInput = revolves.createInput(profa, egy2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(6)
        revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(10)
        revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 't':
        
        profa = xy.profiles.item(0)
        revInput = revolves.createInput(profa, egy2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(10)
        revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(2)
        revInput = revolves.createInput(profa, keto2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(6)
        revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'u':
       
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        #kár hogy a csigának nincs haja
        profa = xy.profiles.item(8)
        revInput = revolves.createInput(profa, keto3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(10)
        revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'v':
        
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(0)
        revInput = revolves.createInput(profa, egy2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(8)
        revInput = revolves.createInput(profa, keto3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(10)
        revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'w':
        
        profa = xy.profiles.item(0)
        revInput = revolves.createInput(profa, egy2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(8)
        revInput = revolves.createInput(profa, keto3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(2)
        revInput = revolves.createInput(profa, keto2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(6)
        revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'x':
        
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(8)
        revInput = revolves.createInput(profa, keto3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(10)
        revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(6)
        revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'y':
        
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(8)
        revInput = revolves.createInput(profa, keto3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(10)
        revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(2)
        revInput = revolves.createInput(profa, keto2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(6)
        revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
    elif ca == 'z':
        profa = xy.profiles.item(4)
        revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(8)
        revInput = revolves.createInput(profa, keto3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(10)
        revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
        profa = xy.profiles.item(2)
        revInput = revolves.createInput(profa, keto2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(math.pi+180)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)
        
def run(context):
    
    try:
        
        doboz = ui.inputBox('braille','szöveg','i stand with ceu')
        szoveg= doboz [0]
        x=len(szoveg)
        ho=6*x+3
        ma=10.6
        al=rootComp.bRepBodies.count
        #lap
        xz = sketches.add(xzPlane)
        vonalxz = xz.sketchCurves.sketchLines
        vonalxz.addByTwoPoints(adsk.core.Point3D.create(0, 0 , 0), adsk.core.Point3D.create(ho,  0, 0))
        vonalxz.addByTwoPoints(adsk.core.Point3D.create(ho, 0 , 0), adsk.core.Point3D.create(ho,  ma, 0))
        vonalxz.addByTwoPoints(adsk.core.Point3D.create(0, 0 , 0), adsk.core.Point3D.create(0,  ma, 0))
        vonalxz.addByTwoPoints(adsk.core.Point3D.create(0, ma , 0), adsk.core.Point3D.create(ho,  ma, 0))
        profk = xz.profiles.item(0)
        distance = adsk.core.ValueInput.createByReal(2)
        extrudes.addSimple(profk, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        #kis szines pöttyök
        
        for n in range(0,x):
             
            betu= szoveg [n]
            # Köszi Máté!
            abc = string.ascii_lowercase[:32]
            if betu in abc:
                 vonal(n,betu)
                
        mind= adsk.core.ObjectCollection.create() 
        ig=rootComp.bRepBodies.count
        target=rootComp.bRepBodies.item(al)
        
        for neveletlengorilla in range(al+1,ig):
            macko=rootComp.bRepBodies.item(neveletlengorilla)
            mind.add(macko)
            
        join1 = combine.createInput(target , mind)
        combine.add(join1) 
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

