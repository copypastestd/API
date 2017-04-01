#Author-copypastestd
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

app = adsk.core.Application.get()

doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)

ui  = app.userInterface
design = app.activeProduct
rootComp = adsk.fusion.Component.cast(design.rootComponent)

# unit - cm
t = 0.3
l = 6
w = 15
h = 8.5

#def ClearData():
#    features = rootComp.features
#    #get one sketch 
#    if features.count > 0:
#        oneFeature = features.item(0)
#        oneFeature.deleteMe()    
#    
#    sketches = rootComp.sketches
#    #get one sketch 
#    if sketches.count > 0:
#        oneSketch = sketches.item(0)
#        oneSketch.deleteMe()
#            
#    #allComps = adsk.core.ObjectCollection.create()
#    
#    #allOccs = rootComp.occurrences    
    

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
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1/2+t, -p1_y/2+t, z_p1), adsk.core.Point3D.create(x_p2/2-t, p2_y/2-t, z_p2))
        # Add side rectangles
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1/2, -p1_y/3/2, z_p1), adsk.core.Point3D.create(-x_p2/2+t, p2_y/3/2, z_p2))
        lines.addTwoPointRectangle(adsk.core.Point3D.create(x_p1/2, -p1_y/3/2, z_p1), adsk.core.Point3D.create(x_p2/2-t, p2_y/3/2, z_p2))
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1/2/3+t, -p1_y/2, z_p1), adsk.core.Point3D.create(x_p2/2/3-t, -p2_y/2+t, z_p2))
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1/2/3+t, p1_y/2, z_p1), adsk.core.Point3D.create(x_p2/2/3-t, p2_y/2-t, z_p2))
    if _name == "Left":
        # Create bace rectangle
        shift = 3*t
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1/2, -shift, z_p1/2), adsk.core.Point3D.create(x_p2/2, p2_y-shift, z_p2/2))
    if _name == "Right":
        # Create bace rectangle
        shift = 3*t
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1/2, -shift, -z_p1/2), adsk.core.Point3D.create(x_p2/2, p2_y-shift, -z_p2/2))    
    if _name == "Front":
        # Create bace rectangle
        shift = 3*t
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1/2+t, -shift, z_p1), adsk.core.Point3D.create(x_p2/2-t, p2_y-shift-t, z_p2))
        # Add side rectangles
        # Left
        #lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1/2, -p1_y/3/2, z_p1), adsk.core.Point3D.create(-x_p2/2+t, p2_y/3/2, z_p2))
        #lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1/2, h/3, z_p1), adsk.core.Point3D.create(-x_p2/2+t, p2_y/3/2, z_p2))
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1/2, p1_y/4, z_p1), adsk.core.Point3D.create(-x_p1/2+t, p2_y/2, z_p2))
        # Right
        lines.addTwoPointRectangle(adsk.core.Point3D.create(x_p1/2, p1_y/4, z_p1), adsk.core.Point3D.create(x_p1/2-t, p2_y/2, z_p2))
        #lines.addTwoPointRectangle(adsk.core.Point3D.create(-3, -5, z_p1), adsk.core.Point3D.create(3, 5, z_p2))

#        lines.addTwoPointRectangle(adsk.core.Point3D.create(x_p1/2, -p1_y/3/2, z_p1), adsk.core.Point3D.create(x_p2/2-t, p2_y/3/2, z_p2))
#        lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1/2/3+t, -p1_y/2, z_p1), adsk.core.Point3D.create(x_p2/2/3-t, -p2_y/2+t, z_p2))
        #lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1/2/3+t, p1_y/2, z_p1), adsk.core.Point3D.create(x_p2/2/3-t, p2_y/2-t, z_p2))
        
        # Top
        lines.addTwoPointRectangle(adsk.core.Point3D.create(-x_p1/2/3+t, p1_y-shift, z_p1), adsk.core.Point3D.create(x_p2/2/3-t, p2_y-t-shift, z_p2))
        
    # Create an object collection to use an input.
    profs = adsk.core.ObjectCollection.create()
    
    # Add all of the profiles to the collection.
    for prof in sketch.profiles:
        profs.add(prof)
    
        
    
    # Create the extrusion
    extrudes = rootComp.features.extrudeFeatures
    extrudeInput = extrudes.createInput(profs, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    
    if _name == "Bottom":
        extrudeInput.setDistanceExtent(False, adsk.core.ValueInput.createByReal(ext))
    if _name == "Left":
        extrudeInput.setDistanceExtent(False, adsk.core.ValueInput.createByReal(-ext))
    if _name == "Right":
        extrudeInput.setDistanceExtent(False, adsk.core.ValueInput.createByReal(ext))
    if _name == "Left":
        extrudeInput.setDistanceExtent(False, adsk.core.ValueInput.createByReal(ext))
    if _name == "Front":
        extrudeInput.setDistanceExtent(False, adsk.core.ValueInput.createByReal(-ext))
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
        CreateSide("Bottom", rootComp.xZConstructionPlane, l, w, 0, l, w, 0, t)
        CreateSide("Left", rootComp.yZConstructionPlane, w, h, l, w, h, l, -t) 
        CreateSide("Right", rootComp.yZConstructionPlane, w, h, l, w, h, l, t)
        CreateSide("Front", rootComp.xYConstructionPlane, l, h*0.9, l, l, h*0.9, l, t)
        #CreateSide("Back", rootComp.xYConstructionPlane, l, h*0.9, -l, l, h*0.9, -l, t)
#        CreateSide("Bottom", rootComp.xZConstructionPlane, 0, t)  
#        CreateSide("Right", rootComp.yZConstructionPlane, l/2, -t)          
#        CreateSide("Left", rootComp.yZConstructionPlane, -l/2, t) 
        

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
