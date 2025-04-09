# Bus Routes
# LeetCode Problem #815: Bus Routes
# https://leetcode.com/problems/bus-routes/

# Problem Description:
# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.
# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (you are not on any bus initially), and you want to go to the bus stop target.
# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

# Example:
# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

# Time Complexity: O(B * S) where B is the number of buses and S is the number of stops
# Space Complexity: O(B * S) for storing the graph

from collections import deque, defaultdict
class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        # If source and target are the same, no buses needed
        if source == target:
            return 0
        
        # Create a mapping from stops to buses that visit them
        stops_to_buses = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                stops_to_buses[stop].append(bus)
        
        # Initialize BFS
        queue = deque()
        stops_visited = set()
        used_buses = set()

        # Start BFS from source stop
        queue.append((source, 0))
        stops_visited.add(source)

        # BFS to find minimum number of buses needed
        while queue:
            current_stop, buses_taken = queue.popleft()

            # Try all buses that can be taken from current stop
            for bus in stops_to_buses[current_stop]:
                if bus in used_buses:
                    continue
                used_buses.add(bus)

                # Try all stops that can be reached by this bus
                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses_taken + 1
                    if next_stop not in stops_visited:
                        queue.append((next_stop, buses_taken+1))
                        stops_visited.add(next_stop)
        
        # If target is not reachable
        return -1 