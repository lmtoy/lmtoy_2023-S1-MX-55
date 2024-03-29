#! /usr/bin/env python
#
# 2023-S1-MX-55 covering spring 2023

import os
import sys

from lmtoy import runs

project="2023-S1-MX-55"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["3CR123.0"] = [ 106007, 106008, 106009, 106011, 106012, 106013, 106015, 106016,
                   106017, 106019, 106020, 106021,                                 # feb 18 
                   106163,]                                                        # feb 19

on["3CR135.0"] = [ 106524, 106525, 106526, 106528, 106529, 106530, 106532, 106533,  # mar 8
                   106534,
                   107292, 107293, 107294, 107297, 107298, 107299,]                 # mar 23/24

on["3CR219.0"] = [ 106691, 106692, 106693, 106695, 106696, 106697, 106699, 106700,
                   106701, 106705, 106706, 106707,]                                 # mar 11/12

on["3CR234.0"] = [ 105304, 105305, 105306, 105308, 105309, 105310, 105312, 105313,
                   105314, 105316, 105317, 105318,                                  # 10-feb
                   105408, 105409, 105410,]                                         # 14-feb

on["3CR236.0"] = [ 106727, 106728, 106729, 106731, 106732, 106733, 106735, 106736,
                   106737, 106739, 106740, 106741,]                                 # mar 11/12

on["3CR287.1"] = [ -105324, -105325, -105326, -105328, -105329, -105330, 105332, 105333,
                   105334, 105336, 105337, 105338,]                                  # 10-feb

on["3CR303.0"] = [ 107409, 107410, 107411, 107413, 107414, 107415, 107417, 107418,
                   107419, 107422, 107423, 107424,]                                  # mar 28

on["3CR319.0"] =  [ 107427, 107428, 107429, 107431, 107432, 107433, 107436, 107437,
                    107438, 107440, 107441, 107442,]                                # mar 28

on["3CR332.0"] =  [ 108952, 108953, 108954, 108956, 108957, 108958, 108960, 108961,
                    108962, 108965, 108966, 108967,]                               # apr 27

on["3CR349.0"] = [ 106884, 106885, 106886, 106888, 106889, 106890, 106892,
                   106893, 106894,                                                 # mar 11/12
                   106974, 106975, 106976, 106979, 106980, 106981,]                # mar 21

on["3CR357.0"] =  [ 106984, 106985, 106986, 106989, 106990, 106991,               # mar 21
                    107126, 107127, 107128, 107131, 107132, 107133, 107136,]      # mar 22

on["3CR381.0"] =  [ 107445, 107446, 107447, 107449, 107450, 107451, 107454,
                    107455, 107456, 107458, 107459, 107460,                       # mar 28
                    108844, 108845, 108846, 108848, 108849, 108850,]              # apr 26


on["3CR401.0"] =  [ 106994, 106995, 106996, 106999, 107000, 107001,               # mar 21
                    107139, 107140, 107141, 107144, 107145, 107146, 107149,]      # mar 22

on["3CR436.0"] =  [ 108865, 108866, 108867, 108869, 108870, 108871, 108873,
                    108874, 108875,                                               # apr 26
                    109084, 109085, 109086,]                                      # apr 28

on["3CR459.0"] =  [ 109093, 109094, 109095,                                       # apr 28
                    109214, 109215, 109216,]                                      # may 2 




#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["3CR123.0"] = "shortlags=32,15.0 badcb=0/2,3/3"   # strong continuum
pars1["3CR135.0"] = "badcb=3/4"   # ok
pars1["3CR219.0"] = "shortlags=32,15.0 badcb=3/3"   # continuum *DS*
pars1["3CR234.0"] = "badcb=3/3"   # ok
pars1["3CR236.0"] = "shortlags=32,15.0 badcb=2/3,3/3,0/2,3/4"   # strong continuum
pars1["3CR287.1"] = "shortlags=32,15.0"   # strong continuum [bench 105323-105325]
pars1["3CR303.0"] = "shortlags=32,15.0 badcb=2/3,3/4"   # strong continuum
pars1["3CR319.0"] = "badcb=3/4"   # ok
pars1["3CR332.0"] = "shortlags=32,10.0"   # weak continuum *DS*
pars1["3CR349.0"] = "shortlags=32,10.0 badcb=3/3,3/4"   # weak 
pars1["3CR357.0"] = "shortlags=32,10.0"   # weak 
pars1["3CR381.0"] = "shortlags=32,10.0 badcb=3/4"   # weak 
pars1["3CR401.0"] = "shortlags=32,15.0 badcb=3/3"   # continuum *DS*
pars1["3CR436.0"] = "shortlags=32,10.0 badcb=3/3"   # weak continuum *DS*
pars1["3CR459.0"] = "shortlags=32,15.0"   # continuum *DS*

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["3CR123.0"] = "srdp=1 admit=0"
pars2["3CR135.0"] = "srdp=1 admit=0"
pars2["3CR219.0"] = "srdp=1 admit=0"
pars2["3CR234.0"] = "srdp=1 admit=0"
pars2["3CR236.0"] = "srdp=1 admit=0"
pars2["3CR287.1"] = "srdp=1 admit=0"
pars2["3CR303.0"] = "srdp=1 admit=0"
pars2["3CR319.0"] = "srdp=1 admit=0"
pars2["3CR332.0"] = "srdp=1 admit=0"
pars2["3CR349.0"] = "srdp=1 admit=0"
pars2["3CR357.0"] = "srdp=1 admit=0"
pars2["3CR381.0"] = "srdp=1 admit=0"
pars2["3CR401.0"] = "srdp=1 admit=0"
pars2["3CR436.0"] = "srdp=1 admit=0"
pars2["3CR459.0"] = "srdp=1 admit=0"

# Found 15 sources

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
