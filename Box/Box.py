#Author-copypastestd
#Description-Test box

import adsk.core, adsk.fusion, adsk.cam, traceback

app = adsk.core.Application.get()
ui  = app.userInterface
design = app.activeProduct
unitsMgr = design.unitsManager

# unit - cm
t = 0.3
h = 10
l = 15
w = 5

def createNewComponent():
    # Get the active design.
    product = app.activeProduct
    design = adsk.fusion.Design.cast(product)
    rootComp = design.rootComponent
    allOccs = rootComp.occurrences
    newOcc = allOccs.addNewComponent(adsk.core.Matrix3D.create())
    return newOcc.component

def run(context):
    ui = None
    try:
        
        
        rootComp = adsk.fusion.Component.cast(design.rootComponent) 
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

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
