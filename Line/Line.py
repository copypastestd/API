#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

toothSize = 0.9
t = 0.3

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        
        rootComp = design.rootComponent

        planeXZ = rootComp.xZConstructionPlane        
        
        sketches = rootComp.sketches
        sketch = sketches.add(planeXZ)
        
        lines = sketch.sketchCurves.sketchLines
        
        line1 = lines.addByTwoPoints(adsk.core.Point3D.create(1, 1, 0), adsk.core.Point3D.create(10, 1, 0)) #horizontal
        #line1 = lines.addByTwoPoints(adsk.core.Point3D.create(1, 1, 0), adsk.core.Point3D.create(1, 10, 0)) #vertical
        
        # Get sketch points
        sketchPoints = sketch.sketchPoints        
              
        
        if line1.length > toothSize:
            print('\n' + 'OK', end=' ' + '\n')

            #summaryDots = line1.length/toothSize/2         
            #print(str(summaryDots))
            #midPoint= sketchPoints.add(adsk.core.Point3D.create(10, 10, 0))
            #sketch.geometricConstraints.addMidPoint(midPoint, line1)
            
            startX = line1.startSketchPoint.geometry.x         
            startY = line1.startSketchPoint.geometry.y
            endX = line1.endSketchPoint.geometry.x
            endY = line1.endSketchPoint.geometry.y
            
#            print("StartX: " + str(startX))
#            print("StartY: " + str(startY))            
#            print("endX: " + str(endX))            
#            print("endY: " + str(endY))            
            
            if startX != endX and startY == endY:
                print("Line in horizontal")
                
                
            if startY != endY and startX == endX:
                print("Line is vertical")
        
            offset = toothSize/2+toothSize/3
            start = startX+offset
            finish = endX-offset
            print("start " + str(start))
            print("finish " + str(finish))
            print("\n")
            
            dist = finish-start
            print("Distance " + str(dist))            
            count = dist/toothSize/2
            print("Count " + str(count))
            count_final = round(count)
            print("count_final " + str(count_final))
            if count_final < 1:
                print('count_final < 1')
                
                mid = (endX+startX)/2
                print("endX " + str(endX))
                print("startX " + str(startX))
                print("mid " + str(mid))
                
                # Place a dot (Optional)
                sketchPoints.add(adsk.core.Point3D.create(mid, startY, 0))
                
                # Draw a CenterPointRectangle
                centerPoint = adsk.core.Point3D.create(mid, startY, 0)
                cornerPoint = adsk.core.Point3D.create(mid+toothSize/2, startY+t, 0)
                lines.addCenterPointRectangle(centerPoint, cornerPoint)
                    
            else:
                print('ELSE')
                #while startX < endX-toothSize/2+toothSize/3:
                while startX < endX:
                    sketchPoints.add(adsk.core.Point3D.create(startX+offset, startY, 0))
                    
                    centerPoint = adsk.core.Point3D.create(startX+offset, startY, 0)
                    
                    #ПОЧЕМУ 0.7 - Я ХЗ
                    cornerPoint = adsk.core.Point3D.create(startX+offset+toothSize/2, startY+t, 0)
    
                    lines.addCenterPointRectangle(centerPoint, cornerPoint)
                    
                    startX = startX+dist/count_final
                    print("startX2 move " + str(startX))

        else:
            print('not OK')
            
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
