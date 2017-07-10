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
def abc (kord):
    daka=len(kord) 
        for zoty in range(0,daka):        
            hupli = kord[zoty]
            if hupli == 1:
                profa = xy.profiles.item(4)
                revInput = revolves.createInput(profa, egy1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            elif hupli == 2:
                profa = xy.profiles.item(0)
                revInput = revolves.createInput(profa, egy2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            elif hupli == 3:
                profa = xy.profiles.item(10)
                revInput = revolves.createInput(profa, egy3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            elif hupli == 4:
                profa = xy.profiles.item(6)
                revInput = revolves.createInput(profa, keto1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            elif hupli == 5:
                profa = xy.profiles.item(2)
                revInput = revolves.createInput(profa, keto2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            elif hupli == 6:
                profa = xy.profiles.item(8)
                revInput = revolves.createInput(profa, keto3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            angle = adsk.core.ValueInput.createByReal(math.pi+180)
            revInput.setAngleExtent(False, angle)
            revolves.add(revInput)
    if ca == 'a':
        kord=[1]
        abc (kord)

    elif ca == 'b':
        kord=[1,2]
        abc (kord)     
    elif ca == 'c':
        kord=[1,4]
        abc (kord)
    elif ca == 'd':
        kord=[5,1,4]
        abc (kord)
    elif ca == 'e':
        kord=[1,5]
        abc (kord)
    elif ca == 'f':
        kord=[1,2,4]
        abc (kord)
    elif ca == 'g':
        kord=[1,2,4,5,]
        abc (kord)
    elif ca == 'h':
        kord=[1,2,4]
        abc (kord)
    elif ca == 'i':
        kord=[2,4]
        abc (kord)
    elif ca == 'j':
        kord=[2,4,5]
        abc (kord)
    elif ca == 'k':
        kord=[1,3]
        #hiper hiper
        abc (kord)
    elif ca == 'l':
        kord=[1,2,3]
        abc (kord)
    elif ca == 'm':
        #mitesznek a méhekek?
        kord=[1,3,4]
        abc (kord)
    elif ca == 'n':
        kord=[1,3,5,4]
        abc (kord)
    elif ca == 'o':
        kord=[1,3,5]
        abc (kord)
    elif ca == 'p':
        kord=[1,2,3,4]
        abc (kord)
    elif ca == 'q':
        kord=[1,2,3,4,5]
        abc (kord)
    elif ca == 'r':
        kord=[1,2,3,5]
        abc (kord)
    elif ca == 's':
        kord=[2,3,4]
        abc (kord)
    elif ca == 't':
        kord=[2,3,4,5]
        abc (kord)
    elif ca == 'u':
        kord=[1,3,6]
        abc (kord)
    elif ca == 'v':
        kord=[1,2,3,6]
        abc (kord)
    elif ca == 'w':
        kord=[2,6,5,4]
        abc (kord)
    elif ca == 'x':
        kord=[1,6,3,4]
        abc (kord)
    elif ca == 'y':
        kord=[1,6,3,5,4]
        abc (kord)
    elif ca == 'z':
        kord=[1,6,3,5]
        abc (kord)  
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
