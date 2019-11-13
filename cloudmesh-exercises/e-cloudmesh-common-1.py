# fa19-516-172: Cloudmesh Common
# E.Cloudmesh.Common.1
# Develop a program that demonstrates the use of BANNER, HEADING, and VERBOSE.

from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.variables import Variables
from cloudmesh.common.debug import VERBOSE

# BANNER Example
banner("Cloudmesh Banner", label='Cloudmesh Assignment 1')

# HEADING Example
HEADING("This exercise is saved in file E.Cloudmesh.Common.1")

# VERBOSE Example
variables = Variables()
variables['verbose'] = 10
verboseExample = {"a": "apple", "b": "ball", "c": "cat"}
VERBOSE(verboseExample)