#https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #create an empty adjacency list
        G = [[] for i in range(numCourses)]
        #used to calculate indegree of each node.
        degree = [0] * numCourses
        #make adjaceny list of the graph.
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        #bfs initially has list of nodes with no indegree i.e. can be taken without taking any other course.
        bfs = [i for i in range(numCourses) if degree[i] == 0]
        for i in bfs:
            #visit non visited adjacent nodes
            for j in G[i]:
                #we remove the node from graph, so degree is decreased by 1.
                degree[j] -= 1
                #if after removing any vertex indegree of j becomes 0, then add it to bfs
                if degree[j] == 0:
                    bfs.append(j)
        #if length isn't same then not possible to fulfill course requirement.
        return bfs if len(bfs) == numCourses else []