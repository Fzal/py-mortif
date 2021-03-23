import re

def find_mortifs(line, n):
    pat1 = 'AATAACAA'
    pat2 = 'AWWRTAANNWWGNCC'
    mortifs = []
    char8 = [line[i:i+8] for i in range(0, len(line), 8)]
    char16 = [line[i:i+16] for i in range(0, len(line), 16)]
    for s in char8:
        mortifs += [ (s[m.start():m.end()], n, m.start(), m.end()) for m in re.finditer(pat1, s) ]
    for s in char16:
        mortifs += [ (s[m.start():m.end()], n, m.start(), m.end()) for m in re.finditer(pat2, s) ]
    return mortifs

def find_oris(line, n):
    patterns = ['ATTA', 'ATTT', 'ATTTTA']
    oris = []
    for pattern in patterns:
        oris += [ (line[m.start():m.end()], n, m.start(), m.end()) for m in re.finditer(pattern, line) ]
    return oris

def find_tgs(line, n):
    patterns = ['TGTTTTG', 'TTTTGGGG', 'TGTTTTTG']
    tgs = []
    for pattern in patterns:
        tgs += [ (line[m.start():m.end()], n, m.start(), m.end()) for m in re.finditer(pattern, line) ]
    return tgs

def find_patterns(line, n, patterns):
    matches = []
    for pattern in patterns:
        matches += [ (line[m.start():m.end()], n, m.start(), m.end()) for m in re.finditer(pattern, line) ]
    return matches

def find_curved(line, n):
    patterns = [
            "AAAAnnnnnnnAAAAnnnnnnnAAAA",
            "TTTTnnnnnnnTTTTnnnnnnnTTTT",
            "TTTAAA"
            ]
    return find_patterns(line, n, patterns)

def find_kinked(line, n):
    patterns = [
            "TAnnnTGnnnCA",
            "TAnnnCAnnnTG",
            "TGnnnTAnnnCA",
            "TGnnnCAnnnTA",
            "CAnnnTGnnnTA",
            "CAnnnTAnnnTG"
            ]
    return find_patterns(line, n, patterns)

def find_topo(line, n):
    patterns = [
            r"[AG]n[TG]nnCnnG[GT]Tn[TC]n[TC]"
            ]
    return find_patterns(line, n, patterns)


def find_special(line, n):
    patterns = [
            "TCTTTAATTTCTAATATATTTAGGA"
            ]
    return find_patterns(line, n, patterns)

def find_ats(line, n):
    patterns = [
            "AAAA",
            "TTTT"
            ]
    return find_patterns(line, n, patterns)



def findsig(filename):
    fh = open(filename)
    b_mof = []
    oris = []
    tgs = []
    curved = []
    kinked = []
    topo = []
    special = []
    ats = []

    lines = fh.readlines()
    line_no = -1
    print(lines)
    for line in lines:
        line_no += 1
        mortifs = find_mortifs(line, line_no)
        if mortifs:
            b_mof.append(mortifs)
        ori = find_oris(line, line_no)
        if ori:
            oris.append(ori)
        tg = find_tgs(line, line_no)
        if tg:
            tgs.append(tg)
        c = find_curved(line, line_no)
        if c:
            curved.append(c)
        k = find_kinked(line, line_no)
        if k:
            kinked.append(k)
        t = find_topo(line, line_no)
        if t:
            topo.append(t)
        s = find_special(line, line_no)
        if s:
            special.append(s)
        at = find_ats(line, line_no)
        if at:
            ats.append(at)



    print('\n\n\nThe Values are in the format:')
    print('(Matching string, line, string start, string end)')
    print('\n\nBipartite Mortifs')
    print(b_mof)
    print('\n\nORI Signals')
    print(oris)
    print('\n\nTG Richness')
    print(tgs)
    print('\n\nCurved DNA')
    print(curved)
    print('\n\nKinked DNA')
    print(kinked)
    print('\n\nTopo')
    print(topo)
    print('\n\nConsensus Motif')
    print(special)
    print('\n\nAT Richness')
    print(ats)






findsig('input.txt')
