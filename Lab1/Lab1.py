#Author-copypastestd
#Description-http://fusion360api.weebly.com

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        # Define the radius variables for circle1 and circle2   
        rad1 = 2
        rad2 =  0.156
        
        # Get the Application and User Interface, used for outputting the message box to the user    
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        
        # Get the root component of the active design.
        rootComp = design.rootComponent
        
        ## Create sketch 1 on the xy plane.
        # First access the sketches collection of the root component        
        sketches = rootComp.sketches
        # Get the xy construction plane from the root component
        xyPlane = rootComp.xYConstructionPlane
        # Add sketch 1 to the sketch collection using the xy plane
        sketch1 = sketches.add(xyPlane)
        
        ## Draw a circle in the sketch.
        # Access the sketchcurves and sketch circles collections within sketch 1
        circles = sketch1.sketchCurves.sketchCircles
        ## Draw a circle in the sketch.
        # Access the sketchcurves and sketch circles collections within sketch 1 
        circle1 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), rad1)        
           
        ## Create sketch 2 on the xy plane.
        # Add sketch 2 to the same sketch collection using the same xy plane           
        sketch2 = sketches.add(xyPlane)
      
        ## Draw a circle in the sketch. You will need to grab again the sketchCircles collection from sketch 2.
        # To create the origin of the second circle on the first circle,
        circles = sketch2.sketchCurves.sketchCircles
        # use the radius of the first circle as the x coordinate when creating the 3Dpoint
        circle2 = circles.addByCenterRadius(adsk.core.Point3D.create(rad1, 0, 0), rad2)
        
        #dimensions = sketch.sketchDimensions
        #dimension1 = dimensions.addDiameterDimension(circle1, adsk.core.Point3D.create(1, -1, 1))

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
