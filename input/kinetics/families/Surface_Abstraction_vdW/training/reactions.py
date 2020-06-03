#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

# reverse of 16, below
# entry(
#     index = 34,
#     label = "H2O* + O* <=> OH_2* + OH_4*",
#     degeneracy = 2,
#     kinetics = SurfaceArrhenius(
#         A = (8.14E20, 'm^2/(mol*s)'),
#         n = -0.274,
#         Ea = (218400, 'J/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""R34
#     test surface mechanism: based upon Olaf Deutschmann's work:
#     "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#     Delgado et al
#     Catalysts, 2015, 5, 871-904""",
# 	  metal = "Ni",
# )

# reverse of 34, above
entry(
    index = 1,
    label = "OH_2* + OH_4* <=> H2O* + O*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (5.691e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (14.0669343, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 16 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.675e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 5.691e16 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 21,
    label = "CH4* + O* <=> CH3* + OH_4*",
    degeneracy = 4,
    kinetics = SurfaceArrhenius(
        A = (5.62E20, 'm^2/(mol*s)'),
        n = -0.101,
        Ea = (92700, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R21
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 2,
    label = "OH_2* + HCO* <=> H2O* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (3.261e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (6.9181644, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 40 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
9.597e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 3.261e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 3,
    label = "HCOO_1* + HCO* <=> HCOOH* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (7.475e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (13.8363288, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 41 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
2.2e14 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 7.475e18 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 4,
    label = "CH3O* + HCO* <=> CH3OH* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (6.572e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (8.76300824, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 45 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.934e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 6.572e16 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 5,
    label = "CH3O* + HCOO_5* <=> HCOOCH3* + O*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.356e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (28.5950795, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 46 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
6.934e11 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 2.356e16 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 6,
    label = "NH3_Pt + O_Pt <=> NH2_Pt + HO_Pt",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A = (1.49013e+16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (55.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 3 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
3.7e11 1/s / 2.483e-05 mol/m^2 = 8.4422e+16 m^2/(mol*s)
""",
    metal="Pt",
    facet="533"
)

entry(
    index = 7,
    label = "NH3_Pt + HOr_Pt <=> NH2_Pt + H2O_Pt",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A = (1.5706e+17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (73.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 6 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
3.9e12 1/s / 2.483e-05 mol/m^2 = 9.6837e+17 m^2/(mol*s)
""",
    metal="Pt",
    facet="533"
)

entry(
    index = 8,
    label = "NH2p_Pt + HOp_Pt  <=> NH_Pt + H2Or_Pt",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (1.36931e+17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (22.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 7 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
3.4e12 1/s / 2.483e-05 mol/m^2 = 9.6837e+17 m^2/(mol*s)
""",
    metal="Pt",
    facet="533"
)

entry(
    index = 9,
    label = "NHp_Pt + HOp_Pt  <=> N_Pt + H2Or_Pt",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A= (2.0540e+16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (22.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 8 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
5.1e11 1/s / 2.483e-05 mol/m^2 = 9.6837e+17 m^2/(mol*s)
""",
    metal="Pt",
    facet="533"
)

entry(
    index = 10,
    label = "NHp_Pt + HOp_Pt  <=> N_Pt + H2Or_Pt",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A=(1.26633e+17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (22.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 8 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
5.1e11 1/s / 2.483e-05 mol/m^2 = 9.6837e+17 m^2/(mol*s)
""",
    metal="Pt",
    facet="533"
)

entry(
    index = 11,
    label = "HOr_Pt + HO123_Pt  <=> O_Pt + H2Or_Pt",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A= (4.02739e+17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (75.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 9 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
1e13 1/s / 2.483e-05 mol/m^2 = 9.6837e+17 m^2/(mol*s)
""",
    metal="Pt",
    facet="533"
)
