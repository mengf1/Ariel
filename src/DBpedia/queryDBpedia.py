from SPARQLWrapper import SPARQLWrapper, SPARQLExceptions, JSON
import json
import os
import fnmatch

# Limit is 10000 thus we run multiple times using different offsets
def queryPerRound(queryStr, offset):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)
    queryStr = queryStr + """ LIMIT 10000 OFFSET """ + str(offset)
    # print queryStr
    sparql.setQuery(queryStr)
    results = sparql.query().convert()
    return results


def query(queryStr, dataType):
    print "Start to query the data: " + dataType
    for i in range(1000):
        offset = 0
        if i != 0:
            offset = i * 10000
        results = queryPerRound(queryStr, offset)
        counts = len(results["results"]["bindings"])
        if counts == 0:
            break
        tot = offset + counts
        print tot
        outputFile = dataType + '-' + str(tot) + ".json"
        with open(outputFile, 'w') as f:
            json.dump(results, f)
    print "Finish querying the data"


def extractFile(inputFile):
    data = {}
    with open(inputFile, 'r') as f:
        for line in f:
            raw = json.loads(line.strip())
            data = raw["results"]["bindings"]
    return data


def preprocess(dataType):
    print "Process the raw data"
    saveFile = dataType + "s.tsv"
    outputF = open(saveFile, 'w')
    for f in os.listdir("."):
        if fnmatch.fnmatch(f, dataType + "-*.json"):
            data = extractFile(f)
            # an example for Person: {"person": {"type": "uri", "value": "http://dbpedia.org/resource/Aa_(architect)"}}
            for item in data:
                link = item[dataType]['value'].encode('utf-8')
                parts = link.split('/')
                name = parts[len(parts) - 1]
                name = name.replace("_", " ")
                # print link + "\t"+ name
                outputF.write(link + "\t" + name + "\n")
    outputF.close()
    print "Finish processing " + dataType + " data"


if __name__ == "__main__":
    # query persons
    queryStr = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT DISTINCT ?person
        WHERE {
            ?person rdf:type <http://dbpedia.org/ontology/Person>
        }"""
    d_type = "person"
    query(queryStr, d_type)
    preprocess(d_type)

    # query locations
    queryStr = """PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        SELECT DISTINCT ?location
        WHERE  {
            ?location a dbo:Place .
            ?location geo:lat ?lat .
            ?location geo:long ?long .
        } """
    d_type = "location"
    query(queryStr, d_type)
    preprocess(d_type)

    # query organisations
    queryStr = """PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        SELECT DISTINCT ?organisation
        WHERE {
            ?organisation a/rdfs:subClassOf* dbo:Organisation .
        }"""
    d_type = "organisation"
    query(queryStr, d_type)
    preprocess(d_type)
