import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import pandas as pd
import numpy as np

@st.cache(suppress_st_warning=True)
def get_graph(file):

    nodes = []
    edges = []
    df = pd.read_csv(file)
    for x in np.unique(df[["Source", "Target"]].values):
        nodes.append(Node(id=x))
    for index, row in df.iterrows():
        edges.append(Edge(source=row["Source"], target=row["Target"], type="CURVE_SMOOTH"))
    config = Config(width=1000, 
                height=800, 
                directed=False,
                nodeHighlightBehavior=True, 
                highlightColor="#F7A7A6", # or "blue"
                collapsible=True,
                # coming soon (set for all): node_size=1000, node_color="blue"
                ) 

    return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)
    return return_value

def app():
    get_graph("BERT_edge_list2.csv")