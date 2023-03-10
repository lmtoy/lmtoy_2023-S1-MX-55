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
on["3CR123.0"] = [ 106007, 106008, 106009, 106011, 106012, 106013, 106015, 106016,
                   106017, 106019, 106020, 106021,                                 # feb 18
                   106163,]                                                        # feb 19

on["3CR135.0"] = [ 106524, 106525, 106526, 106528, 106529, 106530, 106532, 106533,  # mar 8
                   106534,]

on["3CR219.0"] = [ 106691, 106692, 106693, 106695, 106696, 106697, 106699, 106700,
                   106701, 106705, 106706, 106707,]                                 # mar 11/12

on["3CR234.0"] = [ 105304, 105305, 105306, 105308, 105309, 105310, 105312, 105313,
                   105314, 105316, 105317, 105318,                                  # 10-feb
                   105408, 105409, 105410,]                                         # 14-feb

on["3CR236.0"] = [ 106727, 106728, 106729, 106731, 106732, 106733, 106735, 106736,
                   106737, 106739, 106740, 106741,]                                 # mar 11/12

on["3CR287.1"] = [ 105324, 105325, 105326, 105328, 105329, 105330, 105332, 105333,
                   105334, 105336, 105337, 105338,]                                  # 10-feb

on["3CR349.0"] = [ 106884, 106885, 106886, 106888, 106889, 106890, 106892,
                   106893, 106894,]                                                 # mar 11/12


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["3CR123.0"] = ""   # strong continuum
pars1["3CR135.0"] = ""
pars1["3CR219.0"] = ""
pars1["3CR234.0"] = ""   # ok
pars1["3CR236.0"] = ""  
pars1["3CR287.1"] = ""   # strong continuum
pars1["3CR349.0"] = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["3CR123.0"] = "srdp=1 admit=0"
pars2["3CR135.0"] = "srdp=1 admit=0"
pars2["3CR219.0"] = "srdp=1 admit=0"
pars2["3CR234.0"] = "srdp=1 admit=0"
pars2["3CR236.0"] = "srdp=1 admit=0"
pars2["3CR287.1"] = "srdp=1 admit=0"
pars2["3CR349.0"] = "srdp=1 admit=0"


runs.mk_runs(project, on, pars1, pars2)
