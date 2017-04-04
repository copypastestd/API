#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        fileDialog = ui.createFileDialog()
        fileDialog.isMultiSelectEnabled = False
        fileDialog.title = "Select output folder"
        fileDialog.filter = "*.dxf"
        fileDialog.initialDirectory = "C:/"
        dialogResult = fileDialog.showSave()
        #path = fileDialog.filename.substring(0, fileDialog.filename.lastIndexOf('/')) + '/'

        if (dialogResult == adsk.core.DialogResults.DialogOK):
            path = fileDialog.filename.substring(0, fileDialog.filename.lastIndexOf('/')) + '/'
            
    
        # prevent this module from being terminate when the script returns, because we are waiting for event handlers to fire
        adsk.autoTerminate(False)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
