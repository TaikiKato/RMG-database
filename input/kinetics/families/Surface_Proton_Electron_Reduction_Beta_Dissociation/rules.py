#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Proton_Electron_Reduction_Beta/rules"
shortDesc = u""
longDesc = u"""
Surface adsorption of a single radical forming a single bond to the surface site
"""

# entry(
#     index = 0,
#     label = "Adsorbate;Proton;Electron",
#     kinetics = SurfaceChargeTransfer(
#         alpha = 0.25,
#         A = (2.5e14, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
#         n = 0, # temperature coeff, 0 default
#         V0 = None, # Reference potential
#         Ea = (100, 'kJ/mol'), # activation energy at the reversible potential
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#         ne = -1, # electron stochiometric coeff
#     ),
#     rank = 0,
#     shortDesc = u"""Default""",
#     longDesc = u""""""
# )

entry(
    index = 1,
    label = "COX;Proton;Electron",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.25,
        A = (2.5e14, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff, 0 default
        V0 = None, # Reference potential
        Ea = (50, 'kJ/mol'), # activation energy at the reversible potential
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        ne = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)

entry(
    index = 2,
    label = "OCX;Proton;Electron",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.25,
        A = (2.5e14, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff, 0 default
        V0 = None, # Reference potential
        Ea = (30, 'kJ/mol'), # activation energy at the reversible potential
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        ne = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)

entry(
    index = 3,
    label = "OOX;Proton;Electron",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.25,
        A = (2.5e14, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff, 0 default
        V0 = None, # Reference potential
        Ea = (20, 'kJ/mol'), # activation energy at the reversible potential
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        ne = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)

entry(
    index = 4,
    label = "CCX;Proton;Electron",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.25,
        A = (2.5e14, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff, 0 default
        V0 = None, # Reference potential
        Ea = (60, 'kJ/mol'), # activation energy at the reversible potential
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        ne = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)

entry(
    index = 5,
    label = "NNX;Proton;Electron",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.25,
        A = (2.5e14, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff, 0 default
        V0 = None, # Reference potential
        Ea = (20, 'kJ/mol'), # 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        ne = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)

entry(
    index = 6,
    label = "NOX;Proton;Electron",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.25,
        A = (2.5e14, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff, 0 default
        V0 = None, # Reference potential
        Ea = (40, 'kJ/mol'), # 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        ne = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)

entry(
    index = 7,
    label = "ONX;Proton;Electron",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.25,
        A = (2.5e14, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff, 0 default
        V0 = None, # Reference potential
        Ea = (30, 'kJ/mol'), # 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        ne = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)