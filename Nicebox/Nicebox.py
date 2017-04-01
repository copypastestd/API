#Author-copypastestd
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

# unit - cm
t = 0.3
l = 5
w = 10
h = 7,5



def Version_1():
    app = adsk.core.Application.get()
    ui  = app.userInterface
    design = app.activeProduct
    rootComp = adsk.fusion.Component.cast(design.rootComponent)
    
    sketches = rootComp.sketches
    xzPlane = rootComp.xZConstructionPlane
    sketch = sketches.add(xzPlane)
    
    lines = sketch.sketchCurves.sketchLines
    lines.addCenterPointRectangle(adsk.core.Point3D.create(0,0,0), adsk.core.Point3D.create(l/2-t, w/2-t, 0))
    
    extrudes = rootComp.features.extrudeFeatures
    prof = sketch.profiles[0]
    extrudeInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    
    distanceExtrude = adsk.core.ValueInput.createByReal(t)
    extrudeInput.setDistanceExtent(False, distanceExtrude)
    extrude = extrudes.add(extrudeInput)
    
    sideFaces = extrude.sideFaces
    sideFace = sideFaces.item(0)
    edge = sideFace.edges.item(0)
    
    sketch = sketches.add(sideFace)
    lines = sketch.sketchCurves.sketchLines
    lines.addTwoPointRectangle(adsk.core.Point3D.create(-w/3/2, 0, 0), adsk.core.Point3D.create(w/3/2, t, 0))
    
    prof = sketch.profiles[1]
    extrudeInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.JoinFeatureOperation)
    distanceExtrude = adsk.core.ValueInput.createByReal(t)
    extrudeInput.setDistanceExtent(False, distanceExtrude)
    extrude = extrudes.add(extrudeInput)

#def ClearData():
#    app = adsk.core.Application.get()
#    ui  = app.userInterface
#    design = app.activeProduct
#    rootComp = adsk.fusion.Component.cast(design.rootComponent)
#    #allComps = adsk.core.ObjectCollection.create()
#    
#    #allOccs = rootComp.occurrences    
#    
#    
#     occs = rootComp.occurrences
    

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        rootComp = adsk.fusion.Component.cast(design.rootComponent)
        
        #Version_1()
        sketches = rootComp.sketches
        xzPlane = rootComp.xZConstructionPlane
        sketch = sketches.add(xzPlane)
        
        lines = sketch.sketchCurves.sketchLines
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-l/2+t, -w/2+t, 0), adsk.core.Point3D.create(l/2-t, w/2-t, 0))
        
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-l/2, -w/3/2, 0), adsk.core.Point3D.create(-l/2+t, w/3/2, 0))
        lines.addTwoPointRectangle(adsk.core.Point3D.create(l/2, -w/3/2, 0), adsk.core.Point3D.create(l/2-t, w/3/2, 0))
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-l/2/3+t, -w/2, 0), adsk.core.Point3D.create(l/2/3-t, -w/2+t, 0))
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-l/2/3+t, w/2, 0), adsk.core.Point3D.create(l/2/3-t, w/2-t, 0))
        
        # Create an object collection to use an input.
        profs = adsk.core.ObjectCollection.create()
        
        # Add all of the profiles to the collection.
        for prof in sketch.profiles:
            profs.add(prof)
        
        # Create the extrusion.
        extrudeInput = rootComp.features.extrudeFeatures.createInput(profs, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extrudeInput.setDistanceExtent(False, adsk.core.ValueInput.createByReal(t))
        extrude = rootComp.features.extrudeFeatures.add(extrudeInput)        
        

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
