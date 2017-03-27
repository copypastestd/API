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


# Method createSide: Name, rectangle type, 1th point cords, 1th point cords, Extrusion distance
def createSide(_name, rectangle_type, point1_x, point1_y, point1_z, point2_x, point2_y, point2_z, ext):
    side = createNewComponent()
    # Rename component
    side.name = _name
    
    # Create sketch
    sketches = side.sketches
    xzPlane = side.xZConstructionPlane
    sketch1 = sketches.add(xzPlane)
    # Rename sketch
    sketch1.name = _name
        
    # Draw rectangle
    lines = sketch1.sketchCurves.sketchLines;
    if rectangle_type == "center":
        rectangle = lines.addCenterPointRectangle(adsk.core.Point3D.create(point1_x, point1_y, point1_z), adsk.core.Point3D.create(point2_x, point2_y, point2_z))
    if rectangle_type == "2point":
        rectangle = lines.addTwoPointRectangle(adsk.core.Point3D.create(point1_x, point1_y, point1_z), adsk.core.Point3D.create(point2_x, point2_y, point2_z))
    
    #Extrude feature
    extrudes = side.features.extrudeFeatures
    prof = sketch1.profiles[0]
    sideExtrudeInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    
    #Extrude params
    distanceSideExtrude = adsk.core.ValueInput.createByReal(ext)
    sideExtrudeInput.setDistanceExtent(False, distanceSideExtrude)
    sideExtrude = extrudes.add(sideExtrudeInput)
    #Rename feature
    sideExtrude.name = _name
    
    #Rename body
    sideBody = side.bRepBodies.item(side.bRepBodies.count-1)
    sideBody.name = _name     
    

def run(context):
    ui = None
    try:
        
        # Method createSide: Name, rectangle type, 1th point cords, 1th point cords, Extrusion distance
        createSide("Bottom", "center", 0, 0, 0, l/2, w/2, 0, t)
        createSide("Front", "2point", -l/2, -w/2, 0, l/2, -w/2+t, 0, h)
        createSide("Back", "2point", -l/2, w/2, 0, l/2, w/2-t, 0, h)
        createSide("Right", "2point", l/2, w/2, 0, l/2-t, -w/2, 0, h)
        createSide("Left", "2point", -l/2, w/2, 0, -l/2+t, -w/2, 0, h)
        createSide("Top", "center", 0, 0, h-t, l/2, -w/2, h-t, t)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
