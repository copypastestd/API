#Author-copypastestd
#Description-Add circle

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        # Define the radius variables for circle1 and circle2   
        rad1 = 2
        rad2 =  1.5
        
        # Get the Application and User Interface, used for outputting the message box to the user    
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        
        # Get the root component of the active design.
        #rootComp = design.rootComponent
        rootComp = adsk.fusion.Component.cast(design.rootComponent)        
        
        ## Create sketch 1 on the xy plane.
        # First access the sketches collection of the root component        
        sketches = rootComp.sketches
        # Get the xy construction plane from the root component
        xZPlane = rootComp.xZConstructionPlane
        # Add sketch 1 to the sketch collection using the xy plane
        sketch1 = sketches.add(xZPlane)
        
        ## Draw a circle in the sketch.
        # Access the sketchcurves and sketch circles collections within sketch 1
        circles = sketch1.sketchCurves.sketchCircles
        ## Draw a circle in the sketch.
        # Access the sketchcurves and sketch circles collections within sketch 1 
        circle1 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), rad1) 
        
        # Get first profile in the sketch.
        firstCircleProfile = sketch1.profiles.item(0) 
        
        # Create an extrudeInput        
        extrudes = rootComp.features.extrudeFeatures
        firstExtrudeInput = extrudes.createInput(firstCircleProfile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        
        # Assigning the distanse to the extrude
        distanceMainExtrude = adsk.core.ValueInput.createByReal(8)
        # Put the distance value in, False is for symmetric
        firstExtrudeInput.setDistanceExtent(False, distanceMainExtrude)
        # Creating the extrusion
        firstExtrude = extrudes.add(firstExtrudeInput)
        
        ## Create sketch 2 on the xy plane.
        # Add sketch 2 to the same sketch collection using the same xy plane           
        sketch2 = sketches.add(xZPlane)
        
        ## Draw a circle in the sketch. You will need to grab again the sketchCircles collection from sketch 2.
        # To create the origin of the second circle on the first circle,
        circles = sketch2.sketchCurves.sketchCircles
        # use the radius of the first circle as the x coordinate when creating the 3Dpoint
        circle2 = circles.addByCenterRadius(adsk.core.Point3D.create(20, 0, 0), rad2)
        
        # Get second profile in the sketch.
        secondCircleProfile = sketch2.profiles.item(0) 
        
        # Create an extrudeInput        
        extrudes = rootComp.features.extrudeFeatures
        secondExtrudeInput = extrudes.createInput(secondCircleProfile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        
        # Assigning the distanse to the extrude
        distanceMainExtrude = adsk.core.ValueInput.createByReal(8)
        # Put the distance value in, False is for symmetric
        secondExtrudeInput.setDistanceExtent(False, distanceMainExtrude)
        # Creating the extrusion
        secondExtrude = extrudes.add(secondExtrudeInput)
        
        # Creating a Pattern Feature
        # Get the CircuLAR pattern Collection
        circularPatterns = rootComp.features.circularPatternFeatures
        # Creating the entity collection to pass into the input
        inputEntitiesCollection = adsk.core.ObjectCollection.create()
        inputEntitiesCollection.add(secondExtrude)
        inputAxis = rootComp.yConstructionAxis
        # Create the circular pattern input
        circularPatternInput = circularPatterns.createInput(inputEntitiesCollection, inputAxis)
        circularPatternInput.quantity = adsk.core.ValueInput.createByReal(5)
        circularPatternInput.totalAngle = adsk.core.ValueInput.createByString('180 deg')
        circularPatternInput.isSymmetric = False
        # Creating the Circular Pattern
        circularPattern = circularPatterns.add(circularPatternInput)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
