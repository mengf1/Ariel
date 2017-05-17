from sets import Set
inputFile="fifty_nine.table5.multiCCA.size_40.normalized"

# or Turkish - tr
#sel_set = Set(["en", "de", "nl", "da"])
sel_set=Set(["en", "de"])
langs=[]
with open(inputFile, "r") as f:
    for line in f:
        line = line.strip()
        tok = line.split()[0]
        parts = tok.split(":")
        # for example, ``en::''
        #if len(parts) > 2:
        #    print tok
        lang = parts[0]
        if lang not in langs:
            langs.append(lang)
        if lang in sel_set:
            print line

#print langs, len(langs)
