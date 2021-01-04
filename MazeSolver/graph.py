from collections import defaultdict
import pprint
import cv2
import time
import sys



class Graph:

    matrix = ''

    def __init__(self, matrix):
        self.matrix = matrix
        self.nodes_list = []
        self.dict = defaultdict(tuple)
        self.adjacent_list = []
        self.start_vertex = ''
        self.end_vertex = ''
        self.finished_flag = False
        self.path = []
        sys.setrecursionlimit(1500)

    def __str__(self):
        # Print options for quick and dirty debug / troubleshooting / print details
        # pprint.pprint(self.matrix)
        # pprint.pprint(self.dict)
        pprint.pprint(self.path)
        return f'Start Vertex: {self.start_vertex} - End Vertex: {self.end_vertex} - Path Length: {len(self.path)} nodes'



    def getnodes(self):

        # Reads the pixel maze and transforms it into an array of values - 0 for black, 255 for white
        # Captures dimensions of the ndarray

        img = cv2.imread('D:/Python Projects/Algorithms/MazeSolver/maze.png', cv2.IMREAD_UNCHANGED)
        dimensions = img.shape
        height = int(dimensions[0])
        width = int(dimensions[1])

        # Generates nodes list for the graph

        for y in range(height):
            for x in range(width):
                if self.matrix[y][x] != 0:
                    self.nodes_list.append(tuple((y, x)))
                    self.get_adjacency(y, x)
        return self.nodes_list

    def get_adjacency(self, y, x):
        # Checks for a starting node for adjacent white nodes, appends to list
        # This list will become the values for the starting node key in a dict later
        temp_list = []
        try:
            if self.matrix[y - 1][x] == 255:
                dy = y - 1
                temp_list.append((dy, x))
        except IndexError:
            pass
        try:
            if self.matrix[y + 1][x] == 255:
                dy = y + 1
                temp_list.append((dy, x))
        except IndexError:
            pass
        try:
            if self.matrix[y][x - 1] == 255:
                dx = x - 1
                temp_list.append((y, dx))
        except IndexError:
            pass
        try:
            if self.matrix[y][x + 1] == 255:
                dx = x + 1
                temp_list.append((y, dx))
        except IndexError:
            pass
        self.adjacent_list.append(temp_list)



    def create_dict_keys(self):
        for n in self.nodes_list:
            self.dict[n]


    def create_dict_adjacency_values(self):
        foo = 0
        for n in self.nodes_list:
            self.dict[n] = self.adjacent_list[foo]
            foo += 1


    def create_dict(self):
        self.getnodes()
        self.create_dict_keys()
        self.create_dict_adjacency_values()
        return self.dict

    # def find_path(self):
    #     self.find_path_util()

    def find_path_util(self):
        dict_list = list(self.dict)
        visited = []
        start_vertex = dict_list[0]
        self.start_vertex = start_vertex
        end_vertex = dict_list[-1]
        self.end_vertex = end_vertex
        current_vertex = start_vertex

        print(self.start_vertex)
        print(self.end_vertex)

        self.path = self.find_path_logic(dict_list, visited, end_vertex, current_vertex)
        return self.path


    def find_path_logic(self, dict_list, visited, end_vertex, current_vertex):

        # Pathing Logic
        # at my key
        #     mark key as visited
        #     look at key values in the dict
        #     compare key values against visited list
        #     if there are unvisited values
        #         visit first unvisited value
        #             recursion (make this value my new key, repeat)
        #     if there are no unvisited values and it is not the end point
        #         pop second to last key out of the visited list

        # visited list becomes the list of nodes from start to endpoint as we pop out invalid nodes along the way
        # base case is satisfied when we reach the endpoint

        if current_vertex != end_vertex and self.finished_flag == False:
            if current_vertex not in visited:
                visited.append(current_vertex)
            values_list = []
            values_list = self.dict[current_vertex]
            for value in values_list:
                if value not in visited:
                    current_vertex = value
                    if current_vertex not in visited:
                        visited.append(current_vertex)
                    if current_vertex != end_vertex and self.finished_flag == False:

                        visited = self.find_path_logic(dict_list, visited, end_vertex, current_vertex)
                        #print(f'a recursion loop broke, checking {current_vertex} vs {end_vertex}')
                        if visited[-1] != end_vertex:
                            visited.pop(-1)
                        else:
                            self.finished_flag = True
        return visited









