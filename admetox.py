#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = "Devashish Das"
__copyright__ = "Copyright 2013"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Devashish Das"
__email__ = "dasdevashishdas@gmail.com"


"""
# ============================================================================
Feixiong Cheng, Weihua Li, Yadi Zhou, Jie Shen, Zengrui Wu, Guixia Liu, Philip W. Lee, Yun Tang. 
dmetSAR: a comprehensive source and free tool for evaluating chemical ADMET properties. J. Chem. 
nf. Model., 2012, 52(11): 3099-3105. (This paper is the hot paper of JCIM in Dec. 2012).
# ============================================================================

Website: http://www.admetexp.org/
"""

import re
import urllib2
from Tkinter import *
from time import time

global adme_read
global ind 

adme_read = ['Blood-Brain Barrier', 'Human Intestinal Absorption', 'Caco-2 Permeability', 'P-glycoprotein Substrate', 'P-glycoprotein Inhibitor', 'Non-inhibitor', 'Renal Organic Cation Transporter', 'CYP450 2C9 Substrate', 'CYP450 2D6 Substrate', 'CYP450 3A4 Substrate', 'CYP450 1A2 Inhibitor', 'CYP450 2C9 Inhibitor', 'CYP450 2D6 Inhibitor', 'CYP450 2C19 Inhibitor', 'CYP450 3A4 Inhibitor', 'CYP Inhibitory Promiscuity', 'Human Ether-a-go-go-Related Gene Inhibition', 'Non-inhibitor', 'AMES Toxicity', 'Carcinogens', 'Fish Toxicity', 'Tetrahymena Pyriformis Toxicity', 'Honey Bee Toxicity', 'Biodegradation', 'Aqueous solubility', 'Caco-2 Permeability', 'Rat Acute Toxicity', 'Fish Toxicity', 'Tetrahymena Pyriformis Toxicity']

ind = [144, 145, 146, 44, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172]

def complete_tab():
    global query_text_area
    global adme_read
    global ind 
    global str_var
    query = str(query_text_area.get("1.0",END)).split("\n")
    print query
    if query == "": 
        return
    else:
        x = time()
        with open("admetexp_1.ods", mode = "w") as adme:
             for num, each_query in enumerate(query):
                 s = re.findall("-{,1}\d.\d{4}", urllib2.urlopen("http://www.admetexp.org/predict/?smiles=%s&action=A" %each_query).read())
                 str_var.set("Value grabbed for %d of %d" %(num + 1, len(query)))
                 adme.write(each_query + "\t")
                 adme.write("\t".join(s))
                 adme.write("\n")
                 str_var.set("Done Writing: %.2f sec" %(time() - x))

global query_text_area
global str_var
root = Tk()
root.title("ADME Toxicity Prediction")
l = LabelFrame(root, width = 10, height = 10)
l.grid()
query_text_area = Text(l)
query_text_area.grid()
b = LabelFrame(root)
b.grid()
#===
str_var = StringVar(master = root)
str_var.set("Run!!")
Label(b, textvariable = str_var).pack()
#===
Button(b,text = "Run!!!", command = complete_tab).pack()
root.mainloop()
