#Author-copypastestd
#Description-Lab1

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        design = app.activeProduct
    
        rootComp = design.rootComponent
        
#        sketches = rootComp.sketches
#        xyPlane = rootComp.xYConstructionPlane
#        sketch = sketches.add(xyPlane) 
#        
#        circles = sketch.sketchCurves.sketchCircles
#        circle1 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), 2)
#        
        sketches = rootComp.sketches
        yzPlane = rootComp.yZConstructionPlane
        sketch2 = sketches.add(yzPlane) 
        
        circles = sketch2.sketchCurves.sketchCircles
        circle2 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), 2)
        circle3 = circles.addByCenterRadius(adsk.core.Point3D.create(2, 0, 0), 1)
        
    
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
