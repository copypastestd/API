#Author-Autodesk Inc.
#Description-Create bolt

import adsk.core, adsk.fusion, traceback
import math

defaultBoxName = 'Box'
defaultHeadDiameter = 0.3
defaultBodyDiameter = 10
defaultHeadHeight = 10
defaultBodyLength = 10
defaultCutAngle = 0.3
defaultChamferDistance = 1
defaultFilletRadius = 0.3

#wall = self.headDiameter
#h = self.bodyDiameter
#w = self.headHeight
#d = self.bodyLength
#kerf = self.cutAngle
#shiftTotal = self.chamferDistance
#shiftTop    = shiftTotal
#shiftBack   = shiftTotal
#shiftBottom = shiftTotal
#shiftFront  = shiftTotal
#sheetAlpha = self.filletRadius

#wall = 0.3
#h = 10
#w = 10
#d = 10
#kerf = 0.3
#shiftTotal = 1.5
#sheetAlpha = 0.3

# global set of event handlers to keep them referenced for the duration of the command
handlers = []
app = adsk.core.Application.get()
if app:
    ui = app.userInterface

newComp = None

def createNewComponent():
    # Get the active design.
    product = app.activeProduct
    design = adsk.fusion.Design.cast(product)
    rootComp = design.rootComponent
    allOccs = rootComp.occurrences
    newOcc = allOccs.addNewComponent(adsk.core.Matrix3D.create())
    return newOcc.component

class BoltCommandExecuteHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            unitsMgr = app.activeProduct.unitsManager
            command = args.firingEvent.sender
            inputs = command.commandInputs

            bolt = Bolt()
            for input in inputs:
                if input.id == 'boltName':
                    bolt.boltName = input.value
                elif input.id == 'headDiameter':
                    bolt.headDiameter = unitsMgr.evaluateExpression(input.expression, "cm")
                elif input.id == 'height':
                    bolt.bodyDiameter = unitsMgr.evaluateExpression(input.expression, "cm")
                elif input.id == 'headHeight':
                    bolt.headHeight = unitsMgr.evaluateExpression(input.expression, "cm")
                elif input.id == 'bodyLength':
                    bolt.bodyLength = unitsMgr.evaluateExpression(input.expression, "cm")
                elif input.id == 'cutAngle':
                    bolt.cutAngle = unitsMgr.evaluateExpression(input.expression, "cm") 
                elif input.id == 'chamferDistance':
                    bolt.chamferDistance = unitsMgr.evaluateExpression(input.expression, "cm")
                elif input.id == 'filletRadius':
                    bolt.filletRadius = unitsMgr.evaluateExpression(input.expression, "cm")

            bolt.buildBolt();
            args.isValidResult = True

        except:
            if ui:
                #ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
                print('Failed:\n{}'.format(traceback.format_exc()))

class BoltCommandDestroyHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            # when the command is done, terminate the script
            # this will release all globals which will remove all event handlers
            adsk.terminate()
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

class BoltCommandCreatedHandler(adsk.core.CommandCreatedEventHandler):    
    def __init__(self):
        super().__init__()        
    def notify(self, args):
        try:
            cmd = args.command
            cmd.isRepeatable = False
            onExecute = BoltCommandExecuteHandler()
            cmd.execute.add(onExecute)
            onExecutePreview = BoltCommandExecuteHandler()
            cmd.executePreview.add(onExecutePreview)
            onDestroy = BoltCommandDestroyHandler()
            cmd.destroy.add(onDestroy)
            # keep the handler referenced beyond this function
            handlers.append(onExecute)
            handlers.append(onExecutePreview)
            handlers.append(onDestroy)

            #define the inputs
            inputs = cmd.commandInputs
            inputs.addStringValueInput('boltName', 'Blot Name', defaultBoxName)

            initHeadDiameter = adsk.core.ValueInput.createByReal(defaultHeadDiameter)
            inputs.addValueInput('headDiameter', 'Wall','cm',initHeadDiameter)

            initBodyDiameter = adsk.core.ValueInput.createByReal(defaultBodyDiameter)
            inputs.addValueInput('height', 'Height', 'cm', initBodyDiameter)

            initHeadHeight = adsk.core.ValueInput.createByReal(defaultHeadHeight)
            inputs.addValueInput('headHeight', 'Width', 'cm', initHeadHeight)

            initBodyLength = adsk.core.ValueInput.createByReal(defaultBodyLength)
            inputs.addValueInput('bodyLength', 'Depth', 'cm', initBodyLength)

            #to do the thread length

            initCutAngle = adsk.core.ValueInput.createByReal(defaultCutAngle)
            inputs.addValueInput('cutAngle', 'Kerf Laser Cut', 'cm', initCutAngle)

            initChamferDistance = adsk.core.ValueInput.createByReal(defaultChamferDistance)
            inputs.addValueInput('chamferDistance', 'Shift', 'cm', initChamferDistance)

            initFilletRadius = adsk.core.ValueInput.createByReal(defaultFilletRadius)
            inputs.addValueInput('filletRadius', 'Tooth Proportions', '', initFilletRadius)
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

class Bolt:
    def __init__(self):
        self._boxName = defaultBoxName
        self._wall = defaultHeadDiameter
        self._bodyDiameter = defaultBodyDiameter
        self._headHeight = defaultHeadHeight
        self._bodyLength = adsk.core.ValueInput.createByReal(defaultBodyLength)
        self._cutAngle = defaultCutAngle
        self._chamferDistance = adsk.core.ValueInput.createByReal(defaultChamferDistance)
        self._filletRadius = adsk.core.ValueInput.createByReal(defaultFilletRadius)



    #properties
    @property
    def boltName(self):
        return self._boxName
    @boltName.setter
    def boltName(self, value):
        self._boxName = value

    @property
    def headDiameter(self):
        return self._wall
    @headDiameter.setter
    def headDiameter(self, value):
        self._wall = value

    @property
    def bodyDiameter(self):
        return self._bodyDiameter
    @bodyDiameter.setter
    def bodyDiameter(self, value):
        self._bodyDiameter = value 

    @property
    def headHeight(self):
        return self._headHeight
    @headHeight.setter
    def headHeight(self, value):
        self._headHeight = value 

    @property
    def bodyLength(self):
        return self._bodyLength
    @bodyLength.setter
    def bodyLength(self, value):
        self._bodyLength = value   

    @property
    def cutAngle(self):
        return self._cutAngle
    @cutAngle.setter
    def cutAngle(self, value):
        self._cutAngle = value  

    @property
    def chamferDistance(self):
        return self._chamferDistance
    @chamferDistance.setter
    def chamferDistance(self, value):
        self._chamferDistance = value

    @property
    def filletRadius(self):
        return self._filletRadius
    @filletRadius.setter
    def filletRadius(self, value):
        self._filletRadius = value

    def buildBolt(self):
        root = createNewComponent() 
        features = root.features
        extrudes = root.features.extrudeFeatures
        
        
        wall = self.headDiameter
        h = self.bodyDiameter   #height
        w = self.headHeight
        d = self.bodyLength
        kerf = self.cutAngle
        shiftTotal = self.chamferDistance
        shiftTop    = shiftTotal
        shiftBack   = shiftTotal
        shiftBottom = shiftTotal
        shiftFront  = shiftTotal
        
        sheetAlpha = self.filletRadius
        
        
        #wall = self.headDiameter
        #h = self.bodyDiameter
        #w = self.headHeight
        #d = self.bodyLength
        #kerf = self.cutAngle
        #shiftTotal = self.chamferDistance
        #shiftTop    = shiftTotal
        #shiftBack   = shiftTotal
        #shiftBottom = shiftTotal
        #shiftFront  = shiftTotal
        #sheetAlpha = self.filletRadius
        
        sheetZ = (w-2*wall)*sheetAlpha/2                              #2
        sheetXBase = (d-2*wall-shiftFront-shiftBack)*sheetAlpha/2     #1
        sheetXFront = (h-2*wall-shiftTop-shiftBottom)*sheetAlpha/2    #1
        
        conerFront  = d/2-wall-shiftFront #-(wall-kerf)
        conerBack   = d/2-wall-shiftBack        
        
    
        base(shiftBottom,root,w,wall,conerFront,conerBack,sheetZ,sheetXBase)
        base(h-wall-shiftTop,root,w,wall,conerFront,conerBack,sheetZ,sheetXBase)
    
        left((w-wall)/2,root,d,h,wall)
        left(-(w-wall)/2-wall,root,d,h,wall)
    
        back(conerBack,root,w,wall,h,sheetXFront)
        back(-conerFront-wall,root,w,wall,h,sheetXFront)
        
     
        
        
        print(root.bRepBodies.count)
        
        
        
        #Cut
        CombineCutFeats = features.combineFeatures          
        
        #Cut Rigth
        
        
        ToolBodies = adsk.core.ObjectCollection.create()
        ToolBodies.add(root.bRepBodies.item(0))
        ToolBodies.add(root.bRepBodies.item(1))
        ToolBodies.add(root.bRepBodies.item(4))
        ToolBodies.add(root.bRepBodies.item(5))
        
        CombineCutInput = root.features.combineFeatures.createInput(root.bRepBodies.item(2), ToolBodies )
        CombineCutInput.operation = adsk.fusion.FeatureOperations.CutFeatureOperation
        CombineCutInput.isKeepToolBodies = True
        CombineCutFeats.add(CombineCutInput)
        
        #Cut Left
        CombineCutInput = root.features.combineFeatures.createInput(root.bRepBodies.item(3), ToolBodies )
        CombineCutInput.operation = adsk.fusion.FeatureOperations.CutFeatureOperation
        CombineCutInput.isKeepToolBodies = True
        CombineCutFeats.add(CombineCutInput)
        
        #Cut Front
        ToolBodies = adsk.core.ObjectCollection.create()
        ToolBodies.add(root.bRepBodies.item(0))
        ToolBodies.add(root.bRepBodies.item(1))
        
        CombineCutInput = root.features.combineFeatures.createInput(root.bRepBodies.item(4), ToolBodies )
        CombineCutInput.operation = adsk.fusion.FeatureOperations.CutFeatureOperation
        CombineCutInput.isKeepToolBodies = True
        CombineCutFeats.add(CombineCutInput)
        
        #Cut back
        ToolBodies = adsk.core.ObjectCollection.create()
        ToolBodies.add(root.bRepBodies.item(0))
        ToolBodies.add(root.bRepBodies.item(1))
        
        CombineCutInput = root.features.combineFeatures.createInput(root.bRepBodies.item(5), ToolBodies )
        CombineCutInput.operation = adsk.fusion.FeatureOperations.CutFeatureOperation
        CombineCutInput.isKeepToolBodies = True
        CombineCutFeats.add(CombineCutInput)
        
        print(root.bRepBodies.count)
        
        print(root.sketches.count)    
        
def back(offset,root,w,wall,h,sheetXFront):

    sketches = root.sketches
    planeXY = root.xYConstructionPlane
    sketch = sketches.add(planeXY)
    
    lines = sketch.sketchCurves.sketchLines   
    
    lines.addTwoPointRectangle(adsk.core.Point3D.create(-(w-wall)/2,h,offset),adsk.core.Point3D.create((w-wall)/2,0,offset))
    # sheetXFront for left
    lines.addCenterPointRectangle(adsk.core.Point3D.create(-(w-wall)/2,h/2,offset),adsk.core.Point3D.create(-(w-wall)/2-wall,h/2+sheetXFront,offset))
    # sheetXFront for Rigth
    lines.addCenterPointRectangle(adsk.core.Point3D.create((w-wall)/2,h/2,offset),adsk.core.Point3D.create((w-wall)/2+wall,h/2+sheetXFront,offset))
    
    extrudes = root.features.extrudeFeatures
    #prof = sketch.profiles[0]
    
    profs = adsk.core.ObjectCollection.create()
        
    for prof in sketch.profiles:
        profs.add(prof)
        
    extrudeInput = extrudes.createInput(profs, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    distExtrude = adsk.core.ValueInput.createByReal(wall)   
    extrudeInput.setDistanceExtent(False, distExtrude)
    return extrudes.add(extrudeInput)

def left(offset,root,d,h,wall):
    sketches = root.sketches
    planeYZ = root.yZConstructionPlane
    sketch = sketches.add(planeYZ)
    
    lines = sketch.sketchCurves.sketchLines
    
    lines.addTwoPointRectangle(adsk.core.Point3D.create(d/2,h,offset),adsk.core.Point3D.create(-d/2,0,offset))
    
    extrudes = root.features.extrudeFeatures
    #prof = sketch.profiles[0]
    
    profs = adsk.core.ObjectCollection.create()
        
    for prof in sketch.profiles:
        profs.add(prof)
        
    extrudeInput = extrudes.createInput(profs, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    distExtrude = adsk.core.ValueInput.createByReal(wall)   
    extrudeInput.setDistanceExtent(False, distExtrude)
    return extrudes.add(extrudeInput)


def base(offset,root,w,wall,conerFront,conerBack,sheetZ,sheetXBase):
    sketches = root.sketches
    planeXZ = root.xZConstructionPlane
    sketch = sketches.add(planeXZ)
    
    lines = sketch.sketchCurves.sketchLines
    
    
      
    #   half of base from origin to front
    lines.addTwoPointRectangle(adsk.core.Point3D.create(-(w-wall)/2,0,offset),adsk.core.Point3D.create((w-wall)/2,conerFront,offset))
    #   half of base from origin to back        
    lines.addTwoPointRectangle(adsk.core.Point3D.create(-(w-wall)/2,0,offset),adsk.core.Point3D.create((w-wall)/2,-conerBack,offset))
    # sheetZ for front
    lines.addCenterPointRectangle(adsk.core.Point3D.create(0,conerFront,offset),adsk.core.Point3D.create(sheetZ,conerFront-wall,offset))
    # sheetZ for back
    lines.addCenterPointRectangle(adsk.core.Point3D.create(0,-conerBack,offset),adsk.core.Point3D.create(sheetZ,-conerBack-wall,offset))
    # sheetXBase for left
    lines.addCenterPointRectangle(adsk.core.Point3D.create(-(w-wall)/2,0,offset),adsk.core.Point3D.create((-(w-wall)/2)-wall,sheetXBase,offset))   
    # sheetXBase for Rigth
    lines.addCenterPointRectangle(adsk.core.Point3D.create((w-wall)/2,0,offset),adsk.core.Point3D.create(((w-wall)/2)+wall,sheetXBase,offset))   
  
    extrudes = root.features.extrudeFeatures
    #prof = sketch.profiles[0]
    
    profs = adsk.core.ObjectCollection.create()
        
    for prof in sketch.profiles:
        profs.add(prof)
        
    extrudeInput = extrudes.createInput(profs, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    distExtrude = adsk.core.ValueInput.createByReal(wall)   
    extrudeInput.setDistanceExtent(False, distExtrude)
    return extrudes.add(extrudeInput)
            
def run(context):
    try:
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        if not design:
            ui.messageBox('It is not supported in current workspace, please change to MODEL workspace and try again.')
            return
        commandDefinitions = ui.commandDefinitions
        #check the command exists or not
        cmdDef = commandDefinitions.itemById('Bolt')
        if not cmdDef:
            cmdDef = commandDefinitions.addButtonDefinition('Bolt',
                    'Create Bolt',
                    'Create a bolt.',
                    './resources') # relative resource file path is specified

        onCommandCreated = BoltCommandCreatedHandler()
        cmdDef.commandCreated.add(onCommandCreated)
        # keep the handler referenced beyond this function
        handlers.append(onCommandCreated)
        inputs = adsk.core.NamedValues.create()
        cmdDef.execute(inputs)

        # prevent this module from being terminate when the script returns, because we are waiting for event handlers to fire
        adsk.autoTerminate(False)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
