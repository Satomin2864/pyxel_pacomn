import pyxel
import random as rand

class Pacman:
    def __init__(self):
        """
        pacman自体を生成するクラス
        """
        # 0方向なし, 1 上, 2を下, 3を右, 4を左
        self.direction = 0

        # 描画されるドットの座標
        self.dot_x = 8
        self.dot_y = 8

        # パックマンの進む方向の情報
        self.x_change_quantity = 0
        self.y_change_quantity = 0

        # 今いるタイルを座標化する
        self.tile_x = 1
        self.tile_y = 1

        # 描画するかのフラグ
        self.draw_flag = False

        # どのパックマンをプロットするかの情報
        self.plot_pacman_x_coordinate = 0

        # スコア
        self.score = 0
