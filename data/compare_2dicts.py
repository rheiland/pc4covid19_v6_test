import sys
from xml2py import *
from deepdiff import DeepDiff

print("len(sys.argv)= ",len(sys.argv))
if len(sys.argv) < 3:
    print("Usage: <xml-file1> <xml-file2>")
    sys.exit(1)

c1 = sys.argv[1] 
c2 = sys.argv[2] 

#d1 = dict_load("flat.xml")
#d2 = dict_load("baseline_v6_src.xml")
#d1 = dict_load("config/PhysiCell_settings.xml")
#c1 = "baseline.xml"
#c2 = "output_S000000_R00/config.xml"
#c2 = "fix11_output_S000000_R00/config.xml"
print("new: ",c2)
print("old: ",c1)
d1 = dict_load(c1)
d2 = dict_load(c2)
if d1 == d2:
  print("dicts are equal!")
else:
  print("dicts are NOT equal!")
#print(d.keys())
diff = DeepDiff(d1, d2)
# print(diff)
# print("---------------\n")
print(DeepDiff(d1,d2).pretty())

#---------
# d = {"a": 3, "b": 2}
# d1 = {"a": 2, "b": 3}
# res = all((d1.get(k) == v for k, v in d.items()))
#print(res)
#--------
# a = {'Name': 'asif', 'Age': 5}
# b = {'Name': 'lalita', 'Age': 78}
# diff = DeepDiff(a, b)
#print(diff)
