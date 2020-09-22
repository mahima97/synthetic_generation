import cv2
import xml.etree.ElementTree as ET
import os

source = 'output_dir/annotations'
destination = 'output_dir/labels'

if not os.path.exists('destination'):
    os.mkdir(destination)

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    w = box[2]-box[0]
    h = box[3]-box[1]
    x = (box[0] + w+box[0])/2.0
    y = (box[1] + h+box[1])/2.0


    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


Label = open('obj.names','r').read().split('\n')
print(Label)

for file in os.listdir(source):
    print(os.path.join("output_dir/images",file.replace('.xml', '_none.jpg')))
    img = cv2.imread(os.path.join("output_dir/images",file.replace('.xml', '_none.jpg')))
    H, W, C = img.shape
    tree = ET.parse(os.path.join(source,file))
    root = tree.getroot()
    yolo_file = open(os.path.join(destination,file.replace('.xml', '_none.txt')),'w+')
    for member in root.findall('object'):
        class_name = member[0].text
        value = (
                 int(member[1][0].text),
                 int(member[1][2].text),
                 int(member[1][1].text),
                 int(member[1][3].text)
                 )

        x,y,w,h = convert([W,H], value)
        c = Label.index(class_name)
        fmt='{} {} {} {} {}\n'.format(c,x,y,w,h)
        print(fmt)
        yolo_file.write(fmt)

        # xml_list.append(value)
        # cv2.putText(img, fname,(value[0],value[2]-5) , cv2.FONT_HERSHEY_SIMPLEX ,1, (0,255,0), 1, cv2.LINE_AA) 
        # cv2.rectangle(img, (value[0],value[2]), (value[1], value[3]), (0,255,0), 2) #change (0,0,0) to whatever color you want
        # print(value)
       # classes_names.append((member[0].text)


    # cv2.imwrite('exp123.jpg', img)