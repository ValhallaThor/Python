def getLinetype(line):
   if ("[" in line) and ("]" in line):
        return "coord"
   elif (("Metal" in line) and (("Rubies" in line) == False) and (("Mine" in line) == False)):
       return "metal"
   elif (("Crystal" in line) and ("Rubies" in line) == False) and (("Mine" in line) == False):
       return "crystal"
   elif (("Deuterium" in line) and ("Rubies" in line) == False) and (("Synthesizer" in line) == False):
       return "deut"
   elif ("Buildings") in line:
       return "ignore"
   else:
        return ""

def getCoord(line):
    coord = ""
    iStart = line.index("[")
    iEnd = line.index("]")
    iLen = iEnd - iStart - 1
    coord = line[iStart + 1:iEnd]
    return coord

def getMetal(line):
    coord = ""
    iStart = line.index("Metal")
    iEnd = line.index("Crystal")
    coord = line[iStart + 6:iEnd]
    coord = coord.strip(' \n\t')
    coord = coord.replace(".","")
    metal = int(coord)
    return metal

def getCrystal(line):
    coord = ""
    iStart = line.index("Crystal")
    coord = line[iStart + 7:]
    coord = coord.strip(' \n\t')
    coord = coord.replace(".","")
    crystal = int(coord)

    return crystal

def getDeut(line):
    coord = ""
    iStart = line.index("Deuterium")
    iEnd = line.index("Energy")
    coord = line[iStart + 9:iEnd]
    coord = coord.strip(' \n\t')
    coord = coord.replace(".","")
    deut = int(coord)

    return deut

def writeRecord(coord, metal, crystal, deut):
    with open("d:/Data/Zorg/attacklist.txt", "a") as myfile:
        record = "%s, metal:%d, crystal:%d, deut:%d\r\n" % (coord,metal,crystal,deut)
        myfile.write(record)

    return

fname = "d:/Data/Zorg/attack.txt"
startofrecord = False
fh = open("d:/Data/Zorg/attacklist.txt", "w")
fh.close()
ignore = False
record = 0

with open(fname) as f:
    for line in f:
        linetype = getLinetype(line)
        if (linetype == "coord"):
            record += 1
            print(record)
            if startofrecord:
                writeRecord(coord, metal,crystal, deut)
                coord = ""
                metal = 0
                crystal = 0
                deut = 0
                ignore = False
            else:
                startofrecord = True

            coord = getCoord(line)
        elif (linetype == "ignore"):
            ignore = True
        elif (ignore):
            pass
        elif (linetype == "metal"):
            metal = getMetal(line)
            crystal = getCrystal(line)
        elif (linetype == "deut"):
            deut = getDeut(line)
        else:
            pass

if startofrecord:
    writeRecord(coord, metal, crystal, deut)
    startofrecord == False
