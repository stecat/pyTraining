# Author：Steve

import xml.etree.ElementTree as ET

new_xml = ET.Element("personInfolist")  # 根节点
personInfo = ET.SubElement(new_xml, "personInfo", attrib={"enrolled": "yes"})  # 二级子节点
age = ET.SubElement(personInfo, "age", attrib={"checked": "no"})  # 三级子节点，personInfo的子节点
sex = ET.SubElement(personInfo, "sex")  # 三级子节点，personInfo的子节点
age.text = '33'

personInfo2 = ET.SubElement(new_xml, "personInfo2", attrib={"enrolled": "yes"})
age = ET.SubElement(personInfo2, "age", attrib={"checked": "no"})
age.text = '22'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("_8xml_mod1_Create_personInfolist.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式
