import sys
from sets import Set

def process(inputFile, lstr):
    #language set: Set(["en", "de", "nl", "da"])
    # for example, English - en
    langs=Set(lstr.split("-"))
    with open(inputFile, "r") as f:
        for line in f:
            line = line.strip()
            tok = line.split()[0]
            parts = tok.split(":")
            # for example, an exception: ``en::''
            #if len(parts) > 2:
            #    print tok
            lang = parts[0]
            if lang in langs:
                print line

if __name__ == "__main__":
    # the file of word embeddings
    # for example, inputFile="fifty_nine.table5.multiCCA.size_40.normalized"
    inputFile = sys.argv[1]
    # for example, en or en-de
    lstr = sys.argv[2]
    process(inputFile, lstr)
