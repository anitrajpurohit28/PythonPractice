import re
def is_authentic_skewer(s):
    vowels = 'aeiouAEIOU'

    # First and Last character MUST NOT be vowel
    if s[0] in vowels or s[-1] in vowels:
        return False

    # If no alpha OR no symbols, we need to return False
    if not re.search('[a-zA-Z]', s) or not re.search('[^a-zA-Z]', s):
        return False

    # Find the separator
    start_idx = re.search("[^a-zA-Z]", s).start()
    idx = start_idx + 1
    while s[idx] == s[start_idx]:
        idx += 1
    end_idx = idx
    sep = s[start_idx:end_idx]

    # Get the split string
    split_str = s.split(sep)

    # Split string should contains only alphabets
    # and MUST NOT contain any empty strings
    if not all(map(str.isalpha, split_str)):
        return False

    # Check for consonant in even positions and vowels in odd
    for index, char in enumerate(split_str):
        if index%2 == 0 and char in vowels:
            return False
        elif index%2 and char not in vowels:
            return False
    return True
"""
s="GOXXOC-GLYO--BS----------AO----"

print(end)
#print(s.split[1:2])
print(is_authentic_skewer("GOXXOC--GLYO--BS----------AO----"))#, False))#
"""


print(is_authentic_skewer("B--A--N--A--N--A--S"))#, True))#
print(is_authentic_skewer("L-A-B-O-R-A-T-O-R"))#, True))#
print(is_authentic_skewer("M-----E-----M-----E-----S"))#, True))#
print(is_authentic_skewer("A--X--E"))#, False))#
print(is_authentic_skewer("C-L-A-P"))#, False))#
print(is_authentic_skewer("M--A---T-E-S"))#, False))#
print(is_authentic_skewer("C--H----E---E-S-E"))#, False))#
print(is_authentic_skewer("B-E-L-L"))#, False))#
print(is_authentic_skewer("T-I-T-A-N-I-C"))#, True))#
print(is_authentic_skewer("J--E--Q--A--H--E--K--A--Y--U--X--A--P--I--F"))#, True))#
print(is_authentic_skewer("F-U-W"))#, True))#
print(is_authentic_skewer("C-----O-----K-----O-----Z-----O-----D-----E-----W-----O-----T"))#, True))#
print(is_authentic_skewer("T----O----M----O----R"))#, True))#
print(is_authentic_skewer("OZAEZ-----EE"))#, False))#
print(is_authentic_skewer("--UXGV"))#, False))#
print(is_authentic_skewer("W-E-D-A-X-E-P-I-Y-O-L-E-V-A-W"))#, True))#
print(is_authentic_skewer("J---U---X---O---G---O---G---I---D---U---J---O---K---U---V"))#, True))#
print(is_authentic_skewer("APU---V"))#, False))#
print(is_authentic_skewer("U---WIE--------------UACO"))#, False))#
print(is_authentic_skewer("EOAOTJCUE-----U----K-----"))#, False))#
print(is_authentic_skewer("S---O---S---I---W---A---H---U---W---I---J---I---Q---A---C"))#, True))#
print(is_authentic_skewer("R-O-D-U-P-U-C-A-M-A-R-A-T-I-V-U-R"))#, True))#
print(is_authentic_skewer("C----A----T----A----Q----O----M----A----F"))#, True))#
print(is_authentic_skewer("C---A---P---I---B---A---R---O---Z---E---W---A---L---O---J"))#, True))#
print(is_authentic_skewer("H---------O-------"))#, False))#
print(is_authentic_skewer("----------------"))#, False))#
print(is_authentic_skewer("-----OA-------AOP-EJE-UIE---WH"))#, False))#
print(is_authentic_skewer("VKIQYQO----OI----IFII"))#, False))#
print(is_authentic_skewer("GOXXOC--GLYO--BS----------AO----"))#, False))#
print(is_authentic_skewer("R--I--G--A--J--A--N--A--H--O--K--A--L--U--Q--O--W--A--W--E--R"))#, True))#
print(is_authentic_skewer("Q-----E-----P-----U-----X"))#, True))#
print(is_authentic_skewer("EOE----"))#, False))#
print(is_authentic_skewer("CEQEE-----ETUOYXL"))#, False))#
print(is_authentic_skewer("EOOJSI-ER------Z"))#, False))#
print(is_authentic_skewer("--OU"))#, False))#
print(is_authentic_skewer("----KWVEGUMDDI-MNED"))#, False))#
print(is_authentic_skewer("B---A---X---I---N---O---Z---O---D---O---Q"))#, True))#
print(is_authentic_skewer("A---O------FGOK-------EU---EU"))#, False))#
print(is_authentic_skewer("KG----O-----------"))#, False))#
print(is_authentic_skewer("Z---I---T---U---H---O---G---U---R---A---W---E---G---U---W"))#, True))#
print(is_authentic_skewer("H--I--K--U--Q--A--L--O--L--O--H--A--B--E--Z"))#, True))#
print(is_authentic_skewer("ICU-----TA---L-------O--FE----REE"))#, False))#
print(is_authentic_skewer("C-----A-----W-----U-----H-----I-----Z-----U-----J-----I-----L-----O-----C-----I-----K-----E-----R"))#, True))#
print(is_authentic_skewer("H-----I-----R-----A-----Q-----A-----S-----O-----F-----O-----N-----A-----R"))#, True))#
print(is_authentic_skewer("AA----IWEU"))#, False))#
print(is_authentic_skewer("Z----E----S----A----V----A----M----I----V----O----V----E----G----U----G----A----M"))#, True))#
print(is_authentic_skewer("---YAAT--E"))#, False))#
print(is_authentic_skewer("K---O---L---A---D---I---Y---O---G"))#, True))#
print(is_authentic_skewer("J-O-W-E-C-E-D-A-C-U-V-E-V"))#, True))#
print(is_authentic_skewer("UKMU"))#, False))#
print(is_authentic_skewer("D-I-F"))#, True))#
print(is_authentic_skewer("K----O----B----I----F----O----S----A----H----I----W----A----V----I----P----O----P"))#, True))#
print(is_authentic_skewer("-EUUFPV-------"))#, False))#
print(is_authentic_skewer("Z-O-F-I-P-A-K-I-Z-I-H-U-B-E-R-A-W-U-K"))#, True))#
print(is_authentic_skewer("B-----E-----R-----E-----K-----I-----X-----I-----V-----E-----P-----I-----F-----I-----Y-----A-----C-----U-----Q"))#, True))#
print(is_authentic_skewer("Y-----A-----K-----O-----T-----O-----B-----O-----Q-----A-----M-----O-----H-----E-----Y-----O-----D-----A-----H-----A-----T"))#, True))#
print(is_authentic_skewer("Q-I-F"))#, True))#
print(is_authentic_skewer("-----D-----EKGAO"))#, False))#
print(is_authentic_skewer("T--E--X--I--S--I--T--O--K--O--Z--O--M"))#, True))#
print(is_authentic_skewer("C-U-D-I-N-I-N-O-H-I-J"))#, True))#
print(is_authentic_skewer("P--O--D--U--Q--E--G--A--R--I--J--U--V--A--Y"))#, True))#
print(is_authentic_skewer("--------EU"))#, False))#
print(is_authentic_skewer("V----I----L----A----L----U----Z----U----T----E----R----E----X----A----G----O----W----O----H----E----L"))#, True))#
print(is_authentic_skewer("F--E--S--I--K--O--X--U--D--I--J--A--Q--I--Y--E--M"))#, True))#
print(is_authentic_skewer("WL"))#, False))#
print(is_authentic_skewer("Z---NDIA---O-----KV--HTM----A"))#, False))#
print(is_authentic_skewer("S-O-F-A-D-E-J-O-X-E-C-O-M-U-B-E-D-E-D"))#, True))#
print(is_authentic_skewer("F-E-B-E-B-O-K-O-D-I-K-O-J-E-S-I-D"))#, True))#
print(is_authentic_skewer("L-A-B-A-F-A-D-I-P-I-P"))#, True))#
print(is_authentic_skewer("QOM--IBI"))#, False))#
print(is_authentic_skewer("---P---P---A-----GAG-----KUVL"))#, False))#
print(is_authentic_skewer("IXJ---Q"))#, False))#
print(is_authentic_skewer("DA-----XPZER--PO----PIHUR"))#, False))#
print(is_authentic_skewer("UNOO-------"))#, False))#
print(is_authentic_skewer("S-----A-----Z-----O-----J-----U-----Q-----O-----C-----O-----V"))#, True))#
print(is_authentic_skewer("DA-------E---A--GLU---------O-----D"))#, False))#
print(is_authentic_skewer("J--A--D--U--N--A--W--O--H--O--Q--A--Z--E--V--U--S--O--Y--O--R"))#, True))#
print(is_authentic_skewer("UE----Q--DBZA--"))#, False))#
print(is_authentic_skewer("K-----A-----N-----A-----Q-----I-----L-----U-----X-----E-----H-----A-----S-----I-----Y-----A-----M"))#, True))#
print(is_authentic_skewer("X--E--V--U--Y--U--T--O--D--I--P--O--T--U--Q--I--D--A--R"))#, True))#
print(is_authentic_skewer("I--HWT----YB----UUTEIZ-TI"))#, False))#
print(is_authentic_skewer("IA"))#, False))#
print(is_authentic_skewer("E-----E---RXU"))#, False))#
print(is_authentic_skewer("RM-ITU-----"))#, False))#
print(is_authentic_skewer("----PODEUZU--ZSCTI"))#, False))#
print(is_authentic_skewer("----M---I-"))#, False))#
print(is_authentic_skewer("W----I----J----A----Y----O----G----U----Y----I----S----A----B----E----R----I----H----E----M----U----J"))#, True))#
print(is_authentic_skewer("V----I----K----O----B----I----N----E----H----U----B"))#, True))#
print(is_authentic_skewer("R-A-S-E-J-I-M-E-W-E-H-A-B-U-R-E-P-A-T-U-M"))#, True))#
print(is_authentic_skewer("W----U----G"))#, True))#
print(is_authentic_skewer("F--A--V--E--B--I--G--I--G"))#, True))#
print(is_authentic_skewer("E-----------JXA---AXU------MIRIX"))#, False))#
print(is_authentic_skewer("IWZI-----OB----U-----EAI"))#, False))#
print(is_authentic_skewer("CEP--RP---OP-MIE-----G---"))#, False))#
print(is_authentic_skewer("U-----------ZY-PASUEA---"))#, False))#
print(is_authentic_skewer("PA"))#, False))#
print(is_authentic_skewer("ZAN----LKAM"))#, False))#
print(is_authentic_skewer("J-RZR--------U-------O-----"))#, False))#
print(is_authentic_skewer("K----I----Z"))#, True))#
print(is_authentic_skewer("L--U--C--E--S--I--Z--U--Z--I--H--A--F--O--L--I--C--A--K"))#, True))#
print(is_authentic_skewer("UN----V"))#, False))#
print(is_authentic_skewer("A-------DZM---OCQL---UE-----U"))#, False))#
print(is_authentic_skewer("M---E---M"))#, True))#
print(is_authentic_skewer("L-A-C-O-X-O-Z-O-F-A-Z-E-H-U-L-A-L-U-N-U-Z"))#, True))#
print(is_authentic_skewer("AY"))#, False))#
print(is_authentic_skewer("R--I--S--U--K--E--B--A--F"))#, True))#
print(is_authentic_skewer("H--E--K--A--C--I--N--A--X--U--J--A--P"))#, True))#
print(is_authentic_skewer("Y-----A-----L-----U-----V-----A-----V-----E-----J"))#, True))#
print(is_authentic_skewer("K---I---D---A---B---E---X---U---K---U---H"))#, True))#
