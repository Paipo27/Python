# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:27:28 2023

@author: DAFEYEF
"""

from BasesGeneral import convertirBase

numeroDecimal=4579
cadenaOctal=convertirBase(numeroDecimal,8)
cadenaDoce=convertirBase(numeroDecimal,12)
cadenaHexaldecimal=convertirBase(numeroDecimal,16)
print("el numero",numeroDecimal,"en octal es :",cadenaOctal)
print("el numero",numeroDecimal,"en cadenaDoce es :",cadenaDoce)
print("el numero",numeroDecimal,"en HexaDecimal es :",cadenaHexaldecimal)