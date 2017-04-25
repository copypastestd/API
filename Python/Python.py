def run(context):
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface        
        des = adsk.fusion.Design.cast(app.activeProduct)

        # Get a parameter name from the user.
        (paramName, cancelled) = ui.inputBox('Enter the name of the parameter', 'Check for Parameter', '')
        
        # If the input dialog wasn't cancelled, check to see if the parameter exists.
        if not cancelled:
            if paramExists(des, paramName):
                ui.messageBox('The parameter "' + paramName + '" exists.')
            else:
                ui.messageBox('The parameter "' + paramName + '" was NOT found.')
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
    

def paramExists(design, paramName):
    # Try to get the parameter with the specified name.
    param = design.userParameters.itemByName(paramName)            
    
    # Check to see if a parameter was returned.
    if param:
        return True
    else:
        return False