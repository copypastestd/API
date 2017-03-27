#Author-copypastestd
#Description-Create a function that will change some of the parameters in the pulley.

import adsk.core, adsk.fusion, adsk.cam, traceback, os

numberOfTeeth = 18
shaftDiameter = 0.5

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        # Access the import manager and root component
        importManager = app.importManager
        rootComp = app.activeProduct.rootComponent
        # Get the file to be imported, here we are telling it where file is located
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SquareToothPulley.f3d')
        # Create the input options and import them to the target
        importOptions = importManager.createFusionArchiveImportOptions(filename)
        importManager.importToTarget(importOptions, rootComp)
        
        # Get the occurance of the imported component
        pulleyOccurance = rootComp.occurrences.item(rootComp.occurrences.count-1)
        
        # Accessing the parts parameters
        parameters = pulleyOccurance.component.parentDesign.allParameters
        teethNumPeram = parameters.itemByName('teethNum')
        shaftDiamPeram = parameters.itemByName('shaftDiameter')
        teethNumPeram.expression = str(numberOfTeeth)
        shaftDiamPeram.expression = str(shaftDiameter) + 'cm'
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
