import pyxel
import math
import numpy as np
import time
class Pacman:
    def __init__(self):
        """
        pacman自体を生成するクラス
        """
        # 描画されるドットの座標
        self.x = 8
        self.y = 8
        #
        self.x_change_quantity = 0
        self.y_change_quantity = 0
        # パックマンのノーマルは黄色
        # クッキーを食べると青で強くなる
        self.state = "yellow"
        self.count = 0

        # 0方向なし, 1 上, 2を下, 3を右, 4を左
        self.vectol = 0
        # 今いるタイルを座標化する
        # self.tile_x = int(self.x/8)
        # self.tile_y = int(self.y/8)
        self.tile_x = 1
        self.tile_y = 1
        self.draw_flag = False
        self.last_frame_count = 0
        self.plot_pacman_x_coordinate = 0
        self.score = 0


class App:
    def __init__(self):
        pyxel.init(160,160,caption="進捗", fps=20)
        # pyxel.run(self.update, self.draw)
        pyxel.load('pacman.pyxel')
        self.count = 0
        self.now_frame = pyxel.frame_count
        self.reset()
        self.map_state = pyxel.tilemap(0)
        # self.deback_tile()
        # for x in dir(pyxel):
        #     print(x)
        # self.deback()
        # self.deback_draw()
        pyxel.run(self.update, self.draw)

    def deback_tile(self):
        for i in self.map_state.data:
            print(i)

    def draw(self):
        pyxel.cls(0)
        self.tilemap_draw()
        # パックマン
        # pyxel.blt(self.x+8,self.y+8,0,0,0,8,8)
        self.pacman_draw()
        self.draw_text()
        # self.pacman_draw_afet()
        self.count += 1
        # print(pyxel.copy(self.x,self.y,0,0,8,8,8)
        # self.deback_draw()

    def draw_text(self):
        # ここもとりあえずはよし
        s = ""
        if pyxel.btn(pyxel.KEY_W):
            s = "W"
        elif pyxel.btn(pyxel.KEY_D):
            s = "D"
        elif pyxel.btn(pyxel.KEY_S):
            s = "S"
        elif pyxel.btn(pyxel.KEY_A):
            s = "A"
        else:
            s = "Non"
        pyxel.text(80,140,"Input Key = " + s, 11)
        pyxel.text(80,150,"score     = {}".format(self.pacman.score),11)


    def tilemap_draw(self):
        # ここは完成かなぁ
        base_x = 0
        base_y = 0
        tm = 0
        u = 0
        v = 0
        w = 16
        h = 17
        pyxel.bltm(base_x,base_y,tm,u,v,w,h)

    def pacman_draw(self):
        print("self.pacman.vectol = {}".format(self.pacman.vectol))
        if self.pacman.x_change_quantity == 0 and self.pacman.y_change_quantity == 0:
            pass
        else:
            if pyxel.frame_count % 2 == 0:
                self.pacman.plot_pacman_x_coordinate = 0
            elif self.pacman.vectol == 1:
                self.pacman.plot_pacman_x_coordinate = 8
            elif self.pacman.vectol == 2:
                self.pacman.plot_pacman_x_coordinate = 16
            elif self.pacman.vectol == 3:
                self.pacman.plot_pacman_x_coordinate = 24
            elif self.pacman.vectol == 4:
                self.pacman.plot_pacman_x_coordinate = 32
        pyxel.blt(self.pacman.x,self.pacman.y,0,self.pacman.plot_pacman_x_coordinate,0,8,8)
        # if self.pacman.vectol == 1:
        #     pyxel.blt(self.pacman.x,self.pacman.y,0,8,0,8,8)
        # elif self.pacman.vectol == 2:
        #     pyxel.blt(self.pacman.x,self.pacman.y,0,16,0,8,8)
        # elif self.pacman.vectol == 3:
        #     pyxel.blt(self.pacman.x,self.pacman.y,0,24,0,8,8)
        # elif self.pacman.vectol == 4:
        #     pyxel.blt(self.pacman.x,self.pacman.y,0,32,0,8,8)
        # pyxel.blt(self.pacman.x,self.pacman.y,0,0,0,8,8)

    def pacman_draw_afet(self):
        if self.pacman.draw_flag == True:
            if self.pacman.count == 9:
                self.pacman.draw_flag = False
                self.pacman.count = 0
                return
            # 0方向なし, 1 上, 2を下, 3を右, 4を左
            # self.vectol = 0
            if self.pacman.vectol == 1:
                self.pacman.y -= 1
            elif self.pacman.vectol == 2:
                self.pacman.y += 1
            elif self.pacman.vectol == 3:
                self.pacman.x += 1
            elif self.pacman.vectol == 4:
                self.pacman.x -= 1
            self.pacman.count += 1
        pyxel.blt(self.pacman.x,self.pacman.y,0,0,0,8,8)
        print("x = {}, y = {}".format(self.pacman.x, self.pacman.y))

        # else:
        #     pyxel.blt(self.pacman.x,self.pacman.y,0,0,0,8,8)

    def pacman_move_after(self):
        # print(pyxel.btn(pyxel.KEY_W))
        if self.pacman.draw_flag == False:
            if pyxel.btnp(pyxel.KEY_W, period = 8):
                if self.map_state.get(self.pacman.tile_x, self.pacman.tile_y - 1) == 3:
                    self.pacman.vectol = 1
                    self.pacman.tile_y = self.pacman.tile_y - 1
                    self.pacman.last_frame_count = pyxel.frame_count
                    print(pyxel.btn(pyxel.KEY_W))
            elif pyxel.btnp(pyxel.KEY_S, period = 8):
                if self.map_state.get(self.pacman.tile_x, self.pacman.tile_y + 1) == 3:
                    self.pacman.vectol = 2
                    self.pacman.tile_y = self.pacman.tile_y + 1
                    self.pacman.last_frame_count = pyxel.frame_count
                    print(pyxel.btn(pyxel.KEY_S))
            elif pyxel.btnp(pyxel.KEY_D, period = 8):
                if self.map_state.get(self.pacman.tile_x + 1, self.pacman.tile_y) == 3:
                    self.pacman.vectol = 3
                    self.pacman.tile_x = self.pacman.tile_x + 1
                    self.pacman.last_frame_count = pyxel.frame_count
                    print(pyxel.btn(pyxel.KEY_D))
            elif pyxel.btnp(pyxel.KEY_A, period = 8):
                if self.map_state.get(self.pacman.tile_x - 1, self.pacman.tile_y) == 3:
                    self.pacman.vectol = 4
                    self.pacman.tile_x = self.pacman.tile_x - 1
                    self.pacman.last_frame_count = pyxel.frame_count
                    print(pyxel.btn(pyxel.KEY_A))
                self.pacman.draw_flag = True
            else:
                 self.pacman.vectol = 0
                 print("not move")



    def pacman_move(self):
        if self.pacman.x % 8 == 0 and self.pacman.y % 8 == 0:
            if self.map_state.get(self.pacman.tile_x + self.pacman.x_change_quantity, self.pacman.tile_y + self.pacman.y_change_quantity) == 33:
                self.pacman.x_change_quantity = 0
                self.pacman.y_change_quantity = 0
                # self.pacman.vectol = 0
            elif pyxel.btn(pyxel.KEY_W):
                if self.map_state.get(self.pacman.tile_x, self.pacman.tile_y - 1) == 5:
                    self.pacman.x_change_quantity =  0
                    self.pacman.y_change_quantity = -1
                    self.pacman.vectol = 1
                # print("KEY_W")
            elif pyxel.btn(pyxel.KEY_S):
                if self.map_state.get(self.pacman.tile_x, self.pacman.tile_y + 1) == 5:
                    self.pacman.x_change_quantity =  0
                    self.pacman.y_change_quantity =  1
                    self.pacman.vectol = 2
            elif pyxel.btn(pyxel.KEY_D):
                if self.map_state.get(self.pacman.tile_x + 1, self.pacman.tile_y) == 5:
                    self.pacman.x_change_quantity =  1
                    self.pacman.y_change_quantity =  0
                    self.pacman.vectol = 3
            elif pyxel.btn(pyxel.KEY_A):
                if self.map_state.get(self.pacman.tile_x - 1, self.pacman.tile_y) == 5:
                    self.pacman.x_change_quantity = -1
                    self.pacman.y_change_quantity =  0
                    self.pacman.vectol = 4
            self.pacman.tile_x += self.pacman.x_change_quantity
            self.pacman.tile_y += self.pacman.y_change_quantity
        # self.pacman.tile_x = int(self.pacman.x/8)
        # self.pacman.tile_y = int(self.pacman.y/8)
        print("pacman.x = {}, pacman.y = {}".format(self.pacman.x, self.pacman.y))
        print("tile_x = {}, tile_y = {}".format(self.pacman.tile_x, self.pacman.tile_y))
        print(self.map_state.get(self.pacman.tile_x, self.pacman.tile_y))
        # print(self.map_state.get(1, 1))

        self.pacman.x += self.pacman.x_change_quantity
        self.pacman.y += self.pacman.y_change_quantity

        # if self.now_frame == 1:
        #     if self.count % 2 == 0:
        #         pyxel.blt(self.x+30,30,0,0,0,8,8)
        #     else:
        #         pyxel.blt(self.x+30,30,0,8,0,8,8)
        # else:
        #     if self.count % 2 == 0:
        #         pyxel.blt(self.x+30,30,0,0,0,8,8)
        #     else:
        #         pyxel.blt(self.x+30,30,0,0,8,8,8)
        # self.count+=1

        # if self.x == 120:
        #     self.now_frame = -1
        # elif self.x == -40:
        #     self.now_frame = 1
        # self.x+=self.now_frame




        # pyxel.blt(0, 88, 0, 0, 88, 160, 32)
        # pyxel.rect(0,0,10,20,5)

    def update(self):
        self.pacman_move()
        # if self.now_frame % 60 == 0:
        # self.pacman_move_after()
        # 「q」キーで終了
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def reset(self):
        self.map_load()
        self.pacman = Pacman()

    def map_load(self):
        load_file = open("map.txt")
        self.map = [[int(x) for x in line.split()] for line in load_file]

    def deback(self):
        # mapをファイルから読めているか
        for i in self.map:
            print(i)

    def deback_draw(self):
        print(pyxel.tilemap(0).data)

    def check_tilemap_state(self):
        pass
        # print(pyxel.tilemap(0).width)
        # print(pyxel.tilemap(0).height)
        # print(pyxel.tilemap(0).data)
        # print(pyxel.tilemap(0).refimg)

        # print(pyxel.tilemap(0).get(0,1))
        # print(pyxel.tilemap(0).get(1,1))
        # print(pyxel.tilemap(0).get(2,1))
        # print(pyxel.tilemap(0).get(3,1))
        # print(pyxel.tilemap(0).get(4,1))
        # print(pyxel.tilemap(0).get(5,1))
        # print(pyxel.tilemap(0).get(6,1))

        # print(pyxel.image)
        # print()
        # print(pyxel.Image(0).get(1,1))
        # print()

if __name__ == '__main__':
    App()
