import warnings
import time
import logging


import sys
import warnings
import time
import logging
import json
import re
import numpy as np 
import matplotlib.pyplot as plt 

import pandas as pd
from rdflib import Graph, Literal, Namespace, URIRef,BNode
from rdflib.collection import Collection
from rdflib.namespace import FOAF, RDF, RDFS, SKOS, XSD
from rdflib.serializer import Serializer
from rdfpandas.graph import to_dataframe
from SPARQLWrapper import XML, SPARQLWrapper

warnings.filterwarnings("ignore", category=FutureWarning)
measure_dicts={}
social_dicts={}
goal_dicts={}
social_comparison_dicts={}
goal_comparison_dicts={}
annotate_dicts={}
def read(file):
    #start_time = time.time()
    g = Graph()
    g.parse(data=file,format="json-ld")
    #logging.critical(" reading graph--- %s seconds ---" % (time.time() - start_time)) 
    return g

f=open(sys.argv[1])
f3=open(sys.argv[2])
spek_cs = json.load(f)
temp=json.load(f3)
#print(type(content))
spek_cs =json.dumps(spek_cs)
a=read(spek_cs)
b=read(temp)


social_dicts={}
goal_dicts={}
so=URIRef("http://example.com/app#display-lab")
sq12=URIRef("http://example.com/app#display-lab")
pq12=URIRef("http://example.com/slowmo#HasCandidate")
po=URIRef('http://example.com/slowmo#IsAboutMeasure')
p1=URIRef("http://example.com/slowmo#WithComparator")
p3=URIRef('http://schema.org/name')
o5=URIRef("http://purl.obolibrary.org/obo/psdo_0000095")
p5=RDF.type
p6=URIRef("http://example.com/slowmo#ComparisonValue")
p21=URIRef("http://purl.org/dc/terms/title")
p22=URIRef("http://schema.org/name")
o21=Literal("PEERS")
o22=Literal("peers") 
p23=URIRef("http://schema.org/@templates")
p24=URIRef("http://purl.obolibrary.org/obo/IAO_0000136")
p25=RDF.type
pq13=URIRef("psdo:PerformanceSummaryDisplay")
pq14=URIRef("psdo:PerformanceSummaryTextualEntity")
pq15=URIRef("http://schema.org/name")

cp=RDF.type
co=URIRef("http://purl.obolibrary.org/obo/cpo_0000053")
cp1=URIRef("name")
cp2=URIRef("psdo:PerformanceSummaryTextualEntity")
cp3=URIRef("psdo:PerformanceSummaryDisplay")
cp4=RDF.type
cop4=URIRef("http://purl.obolibrary.org/obo/RO_0000091")
cp23=URIRef("http://example.com/slowmo#RegardingComparator")
cp24=URIRef("http://example.com/slowmo#RegardingMeasure")
cp25="http://purl.obolibrary.org/obo/psdo_0000102"
cp26=URIRef("http://example.com/slowmo#AncestorPerformer")
cp27=URIRef("http://example.com/slowmo#AncestorTemplate")


cp21=URIRef("http://example.com/slowmo#AncestorTemplate")
# f1 = open("test23.txt", "w")
# f2 = open("test24.txt", "w")
ac=[]
ab=[]
text_dicts={}
name_dicts={}
display_dicts={}
template_type_dicts={}
candidate_id_dicts={}
graph_type_list=[]

def get_graph_type():
    for s,p,o in a.triples((so, po, None)):
        s1=o
        for s2,p2,o2 in a.triples((s1,p1,None)):
            measure_dicts[s1]=o2
            s3=o2
            node_type=[]
            node_type.append(s1)
            node_type.append(o2)
            for s4,p4,o4 in a.triples((s3,p3,None)):
                if str(o4)=="goal":
                    goal_dicts[s1]=o2
                
                    s7=o2
            for  s81,p81,o81 in a.triples((None, None,o2)):
                for s82,p82,o82 in a.triples((s81,RDF.type,None)):
                    if str(o82) != cp25:
                        node_type.append(o82)
                    
            node_type_tuple=tuple(node_type)
        
            graph_type_list.append(node_type_tuple)
    



    df_graph = pd.DataFrame(graph_type_list)
    df_graph = df_graph.rename({0:"Measure_Name"}, axis=1)
    df_graph = df_graph.rename({1:"Comparator_Node"}, axis=1)
    df_graph = df_graph.rename({2:"graph_type1"}, axis=1)
    df_graph = df_graph.rename({3:"graph_type2"}, axis=1)
    df_graph = df_graph.rename({4:"graph_type3"}, axis=1)
    df_graph = df_graph.rename({5:"graph_type4"}, axis=1)
    df_graph = df_graph.rename({6:"graph_type5"}, axis=1)
    df_graph = df_graph.rename({7:"graph_type6"}, axis=1)
    df_graph = df_graph.fillna(0)
    df_graph=df_graph.reset_index(drop=True)
    return df_graph

       

def get_template_data():
    for s,p,o in b.triples((None,p23,None)):
        ac.append(str(o))
    a25_dicts={}
    a26_dicts={}
    a27_dicts={}
    templatetype_dicts={}
    for x in range(len(ac)):
        s24=URIRef(ac[x])
        af=[]
        ab=[]
        for s29,p29,o29 in b.triples((s24,pq13,None)):
            a25_dicts[ac[x]]=str(o29)
        for s30,p30,o30 in b.triples((s24,pq14,None)):
            a26_dicts[ac[x]]=str(o30)
        for s31,p31,o31 in b.triples((s24,pq15,None)):
            a27_dicts[ac[x]]=str(o31)

        for s,p,o in b.triples((s24,p24,None)):
            s25=o
            for s,p,o in b.triples((s25,p25,None)):
                templatetype=str(o)
                ab.append(templatetype)
        ad=tuple(ab)
        templatetype_dicts[ac[x]]=ad
    display_dicts=a25_dicts
    text_dicts=a26_dicts
    name_dicts=a27_dicts
    template_type_dicts=templatetype_dicts
    df_text = pd.DataFrame.from_dict(text_dicts,orient='index')
    df_text = df_text.rename({0:"text"}, axis=1)
    df_display_dicts=pd.DataFrame.from_dict(display_dicts,orient='index')
    df_display_dicts = df_display_dicts.rename({0:"display"}, axis=1)
    df_name_dicts=pd.DataFrame.from_dict(name_dicts,orient='index')
    df_name_dicts = df_name_dicts.rename({0:"name"}, axis=1)
    df_template_type_dicts=pd.DataFrame.from_dict(template_type_dicts,orient='index')
    df_template_type_dicts = df_template_type_dicts.rename({0:"template_type_dicts"}, axis=1)
    df=pd.concat([df_text, df_display_dicts,df_name_dicts,df_template_type_dicts], axis=1)
    df = df.rename({1:"template_type_dicts1"}, axis=1)
    df = df.rename({2:"template_type_dicts2"}, axis=1)
    df = df.rename({3:"template_type_dicts3"}, axis=1)
    df = df.rename({4:"template_type_dicts4"}, axis=1)
    df = df.fillna(0)
    df = df.reset_index()
    
    
    return df

def create_candidates(df,df_graph):
    count=0
    for rowIndex,row in df.iterrows():
    
        for rowIndex1, row1 in df_graph.iterrows():
            measure_name=row1["Measure_Name"]
            oxcv=BNode(row1["Comparator_Node"][0])
        
            oq=BNode()
            count=count+1
        #print(row1)
            ah=BNode(row1["Comparator_Node"])
            ag=Literal(measure_name)
            a.add((sq12,pq12,oq) )
            a.add((oq,cp,co))
            a25=URIRef(row["text"])
            a27=URIRef(row["name"])
            a26=URIRef(row["display"])
            a28=URIRef(row["template_type_dicts"])
            a29=URIRef(row["template_type_dicts1"])
        
            a.add((oq,cp2,a25))
            a.add((oq,cp1,a27))
            a.add((oq,cp3,a26))
            if(row["template_type_dicts"] != 0):
                ov=BNode()
                a.add((oq,cop4,ov))
                a.add((ov,RDF.type,a28))
            if(row["template_type_dicts1"] != 0):
                ov=BNode()
                a.add((oq,cop4,ov))
                a.add((ov,RDF.type,a29))
            if (row["template_type_dicts2"] != 0):
                a30=URIRef(row["template_type_dicts2"])
                ov=BNode()
                a.add((oq,cop4,ov))
                a.add((ov,RDF.type,a30))
            if (row["template_type_dicts3"] != 0):
                a31=URIRef(row["template_type_dicts3"])
                ov=BNode()
                a.add((oq,cop4,ov))
                a.add((ov,RDF.type,a31))
            if (row["template_type_dicts4"] != 0):
                a32=URIRef(row["template_type_dicts4"])
                ov=BNode()
                a.add((oq,cop4,ov))
                a.add((ov,RDF.type,a32))
            if (row1["graph_type1"] != 0):
                a33=URIRef(row1["graph_type1"])
                ov=BNode()
                a.add((oq,cop4,ov))
                a.add((ov,RDF.type,a33))
                a.add((ov,cp23,ah))
                a.add((ov,cp24,ag))
            if (row1["graph_type2"] != 0):
                a34=URIRef(row1["graph_type2"])
                ov=BNode()
                a.add((oq,cop4,ov))
                a.add((ov,RDF.type,a34))
                a.add((ov,cp23,ah))
                a.add((ov,cp24,ag))
            if (row1["graph_type3"] != 0):
                a34=URIRef(row1["graph_type3"])
                ov=BNode()
                a.add((oq,cop4,ov))
                a.add((ov,RDF.type,a34))
                a.add((ov,cp23,ah))
                a.add((ov,cp24,ag))
            if (row1["graph_type4"] != 0):
                a34=URIRef(row1["graph_type4"])
                ov=BNode()
                a.add((oq,cop4,ov))
                a.add((ov,RDF.type,a34))
                a.add((ov,cp23,ah))
                a.add((ov,cp24,ag))
            if (row1["graph_type5"] != 0):
                a34=URIRef(row1["graph_type5"])
                ov=BNode()
                a.add((oq,cop4,ov))
                a.add((ov,RDF.type,a34))
                a.add((ov,cp23,ah))
                a.add((ov,cp24,ag))
            if (row1["graph_type6"] != 0):
                a34=URIRef(row1["graph_type6"])
                ov=BNode()
                a.add((oq,cop4,ov))
                a.add((ov,RDF.type,a34))
                a.add((ov,cp23,ah))
                a.add((ov,cp24,ag))
            a35=BNode("-p1")
            a.add((oq,cp26,a35))
            a36=URIRef(row["index"])
            a.add((oq,cp27,a36))
    print(count)
    return a




# ac=get_template_list()
#display_dicts,text_dicts,name_dicts,template_type_dicts=get_template_data(ac)
df= get_template_data()
df_graph=get_graph_type()
# df.to_csv("template.csv")
d=create_candidates(df,df_graph)






              



    




        
           



C=d.serialize(format='json-ld', indent=4)
f12 = open("test12.json", "w")
f12.write(C)    
f12.close()
        
        
                




