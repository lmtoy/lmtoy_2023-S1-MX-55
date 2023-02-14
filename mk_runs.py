#! /usr/bin/env python
#
#   script generator for project="2021-S1-US-3"
#
#   lmtinfo.py grep US-3 Science Map | awk '{print $2}' | sort


import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy)
    from lmtoy import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2023-S1-MX-55"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["3CR234.0"] = [ 105304, 105305, 105306, 105308, 105309, 105310, 105312, 105313,
                   105314, 105316, 105317, 105318,                                  # 10-feb
                   105408, 105409, 105410,]                                         # 14-feb


on["3CR287.1"] = [ 105324, 105325, 105326, 105328, 105329, 105330, 105332, 105333,
                   105334, 105336, 105337, 105338,]                                  # 10-feb


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["3CR234.0"] = ""
pars1["3CR287.1"] = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["3CR234.0"] = "srdp=1 admit=0"
pars2["3CR287.1"] = "srdp=1 admit=0"


runs.mk_runs(project, on, pars1, pars2)
