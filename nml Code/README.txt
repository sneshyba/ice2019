The nml code is a replacement to the chaing of if/elif statements currently
in Bscatter_retreive. The Parameter.nml file can be edited to contain the 
variables for each specific case and will be included in that case folder.
That path can be put in the python code which will retreive the values and
rename them so they fit into the existing code. It then calculates the values
that are needed but are directly entered into the nml file.
The module 'f90nml' is what allows us to use the namelist objects, and it 
should come preinstalled with pip, but I was unable to find it on my machine
nor could I find a useful way to download the module from pythons library.
I cloned a respository off of GitHub that had it and was able to get that to
run. 
***But, I have to run the setup file from that GitHub repository each time
I want to import f90nml, I don't know how to get around that. As far as I
know, everything else works.

nml formatting notes are in the nml file