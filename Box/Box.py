#Author-copypastestd
#Description-Test box

import adsk.core, adsk.fusion, adsk.cam, traceback

app = adsk.core.Application.get()
ui  = app.userInterface
design = app.activeProduct
unitsMgr = design.unitsManager

# unit - cm
t = 0.3
h = 5
l = 15
w = 10

def createNewComponent():
    # Get the active design.
    product = app.activeProduct
    design = adsk.fusion.Design.cast(product)
    rootComp = design.rootComponent
    allOccs = rootComp.occurrences
    newOcc = allOccs.addNewComponent(adsk.core.Matrix3D.create())
    return newOcc.component

def createBottom(test):
    ui.messageBox(test)
    bottom = createNewComponent()
    bottom.name = "Bottom"
        
    sketches = bottom.sketches
    xzPlane = bottom.xZConstructionPlane
    sketch1 = sketches.add(xzPlane)
    sketch1.name = "Bottom"
        
    lines = sketch1.sketchCurves.sketchLines;
    rectangle = lines.addCenterPointRectangle(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(l/2, w/2, 0))
        
    extrudes = bottom.features.extrudeFeatures
    prof = sketch1.profiles[0]
    bottomExtrudeInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        
    distanceBottomExtrude = adsk.core.ValueInput.createByReal(t)
    bottomExtrudeInput.setDistanceExtent(False, distanceBottomExtrude)
    bottomExtrude = extrudes.add(bottomExtrudeInput)
    bottomExtrude.name = "Bottom"
    
    bottomBody = bottom.bRepBodies.item(bottom.bRepBodies.count-1)
    bottomBody.name = "Bottom"  

def createFront():  
    front = createNewComponent()
    front.name = "Front"
        
    sketches = front.sketches
    xzPlane = front.xZConstructionPlane
    sketch1 = sketches.add(xzPlane)
    sketch1.name = "Front"

    lines = sketch1.sketchCurves.sketchLines;
    rectangle = lines.addTwoPointRectangle(adsk.core.Point3D.create(-l/2, -w/2, 0), adsk.core.Point3D.create(l/2, -w/2+t, 0))         
        
    extrudes = front.features.extrudeFeatures
    prof = sketch1.profiles[0]
    frontExtrudeInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        
    distanceFrontExtrude = adsk.core.ValueInput.createByReal(h)
    frontExtrudeInput.setDistanceExtent(False, distanceFrontExtrude)
    frontExtrude = extrudes.add(frontExtrudeInput)
    frontExtrude.name = "Front"
    
    frontBody = front.bRepBodies.item(front.bRepBodies.count-1)
    frontBody.name = "Front"  

def createBack():
    back = createNewComponent()
    back.name = "Back"
        
    sketches = back.sketches
    xzPlane = back.xZConstructionPlane
    sketch1 = sketches.add(xzPlane)
    sketch1.name = "Back"

    lines = sketch1.sketchCurves.sketchLines;
    rectangle = lines.addTwoPointRectangle(adsk.core.Point3D.create(-l/2, w/2, 0), adsk.core.Point3D.create(l/2, w/2-t, 0))         
        
    extrudes = back.features.extrudeFeatures
    prof = sketch1.profiles[0]
    backExtrudeInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        
    distanceBackExtrude = adsk.core.ValueInput.createByReal(h)
    backExtrudeInput.setDistanceExtent(False, distanceBackExtrude)
    backExtrude = extrudes.add(backExtrudeInput)
    backExtrude.name = "Back"
    
    backBody = back.bRepBodies.item(back.bRepBodies.count-1)
    backBody.name = "Back"  
    
def createRight():
    right = createNewComponent()
    right.name = "Right"
        
    sketches = right.sketches
    xzPlane = right.xZConstructionPlane
    sketch1 = sketches.add(xzPlane)
    sketch1.name = "Right"

    lines = sketch1.sketchCurves.sketchLines;
    rectangle = lines.addTwoPointRectangle(adsk.core.Point3D.create(l/2, w/2, 0), adsk.core.Point3D.create(l/2-t, -w/2, 0))         
        
    extrudes = right.features.extrudeFeatures
    prof = sketch1.profiles[0]
    rightExtrudeInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        
    distanceRightExtrude = adsk.core.ValueInput.createByReal(h)
    rightExtrudeInput.setDistanceExtent(False, distanceRightExtrude)
    rightExtrude = extrudes.add(rightExtrudeInput)
    rightExtrude.name = "Right"
    
    rightBody = right.bRepBodies.item(right.bRepBodies.count-1)
    rightBody.name = "Right"  

def createLeft():
    left = createNewComponent()
    left.name = "Left"
        
    sketches = left.sketches
    xzPlane = left.xZConstructionPlane
    sketch1 = sketches.add(xzPlane)
    sketch1.name = "Left"

    lines = sketch1.sketchCurves.sketchLines;
    rectangle = lines.addTwoPointRectangle(adsk.core.Point3D.create(-l/2, w/2, 0), adsk.core.Point3D.create(-l/2+t, -w/2, 0))         
        
    extrudes = left.features.extrudeFeatures
    prof = sketch1.profiles[0]
    leftExtrudeInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        
    distanceLeftExtrude = adsk.core.ValueInput.createByReal(h)
    leftExtrudeInput.setDistanceExtent(False, distanceLeftExtrude)
    leftExtrude = extrudes.add(leftExtrudeInput)
    leftExtrude.name = "Left"  

    leftBody = left.bRepBodies.item(left.bRepBodies.count-1)
    leftBody.name = "Left"     

def createTop():
    top = createNewComponent()
    top.name = "Top"
        
    sketches = top.sketches
    xzPlane = top.xZConstructionPlane
    sketch1 = sketches.add(xzPlane)
    sketch1.name = "Top"
        
    lines = sketch1.sketchCurves.sketchLines;
    rectangle = lines.addCenterPointRectangle(adsk.core.Point3D.create(0, 0, h-t), adsk.core.Point3D.create(l/2, w/2, h-t))
        
    extrudes = top.features.extrudeFeatures
    prof = sketch1.profiles[0]
    topExtrudeInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        
    distanceTopExtrude = adsk.core.ValueInput.createByReal(t)
    topExtrudeInput.setDistanceExtent(False, distanceTopExtrude)
    topExtrude = extrudes.add(topExtrudeInput)
    topExtrude.name = "Top"
    
    topBody = top.bRepBodies.item(top.bRepBodies.count-1)
    topBody.name = "Top"
    

def run(context):
    ui = None
    try:
        
        #rootComp = adsk.fusion.Component.cast(design.rootComponent)
        createBottom("Test text")
        createFront()        
        createBack()
        createRight()
        createLeft()
        createTop()
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
