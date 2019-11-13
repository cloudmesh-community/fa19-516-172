# E.Cloudmesh.Shell.1
# Install cmd5 and the command cms on your computer.

from cloudmesh.common.Shell import Shell

commandResult = Shell.execute('cms', 'help')
print(commandResult)