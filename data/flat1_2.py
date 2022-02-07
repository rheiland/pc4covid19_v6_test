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
</file1

<file2>
<secretion>
  <substrate name="sub1">
    <uptake_rate>1</uptake_rate>
  </substrate>
  <substrate name="sub2">
    <uptake_rate>2</uptake_rate>
  </substrate>
</secretion>
</file2>
"""
import xml.etree.ElementTree as ET

tree1 = ET.parse("file1.xml")  
xml_root1 = tree1.getroot()

tree2 = ET.parse("file2.xml")  
xml_root2 = tree2.getroot()
