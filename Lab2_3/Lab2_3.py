#Author-copypastestd
#Description-Using userInterface.selectEntity, ask the user to select two points. Calculate the length of a belt if there were two pulleys at those two selected points. The belt length should consider the radii of the two pulleys. Output the answer to the users screen.

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        # Get the User Interface
        ui = app.userInterface
        # The needed parameters for selectEntity are (Prompt, filter)
        selectedEntity = ui.selectEntity("Select a Point", "SketchPoints,Vertices,ConstructionPoints")
        # Grab the point from the entity selected
        ​selectedEntityPoint = selectedEntity.point

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
