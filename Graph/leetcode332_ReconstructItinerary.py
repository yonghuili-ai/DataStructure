"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

"""
# this problem can be derived as given a nodes edge info, how can we reconstruct the tree?


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Euler cycle is a in a finite graph, vist every edge exactly once. In this problem, construct an itinerary that uses all flights from JFK. This problem is a variant of Euler Path, with a fixing starting point. 
        # to find the Eular path, we need to
        # 1) starting at starting vertex, we keep following the ordered and unused edges until we get stuck at certain vertext where no more unvisited outgoing edges
        # 2) the point we got stuck would be the last airport visited. Then we follow the visited vertex backwards, to obtain the final itinerary. 
# https://leetcode.com/problems/reconstruct-itinerary/solutions/4042004/beats-99-17-dfs-recursive-iterative-euler-path-intuition-commented-code/
        from collections import defaultdict
        graph = defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        # print(graph)
        for k,v in graph.items():
            v.sort(reverse=True)
        # print(graph)
        stack = ['JFK']
        res = []
        while stack:
            curr = stack[-1]
            if len(graph[curr]) > 0:
                destination = graph[curr].pop()
                stack.append(destination)
            # no more destinations from the current airport, this is the last airflow to visit
            else:
                res.append(curr)
                # pop it from stack
                stack.pop()
        return res[::-1]# return the iternary from JFK to last vertet

            


        
        
        