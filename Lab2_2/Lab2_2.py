#Author-copypastestd
#Description-Using the code from Lab 1, query the profile geometry from the two circles that were created. This profile will be needed to create the extrude for the pulley geometry. 

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('Hello script')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
