#Text Proccessing with Kmin - Graduation Project

Today, text processing works in many fields and with many methods. We tried to solve this problem with Solving the Minimum Dominating Set Problem by Polynomial Method (KMax - KMin tree) in the graduation project. 

<br>Source link we used = > https://dergipark.org.tr/en/download/article-file/2095100</br>

First we get the text from any medium website , audio-to-text-converted text etc.

We get the text as a short link from the website using agile.

# The stages are as follows:
<br>1 -> First we get any text from somewhere. Then we remove the stop words from this text. Then, we take every sentence in this text as a node and turn the text into a graph.</br>
<br>2 -> Kmin tree is coded</br>
<br>3 -> Finalization and score calculation</br>

I will talk about kmin tree, which is my own part in my article.

In this study, the expansion tree defined by Ali Karcı will be used. The kmin tree was defined by the snowman.

Let's use the graph from step 1

iGraph library is used for graph

![Graph](https://github.com/mtfsahin/Text-Proccessing-with-kmin-School-Prohect/blob/main/graph.jpeg)


```
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
```
We determine the weight of each node by summing the rows of the matrix, then we choose the node with the lowest degree of node (weight) as we will construct the kmin tree.

```
ATm = pd.DataFrame(AT, columns=column_names, index=row_names)
B = ATm.values
# create graph from matrix
g = igraph.Graph.Adjacency((B > 0).tolist())
print("matris" , g)
# row total
a = AT.sum(axis=0)
# min row = minimum wedding weight
min_deg = min(a)
print("derece sirala" , a)
print("minimum" , min_deg)

# We create an empty k min tree
kmin_agaci = Graph()
kmin_agaci.add_vertices(8) #vertex_size
```
# Let's create the K min tree
```
def kmin (kmin_agaci=kmin_agaci,a = a,g = g,min_deg = min(a)):
    for x in range(7): # loop returns 1 less than the number of nodes of the graph (vertex_size - 1)
    
        #node with minimum weight is found
        bul = g.vs.find(_degree=min_deg)
        bul_dugum_temiz = bul.index
        
        #minimum selected node has neighbors
        endusukListe = list(g.neighbors(bul, mode=ALL))
        
        # a => our node
        # b => node's neighbors
        # a & b cartesian product
        a = np.array([bul_dugum_temiz])
        b = np.array(endusukListe)
        kartezyen = [(a0, b0) for a0 in a for b0 in b]
        print(kartezyen)
        
        # Adding the node to the tree
        add_kmin=list(kartezyen)
        kmin_agaci.add_edges(add_kmin)
        print("kmin = " , kmin_agaci)
   
        m = bul_dugum_temiz
        y = endusukListe
        
        # Reset all connections of the node to avoid visiting this node again.
        for x, val in enumerate(y):
            m = m
            n = val
            AT[m][n] = 0
            AT[n][m] = 0
            ATm[m][n] = 0
            ATm[n][m] = 0
            g = igraph.Graph.Adjacency((B > 0).tolist())
            matrissifirsayisi = np.count_nonzero(AT)
            
            #stop function when all nodes are reset
            if(matrissifirsayisi == 0):
                print("Bitti")
                break
            kmin = []
            kmin.append(m)
            #new minimum
            a = g.degree()
            # I remove it from the list so that the values we reset do not appear as minimum again.
            a = listeden_sifirlari_sil(a, 0)
            min_deg = min(a)

```
# Function that removes zeros from the list
```
def listeden_sifirlari_sil(the_list, val):
   return [value for value in the_list if value != val]
```
#Kmin tree

![Kmin](https://github.com/mtfsahin/Text-Proccessing-with-kmin-School-Prohect/blob/main/kmin.jpeg)

#Deficiencies

There is a possibility that two nodes with the same node degree will come, if such a situation is encountered, the tree level should be checked and the lower one should be taken.


# Creating the cut matrix and node degrees


```
# I get the neighborhood of the newly formed kmin tree
kesme = kmin_agaci.get_adjacency()

# Then I also transpose the matrix kesme
kesmeTranspoze = np.transpose(kesme)

# sample matrix
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

# I multiply the matrix of the GraphMatrisi with the kesmeTranspoze matrix that I created, and I get the cut degrees matrix.
kesmeDereceMatrix = np.dot(GraphMatrisi,kesmeTranspoze)
print("Kesme dereceleri",kesmeDereceMatrix)

# To find the minimum node of the shear matrix matrix, the rows are summed and the minimum node is found.
kesmeDereceleri = np.sum(kesmeDereceMatrix,axis=1).tolist()
print(kesmeDereceleri)
kesmeDereceleri.sort()
min_deg = min(kesmeDereceleri)
print(min_deg)

index_=[0,1,2,3,4,5,6,7] # Here it will be more useful to produce as many indexes as the number of nodes with a for loop.

baskinlik_column=["kesmeDereceleri"]
baskinlikDF =  pd.DataFrame(kesmeDereceleri, columns=baskinlik_column, index=index_)
min_deg = min(kesmeDereceleri)
print(baskinlikDF)
print("mimimum baskınlık değeri =>",min_deg)


#Determining the node to delete

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

# Then, with the deletion method we apply in kmin, the matrix is reset and we get the node dominance degrees.

```

Output 

```
   kesmeDereceleri
0               22
1               40
2               40
3               42
4               44
5               46
6              268
7              738
mimimum baskınlık değeri => 22
silinecek düğüm 0
```

#Result

The node with the minimum degree of nodes is the least interactive sentence. 

