import cv2
import xml.etree.ElementTree as ET




img = cv2.imread("output_dir/images/123_none.jpg")
tree = ET.parse("output_dir/annotations/123.xml")
root = tree.getroot()
for member in root.findall('object'):
    fname = member[0].text
    value = (
             int(member[1][0].text),
             int(member[1][1].text),
             int(member[1][2].text),
             int(member[1][3].text)
             )
    # xml_list.append(value)
    cv2.putText(img, fname,(value[0],value[2]-5) , cv2.FONT_HERSHEY_SIMPLEX ,1, (0,255,0), 1, cv2.LINE_AA) 
    cv2.rectangle(img, (value[0],value[2]), (value[1], value[3]), (0,255,0), 2) #change (0,0,0) to whatever color you want
    print(value)
   # classes_names.append((member[0].text)


cv2.imwrite('exp123.jpg', img)