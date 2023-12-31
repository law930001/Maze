import random
import copy

from GameSettings import COLOR, WINDOW_ATTRIBUTE

class GameObjects:

    def __init__(self):

        self.raw_object_count = WINDOW_ATTRIBUTE["window_size"][0] // WINDOW_ATTRIBUTE["object_size"][0]
        self.col_object_count = WINDOW_ATTRIBUTE["window_size"][1] // WINDOW_ATTRIBUTE["object_size"][1]

        self.rects = [[[0] * 2 for _ in range(self.col_object_count)] for _ in range(self.raw_object_count)]
        # 0: default, 1: space, 2: wall, 3:solution_path, 4: start_point, 5: end_point
        self.object = [[0] * self.col_object_count for _ in range(self.raw_object_count)]
        self.player = [1, 1]

        self.start_point = None
        self.end_point = None
        self.solution_path = None

    def initialize(self):

        # init start and end point
        start_r = 1
        start_c = 1
        self.start_point = [start_r, start_c]
        self.object[start_r][start_c] = 4 # start point
        end_r = self.raw_object_count - 2
        end_c = self.col_object_count - 2
        self.end_point = [end_r, end_c]
        self.object[end_r][end_c] = 5 # end point

        # init rects position
        for r in range(self.raw_object_count):
            for c in range(self.col_object_count):
                self.rects[r][c] = [r * WINDOW_ATTRIBUTE["object_size"][0], c * WINDOW_ATTRIBUTE["object_size"][1]]

        # init wall position
        for r in range(self.raw_object_count):
            for c in range(self.col_object_count):
                if r % 2 == 0 or c % 2 == 0:
                    self.object[r][c] = 2 # wall
        # build maze
        maze_path = self.build_maze()
        maze_path[self.end_point[0]][self.end_point[1]] = 5
        self.object = maze_path

        # find solution
        self.solution_path = self.find_maze_solution()
        self.object = self.solution_path


    def random_choose_point(self, N):
        list_N = [i for i in range(0, int(N))]
        return random.choice(list_N)

    def build_maze(self):
        
        four_dir = [[0, 2], [2, 0], [-2, 0], [0, -2]]
        maze_queue = [[self.start_point, copy.deepcopy(self.object)]]

        while maze_queue:
            
            cur_pos, cur_obj = maze_queue.pop(-1)
              
            random.shuffle(four_dir)
            for x, y in four_dir:
                new_x = cur_pos[0] + x
                new_y = cur_pos[1] + y
                if new_x >= 0 and new_y >= 0 and new_x < self.raw_object_count and new_y < self.col_object_count:
                    if cur_obj[new_x][new_y] not in [1, 4]: # not went before
                        cur_obj[(cur_pos[0] + new_x) // 2][(cur_pos [1]+ new_y) // 2] = 1 # already went
                        cur_obj[new_x][new_y] = 1 # already went
                        maze_queue.append([[new_x, new_y], cur_obj])

        return cur_obj
        
    def find_maze_solution(self):
        four_dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        solution_queue = [[self.start_point, copy.deepcopy(self.object)]]

        while True:
            
            cur_pos, cur_obj = solution_queue.pop(-1)

            for x, y in four_dir:
                new_x = cur_pos[0] + x
                new_y = cur_pos[1] + y
                if new_x >= 0 and new_y >= 0 and new_x < self.raw_object_count and new_y < self.col_object_count:
                    if cur_obj[new_x][new_y] == 5:
                        return cur_obj
                    if cur_obj[new_x][new_y] == 1:
                        cur_obj[new_x][new_y] = 3
                        solution_queue.append([[new_x, new_y], copy.deepcopy(cur_obj)])
                        cur_obj[new_x][new_y] = 1