#This code gets and returns the parametes for a given case. Reads what is necessary then calculates the rest.

import f90nml #need to figure out problem of always executing nml setup code before each run
nml=f90nml.read('C:/Users/cjkri/Desktop/nml Code/Parameters.nml') #reads the file at a given path
#nml['Parameters_nml']['Variable Name'] general structure for indexing items in nml
nysegments=nml['Parameters_nml']['nysegments'] #pull all the variables that should be stored in the case specific nml file
nxsegments=nml['Parameters_nml']['nxsegments'] #all of the values are stored, defining these variables simply makes calling them later easier
nacross=nml['Parameters_nml']['nacross']
ndown=nml['Parameters_nml']['ndown']
nxstart=nml['Parameters_nml']['nxstart']
ny1start=nml['Parameters_nml']['ny1start']
ny2start = ny1start+ndown 

pA=nml['Parameters_nml']['pA']
pB=nml['Parameters_nml']['pB']
pC=nml['Parameters_nml']['pC']
pD=nml['Parameters_nml']['pD']

nx1list = []; nx2list = []
ny1list = []; ny2list = []

for ix in range(nxsegments):
    nx1start = nxstart+ix*nacross; nx2start = nxstart+(ix+1)*nacross 
    for i in range(nysegments):
        nx1list.append(nx1start); nx2list.append(nx2start)
        ny1list.append(ny1start+i*ndown); ny2list.append(ny2start+i*ndown)
nsegments = nxsegments*nysegments

#print(str(nx1list) +'\n'+str(ny1list)) this line used to check values
