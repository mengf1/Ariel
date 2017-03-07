import sys

# import alternateNames.txt, from which we can extract names in UG
def processGeoNames(altNamesFile, allNamesFile):
    geo2ug = {}
    with open(altNamesFile, 'r') as f:
        for line in f:
            parts = line.strip().split("\t")
            geo_id = int(parts[1])
            lang_flag = parts[2]
            lang = parts[3]
            if lang_flag == "ug":
                if geo_id not in geo2ug:
                    geo2ug[geo_id] = [lang]
                else:
                    geo2ug[geo_id].append(lang)
    # extract GeoNames
    en2geo = {}
    with open(allNamesFile, 'r') as f:
        for line in f:
            parts = line.strip().split("\t")
            geo_id = int(parts[0])
            geo_en = parts[1]
            if geo_id in geo2ug:
                en2geo[geo_en] = geo_id
    # size of geo2en < size of geo2ug
    print len(geo2ug), len(en2geo)
    return geo2ug, en2geo

# import the GeoNames file
def processDBlocations(geo2ug, en2geo, locationsFile):
    outputF = open("ugGeoNames.txt", "w")
    i = 0
    with open(locationsFile, 'r') as f:
        for line in f:
            link, name = line.strip().split("\t")
            if name in en2geo:
                i +=1
                geo_id = en2geo[name]
                #print geo_id, link, name, geo2ug[geo_id]
                re = str(geo_id) +"\t"+link+"\t"+name
                for item in geo2ug[geo_id]:
                    re += "\t" + item
                outputF.write(re+"\n")
    outputF.close()
    print "Find", i

if __name__ == "__main__":
    allNamesFile = sys.argv[1]
    altNamesFile = sys.argv[2]
    locationsFile = sys.argv[3]
    geo2ug, en2geo = processGeoNames(altNamesFile, allNamesFile)
    processDBlocations(geo2ug, en2geo, locationsFile)
    print ": ) Good luck : )"
