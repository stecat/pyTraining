# Author：Steve
# xml模块
import xml.etree.ElementTree as ET

tree = ET.parse("_8xml_mod.xml")  # 读xlm文件
root = tree.getroot()  # 找到root节点
print(root)
print(root.tag)

# 遍历xml文档
for child in root:
    # child.tag是对应xml的标签country， child.attrib为name="Liechtenstein"属性-->（<country name="Liechtenstein">）
    print(child.tag, child.attrib)
    for i in child:
        # i.tag是对应rank，i.attrib为updated="yes"，i.text为2--->（<rank updated="yes">2</rank>）
        print(i.tag, i.attrib, i.text)
        # 其中neighbor有自结束标签'/'，没有具体text内容---> (<neighbor name="Austria" direction="E"/>)

# 只遍历year节点, root.iter(tagName)
for node in root.iter('year'):
    print(node.tag, node.text)
