# Author：Steve

import xml.etree.ElementTree as ET

tree = ET.parse("_8xml_mod.xml")
root = tree.getroot()

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1  # node.text为string， 所以要转为int()
    node.text = str(new_year)
    node.set("updated", "yes")  # 给year加属性updated='yes'

tree.write("_8xml_mod.xml")

# 删除node
for country in root.findall('country'):  # 用root.findall('country')来找所有country的属性
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)  # 移除
tree.write('_8xml_mod_rmRank.xml')