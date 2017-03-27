#Author-copypastestd
#Description-Create a function that uses the API to import a file containing a pulley.

import adsk.core, adsk.fusion, adsk.cam, traceback, os

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
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
