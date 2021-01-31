#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Proton_Electron_Reduction_Alpha/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "CH3X + H + e <=> CH4X",
    degeneracy = 1,
    kinetics = SurfaceChargeTransfer(
        alpha = 0.12, # charge transfer coeff
        A = (2.5e14, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (0.51, 'V'), # reference potential
        Ea = (0.89, 'eV/molecule'), # activation energy
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        ne = -1, # electron stochiometric coeff 
    ),
    shortDesc = u"""https://doi.org/10.1016/j.cattod.2017.01.050""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
    site = "",
    rank = 5,
)

entry(
    index = 2,
    label = "HOX + H + e <=> H2OX",
    degeneracy = 1,
    kinetics = SurfaceChargeTransfer(
        alpha = 0.07, # charge transfer coeff
        A = (2.5e14, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (0.39, 'V'), # reference potential
        Ea = (0.14, 'eV/molecule'), # activation energy
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        ne = -1, # electron stochiometric coeff 
    ),
    shortDesc = u"""https://doi.org/10.1016/j.cattod.2017.01.050""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
    site = "",
    rank = 5,
)

