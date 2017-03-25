#Author-CopyPasteStd
#Description-Python discript in Spider

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        design = app.activeProduct
        # Корневой компонент в активном дизайне
        rootComp = design.rootComponent;
        # Новый эскиз на плоскости XY
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)
        # Создаем окружность
        circles = sketch.sketchCurves.sketchCircles
        circle1 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0),
        2)
        # Фиксируем размером диаметр окружности
        sketch.sketchDimensions.addDiameterDimension(circle1,
        adsk.core.Point3D.create(3, 3, 0))
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
