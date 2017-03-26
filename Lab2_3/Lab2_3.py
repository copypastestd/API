#Author-copypastestd
#Description-Using userInterface.selectEntity, ask the user to select two points. Calculate the length of a belt if there were two pulleys at those two selected points. The belt length should consider the radii of the two pulleys. Output the answer to the users screen.

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        
        ui  = app.userInterface
        ui.messageBox('Select two cylindrical faces')
        selectedItem1 = ui.selectEntity("Select a Cilinder","CylindricalFaces")
        selectedItem1Value = selectedItem1.point
        selectedItem2 = ui.selectEntity("Select another Cilinder","CylindricalFaces")
        selectedItem2Value = selectedItem2.point
        lenghtBetweenPoints = selectedItem1Value.distanceTo(selectedItem2Value)
        
        #unitsMgr = design.unitsManager
        #ui.messageBox(unitsMgr.formatInternalValue(lenghtBetweenPoints, unitsMgr.defaultLengthUnits, True))
        # Entering Radius values of Pulleys. I believe these have to be in the same units
        #   as a active design units
        radius1 = 4
        radius2 = 3
        adjustedLengthBetweenPulleys = math.sqrt(math.pow(lenghtBetweenPoints, 2) + math.pow(radius1 - radius2, 2))
        beltLength = (adjustedLengthBetweenPulleys * 2) + (math.pi * radius1) + (math.pi * radius2)
        unitsMgr = design.unitsManager
        displayBeltLenght = unitsMgr.formatInternalValue(beltLength, unitsMgr.defaultLengthUnits, True)
        ui.messageBox('The needs belt length is: ' + displayBeltLenght)
        

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
