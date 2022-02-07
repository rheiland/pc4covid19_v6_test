#
# Goal: copy "uptake_rate" param values from file2's XML to file1's XML
#
# Usage: 
#   $ python flatten_simple.p
# Output:
#   simple.xml  (= file1.xml, but with the "uptake_rate" valuess from file2.xml) 
#
# rf. https://docs.python.org/3.7/library/xml.etree.elementtree.html
#
"""
<file1>
<secretion>
  <substrate name="sub1">
    <uptake_rate>0</uptake_rate>
  </substrate>
  <substrate name="sub2">
    <uptake_rate>0</uptake_rate>
  </substrate>
</secretion>
</file1>
--------------
<file2>
<secretion>
  <substrate name="sub1">
    <uptake_rate>41</uptake_rate>
  </substrate>
  <substrate name="sub2">
    <uptake_rate>42</uptake_rate>
  </substrate>
</secretion>
</file2>
"""
import xml.etree.ElementTree as ET
import sys
tree1 = ET.parse("file1.xml")  
xml_root1 = tree1.getroot()
tree2 = ET.parse("file2.xml")  
xml_root2 = tree2.getroot()
def update_all_substrate_params(xmlpath, save_param_val, substrate_name_in):
        # for elm in xml_root1.findall('secretion//substrate'):
        print("*** ENTER: update_all_substrate_params: substrate_name (param) = ",substrate_name_in)
        for elm in xml_root1.findall('secretion'):
            for elm_sub in elm.findall('substrate'):
                substrate_name = elm_sub.attrib["name"]
                print('  *-- elm_sub ',elm_sub, ", name=",substrate_name)
                if (substrate_name_in != substrate_name):
                    print("   THIS IS NOT THE DROID YOU'RE LOOKING FOR")
                    continue
                print('   -- update ',elm, ', xmlpath=',xmlpath, ", save_param_val=",save_param_val)
                # if "secretion//substrate" in xmlpath:
                if "substrate//uptake_rate" in xmlpath:
                    print("   =======  need special handling of secretion//substrate//uptake_rate  for ", substrate_name_in)
                    if "uptake_rate" in xmlpath[-13:]:
                        print("\n   =======     handle uptake_rate")
                        print("   =======     xmlpath[:-13]",xmlpath[:-13] )
                        print("   =======     substrate_name as param= ",substrate_name_in )
                        if (substrate_name == substrate_name_in):
                            print("   WEEEEEEEEEEEEE!!! match found")
                            print('   xmlpath=',xmlpath)
                            # elm.find('.'+xmlpath).text = save_param_val   # FINALLY, update the value
                            # elm_sub.find('.'+xmlpath).text = save_param_val   # FINALLY, update the value
                            elm_sub.find('.'+'//uptake_rate').text = save_param_val   # FINALLY, update the value
                            break
        print("*** EXIT ")

def recurse_node(root,xmlpath,substrate_name):
    global save_param_val
    xmlpath = xmlpath + "//" + root.tag[root.tag.rfind('}')+1:]
    param_val = ''
    # substrate_name = ""
    if (root.tag == "substrate") and (len(root.attrib) > 0):   # don't want substrate for chemotaxis, just secretion
        print("recurse_node: ========>> found substrate (for secretion), attrib=",root.attrib)
        substrate_name = root.attrib["name"]
        print("recurse_node: ========>> substrate_name =",substrate_name ,"\n")
    for child in root:
        param_val = ' '.join(child.text.split())
        if param_val != '':
            # print('param value=',param_val, ' for ',end='')
            save_param_val = param_val
            # uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float27.value)
        recurse_node(child,xmlpath,substrate_name)
    if len(list(root)) == 0:  # we are finally at the bottom of the recursion; the element of interest.
        # e.g.  //phenotype//motility//options//chemotaxis//direction  =  1
        #       //phenotype//secretion//substrate//uptake_rate  =  0.01    (WRONG - also need to know substrate *name*)
        # print(xmlpath)
        print(">END of recurse_node: xmlpath=", xmlpath,' = ',save_param_val)
        update_all_substrate_params(xmlpath, save_param_val, substrate_name)
#tree_orig = ET.parse("PhysiCell_settings.xml")  
#xml_orig = tree_orig.getroot()
uep = None
# for uptake_rate param values in file2, copy them into file1
# for elm in xml_orig.findall('cell_definitions//cell_definition'):
# for elm in xml_root2.findall('secretion//substrate'):
for elm in xml_root2.findall('secretion'):
    print("in xml_root2, found elm = ",elm)
    # idx += 1
    if True: #  cd.attrib["name"] == "immune":  # we only want the "immune" cell def
        # uep = elm
        # print("---------------- processing immune cell_def at idx= ",idx)   # 2  (0=default, 1=lung epi)
        for child in elm:
            if child.tag != 'custom_data':
                print("\nINVOKING recurse_node on child=",child)
                if child.tag == "substrate":
                    print('   substrate name=',child.attrib["name"])
                recurse_node(child,"","") 
print("\nDone.")
new_xml_file = "simple.xml"
tree1.write(new_xml_file)
print("---> wrote ",new_xml_file)