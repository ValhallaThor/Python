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
            return "Raw Materials"
        elif ("Metal" in line) and (zorg.section == 1):
            return "Metal"
        elif ("Crystal" in line) and (zorg.section == 1):
            return "Crystal"
        elif ("Deuterium" in line) and (zorg.section == 1):
            return "Deuterium"
        elif ("Rocket Launcher" in line) and (zorg.section == 2):
            return "Rocket Launcher"
        elif ("Light Laser" in line) and (zorg.section == 2):
            return "Light Laser"
        elif ("Heavy Laser" in line) and (zorg.section == 2):
            return "Heavy Laser"
        elif ("Gauss Cannon" in line) and (zorg.section == 2):
            return "Gauss Cannon"
        elif ("Ion Cannon" in line) and (zorg.section == 2):
            return "Ion Cannon"
        elif ("Plasma Cannon" in line) and (zorg.section == 2):
            return "Plasma Cannon"
        elif ("Small Shield Dome" in line) and (zorg.section == 2):
            return "Small Shield Dome"
        elif ("Large Shield Dome" in line) and (zorg.section == 2):
            return "Large Shield Dome"
        elif ("Antiballistic Missile" in line) and (zorg.section == 2):
            return "Antiballistic Missile"
        elif ("Interplanetary Missile" in line) and (zorg.section == 2):
            return "Interplanetary Missile"
        elif ("" in line) and (zorg.section == 3):
            return ""
        else:
            return ""

    def strip(line, linetype):
        iStart = line.index(linetype)
        return line[iStart+len(linetype):]

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

    def getStruct(inputfilename):
        fname = inputfilename
        startofrecord = False
        ignore = False
        record = 0

        strs = []

        with open(fname) as f:
            for line in f:
                linetype = zorg.getLinetype(line)
                while (linetype != ""):
                    if (linetype == "Raw Materials"):
                        record += 1
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
                    elif (linetype == "Crystal"):
                        crystal = zorg.getCrystal(line)
                    elif (linetype == "Deuterium"):
                        deut = zorg.getDeut(line)
                    else:
                        pass

                    if linetype == "Raw Materials":
                        linetype = ""
                    else:
                        line = zorg.strip(line, linetype)
                        linetype = zorg.getLinetype(line)

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


