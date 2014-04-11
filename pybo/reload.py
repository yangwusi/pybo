# This is a stupid workaround for crappy deep-reload behavior in python. While
# developing I often want to reload the entire package I'm working on... so if
# fnames contains a depth-first traversal of the modules contained in the
# package this will import and reload all of them.

fnames = """
pybo.utils.ldsample
pybo.utils
pybo.models.functions
pybo.models
pybo.policies._base
pybo.policies.gpopt._base
pybo.policies.gpopt.gpei
pybo.policies.gpopt.gppi
pybo.policies.gpopt.gpucb
pybo.policies.gpopt
pybo.policies
pybo
""".split()

import importlib

for fname in list(reversed(fnames)) + fnames:
    module = importlib.import_module(fname)
    reload(module)