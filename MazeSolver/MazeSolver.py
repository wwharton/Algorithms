import numpy as np
import cv2
from PIL import Image, ImageDraw
from graph import Graph

def read_maze():
    img_path = 'D:/Python Projects/Algorithms/MazeSolver/maze.png'
    img = cv2.imread(img_path, 0)
    return img

def update_matrix_with_path(matrix, path):
    # use opencv to get image dimensions
    img = cv2.imread('D:/Python Projects/MazeSolver/maze.png', cv2.IMREAD_UNCHANGED)
    dimensions = img.shape
    height = int(dimensions[0])
    width = int(dimensions[1])
    print(height)
    print(width)

    # use pil to prep the maze object and then fill in the path
    image = Image.open('maze.png')


    # Calculate # of Vertices
    v = 0
    for y in range(height):
        for x in range(width):
            if str(img[y][x]) == '[255 255 255 255]':
                v += 1



    for y in range(height):
        for x in range(width):
            value = tuple((y, x))
            if value in path:
                # Value found in path, recolor pixel
                image.putpixel((x, y), 200)
    # Show and save final maze solution
    print(f'# of vertices: {v}')
    image.show()
    image.save('solvedmaze.png')


if __name__ == '__main__':
    matrix = read_maze()
    my_graph = Graph(matrix)
    my_graph.create_dict()
    path = my_graph.find_path_util()
    update_matrix_with_path(matrix, path)
    # Class print for added info / data
    # print(my_graph)


