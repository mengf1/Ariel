import sys

def process(inputFile,lang):
    toks = []
    tags = []
    for line in open(inputFile):
        line = line.strip()
        if line[0:1] == "#":
            continue
        if len(line) < 1:
            if len(toks) == 0:
                print "No tags .."
                break
            if len(toks) != len(tags):
                print "Missing tags .."
                break
            newline = ""
            for item in toks:
                newline += item + " "
            newline += "\n"
            for item in tags:
                newline += item +" "
            print newline.strip()
            print ""
            toks = []
            tags = []
            continue
        parts = line.split()
        tok = parts[2]
        if lang != "NON":
            tok = lang+":"+tok
        tag = parts[3]
        toks.append(tok)
        tags.append(tag)

if __name__ == "__main__":
    inputFile = sys.argv[1]
    lang = sys.argv[2]
    process(inputFile, lang)
