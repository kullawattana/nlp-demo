from nltk import Tree

parse_str = "(ROOT (S (NP (PRP You)) (VP (MD could) (VP (VB say) (SBAR (IN that)" \
"(S (NP (PRP they)) (ADVP (RB regularly)) (VP (VB catch) (NP (NP (DT a) (NN shower)) (, ,)" \
"(SBAR (WHNP (WDT which)) (S (VP (VBZ adds) (PP (TO to) (NP (NP (PRP$ their) (NN exhilaration))" \
"(CC and) (NP (FW joie) (FW de) (FW vivre))))))))))))) (. .)))"
t = Tree.fromstring(parse_str)

subtexts = []
for subtree in t.subtrees():
    if subtree.label() == "S" or subtree.label() == "SBAR":
        subtexts.append(' '.join(subtree.leaves()))
print (subtexts)

presubtexts = subtexts[:]       # ADDED IN EDIT for leftover check
for i in reversed(range(len(subtexts)-1)):
    subtexts[i] = subtexts[i][0:subtexts[i].index(subtexts[i+1])]

for text in subtexts:
    print (text)

# ADDED IN EDIT - Not sure for generalized cases
leftover = presubtexts[0][presubtexts[0].index(presubtexts[1])+len(presubtexts[1]):]
print (leftover)