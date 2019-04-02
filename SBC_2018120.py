#!/usr/bin/env python3

import re
import itertools

ROLLNUM_REGEX = "201[0-9]{4}"

class Graph(object):
    name = "Vrinda Narayan"
    email = "vrinda18120@iiitd.ac.in"
    roll_num = "2018120"

    def __init__ (self, vertices, edges):
        """
        Initializes object for the class Graph

        Args:
            vertices: List of integers specifying vertices in graph
            edges: List of 2-tuples specifying edges in graph
        """

        self.vertices = vertices
        
        ordered_edges = list(map(lambda x: (min(x), max(x)), edges))
        
        self.edges    = ordered_edges
        
        self.validate()

    def validate(self):
        """
        Validates if Graph if valid or not

        Raises:
            Exception if:
                - Name is empty or not a string
                - Email is empty or not a string
                - Roll Number is not in correct format
                - vertices contains duplicates
                - edges contain duplicates
                - any endpoint of an edge is not in vertices
        """

        if (not isinstance(self.name, str)) or self.name == "":
            raise Exception("Name can't be empty")

        if (not isinstance(self.email, str)) or self.email == "":
            raise Exception("Email can't be empty")

        if (not isinstance(self.roll_num, str)) or (not re.match(ROLLNUM_REGEX, self.roll_num)):
            raise Exception("Invalid roll number, roll number must be a string of form 201XXXX. Provided roll number: {}".format(self.roll_num))

        if not all([isinstance(node, int) for node in self.vertices]):
            raise Exception("All vertices should be integers")

        elif len(self.vertices) != len(set(self.vertices)):
            duplicate_vertices = set([node for node in self.vertices if self.vertices.count(node) > 1])

            raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(vertices, duplicate_vertices))

        edge_vertices = list(set(itertools.chain(*self.edges)))

        if not all([node in self.vertices for node in edge_vertices]):
            raise Exception("All endpoints of edges must belong in vertices")

        if len(self.edges) != len(set(self.edges)):
            duplicate_edges = set([edge for edge in self.edges if self.edges.count(edge) > 1])

            raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(edges, duplicate_edges))

    def min_dist(self, all_paths):
        '''
        Finds minimum distance between start_node and end_node

        Args:
            all_paths : a list with all possible nodes from start node to end node

        Returns:
            An integer denoting minimum distance between start_node
            and end_node
        '''
        m=len(all_paths[0])
        for i in range(len(all_paths)):
            if (len(all_paths[i])<m):
                m=len(all_paths[i])
        return m-1

        raise NotImplementedError

    def all_paths(self, minimum_dist, all_path):
        """
        Finds all paths between start_node and end_node.
        When dist=minimum distance than it find a list of all shortest paths.

        Args:
            minimum_dist : paths should have a length of this value
            all_paths : a list of all of the paths

        Returns:
            A list of path, where each path is a list of integers.
        """
        p=[]
        for i in range(len(all_path)):
            if len(all_path[i])==(minimum_dist+1):
                p=p+[all_path[i]]
        return p

        raise NotImplementedError

    def betweenness_centrality(self, node, dic):
        """
        Find betweenness centrality of the given node

        Args:
            node: Node to find betweenness centrality of.
            dic: a dictionary with all nodes as keys and the nodes they are conneceted to as values

        Returns:
            Single floating point number, denoting betweenness centrality
            of the given node
        """
        final=0
        for i in range(len(self.vertices)):
            for j in range(i+1, len(self.vertices)):
                a=0
                i1=self.vertices[i]
                j1=self.vertices[j]
                #find all possible pairs except given nodes
                if i1!=node and j1!=node:
                    x=all_paths_list(dic, i1, j1)
                    #finds all the paths between the two nodes
                    min_dist=self.min_dist(x)
                    #calculates the shortest distance
                    short_paths=self.all_paths(min_dist,x)
                    #finds all paths with len = shortest distance
                    s=0
                    for y in range(len(short_paths)):
                        if node in short_paths[y]:
                            s=s+1
                    a=a+(s/len(short_paths))
                    #formula for calculating betweeness centrality
                final=final+a
        return final
        raise NotImplementedError

    def top_k_betweenness_centrality(self, dic, k):
        """
        Find top k nodes based on highest equal betweenness centrality.

        
        Returns:
            List a integer, denoting top k nodes based on betweenness
            centrality.
        """
        d={}
        l=[]
        for i in self.vertices:
               d[i]=self.betweenness_centrality(i, dic)
               #for all vertices it calculates betweeness centrality and stores them in a dictionary
               #as well as a list
               l=l+[d[i]]
        l.sort(reverse=True)
        #sorts the list in descending order
        final=[]
        for i in l[0:k]:
            for j in d.keys():
                if i==d[j]:
                    #if the value of the betweeness centrality of a node is equal to the max betweeness centrality it adds it to a final list
                    final=final+[j]
        #as some lists might have same betweeness centrality prints the first k
        return final[0:k]
        raise NotImplementedError
abc=0    
def all_paths_list(dic, start_node, end_node, path=[]):
    path = path + [start_node]
    global abc
    #when start and end are equal, we have reached our destination
    if start_node == end_node:
        return [path]
    abc=abc+1
    #if start node is not present, error
    if start_node not in dic.keys():
        return []
    paths = []
    abc=abc+2
    #goes to every node connected to start_node
    for new_node in dic[start_node]:
        #to avoid loops check if it isnt already covered
        if new_node not in path:
            abc=abc+5
            #recursion to find path with new node as start node
            newpaths = all_paths_list(dic, new_node, end_node, path)
            abc=abc+7
            #adds all new paths to paths 
            for newpath in newpaths:
                paths.append(newpath)
                abc=abc+1
    return paths
if __name__ == "__main__":
    vertices = [1, 2, 3, 4, 5, 6]
    edges    = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)]

    graph = Graph(vertices, edges)
    d={}
    for i in (graph.vertices):
    	d[i]=[]
    g=str(graph.edges)
    #converts it into a dictionary
    #with keys as vertices and values as all the nodes connected to it
    for i in (d.keys()):
    	a=str(i)
    	x=g.find(a)
    	s=0
    	while(x!=-1):
    		if g[x-1]=='(':
    			d[i]+=[int(g[x+3])]
    		else:
    			d[i]+=[int(g[x-3])]
    		s=x+1
    		x=g.find(a,s)
    print(graph.top_k_betweenness_centrality(d, 3))
    
