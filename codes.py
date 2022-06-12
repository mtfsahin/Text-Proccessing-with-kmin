import pandas as pd
import numpy as np
import networkx as nx
import igraph
from igraph import *

def listeden_sifirlari_sil(the_list, val):
   return [value for value in the_list if value != val]

column_names = [0, 1, 2, 3, 4, 5, 6, 7]
row_names = [0, 1, 2, 3, 4, 5, 6, 7]
AT = np.reshape((
    0, 1, 1, 1, 0, 1, 1, 1,
    1, 0, 0, 0, 123, 1, 0, 0,
    1, 0, 0, 1, 0, 1, 1, 1,
    1, 0, 1, 0, 0, 1, 1, 0,
    0, 123, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 0, 0, 1, 0,
    1, 0, 1, 1, 0, 1, 0, 0,
    1, 0, 1, 0, 0, 0, 0, 0,
), (8, 8))
GraphMatrisi = np.array(AT)

ATm = pd.DataFrame(AT, columns=column_names, index=row_names)
B = ATm.values
g = igraph.Graph.Adjacency((B > 0).tolist())
print("matris" , g)
a = g.degree()
print("derece" , a)
#edge weight
a.sort()
min_deg = min(a)
kmin_agaci = Graph()
kmin_agaci.add_vertices(8)

def kmin (kmin_agaci=kmin_agaci,a = a,g = g,min_deg = min(a)):
    for x in range(7):
        bul = g.vs.find(_degree=min_deg)
        bul_dugum_temiz = bul.index

        endusukListe = list(g.neighbors(bul, mode=ALL))
        a = np.array([bul_dugum_temiz])
        b = np.array(endusukListe)
        kartezyen = [(a0, b0) for a0 in a for b0 in b]
        print(kartezyen)
        aaa=list(kartezyen)
        kmin_agaci.add_edges(aaa)

        print("kmin = " , kmin_agaci)

        m = bul_dugum_temiz
        y = endusukListe

        for x, val in enumerate(y):
            m = m
            n = val
            AT[m][n] = 0
            AT[n][m] = 0
            ATm[m][n] = 0
            ATm[n][m] = 0
            g = igraph.Graph.Adjacency((B > 0).tolist())
            matrissifirsayisi = np.count_nonzero(AT)
            if(matrissifirsayisi == 0):
                print("Bitti")
                break
            kmin = []
            kmin.append(m)
            a = g.degree()
            a = listeden_sifirlari_sil(a, 0)
            min_deg = min(a)
kmin()

kesme = kmin_agaci.get_adjacency()
kesmeTranspoze = np.transpose(kesme)
AT = np.reshape((
 0, 2, 2, 2, 0, 2, 2, 2,
 2, 0, 0, 0, 2, 2, 0, 0,
 2, 0, 0, 2, 0, 2, 2, 2,
 2, 0, 2, 0, 0, 2, 2, 0,
 0, 2, 0, 0, 0, 0, 0, 0,
 2, 2, 2, 2, 0, 0, 2, 0,
 2, 0, 2, 2, 0, 2, 0, 0,
 2, 0, 2, 0, 0, 0, 0, 0), (8, 8))
kesmeTranspoze = np.array(AT)
kesmeDereceMatrix = np.dot(GraphMatrisi,kesmeTranspoze)
print("Kesme dereceleri",kesmeDereceMatrix)

kesmeDereceleri = np.sum(kesmeDereceMatrix,axis=1).tolist()
print(kesmeDereceleri)

kesmeDereceleri.sort()
min_deg = min(kesmeDereceleri)
print(min_deg)

index_=[0,1,2,3,4,5,6,7]
baskinlik_column=["kesmeDereceleri"]
asd =  pd.DataFrame(kesmeDereceleri, columns=baskinlik_column, index=index_)
min_deg = min(kesmeDereceleri)
print(asd)
print("mimimum baskınlık değeri =>",min_deg)

komsuluk_column_names = [0,1,2,3,4,5,6,7]
komsuluk_row_names    = [0,1,2,3,4,5,6,7]

komsuluk = np.reshape((
0,1,1,1,0,1,1,1,
1,0,0,0,1,1,0,0,
1,0,0,1,0,1,1,1,
1,0,1,0,0,1,1,0,
0,1,0,0,0,0,0,0,
1,1,1,1,0,0,1,0,
1,0,1,1,0,1,0,0,
1,0,1,0,0,0,0,0,
),(8,8))

df_komsu = pd.DataFrame(komsuluk, columns=komsuluk_column_names, index=komsuluk_row_names)

gri_liste=[]
kMin = min(kesmeDereceleri)
silinecek=index_[kesmeDereceleri.index(kMin)]

column_names = [0,1,2,3,4,5,6,7]
row_names    = [0,1,2,3,4,5,6,7]
for i in range(len(row_names)):
    tempp = komsuluk[row_names.index(index_[kesmeDereceleri.index(kMin)])][i]
    if (tempp == 1):
        gri_liste.append(row_names[tempp])

print("silinecek düğüm",row_names[komsuluk_row_names.index(silinecek)])

kesmeTranspoze