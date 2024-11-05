# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import pickle
import numpy as np
import glob
import os

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 0.0), point1=(1.16665, 0.0))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(7.0, 70.0), 
    point2=(-7.0, -70.0))
# mdb.models['Model-1'].sketches.changeKey(fromName='__profile__', toName=
#     'specimen')
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 0.0), point1=(1.16665, 0.0))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(7.0, 70.0), 
    point2=(-7.0, -70.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-1'].BaseSolidExtrude(depth=0.32, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts.changeKey(fromName='Part-1', toName='layer_1')
mdb.models['Model-1'].Part(name='layer_2', objectToCopy=
    mdb.models['Model-1'].parts['layer_1'])
mdb.models['Model-1'].Part(name='layer_3', objectToCopy=
    mdb.models['Model-1'].parts['layer_2'])
mdb.models['Model-1'].Part(name='layer_4', objectToCopy=
    mdb.models['Model-1'].parts['layer_3'])
mdb.models['Model-1'].Part(name='layer_5', objectToCopy=
    mdb.models['Model-1'].parts['layer_4'])
mdb.models['Model-1'].Part(name='layer_6', objectToCopy=
    mdb.models['Model-1'].parts['layer_5'])
mdb.models['Model-1'].Part(name='layer_7', objectToCopy=
    mdb.models['Model-1'].parts['layer_6'])
mdb.models['Model-1'].Part(name='layer_8', objectToCopy=
    mdb.models['Model-1'].parts['layer_7'])
mdb.models['Model-1'].Part(name='layer_9', objectToCopy=
    mdb.models['Model-1'].parts['layer_8'])
mdb.models['Model-1'].Part(name='layer_10', objectToCopy=
    mdb.models['Model-1'].parts['layer_9'])
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_1-1', 
    part=mdb.models['Model-1'].parts['layer_1'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_2-1', 
    part=mdb.models['Model-1'].parts['layer_2'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_3-1', 
    part=mdb.models['Model-1'].parts['layer_3'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_4-1', 
    part=mdb.models['Model-1'].parts['layer_4'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_5-1', 
    part=mdb.models['Model-1'].parts['layer_5'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_6-1', 
    part=mdb.models['Model-1'].parts['layer_6'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_7-1', 
    part=mdb.models['Model-1'].parts['layer_7'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_8-1', 
    part=mdb.models['Model-1'].parts['layer_8'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_9-1', 
    part=mdb.models['Model-1'].parts['layer_9'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_10-1', 
    part=mdb.models['Model-1'].parts['layer_10'])
mdb.models['Model-1'].rootAssembly.instances['layer_2-1'].translate(vector=(
    15.4, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.instances['layer_3-1'].translate(vector=(
    30.8, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.instances['layer_4-1'].translate(vector=(
    46.2, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.instances['layer_5-1'].translate(vector=(
    61.6, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.instances['layer_6-1'].translate(vector=(
    77.0, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.instances['layer_7-1'].translate(vector=(
    92.4, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.instances['layer_8-1'].translate(vector=(
    107.8, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.instances['layer_9-1'].translate(vector=(
    123.2, 0.0, 0.0))
del mdb.models['Model-1'].rootAssembly.features['layer_10-1']
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_10-1', 
    part=mdb.models['Model-1'].parts['layer_10'])
mdb.models['Model-1'].rootAssembly.instances['layer_10-1'].translate(vector=(
    138.6, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('layer_2-1', ), 
    vector=(-15.4, 0.0, 0.32))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('layer_3-1', ), 
    vector=(-30.8, 0.0, 0.64))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('layer_4-1', ), 
    vector=(53.2, -70.0, 0.0))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('layer_5-1', ), 
    vector=(-61.6, 0.0, 0.96))
mdb.models['Model-1'].rootAssembly.deleteFeatures(('layer_1-1', 'layer_2-1', 
    'layer_3-1', 'layer_4-1', 'layer_5-1', 'layer_6-1', 'layer_7-1', 
    'layer_8-1', 'layer_9-1', 'layer_10-1'))
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)

layer2_porosity = 0
layer3_porosity = 0
layer4_porosity = 0
layer5_porosity = 0
layer6_porosity = 0
layer7_porosity = 0
layer8_porosity = 0
layer9_porosity = 0

# this is the second layer
def layer2_update(defect_info):
    mdb.models['Model-1'].ConstrainedSketch(gridSpacing=7.03, name='__profile__', sheetSize=281.39, transform=mdb.models['Model-1'].parts['layer_2'].MakeSketchTransform(sketchPlane=mdb.models['Model-1'].parts['layer_2'].faces[5], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['layer_2'].edges[0], sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.32)))
    #mdb.models['Model-1'].parts['layer_2'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
    #mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-3.515, 31.635), point2=(-1.7575, 24.605))
    #mdb.models['Model-1'].parts['layer_2'].CutExtrude(flipExtrudeDirection=OFF, sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT, sketchPlane=mdb.models['Model-1'].parts['layer_2'].faces[5], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['layer_2'].edges[0])
    for i in range(len(defect_info)):
        for j in range(len(defect_info[i])):
            if j < len(defect_info[i]) - 1:
                #print((defect_info[i][j][0] - 400) * 0.02)
                #print((defect_info[i][j][1] - 600) * 0.02)
                mdb.models['Model-1'].parts['layer_2'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=((545 - defect_info[i][j][0]) * 0.1, (725 - defect_info[i][j][1]) * 0.1), point2=(( 545 - defect_info[i][j + 1][0]) * 0.1, (725 - defect_info[i][j + 1][1]) * 0.1))
            else:
                #print((defect_info[i][j][0] - 400) * 0.02)
                #print((defect_info[i][j][1] - 600) * 0.02)
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=((545 -defect_info[i][j][0]) * 0.1, (725 - defect_info[i][j][1]) * 0.1), point2=((545- defect_info[i][0][0]) * 0.1, (725 - defect_info[i][0][1]) * 0.1))
            #s.unsetPrimaryObject()
    mdb.models['Model-1'].parts['layer_2'].CutExtrude(flipExtrudeDirection=OFF, sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation= RIGHT, sketchPlane=mdb.models['Model-1'].parts['layer_2'].faces[5], sketchPlaneSide=SIDE1, sketchUpEdge= mdb.models['Model-1'].parts['layer_2'].edges[0])
    del mdb.models['Model-1'].sketches['__profile__']
    layer2_porosity = porosity[1]
    print('layer 2 extrude cut finished')
    return layer2_porosity


# this is the third layer
def layer3_update(defect_info):
    for i in range(len(defect_info)):
        for j in range(len(defect_info[i])):
            if j < len(defect_info[i]) - 1:
                mdb.models['Model-1'].parts['layer_3'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=((defect_info[i][j][0] - 445) * 0.12, (defect_info[i][j][1] - 675) * 0.12), point2=((defect_info[i][j + 1][0] - 445) * 0.12, (defect_info[i][j + 1][1] - 675) * 0.12))
    mdb.models['Model-1'].parts['layer_3'].CutExtrude(flipExtrudeDirection=OFF, sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT, sketchPlane=mdb.models['Model-1'].parts['layer_3'].faces[16], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['layer_3'].edges[19])
    del mdb.models['Model-1'].sketches['__profile__']
    layer3_porosity = porosity[2]
    print('layer 3 extrude cut finished')
    return layer3_porosity
    
    
# here is the fourth layer    
def layer4_update(defect_info):
    for i in range(len(defect_info)):
        if (len(defect_info[i]) > 15):
            for j in range(len(defect_info[i])):
                if j < (len(defect_info[i]) - 1):
                    mdb.models['Model-1'].parts['layer4'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
                    mdb.models['Model-1'].sketches['__profile__'].Line(point1=((defect_info[i][j][0] - 445) * 0.12, (defect_info[i][j][1] - 675) * 0.12), point2=((defect_info[i][j + 1][0] - 445) * 0.12, (defect_info[i][j + 1][1] - 675) * 0.12))
                #s.unsetPrimaryObject()
    mdb.models['Model-1'].parts['layer4'].CutExtrude(flipExtrudeDirection=OFF,sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT, sketchPlane=mdb.models['Model-1'].parts['layer4'].faces[16], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['layer4'].edges[45])
    layer4_porosity = porosity[3]
    print('layer 4 extrude cut finished')
    del mdb.models['Model-1'].sketches['__profile__']   
    return layer4_porosity


# this is the fifth layer
def layer5_update(defect_info):
    for i in range(len(defect_info)):
        for j in range(len(defect_info[i])):
            if j < len(defect[i]) - 1:
                mdb.models['Model-1'].parts['layer5'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=((defect_info[i][j][0] - 445) * 0.12, (defect_info[i][j][1] - 675) * 0.12), point2=((defect_info[i][j + 1][0] - 445) * 0.12, (defect_info[i][j + 1][1] - 675) * 0.12))
    mdb.models['Model-1'].parts['layer5'].CutExtrude(flipExtrudeDirection=OFF, sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT, sketchPlane=mdb.models['Model-1'].parts['layer5'].faces[17], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['layer5'].edges[15])
    del mdb.models['Model-1'].sketches['__profile__']
    layer5_porosity = porosity[4]
    print('layer 5 extrude cut finished')
    return layer5_porosity
    
# this is the sixth layer    
def layer6_update(defect_info):
    for i in range(len(defect_info)):
        for j in range(len(defect_info[i])):
            if j < len(defect_info[i]) - 1:
                mdb.models['Model-1'].parts['layer6'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=((defect_info[i][j][0] - 445) * 0.12, (defect_info[i][j][1] - 675) * 0.12), point2=((defect_info[i][j + 1][0] - 445) * 0.12, (defect_info[i][j + 1][1] - 675) * 0.12))
    mdb.models['Model-1'].parts['layer6'].CutExtrude(flipExtrudeDirection=OFF, sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT, sketchPlane=mdb.models['Model-1'].parts['layer6'].faces[16], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['layer6'].edges[15])
    del mdb.models['Model-1'].sketches['__profile__']
    layer6_porosity = porosity[5]
    print('layer 6 extrude cut finished')
    return layer6_porosity
   

# this is the seventh layer   
def layer7_update(defect_info):
    for i in range(len(defect_info)):
        for j in range(len(defect_info[i])):
            if j < len(defect_info[i]) - 1:
                mdb.models['Model-1'].parts['layer7'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=((defect_info[i][j][0] - 445) * 0.12, (defect_info[i][j][1] - 675) * 0.12), point2=((defect_info[i][j + 1][0] - 445) * 0.12, (defect_info[i][j + 1][1] - 675) * 0.12))
    mdb.models['Model-1'].parts['layer7'].CutExtrude(flipExtrudeDirection=OFF, sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT, sketchPlane=mdb.models['Model-1'].parts['layer7'].faces[16], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['layer7'].edges[15])
    del mdb.models['Model-1'].sketches['__profile__']
    layer7_porosity = porosity[6]
    print('layer 7 extrude cut finished')
    return layer7_porosity
    
# this is the eighth layer    
def layer8_update(defect_info):
    for i in range(len(defect_info)):
        for j in range(len(defect_info[i])):
            if j < len(defect_info[i]) - 1:
                mdb.models['Model-1'].parts['layer8'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=((defect_info[i][j][0] - 445) * 0.12, (defect_info[i][j][1] - 675) * 0.12), point2=((defect_info[i][j + 1][0] - 445) * 0.12, (defect_info[i][j + 1][1] - 675) * 0.12))
    mdb.models['Model-1'].parts['layer8'].CutExtrude(flipExtrudeDirection=OFF, sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT, sketchPlane=mdb.models['Model-1'].parts['layer8'].faces[16], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['layer8'].edges[15])
    del mdb.models['Model-1'].sketches['__profile__']
    layer8_porosity = porosity[7]
    print('layer 8 extrude cut finished')
    return layer8_porosity
    
    
# this is the nineth layer    
def layer9_update(defect_info):
    for i in range(len(defect)):
        for j in range(len(defect_info[i])):
            if j < len(defect_info[i]) - 1:
                mdb.models['Model-1'].parts['layer9'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=((defect_info[i][j][0] - 445) * 0.05, (defect_info[i][j][1] - 675) * 0.12), point2=((defect_info[i][j + 1][0] - 445) * 0.05, (defect_info[i][j + 1][1] - 675) * 0.12))
    mdb.models['Model-1'].parts['layer9'].CutExtrude(flipExtrudeDirection=OFF, sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT, sketchPlane=mdb.models['Model-1'].parts['layer9'].faces[16], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['layer9'].edges[15])
    del mdb.models['Model-1'].sketches['__profile__']
    layer9_porosity = porosity[8]
    print('layer 9 extrude cut finished')
    return layer9_porosity  
#test_img2 = cv2.imread('C:\\Users\\yanzhouf\\Dropbox\\Paper\\Paper_2022\\Fu_Plastic_model_updating\\Data\\Python Code\\3d_printer_fea\\test\\defect1.png',2)

list_of_files = glob.glob('test\pkl_outputs\*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
latestPKL = os.path.basename(latest_file)

#%%
current_layer = latestPKL[0:1]
print('current layer is ' + current_layer)
layers_with_defect = []
layersNO_with_defect = []
porosity = []
# first and bottom always good without defect 
if int(current_layer) == 0 or int(current_layer) == 10:
    print('this is top or bottom without defect')
else:
    for file in list_of_files:
        classifier_file = open(str(file), mode='rb')
        pickledata= pickle.load(classifier_file)
        current_porosity = pickledata[0]
        defect = pickledata[1]
        porosity.append(current_porosity)
        print(len(defect))
       # print(defect)
        if len(defect) == 0:
            print('this layer without defect')
        else:
            layersNO_with_defect.append(int(os.path.basename(file)[0:1]))
            layers_with_defect.append(defect)

            future_porosity = sum(porosity)/len(porosity)
    for i in range(len(layersNO_with_defect)):
        if layersNO_with_defect[i] == 1:
            layer2_update(defect)
        if layersNO_with_defect[i] == 2:
            layer3_update(layers_with_defect[i])
        if layersNO_with_defect[i] == 3:
            layer4_update(layers_with_defect[i])
        if layersNO_with_defect[i] == 4:
            layer5_update(layers_with_defect[i])
        if layersNO_with_defect[i] == 5:
            layer6_update(layers_with_defect[i])
        if layersNO_with_defect[i] == 6:
            layer7_update(layers_with_defect[i])
        if layersNO_with_defect[i] == 7:
            layer8_update(layers_with_defect[i])
        if layersNO_with_defect[i] == 8:
            layer9_update(layers_with_defect[i])
        if layersNO_with_defect[i] == 9:
            layer9_update(layers_with_defect[i])



mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_1-1', 
    part=mdb.models['Model-1'].parts['layer_1'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_2-1', 
    part=mdb.models['Model-1'].parts['layer_2'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_3-1', 
    part=mdb.models['Model-1'].parts['layer_3'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_4-1', 
    part=mdb.models['Model-1'].parts['layer_4'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_5-1', 
    part=mdb.models['Model-1'].parts['layer_5'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_6-1', 
    part=mdb.models['Model-1'].parts['layer_6'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_7-1', 
    part=mdb.models['Model-1'].parts['layer_7'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_8-1', 
    part=mdb.models['Model-1'].parts['layer_8'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_9-1', 
    part=mdb.models['Model-1'].parts['layer_9'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer_10-1', 
    part=mdb.models['Model-1'].parts['layer_10'])
mdb.models['Model-1'].rootAssembly.instances['layer_2-1'].translate(vector=(
    15.4, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.instances['layer_3-1'].translate(vector=(
    30.8, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.instances['layer_4-1'].translate(vector=(
    46.2, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.instances['layer_5-1'].translate(vector=(
    61.6, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.instances['layer_6-1'].translate(vector=(
    77.0, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.instances['layer_7-1'].translate(vector=(
    92.4, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.instances['layer_8-1'].translate(vector=(
    107.8, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.instances['layer_9-1'].translate(vector=(
    123.2, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.instances['layer_10-1'].translate(vector=(
    138.6, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('layer_2-1', ), 
    vector=(-15.4, 0.0, 0.32))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('layer_3-1', ), 
    vector=(-30.8, 0.0, 0.64))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('layer_4-1', ), 
    vector=(-46.2, 0.0, 0.96))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('layer_5-1', ), 
    vector=(-61.6, 0.0, 1.28))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('layer_6-1', ), 
    vector=(-77.0, 0.0, 1.6))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('layer_7-1', ), 
    vector=(-92.4, 0.0, 1.92))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('layer_8-1', ), 
    vector=(-107.8, 0.0, 2.24))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('layer_9-1', ), 
    vector=(-123.2, 0.0, 2.56))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('layer_10-1', ), 
    vector=(-138.6, 0.0, 2.88))
mdb.models['Model-1'].rootAssembly.InstanceFromBooleanMerge(domain=GEOMETRY, 
    instances=(mdb.models['Model-1'].rootAssembly.instances['layer_1-1'], 
    mdb.models['Model-1'].rootAssembly.instances['layer_2-1'], 
    mdb.models['Model-1'].rootAssembly.instances['layer_3-1'], 
    mdb.models['Model-1'].rootAssembly.instances['layer_4-1'], 
    mdb.models['Model-1'].rootAssembly.instances['layer_5-1'], 
    mdb.models['Model-1'].rootAssembly.instances['layer_6-1'], 
    mdb.models['Model-1'].rootAssembly.instances['layer_7-1'], 
    mdb.models['Model-1'].rootAssembly.instances['layer_8-1'], 
    mdb.models['Model-1'].rootAssembly.instances['layer_9-1'], 
    mdb.models['Model-1'].rootAssembly.instances['layer_10-1']), 
    keepIntersections=ON, name='specimen', originalInstances=SUPPRESS)

mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].parts['specimen'].DatumPlaneByPrincipalPlane(offset=40.0, 
    principalPlane=XZPLANE)

mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].parts['specimen'].DatumPlaneByPrincipalPlane(offset=-40.0
    , principalPlane=XZPLANE)



mdb.models['Model-1'].Material(name='pla')
mdb.models['Model-1'].materials['pla'].Density(table=((1.36e-09, ), ))
mdb.models['Model-1'].materials['pla'].Elastic(table=((3600, 0.3), ))
mdb.models['Model-1'].materials['pla'].Plastic(scaleStress=None, table=((17.28, 
    0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 0.0072), (
    34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)

mdb.models['Model-1'].parts['specimen'].Set(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#3ff ]', ), ), name='Set-1')


# Save by YANZHOUF on 2023_06_07-13.57.08; build 2023 2022_09_28-14.11.55 183150
mdb.models['Model-1'].Material(name='pla1')
mdb.models['Model-1'].materials['pla1'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla1'].Elastic(table=((3600, 0.3), ))
mdb.models['Model-1'].materials['pla1'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla1'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla1'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)



if len(porosity) == 0:
    layer2_porosity == 0
else:
    layer2_porosity = sum(porosity)/len(porosity)
    

mdb.models['Model-1'].Material(name='pla2')
mdb.models['Model-1'].materials['pla2'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla2'].Elastic(table=((3600*(74953 - layer2_porosity)/74953, 0.3), ))
mdb.models['Model-1'].materials['pla2'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla2'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla2'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)


if len(porosity) == 0:
    layer3_porosity == 0
else:
    layer3_porosity = sum(porosity)/len(porosity)
    
mdb.models['Model-1'].Material(name='pla3')
mdb.models['Model-1'].materials['pla3'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla3'].Elastic(table=((3600*(74953 - layer3_porosity)/74953, 0.3), ))
mdb.models['Model-1'].materials['pla3'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla3'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla3'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)

if len(porosity) == 0:
    layer4_porosity == 0
else:
    layer4_porosity = sum(porosity)/len(porosity)
    

mdb.models['Model-1'].Material(name='pla4')
mdb.models['Model-1'].materials['pla4'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla4'].Elastic(table=((3600*(74953 - layer4_porosity)/74953, 0.3), ))
mdb.models['Model-1'].materials['pla4'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla4'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla4'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)

if len(porosity) == 0:
    layer5_porosity == 0
else:
    layer5_porosity = sum(porosity)/len(porosity)
    

mdb.models['Model-1'].Material(name='pla5')
mdb.models['Model-1'].materials['pla5'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla5'].Elastic(table=((3600*(74953 - layer5_porosity)/74953, 0.3), ))
mdb.models['Model-1'].materials['pla5'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla5'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla5'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)

if len(porosity) == 0:
    layer6_porosity == 0
else:
    layer6_porosity = sum(porosity)/len(porosity)
    
mdb.models['Model-1'].Material(name='pla6')
mdb.models['Model-1'].materials['pla6'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla6'].Elastic(table=((3600*(74953 - layer6_porosity)/74953, 0.3), ))
mdb.models['Model-1'].materials['pla6'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla6'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla6'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)

if len(porosity) == 0:
    layer7_porosity == 0
else:
    layer7_porosity = sum(porosity)/len(porosity)
    
mdb.models['Model-1'].Material(name='pla7')
mdb.models['Model-1'].materials['pla7'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla7'].Elastic(table=((3600*(74953 - layer7_porosity)/74953, 0.3), ))
mdb.models['Model-1'].materials['pla7'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla7'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla7'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)

if len(porosity) == 0:
    layer8_porosity == 0
else:
    layer8_porosity = sum(porosity)/len(porosity)
    
mdb.models['Model-1'].Material(name='pla8')
mdb.models['Model-1'].materials['pla8'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla8'].Elastic(table=((3600*(74953 - layer8_porosity)/74953, 0.3), ))
mdb.models['Model-1'].materials['pla8'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla8'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla8'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)

if len(porosity) == 0:
    layer9_porosity == 0
else:
    layer9_porosity = sum(porosity)/len(porosity)
    
mdb.models['Model-1'].Material(name='pla9')
mdb.models['Model-1'].materials['pla9'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla9'].Elastic(table=((3600*(74953 - layer9_porosity)/74953, 0.3), ))
mdb.models['Model-1'].materials['pla9'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla9'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla9'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)


mdb.models['Model-1'].Material(name='pla10')
mdb.models['Model-1'].materials['pla10'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla10'].Elastic(table=((3600, 0.3), ))
mdb.models['Model-1'].materials['pla10'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla10'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla10'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)





mdb.models['Model-1'].HomogeneousSolidSection(material='pla1', name='layer1', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='pla2', name='layer2', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='pla3', name='layer3', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='pla4', name='layer4', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='pla5', name='layer5', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='pla6', name='layer6', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='pla7', name='layer7', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='pla8', name='layer8', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='pla9', name='layer9', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='pla10', name='layer10', 
    thickness=None)
mdb.models['Model-1'].parts['layer_1'].Set(cells=
    mdb.models['Model-1'].parts['layer_1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['layer_1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['layer_1'].sets['Set-1'], sectionName='layer1', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['layer_2'].Set(cells=
    mdb.models['Model-1'].parts['layer_2'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['layer_2'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['layer_2'].sets['Set-1'], sectionName='layer2', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['layer_3'].Set(cells=
    mdb.models['Model-1'].parts['layer_3'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['layer_3'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['layer_3'].sets['Set-1'], sectionName='layer3', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['layer_4'].Set(cells=
    mdb.models['Model-1'].parts['layer_4'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['layer_4'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['layer_4'].sets['Set-1'], sectionName='layer4', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['layer_5'].Set(cells=
    mdb.models['Model-1'].parts['layer_5'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['layer_5'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['layer_5'].sets['Set-1'], sectionName='layer5', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['layer_6'].Set(cells=
    mdb.models['Model-1'].parts['layer_6'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['layer_6'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['layer_6'].sets['Set-1'], sectionName='layer6', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['layer_7'].Set(cells=
    mdb.models['Model-1'].parts['layer_7'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['layer_7'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['layer_7'].sets['Set-1'], sectionName='layer7', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['layer_8'].Set(cells=
    mdb.models['Model-1'].parts['layer_8'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['layer_8'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['layer_8'].sets['Set-1'], sectionName='layer8', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['layer_9'].Set(cells=
    mdb.models['Model-1'].parts['layer_9'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['layer_9'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['layer_9'].sets['Set-1'], sectionName='layer9', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['layer_10'].Set(cells=
    mdb.models['Model-1'].parts['layer_10'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['layer_10'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['layer_10'].sets['Set-1'], sectionName=
    'layer10', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].sections['layer1'].setValues(material='pla1', thickness=
    None)
mdb.models['Model-1'].sections['layer2'].setValues(material='pla2', thickness=
    None)
mdb.models['Model-1'].sections['layer3'].setValues(material='pla3', thickness=
    None)
mdb.models['Model-1'].sections['layer4'].setValues(material='pla4', thickness=
    None)
mdb.models['Model-1'].sections['layer5'].setValues(material='pla5', thickness=
    None)
mdb.models['Model-1'].sections['layer6'].setValues(material='pla6', thickness=
    None)
mdb.models['Model-1'].sections['layer7'].setValues(material='pla7', thickness=
    None)
mdb.models['Model-1'].sections['layer8'].setValues(material='pla8', thickness=
    None)
mdb.models['Model-1'].sections['layer9'].setValues(material='pla9', thickness=
    None)
mdb.models['Model-1'].sections['layer10'].setValues(material='pla10', 
    thickness=None)


# mdb.models['Model-1'].parts['specimen'].Set(cells=
#     mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
#     '[#3ff ]', ), ), name='Set-1')
# mdb.models['Model-1'].parts['specimen'].SectionAssignment(offset=0.0, 
#     offsetField='', offsetType=MIDDLE_SURFACE, region=
#     mdb.models['Model-1'].parts['specimen'].sets['Set-1'], sectionName='layer1', 
#     thicknessAssignment=FROM_SECTION)
# mdb.models['Model-1'].rootAssembly.regenerate()
# mdb.models['Model-1'].parts['specimen'].DatumPlaneByPrincipalPlane(offset=-40.0
#     , principalPlane=XZPLANE)

# mdb.models['Model-1'].HomogeneousSolidSection(material='pla1', name='layer1', 
#     thickness=None)
# mdb.models['Model-1'].parts['specimen'].Set(cells=
#     mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
#     '[#3fffffff ]', ), ), name='Set-3')
# mdb.models['Model-1'].parts['specimen'].SectionAssignment(offset=0.0, 
#     offsetField='', offsetType=MIDDLE_SURFACE, region=
#     mdb.models['Model-1'].parts['specimen'].sets['Set-3'], sectionName=
#     'layer1', thicknessAssignment=FROM_SECTION)
# # Save by YANZHOUF on 2023_06_07-14.45.30; build 2023 2022_09_28-14.11.55 183150


mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].ExplicitDynamicsStep(improvedDtMethod=ON, massScaling=((
    SEMI_AUTOMATIC, MODEL, AT_BEGINNING, 0.0, 0.0001, BELOW_MIN, 0, 0, 0.0, 
    0.0, 0, None), ), name='Step-1', previous='Initial')
mdb.models['Model-1'].rootAssembly.Set(cells=
    mdb.models['Model-1'].rootAssembly.instances['specimen-1'].cells.getSequenceFromMask(
    ('[#3ff ]', ), ), name='Set-1')
del mdb.models['Model-1'].parts['specimen'].sets['Set-1']
mdb.models['Model-1'].parts['specimen'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#3ff ]', ), ), datumPlane=
    mdb.models['Model-1'].parts['specimen'].datums[2])

mdb.models['Model-1'].parts['specimen'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#801ff ]', ), ), datumPlane=
    mdb.models['Model-1'].parts['specimen'].datums[3])


mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].rootAssembly.Set(cells=
    mdb.models['Model-1'].rootAssembly.instances['specimen-1'].cells.getSequenceFromMask(
    ('[#801ff ]', ), ), edges=
    mdb.models['Model-1'].rootAssembly.instances['specimen-1'].edges.getSequenceFromMask(
    ('[#80000000 #60c18303 #60c1830 #cc60021c #80cccccc #88888883 #88 ]', ), ), 
    faces=
    mdb.models['Model-1'].rootAssembly.instances['specimen-1'].faces.getSequenceFromMask(
    ('[#92492400 #49280124 #c30e0492 #30c30c30 #420c ]', ), ), name='Set-2', 
    vertices=
    mdb.models['Model-1'].rootAssembly.instances['specimen-1'].vertices.getSequenceFromMask(
    ('[#10c00000 #c1111111 #10aaaa4 ]', ), ))
mdb.models['Model-1'].EncastreBC(createStepName='Initial', localCsys=None, 
    name='FIXED', region=mdb.models['Model-1'].rootAssembly.sets['Set-2'])
mdb.models['Model-1'].TabularAmplitude(data=((0.0, 0.0), (0.1, 0.1), (0.2, 
    0.2), (0.3, 0.3), (0.4, 0.4), (0.5, 0.5), (0.6, 0.6), (0.7, 0.7), (0.8, 
    0.8), (0.9, 0.9), (1.0, 1.0)), name='Amp-1', smooth=SOLVER_DEFAULT, 
    timeSpan=STEP)
mdb.models['Model-1'].rootAssembly.Set(cells=
    mdb.models['Model-1'].rootAssembly.instances['specimen-1'].cells.getSequenceFromMask(
    ('[#3ff00000 ]', ), ), edges=
    mdb.models['Model-1'].rootAssembly.instances['specimen-1'].edges.getSequenceFromMask(
    ('[#0:3 #33800000 #7b333333 #7777777c #177 ]', ), ), faces=
    mdb.models['Model-1'].rootAssembly.instances['specimen-1'].faces.getSequenceFromMask(
    ('[#0 #92500000 #2cb14924 #cb2cb2cb #2cb2 ]', ), ), name='Set-3', vertices=
    mdb.models['Model-1'].rootAssembly.instances['specimen-1'].vertices.getSequenceFromMask(
    ('[#0:2 #fed55558 #7 ]', ), ))
mdb.models['Model-1'].DisplacementBC(amplitude='Amp-1', createStepName='Step-1'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'LOAD', region=mdb.models['Model-1'].rootAssembly.sets['Set-3'], u1=0.0, 
    u2=10.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0)
mdb.models['Model-1'].parts['specimen'].setMeshControls(regions=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#3fffffff ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['specimen'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=1.0)
mdb.models['Model-1'].parts['specimen'].generateMesh()
mdb.models['Model-1'].parts['specimen'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT, elemDeletion=ON, maxDegradation=0.98), ElemType(
    elemCode=C3D6, elemLibrary=EXPLICIT), ElemType(elemCode=C3D4, 
    elemLibrary=EXPLICIT)), regions=(
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#3fffffff ]', ), ), ))
# Save by YANZHOUF on 2023_06_07-14.33.35; build 2023 2022_09_28-14.11.55 183150

mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].rootAssembly.Set(cells=
    mdb.models['Model-1'].rootAssembly.instances['specimen-1'].cells.getSequenceFromMask(
    ('[#7fe00 ]', ), ), name='GAUGERANGE')
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(rebar=EXCLUDE
    , region=mdb.models['Model-1'].rootAssembly.sets['GAUGERANGE'], 
    sectionPoints=DEFAULT, variables=('MISESMAX', ))
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].setValues(rebar=
    EXCLUDE, region=mdb.models['Model-1'].rootAssembly.sets['GAUGERANGE'], 
    sectionPoints=DEFAULT, variables=('U2', 'RF2'))




mdb.models['Model-1'].parts['specimen'].Set(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#20020100 ]', ), ), name='Set-5')
mdb.models['Model-1'].parts['specimen'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['specimen'].sets['Set-5'], sectionName='layer1'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['specimen'].Set(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#1c0000 ]', ), ), name='Set-6')
mdb.models['Model-1'].parts['specimen'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['specimen'].sets['Set-6'], sectionName='layer2'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['specimen'].Set(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#210080 ]', ), ), name='Set-7')
mdb.models['Model-1'].parts['specimen'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['specimen'].sets['Set-7'], sectionName='layer3'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['specimen'].Set(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#408040 ]', ), ), name='Set-8')
mdb.models['Model-1'].parts['specimen'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['specimen'].sets['Set-8'], sectionName='layer4'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['specimen'].Set(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#804020 ]', ), ), name='Set-9')
mdb.models['Model-1'].parts['specimen'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['specimen'].sets['Set-9'], sectionName='layer5'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['specimen'].Set(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#1002010 ]', ), ), name='Set-10')
mdb.models['Model-1'].parts['specimen'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['specimen'].sets['Set-10'], sectionName=
    'layer6', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['specimen'].Set(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#2001008 ]', ), ), name='Set-11')
mdb.models['Model-1'].parts['specimen'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['specimen'].sets['Set-11'], sectionName=
    'layer7', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['specimen'].Set(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#4000804 ]', ), ), name='Set-12')
mdb.models['Model-1'].parts['specimen'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['specimen'].sets['Set-12'], sectionName=
    'layer8', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['specimen'].Set(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#8000402 ]', ), ), name='Set-13')
mdb.models['Model-1'].parts['specimen'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['specimen'].sets['Set-13'], sectionName=
    'layer9', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['specimen'].Set(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#10000201 ]', ), ), name='Set-14')
mdb.models['Model-1'].parts['specimen'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['specimen'].sets['Set-14'], sectionName=
    'layer10', thicknessAssignment=FROM_SECTION)

mdb.models['Model-1'].parts['specimen'].Set(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#3ff00000 ]', ), ), name='load_set')
mdb.models['Model-1'].parts['specimen'].Set(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#401ff ]', ), ), name='fixed_set')
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].boundaryConditions['FIXED'].setValues(region=
    mdb.models['Model-1'].rootAssembly.instances['specimen-1'].sets['fixed_set'])
mdb.models['Model-1'].boundaryConditions['LOAD'].setValues(region=
    mdb.models['Model-1'].rootAssembly.instances['specimen-1'].sets['load_set'])

mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].parts['specimen'].Set(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#bfe00 ]', ), ), name='out_gauge')
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(region=
    mdb.models['Model-1'].rootAssembly.allInstances['specimen-1'].sets['out_gauge'])
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].setValues(region=
    mdb.models['Model-1'].rootAssembly.allInstances['specimen-1'].sets['out_gauge'])


mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['Job-1'].submit(consistencyChecking=OFF, datacheckJob=False)
mdb.Job(activateLoadBalancing=False, atTime=None, contactPrint=OFF, 
    description='', echoPrint=OFF, explicitPrecision=SINGLE, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job-1', nodalOutputPrecision=
    SINGLE, numCpus=4, numDomains=4, numThreadsPerMpiProcess=1, queue=None, 
    resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine='', waitHours=
    0, waitMinutes=0)
    
    
mdb.models['Model-1'].Material(name='pla')
mdb.models['Model-1'].materials['pla'].Density(table=((1.36e-09, ), ))
mdb.models['Model-1'].materials['pla'].Elastic(table=((3600, 0.3), ))
mdb.models['Model-1'].materials['pla'].Plastic(scaleStress=None, table=((17.28, 
    0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 0.0072), (
    34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)

mdb.models['Model-1'].parts['specimen'].Set(cells=
    mdb.models['Model-1'].parts['specimen'].cells.getSequenceFromMask((
    '[#3ff ]', ), ), name='Set-1')


# Save by YANZHOUF on 2023_06_07-13.57.08; build 2023 2022_09_28-14.11.55 183150
mdb.models['Model-1'].Material(name='pla2')
mdb.models['Model-1'].materials['pla2'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla2'].Elastic(table=((3600, 0.3), ))
mdb.models['Model-1'].materials['pla2'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla2'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla2'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)
	
	# Save by YANZHOUF on 2023_06_07-13.57.08; build 2023 2022_09_28-14.11.55 183150
mdb.models['Model-1'].Material(name='pla3')
mdb.models['Model-1'].materials['pla3'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla3'].Elastic(table=((3600, 0.3), ))
mdb.models['Model-1'].materials['pla3'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla3'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla3'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)
	
	# Save by YANZHOUF on 2023_06_07-13.57.08; build 2023 2022_09_28-14.11.55 183150
mdb.models['Model-1'].Material(name='pla4')
mdb.models['Model-1'].materials['pla4'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla4'].Elastic(table=((3600, 0.3), ))
mdb.models['Model-1'].materials['pla4'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla4'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla4'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)
	
	# Save by YANZHOUF on 2023_06_07-13.57.08; build 2023 2022_09_28-14.11.55 183150
mdb.models['Model-1'].Material(name='pla5')
mdb.models['Model-1'].materials['pla5'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla5'].Elastic(table=((3600, 0.3), ))
mdb.models['Model-1'].materials['pla5'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla5'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla5'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)
	
	# Save by YANZHOUF on 2023_06_07-13.57.08; build 2023 2022_09_28-14.11.55 183150
mdb.models['Model-1'].Material(name='pla6')
mdb.models['Model-1'].materials['pla6'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla6'].Elastic(table=((3600, 0.3), ))
mdb.models['Model-1'].materials['pla6'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla6'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla6'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)
	

		# Save by YANZHOUF on 2023_06_07-13.57.08; build 2023 2022_09_28-14.11.55 183150
mdb.models['Model-1'].Material(name='pla7')
mdb.models['Model-1'].materials['pla7'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla7'].Elastic(table=((3600, 0.3), ))
mdb.models['Model-1'].materials['pla7'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla7'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla7'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)
	
		# Save by YANZHOUF on 2023_06_07-13.57.08; build 2023 2022_09_28-14.11.55 183150
mdb.models['Model-1'].Material(name='pla8')
mdb.models['Model-1'].materials['pla8'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla8'].Elastic(table=((3600, 0.3), ))
mdb.models['Model-1'].materials['pla8'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla8'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla8'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)
	
		# Save by YANZHOUF on 2023_06_07-13.57.08; build 2023 2022_09_28-14.11.55 183150
mdb.models['Model-1'].Material(name='pla9')
mdb.models['Model-1'].materials['pla9'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla9'].Elastic(table=((3600, 0.3), ))
mdb.models['Model-1'].materials['pla9'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla9'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla9'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)
	
		# Save by YANZHOUF on 2023_06_07-13.57.08; build 2023 2022_09_28-14.11.55 183150
mdb.models['Model-1'].Material(name='pla10')
mdb.models['Model-1'].materials['pla10'].Density(table=((1.36e-09, ), ))
# 74953 is the total specimen area, this equation calcuated the porosity realted Young's modulous
mdb.models['Model-1'].materials['pla10'].Elastic(table=((3600, 0.3), ))
mdb.models['Model-1'].materials['pla10'].Plastic(scaleStress=None, table=((
    17.28, 0.0), (19.44, 0.0054), (21.81, 0.006), (23.76, 0.0066), (25.69, 
    0.0072), (34.5, 0.0102), (45.43, 0.015), (47.09, 0.0162)))
mdb.models['Model-1'].materials['pla10'].DuctileDamageInitiation(table=((0.25, 
    1.35, 1.0), ))
mdb.models['Model-1'].materials['pla10'].ductileDamageInitiation.DamageEvolution(
    table=((0.05, ), ), type=DISPLACEMENT)