# 2023-S1-MX-55

this project has a number of strong cont sources and need a badlags flag to
ignore the variations in the first 32 lags.

Here's a rough account of sources and slopes of the continuum, unless otherwise
noted, their slopes are all such that flux is less at highest frequency.


     source     cont?    flux (mK)    comments

     3CR123.0   strong   20 - 80
     3CR135.0   weak     0.5 - 2
     3CR219.0   strong   15 - 25      mismatching bands
     3CR234.0   weak     1.5          flat
     3CR236.0   strong   20 - 60
     3CR287.1   strong   50 - 100
     3CR303.0   strong   50 - 90
     3CR319.0   none?    -0.5 - 0.5
     3CR332.0   weak     1.5          varying
     3CR349.0   weak     0.5 - 2.5
     3CR357.0   weak     2 - 5 
     3CR381.0   weak     1   - 2
     3CR401.0   strong   10 - 24
     3CR436.0   weak     4-6          varying
     3CR459.0   strong   8 - 20

QA notes: Many obsnums are techincally QAFAILS due to RMS > 1.4. However, due to the continuum contamination in most of the sources, I have ignored this RMS cutoff; the sources marked as QAFAILS are bad regardless of RMS.        
