#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        root = app.activeProduct.rootComponent
        features = root.features
        TargetBody = root.bRepBodies.itemByName('Body1')
        ToolBodies = adsk.core.ObjectCollection.create()
        ToolBodies.add(root.bRepBodies.itemByName('Body2'))
        CombineCutInput = root.features.combineFeatures.createInput(TargetBody, ToolBodies )
        CombineCutFeats = features.combineFeatures
        CombineCutInput = CombineCutFeats.createInput(TargetBody, ToolBodies)
        CombineCutInput.operation = adsk.fusion.FeatureOperations.CutFeatureOperation
        CombineCutFeats.add(CombineCutInput)
        ui.messageBox('Hello script')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
