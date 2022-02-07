import xml.etree.ElementTree as ET
import sys

#tree = ET.parse('nanobio_settings.xml')
#tree = ET.parse('test1.xml')
#tree = ET.parse('/Users/heiland/git/mcds2isa/HUVEC/HUVEC_v4_SHF_test.xml')
tree = ET.parse('PhysiCell_settings-v4-inherit.xml')
root = tree.getroot()

num_nodes = 0
#for node in root.iter():
for node in []:
  print(node)
  num_nodes += 1
print("num_nodes=",num_nodes)

print('----- recursive -----')
prefix = ""
mypath = ""
def print_children(parent):
  global prefix, mypath
  for child in parent:
    print(prefix,child.tag)
    text = ' '.join(child.text.split())
    if text != '':
        print(mypath + '//' + child.tag)
        print("  --> value=",text)
    else:
        mypath += '//' + child.tag
    # if child.tag == 'cell_definition':
        # sys.exit(1)
    prefix = prefix + "--"
    print_children(child)
#  prefix = prefix - "--"
  prefix = prefix[2:]

#print_children(root)
#		<cell_definition name="immune" parent_type="default" ID="2">
#uep = root.find('.//cell_definitions')
uep = root.find('.//cell_definitions//cell_definition')
#print_children(uep)

for cell_def in root.iter('cell_definition'):
    print(cell_def.attrib)
    if cell_def.attrib['name'] == 'immune':
        if len(list(cell_def)) > 0: 
            mypath = ""
            print_children(cell_def)
            # for child in cell_def: 
                # print(child)
            break

# sys.exit(1)

print('-----------------------')
print('-----------------------')
# for child in root:
#   print(child.tag)
#   for child2 in child:
#     print('--',child2.tag)
#     for child3 in child2:
#       print('----',child3.tag)
#       for child4 in child3:
#         print('------',child4.tag)
#  print(child.tag, child.attrib)


def parseXML(root,sm):
    sm = sm + "/" + root.tag[root.tag.rfind('}')+1:]
    for child in root:
      parseXML(child,sm)
    if len(list(root)) == 0:
      print(sm)

parseXML(root,"")
#uep = root.find('.//cell_definitions//cell_definition')