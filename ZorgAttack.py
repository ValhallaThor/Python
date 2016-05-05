class zorg:

    section = 0

    def __init__(self):
        self.section = 0

    def getSection(line):
        if ("Raw Materials" in line) and ((zorg.section < 1) or (zorg.section > 2)):
            zorg.section = 1
        elif ("Defenses" in line and zorg.section == 1):
            zorg.section = zorg.section + 1
        elif ("Buildings" in line and zorg.section == 2):
            zorg.section = zorg.section + 1
        elif ("Research" in line and zorg.section == 3):
            zorg.section = zorg.section + 1

    def getLinetype(line):
        zorg.getSection(line)
        if ("[" in line) and ("]" in line and zorg.section == 1):
            return "coord"
        elif (("Metal" in line) and (zorg.section == 1)):
            return "Metal"
        elif (("Crystal" in line) and (zorg.section == 1)):
            return "Crystal"
        elif (("Deuterium" in line) and (zorg.section == 1)):
            return "Deuterium"
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

    def buildAttacklist(inputfile, outputfile):
        # old attack function will be replace by getStruct function
        fname = inputfile
        startofrecord = False
        fh = open(outputfile, "w")
        fh.close()
        ignore = False
        record = 0

        with open(fname) as f:
            for line in f:
                linetype = zorg.getLinetype(line)
                if (linetype == "coord"):
                    record += 1
                    print(record)
                    if startofrecord:
                        zorg.writeRecord(coord, metal, crystal, deut)
                        coord = ""
                        metal = 0
                        crystal = 0
                        deut = 0
                        ignore = False
                    else:
                        startofrecord = True

                    coord = zorg.getCoord(line)
                elif (linetype == "ignore"):
                    ignore = True
                elif (ignore):
                    pass
                elif (linetype == "Metal"):
                    metal = zorg.getMetal(line)
                    crystal = zorg.getCrystal(line)
                elif (linetype == "Deuterium"):
                    deut = zorg.getDeut(line)
                else:
                    pass

        if startofrecord:
            zorg.writeRecord(coord, metal, crystal, deut)
            startofrecord == False

    def getStruct(inputfilename):
        fname = inputfilename
        startofrecord = False
        ignore = False
        record = 0

        strs = []

        with open(fname) as f:
            for line in f:
                linetype = zorg.getLinetype(line)
                if (linetype == "coord"):
                    record += 1
                    print(record)
                    if startofrecord:
                        strs.append((coord, metal, crystal, deut))
                        coord = ""
                        metal = 0
                        crystal = 0
                        deut = 0
                        ignore = False
                    else:
                        startofrecord = True

                    coord = zorg.getCoord(line)
                elif (linetype == "ignore"):
                    ignore = True
                elif (ignore):
                    pass
                elif (linetype == "Metal"):
                    metal = zorg.getMetal(line)
                    crystal = zorg.getCrystal(line)
                elif (linetype == "Deuterium"):
                    deut = zorg.getDeut(line)
                else:
                    pass

        if startofrecord:
            strs.append((coord, metal, crystal, deut))
            startofrecord == False

        return strs

extreme = zorg()

ifile = "d:/Data/Zorg/attack.txt"
regels = zorg.getStruct(ifile)

print(len(regels))
for x in regels:
    print (x)


