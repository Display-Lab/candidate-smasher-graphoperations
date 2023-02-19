import warnings
import time
import logging
import json
import pandas as pd
import sys
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.collection import Collection
from rdflib.namespace import FOAF, RDF, RDFS, SKOS, XSD
from rdflib.serializer import Serializer
from rdfpandas.graph import to_dataframe


warnings.filterwarnings("ignore")
from candidatesmasher import CandidateSmasher

def read_graph(file):
    start_time = time.time()
    g = Graph()
    g.parse(file)
    
    logging.critical(" reading graph--- %s seconds ---" % (time.time() - start_time)) 
    return g

spek_bs =open(sys.argv[1])
template = open(sys.argv[2])
f3json=json.load(spek_bs)
f4json=json.load(template)

#print(type(content))
BS=read_graph(f3json)
template=read_graph(f4json)



cs=CandidateSmasher(BS,template)
df_graph=cs.get_graph_type()
df_template=cs.get_template_data()
CS=cs.create_candidates(df_graph,df_template)