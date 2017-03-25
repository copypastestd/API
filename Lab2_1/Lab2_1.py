#Author-copypastestd
#Description-Create a new script. In this script, use selectEntity to get two points that the user selects

import adsk.core, adsk.fusion, adsk.cam, traceback, math

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        design = app.activeProduct
        
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
