#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Proton_Electron_Reduction_Beta/rules"
shortDesc = u""
longDesc = u"""
Surface adsorption of a single radical forming a single bond to the surface site
"""

entry(
    index = 1,
    label = "Adsorbate;Proton;Electron",
    kinetics = SurfaceChargeTransfer(
        a = 0.5, # charge transfer coeff
        A = (1.0e10, 'm^3/(mol*s)'), # pre-exponential factor
        n = 0, # temperature coeff
        V0 = (0, 'V') # reference potential
        Ea = (40, 'kJ/mol') # activation energy
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        ne = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up Placeholder"""
)