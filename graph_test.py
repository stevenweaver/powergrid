import maps
import networkx as nx
import operator

G = maps.usa()
print("Betweenness")
b=nx.betweenness_centrality(G)
sorted_b = sorted(b.iteritems(), key=operator.itemgetter(1), reverse=True)
for x in sorted_b:
    print("%s : %5.3f"%x)


#import pprint
#pprint.pprint(shortest_path(G, source="Chicago", weight="weight"))
#pprint.pprint(shortest_path(G, source="Chicago"))


print("\nMean Path Lengths")
m = []
for k,v in nx.shortest_path_length(G, weight="weight").iteritems():
    lol = [w for j, w in v.iteritems()]
    mean = float(sum(lol))/len(lol)
    m.append((k,mean))

sorted_m = sorted(m, key=operator.itemgetter(1))
for x in sorted_m:
    print("%s : %5.3f")%x

#print("\nDegree centrality")
#d=degree_centrality(G)
#sorted_d = sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)
#for x in sorted_d:
#    print("%s : %5.3f"%(x[0],x[1]))

#print("\nCloseness centrality")
#c=closeness_centrality(G)
#sorted_c = sorted(c.iteritems(), key=operator.itemgetter(1), reverse=True)
#for x in sorted_c:
#    print("%s : %5.3f"%(x[0],x[1]))
