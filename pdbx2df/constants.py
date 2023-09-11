# pdbx2df
# Author: Ruibin Liu <ruibinliuphd@gmail.com>
# License: MIT
# Code Repository: https://github.com/Ruibin-Liu/pdbx2df
"""Constants"""

AMINO_ACIDS = {
    "ALA": "A",
    "ARG": "R",
    "ASN": "N",
    "ASP": "D",
    "ASH": "D",  # protonated Asp
    "CYS": "C",
    "CYX": "C",  # disulfide Cys
    "CYM": "C",  # deprotonated Cys
    "GLN": "Q",
    "GLU": "E",
    "GLH": "E",  # protonated Glu
    "GLY": "G",
    "HIS": "H",
    "HIP": "H",  # protonated His
    "HIE": "H",  # H in NE tautomer
    "HID": "H",  # H in ND tautomer
    "ILE": "I",
    "LEU": "L",
    "LYS": "K",
    "LYN": "K",  # deprotonated Lys
    "MET": "M",
    "PHE": "F",
    "PRO": "P",
    "PYL": "O",  # pyrrolysine
    "SEC": "U",  # selenocysteine
    "SER": "S",
    "THR": "T",
    "TRP": "W",
    "TYR": "Y",
    "VAL": "V",
}

# https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl
# keep at most 3 digits of the average between the upper and lower bounds
# in the 'Standard Atomic Weight' column
ELEMENT_MASSES = {
    "H": 1.008,
    "He": 4.003,
    "Li": 6.968,
    "Be": 9.012,
    "B": 10.814,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "F": 18.998,
    "Ne": 20.180,
    "Na": 22.990,
    "Mg": 24.306,
    "Al": 26.982,
    "Si": 28.085,
    "P": 30.974,
    "S": 32.067,
    "Cl": 35.451,
    "Ar": 39.948,
    "K": 39.098,
    "Ca": 40.078,
    "Sc": 44.956,
    "Ti": 47.867,
    "V": 50.942,
    "Cr": 51.996,
    "Mn": 54.938,
    "Fe": 55.845,
    "Co": 58.933,
    "Ni": 58.693,
    "Cu": 63.546,
    "Zn": 65.380,
    "Ga": 69.723,
    "Ge": 72.630,
    "As": 74.922,
    "Se": 78.971,
    "Br": 79.904,
    "Kr": 83.798,
    "Rb": 85.468,
    "Sr": 87.620,
    "Y": 88.906,
    "Zr": 91.224,
    "Nb": 92.906,
    "Mo": 95.95,
    "Tc": 98,
    "Ru": 101.07,
    "Rh": 102.906,
    "Pd": 106.42,
    "Ag": 107.868,
    "Cd": 112.414,
    "In": 114.818,
    "Sn": 118.710,
    "Sb": 121.760,
    "Te": 127.60,
    "I": 126.904,
    "Xe": 131.293,
    "Cs": 132.905,
    "Ba": 137.327,
    "La": 138.905,
    "Ce": 140.116,
    "Pr": 140.908,
    "Nd": 144.242,
    "Pm": 145,
    "Sm": 150.36,
    "Eu": 151.964,
    "Gd": 157.25,
    "Tb": 158.925,
    "Dy": 162.500,
    "Ho": 164.930,
    "Er": 167.259,
    "Tm": 168.934,
    "Yb": 173.054,
    "Lu": 174.967,
    "Hf": 178.49,
    "Ta": 180.948,
    "W": 183.84,
    "Re": 186.207,
    "Os": 190.23,
    "Ir": 192.217,
    "Pt": 195.084,
    "Au": 196.967,
    "Hg": 200.592,
    "Tl": 204.384,
    "Pb": 207.2,
    "Bi": 208.980,
    "Po": 209,
    "At": 210,
    "Rn": 222,
    "Fr": 223,
    "Ra": 226,
    "Ac": 227,
    "Th": 232.038,
    "Pa": 231.036,
    "U": 238.029,
    "Np": 237,
    "Pu": 244,
    "Am": 242.059,
    "Cm": 245.567,
    "Bk": 248.073,
    "Cf": 250.578,
    "Es": 252.083,
    "Fm": 257.095,
    "Md": 259.101,
    "No": 259.101,
    "Lr": 262.110,
    "Rf": 267.122,
    "Db": 268.126,
    "Sg": 271.134,
    "Bh": 272.138,
    "Hs": 270.134,
    "Mt": 276.152,
    "Ds": 281.164,
    "Rg": 280.165,
    "Cn": 285.177,
    "Nh": 284.178,
    "Fl": 289.190,
    "Mc": 288.193,
    "Lv": 293.204,
    "Ts": 292.207,
    "Og": 294.214,
    "D": 2.01410177812,
    "T": 3.0160492779,
}
# No Standard Atomic Weight values from 'Am' onward;
# used averaged value of the Relative Atomic Mass instead.
