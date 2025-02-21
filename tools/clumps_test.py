import chivolib.workspace as ws
import chivolib.clumps as cl
import numpy as np
import timeit
from chivolib.spectral import Cube

global M
global model

ws.import_file("fits/combined-278000.fits")
#ws.import_file("fits/calibrated.ms.image.spectrum.J113740.6-010454.spw0.image.fits")
#ws.import_file("fits/calibrated.ms.line.spw0.source15.image.fits")
#ws.import_file("fits/Boom.cm.cln.fits")

elm=ws.elements()
#print elm
ndd=elm['combined-278000-0']
#ndd=elm['calibrated.ms.image.spectrum.J113740.6-010454.spw0.image-0']
#ndd=elm['calibrated.ms.line.spw0.source15.image-0']
#ndd=elm['Boom.cm.cln-0']
params=cl.gauss_clumps_params()
if ndd.meta['NAXIS']==4:
   cb=Cube(ndd.data[0],ndd.meta)
else:
   cb=Cube(ndd.data,ndd.meta)
theta=cl.gauss_clumps(cb,params)



