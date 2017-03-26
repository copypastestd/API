#Author-copypastestd
#Description-Using userInterface.selectEntity, ask the user to select two points. Calculate the length of a belt if there were two pulleys at those two selected points. The belt length should consider the radii of the two pulleys. Output the answer to the users screen.

import adsk.core, adsk.fusion, adsk.cam, traceback, math

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        unitsMgr = design.unitsManager

        rootComp = adsk.fusion.Component.cast(design.rootComponent) 
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch1 = sketches.add(xyPlane)
        sketch1.name = "Sketch number 1"
        
        sketchPoints = sketch1.sketchPoints        
        
        point1 = adsk.core.Point3D.create(-1, 0, 0)
        point2 = adsk.core.Point3D.create(2, 0, 0)
        
        sketchPoint = sketchPoints.add(point1)
        sketchPoint = sketchPoints.add(point2)
        
        ui.messageBox('Select two points')
        selectedItem1 = ui.selectEntity("Select a Point","SketchPoints")
        selectedItem1Value = selectedItem1.point
        selectedItem2 = ui.selectEntity("Select another Point","SketchPoints")
        selectedItem2Value = selectedItem2.point
        lenghtBetweenPoints = selectedItem1Value.distanceTo(selectedItem2Value)
        displayPointsLenght = unitsMgr.formatInternalValue(lenghtBetweenPoints, unitsMgr.defaultLengthUnits, True)
        ui.messageBox('Lengh between Points is: ' + displayPointsLenght)
#        ui.messageBox('The needs belt length is: ' + displayBeltLenght)
#        ui.messageBox('Select two cylindrical faces')
#        selectedItem1 = ui.selectEntity("Select a Cilinder","CylindricalFaces")
#        selectedItem1Value = selectedItem1.point
#        selectedItem2 = ui.selectEntity("Select another Cilinder","CylindricalFaces")
#        selectedItem2Value = selectedItem2.point
#        lenghtBetweenPoints = selectedItem1Value.distanceTo(selectedItem2Value)
        
        #unitsMgr = design.unitsManager
        #ui.messageBox(unitsMgr.formatInternalValue(lenghtBetweenPoints, unitsMgr.defaultLengthUnits, True))
        # Entering Radius values of Pulleys. I believe these have to be in the same units
        #   as a active design units
#        radius1 = 4
#        radius2 = 3
#        adjustedLengthBetweenPulleys = math.sqrt(math.pow(lenghtBetweenPoints, 2) + math.pow(radius1 - radius2, 2))
#        beltLength = (adjustedLengthBetweenPulleys * 2) + (math.pi * radius1) + (math.pi * radius2)
#
#        displayBeltLenght = unitsMgr.formatInternalValue(beltLength, unitsMgr.defaultLengthUnits, True)
#        ui.messageBox('The needs belt length is: ' + displayBeltLenght)
#        

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
