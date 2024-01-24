# ICLSubFind

This repository contains the necessary files to classify stars in the main halo of a galaxy cluster or group according to their kinematics (see [Marini+2022](https://ui.adsabs.harvard.edu/abs/2022MNRAS.514.3082M/abstract) for more details). The classification can shed light on whether a particle is more likely to be a star particle associated with the Brightest Cluster Galaxy (BCG) or the IntraCluster Light (ICL). The underlying theoretical assumptions are fully described in Dolag+2010. 

The algorithm takes as input three observables associated with each star particle. These are the distance of the particle from the cluster's centre of mass normalised for R200 (critical), the rest-frame velocity normalised for V200 (critical) and the logarithm of the halo mass M200 (in terms of 1e14 Msun). It is important to provide to the code the input parameter exactly in this order.  

You can check the example notebook to understand how to make the package work. 
