#Author-Autodesk Inc.
#Description-Demo command input examples
import adsk.core, adsk.fusion, traceback

app = None
ui  = None
commandId = 'CommandInputGallery'
commandName = 'Box'
commandDescription = 'Demo command input examples.'
rowNumber = 0

# Global set of event handlers to keep them referenced for the duration of the command
handlers = []

#def addRow(tableInput):
#    tableChildInputs = tableInput.commandInputs
#    childTableValueInput = tableChildInputs.addValueInput(tableInput.id + '_value{}'.format(rowNumber), 'Value', 'cm', adsk.core.ValueInput.createByReal(0.0))
#    childTableStringInput =  tableChildInputs.addStringValueInput(tableInput.id + '_string{}'.format(rowNumber), 'String', '1')
#    childTableSpinnerInput = tableChildInputs.addIntegerSpinnerCommandInput(commandId + '_spinnerInt{}'.format(rowNumber), 'Integer Spinner', 2 , 9 , 2, 2)
#    
#    row = tableInput.rowCount
#    tableInput.addCommandInput(childTableValueInput, row, 0)
#    tableInput.addCommandInput(childTableStringInput, row, 1)
#    tableInput.addCommandInput(childTableSpinnerInput, row, 2)
#    
#    global rowNumber
#    rowNumber = rowNumber + 1

class MyCommandInputChangedHandler(adsk.core.InputChangedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
           command = args.firingEvent.sender   
           cmdInput = args.input                   
           inputs = command.commandInputs
           
#           tableInput = inputs.itemById(commandId + '_table')
#           if cmdInput.id == tableInput.id + '_add':
#               addRow(tableInput)
#           elif cmdInput.id == tableInput.id + '_delete':
#               if tableInput.selectedRow == -1:
#                   ui.messageBox('Select one row to delete')
#               else:
#                   tableInput.deleteRow(tableInput.selectedRow)
          
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
                
class MyCommandDestroyHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            # When the command is done, terminate the script
            # This will release all globals which will remove all event handlers
            adsk.terminate()
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

class MyCommandCreatedHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            cmd = args.command
            onDestroy = MyCommandDestroyHandler()
            cmd.destroy.add(onDestroy)
            # Keep the handler referenced beyond this function
            handlers.append(onDestroy)
            
            onInputChanged = MyCommandInputChangedHandler()
            cmd.inputChanged.add(onInputChanged)
            handlers.append(onInputChanged)    
            
            inputs = cmd.commandInputs
            global commandId

            # Create value input
            inputs.addValueInput(commandId + '_value', 'Value', 'cm', adsk.core.ValueInput.createByReal(0.0))
            
            
#            # Create tab input 1
#            tabCmdInput1 = inputs.addTabCommandInput(commandId + '_tab_1', 'Tab 1');
#            tab1ChildInputs = tabCmdInput1.children;
#
#            # Create readonly textbox input
#            tab1ChildInputs.addTextBoxCommandInput(commandId + '_textBox', 'Text Box', 'This is an example of Text Box. It is readonly.', 2, True)
#            # Create editable textbox input
#            tab1ChildInputs.addTextBoxCommandInput(commandId + '_textBox', 'Text Box2', 'This is an example of Text Box. It is not readonly.', 2, False)
#            # Create selection input
#            selectionInput = tab1ChildInputs.addSelectionInput(commandId + '_selection', 'Select', 'Basic select command input')
#            selectionInput.setSelectionLimits(0)
#            # Create string value input
#            tab1ChildInputs.addStringValueInput(commandId + '_string', 'Text', 'Basic string command input')
#            # Create value input
#            tab1ChildInputs.addValueInput(commandId + '_value', 'Value', 'cm', adsk.core.ValueInput.createByReal(0.0))
#            # Create bool value input with checkbox style
#            tab1ChildInputs.addBoolValueInput(commandId + '_checkbox', 'Checkbox', True, '', False)
#            # Create bool value input with button style
#            tab1ChildInputs.addBoolValueInput(commandId + '_button', 'Button', False, 'resources', True)
#            # Create float slider input with two sliders
#            tab1ChildInputs.addFloatSliderCommandInput(commandId + '_floatSlider', 'Float Slider', 'cm', 0, 10.0, True)
#            # Create float slider input with two sliders and a value list
#            floatValueList = [1.0, 3.0, 4.0, 7.0]
#            tab1ChildInputs.addFloatSliderListCommandInput(commandId + '_floatSlider2', 'Float Slider 2', 'cm', floatValueList)
#            # Create float slider input with two sliders and visible texts
#            floatSlider3 = tab1ChildInputs.addFloatSliderCommandInput(commandId + '_floatSlider3', 'Float Slider 3', '', 0, 50.0, False)
#            floatSlider3.setText('Min', 'Max')
#            # Create integer slider input with one slider
#            tab1ChildInputs.addIntegerSliderCommandInput(commandId + '_intSlider', 'Integer Slider', 0, 10);
#            valueList = [1, 3, 4, 7, 11]
#            # Create integer slider input with two sliders and a value list
#            tab1ChildInputs.addIntegerSliderListCommandInput(commandId + '_intSlider2', 'Integer Slider 2', valueList)
#            # Create float spinner input
#            tab1ChildInputs.addFloatSpinnerCommandInput(commandId + '_spinnerFloat', 'Float Spinner', 'cm', 0.2 , 9.0 , 2.2, 1)
#            # Create integer spinner input
#            tab1ChildInputs.addIntegerSpinnerCommandInput(commandId + '_spinnerInt', 'Integer Spinner', 2 , 9 , 2, 3)
#            # Create dropdown input with checkbox style
#            dropdownInput = tab1ChildInputs.addDropDownCommandInput(commandId + '_dropdown', 'Dropdown', adsk.core.DropDownStyles.CheckBoxDropDownStyle)
#            dropdownItems = dropdownInput.listItems
#            dropdownItems.add('Item 1', False, 'resources')
#            dropdownItems.add('Item 2', False, 'resources')
#            # Create dropdown input with icon style
#            dropdownInput2 = tab1ChildInputs.addDropDownCommandInput(commandId + '_dropdown2', 'Dropdown2', adsk.core.DropDownStyles.LabeledIconDropDownStyle);
#            dropdown2Items = dropdownInput2.listItems
#            dropdown2Items.add('Item 1', True, 'resources')
#            dropdown2Items.add('Item 2', False, 'resources')
#            # Create dropdown input with radio style
#            dropdownInput3 = tab1ChildInputs.addDropDownCommandInput(commandId + '_dropdown3', 'Dropdown3', adsk.core.DropDownStyles.LabeledIconDropDownStyle);
#            dropdown3Items = dropdownInput3.listItems
#            dropdown3Items.add('Item 1', True, '')
#            dropdown3Items.add('Item 2', False, '')
#            # Create dropdown input with test list style
#            dropdownInput4 = tab1ChildInputs.addDropDownCommandInput(commandId + '_dropdown4', 'Dropdown4', adsk.core.DropDownStyles.TextListDropDownStyle);
#            dropdown4Items = dropdownInput4.listItems
#            dropdown4Items.add('Item 1', True, '')
#            dropdown4Items.add('Item 2', False, '')
#            # Create single selectable button row input
#            buttonRowInput = tab1ChildInputs.addButtonRowCommandInput(commandId + '_buttonRow', 'Button Row', False)
#            buttonRowInput.listItems.add('Item 1', False, 'resources')
#            buttonRowInput.listItems.add('Item 2', False, 'resources')
#            # Create multi selectable button row input
#            buttonRowInput2 = tab1ChildInputs.addButtonRowCommandInput(commandId + '_buttonRow2', 'Button Row 2', True)
#            buttonRowInput2.listItems.add('Item 1', False, 'resources')
#            buttonRowInput2.listItems.add('Item 2', False, 'resources')
#
#            # Create tab input 2
#            tabCmdInput2 = inputs.addTabCommandInput(commandId + '_tab_2', 'Tab 2')
#            tab2ChildInputs = tabCmdInput2.children
#
#            # Create group input
#            groupCmdInput = tab2ChildInputs.addGroupCommandInput(commandId + '_group', 'Group')
#            groupCmdInput.isExpanded = True
#            groupCmdInput.isEnabledCheckBoxDisplayed = True
#            groupChildInputs = groupCmdInput.children
#            
#            # Create radio button group input
#            radioButtonGroup = groupChildInputs.addRadioButtonGroupCommandInput(commandId + '_radioButtonGroup', 'Radio button group')
#            radioButtonItems = radioButtonGroup.listItems
#            radioButtonItems.add("Item 1", False)
#            radioButtonItems.add("Item 2", False)
#            radioButtonItems.add("Item 3", False)
#            
#            # Create image input
#            groupChildInputs.addImageCommandInput(commandId + "_image", "Image", "resources/image.png")
#            
#            # Create direction input 1
#            directionCmdInput = tab2ChildInputs.addDirectionCommandInput(commandId + '_direction', 'Direction')
#            directionCmdInput.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(1, 0, 0))
#            
#            # Create direction input 2
#            directionCmdInput2 = tab2ChildInputs.addDirectionCommandInput(commandId + '_direction2', 'Direction 2', 'resources')
#            directionCmdInput2.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(0, 1, 0)) 
#            directionCmdInput2.isDirectionFlipped = True
#            
#            # Create distance value input 1
#            distanceValueInput = tab2ChildInputs.addDistanceValueCommandInput(commandId + '_distanceValue', 'DistanceValue', adsk.core.ValueInput.createByReal(2))
#            distanceValueInput.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(1, 0, 0))
#            distanceValueInput.minimumValue = 0
#            distanceValueInput.isMinimumValueInclusive = True
#            distanceValueInput.maximumValue = 10
#            distanceValueInput.isMaximumValueInclusive = True
#            
#            # Create distance value input 2
#            distanceValueInput2 = tab2ChildInputs.addDistanceValueCommandInput(commandId + '_distanceValue2', 'DistanceValue 2', adsk.core.ValueInput.createByReal(1))
#            distanceValueInput2.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(0, 1, 0))
#            distanceValueInput2.expression = '1 in'
#            distanceValueInput2.hasMinimumValue = False
#            distanceValueInput2.hasMaximumValue = False
#            
#            # Create table input
#            tableInput = tab2ChildInputs.addTableCommandInput(commandId + '_table', 'Table', 3, '1:1:1')
#            addRow(tableInput)
#            
#            addButtonInput = tab2ChildInputs.addBoolValueInput(tableInput.id + '_add', 'Add', False, '', True)
#            tableInput.addToolbarCommandInput(addButtonInput)
#            deleteButtonInput = tab2ChildInputs.addBoolValueInput(tableInput.id + '_delete', 'Delete', False, '', True)
#            tableInput.addToolbarCommandInput(deleteButtonInput)
#            
#            # Create angle value input
#            angleValueInput = tab2ChildInputs.addAngleValueCommandInput(commandId + '_angleValue', 'AngleValue', adsk.core.ValueInput.createByString('30 degree'))
#            angleValueInput.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(1, 0, 0), adsk.core.Vector3D.create(0, 0, 1))
#            angleValueInput.hasMinimumValue = False
#            angleValueInput.hasMaximumValue = False
#            
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def run(context):
    ui = None
    try:
        global app
        app = adsk.core.Application.get()
        global ui
        ui = app.userInterface

        global commandId
        global commandName
        global commandDescription

        # Create command defintion
        cmdDef = ui.commandDefinitions.itemById(commandId)
        if not cmdDef:
            cmdDef = ui.commandDefinitions.addButtonDefinition(commandId, commandName, commandDescription)

        # Add command created event
        onCommandCreated = MyCommandCreatedHandler()
        cmdDef.commandCreated.add(onCommandCreated)
        # Keep the handler referenced beyond this function
        handlers.append(onCommandCreated)

        # Execute command
        cmdDef.execute()

        # Prevent this module from being terminate when the script returns, because we are waiting for event handlers to fire
        adsk.autoTerminate(False)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))