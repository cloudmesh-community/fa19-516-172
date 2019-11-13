# fa19-516-172: Cloudmesh Common
# E.Cloudmesh.Common.4
# Develop a program that demonstrates the use of cloudmesh.common.Shell .

from cloudmesh.common.Shell import Shell
result = Shell.execute('pwd')
print(result)

result = Shell.execute('ls')
print(result)

result = Shell.execute('ls', ["-l", "-a"])
print(result)