# fa19-516-172: Cloudmesh Common
# E.Cloudmesh.Common.2
# Develop a program that demonstrates the use of dotdict.

from cloudmesh.common.dotdict import dotdict

# dotdict Example
data = {
"name": "Nayeem"
}
datadot = dotdict(data)

if datadot.name is "Nayeem":
    print("datadot.name is Nayeem")

if data["name"] is "Nayeem":
    print("data['name'] is Nayeem")