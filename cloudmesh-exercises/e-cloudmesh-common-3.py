# fa19-516-172: Cloudmesh Common
# E.Cloudmesh.Common.3
# Develop a program that demonstrates the use of FlatDict .

from cloudmesh.common.FlatDict import FlatDict

data = {
    "name" : "Nayeem",
    "address": {
    "city" : "Bloomington",
    "state" : "IN"
}
}
flat = FlatDict(data, sep =".")
print(flat)