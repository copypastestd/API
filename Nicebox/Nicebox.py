#Author-copypastestd
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

app = adsk.core.Application.get()
ui  = app.userInterface
design = app.activeProduct
rootComp = adsk.fusion.Component.cast(design.rootComponent)

# unit - cm
t = 0.3
l = 5
w = 10
h = 7,5

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

#def CreateSide(_name, plane, z_point, ext):
def CreateSide(_name, plane, x_p1, p1_y, z_p1, x_p2, p2_y, z_p2, ext):  
    sketches = rootComp.sketches
    
    sketch = sketches.add(plane)
    # Rename sketch
    sketch.name = _name
    
#        # Create bace rectangle
#        lines.addTwoPointRectangle(adsk.core.Point3D.create(-l/2+t, -w/2+t, z_point), adsk.core.Point3D.create(l/2-t, w/2-t, z_point))
#        # Add side rectangles
#        lines.addTwoPointRectangle(adsk.core.Point3D.create(-l/2, -w/3/2, z_point), adsk.core.Point3D.create(-l/2+t, w/3/2, z_point))
#        lines.addTwoPointRectangle(adsk.core.Point3D.create(l/2, -w/3/2, z_point), adsk.core.Point3D.create(l/2-t, w/3/2, z_point))
#        lines.addTwoPointRectangle(adsk.core.Point3D.create(-l/2/3+t, -w/2, z_point), adsk.core.Point3D.create(l/2/3-t, -w/2+t, z_point))
#        lines.addTwoPointRectangle(adsk.core.Point3D.create(-l/2/3+t, w/2, z_point), adsk.core.Point3D.create(l/2/3-t, w/2-t, z_point))
        
    lines = sketch.sketchCurves.sketchLines
    if _name == "Bottom":
        # Create bace rectangle
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1+t, -p1_y+t, z_p1), adsk.core.Point3D.create(x_p2-t, p2_y-t, z_p2))
        # Add side rectangles
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1, -p1_y/3, z_p1), adsk.core.Point3D.create(-x_p2+t, p2_y/3, z_p2))
        lines.addTwoPointRectangle(adsk.core.Point3D.create(x_p1, -p1_y/3, z_p1), adsk.core.Point3D.create(x_p2-t, p2_y/3, z_p2))
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1/3+t, -p1_y, z_p1), adsk.core.Point3D.create(x_p2/3-t, -p2_y+t, z_p2))
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1/3+t, p1_y, z_p1), adsk.core.Point3D.create(x_p2/3-t, p2_y-t, z_p2))
#    else:    
#        # Create bace rectangle
#        lines.addTwoPointRectangle(adsk.core.Point3D.create(-l/2+t, -w/2+t, z_point), adsk.core.Point3D.create(l/2-t, w/2-t, z_point))
#        # Add side rectangles
#        lines.addTwoPointRectangle(adsk.core.Point3D.create(-l/2, -w/3/2, z_point), adsk.core.Point3D.create(-l/2+t, w/3/2, z_point))
#        lines.addTwoPointRectangle(adsk.core.Point3D.create(l/2, -w/3/2, z_point), adsk.core.Point3D.create(l/2-t, w/3/2, z_point))
#        lines.addTwoPointRectangle(adsk.core.Point3D.create(-l/2/3+t, -w/2, z_point), adsk.core.Point3D.create(l/2/3-t, -w/2+t, z_point))
#        lines.addTwoPointRectangle(adsk.core.Point3D.create(-l/2/3+t, w/2, z_point), adsk.core.Point3D.create(l/2/3-t, w/2-t, z_point))
        
    # Create an object collection to use an input.
    profs = adsk.core.ObjectCollection.create()
    
    # Add all of the profiles to the collection.
    for prof in sketch.profiles:
        profs.add(prof)
    
    # Create the extrusion
    extrudes = rootComp.features.extrudeFeatures
    extrudeInput = extrudes.createInput(profs, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    extrudeInput.setDistanceExtent(False, adsk.core.ValueInput.createByReal(ext))
    extrude = rootComp.features.extrudeFeatures.add(extrudeInput)
    
    #Rename body
    body = rootComp.bRepBodies.item(rootComp.bRepBodies.count-1)
    body.name = _name         
    
#    sideFaces = extrude.sideFaces
#    sideFace = sideFaces.item(0)
    
#    quantityFaces = sideFaces.count
#    ui.messageBox("Total {} sides under root component".format(quantityFaces))
    
    
#    return sideFace
    

def run(context):
    ui = None
    try:
        # Method createSide: Name, plane, 1th point cords, 1th point cords, Extrusion distance
        CreateSide("Bottom", rootComp.xZConstructionPlane, l/2, w/2, 0, l/2, w/2, 0, t)  
        
#        CreateSide("Bottom", rootComp.xZConstructionPlane, 0, t)  
#        CreateSide("Right", rootComp.yZConstructionPlane, l/2, -t)          
#        CreateSide("Left", rootComp.yZConstructionPlane, -l/2, t) 
        

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
