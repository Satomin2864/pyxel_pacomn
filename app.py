import pyxel

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
class Enemy:
    def __init__(self,tile_x, tile_y):
        # 描画されるドットの座標
        self.dot_x = 8 * tile_x
        self.dot_y = 8 * tile_y
        # 敵の進む方向の情報
        self.x_change_quantity = 0
        self.y_change_quantity = 0
        # 0方向なし, 1 上, 2を下, 3を右, 4を左
        self.direction = 0

        # 今いるタイルを座標化する
        self.tile_x = tile_x
        self.tile_y = tile_y
        # いらない説はある
        self.score = 0
        self.update_flag = False
class App:
    def __init__(self):
        # ゲームの設定。widthとheightの単位はドット
        # init(width, height, [caption], [fps])
        pyxel.init(128,140,caption="パックマンぽいゲーム", fps=25)
        # 作成したドット絵やタイルマップの情報を読み込む
        pyxel.load('pacman.pyxel')
        # 追加
        # パックマンクラスをインスタンス生成する
        self.pacman = Pacman()
        self.enemy = Enemy(7,7)
        # 追加
        # タイルマップの情報を持った変数を生成
        self.tilemap_state = pyxel.tilemap(0)
        # 毎フレーム毎にupdateとdrawを呼び出す
        pyxel.run(self.update, self.draw)

    # ゲーム内で扱う情報を更新したり、キー入力の処理などを行う
    def update(self):
        # qキーが押されたらゲームを終了する。
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # 追加：パックマンの移動処理を実装
        self.update_pacman_state()
        # self.update_enemy_state()
        self.update_tilemap()

    def update_enemy_state(self):
        # 描画が終わったら、次の移動判定をする
        if self.enemy.dot_x % 8 == 0 and self.enemy.dot_y % 8 == 0:
            # まずは適当に動くやつ決めるかな
            if self.tilemap_state.get(self.enemy.tile_x + self.enemy.x_change_quantity ,self.enemy.tile_y + self.enemy.y_change_quantity) == 33:
                self.enemy.update_flag = False
            if self.enemy.update_flag == False:
                tmp_x = 0
                tmp_y = 0
                import random as rand
                # TODO
                # 今の実装だと、ここで無限ループ入るから描画が止まる説
                while True:
                    tmp_x = rand.choice([1, -1, 0])
                    tmp_y = rand.choice([1, -1, 0])
                    if abs(tmp_x) != abs(tmp_y):
                        print(self.tilemap_state.get(self.enemy.tile_x + tmp_x ,self.enemy.tile_y + tmp_y))
                        if self.tilemap_state.get(self.enemy.tile_x + tmp_x ,self.enemy.tile_y + tmp_y) != 33:
                            break
                self.enemy.x_change_quantity = tmp_x
                self.enemy.y_change_quantity = tmp_y
                print("tmp_x = {}, tmp_y = {}".format(self.enemy.tile_x + tmp_x,self.enemy.tile_y + tmp_y))
                # self.enemy.update_flag = True
            print(self.tilemap_state.get(self.enemy.tile_x + self.enemy.x_change_quantity,self.enemy.tile_y + self.enemy.y_change_quantity))

            if self.tilemap_state.get(self.enemy.tile_x + self.enemy.x_change_quantity,self.enemy.tile_y + self.enemy.y_change_quantity) == 33:
                # self.enemy.x_change_quantity = 0
                # self.enemy.y_change_quantity = 0
                self.enemy.update_flag = True
            else:
                print("test")
                self.enemy.tile_x += self.enemy.x_change_quantity
                self.enemy.tile_y += self.enemy.x_change_quantity

        self.enemy.dot_x += self.enemy.x_change_quantity
        self.enemy.dot_y += self.enemy.y_change_quantity

    def update_pacman_state(self):
        # 描画が終わったら、次の移動判定をする
        if self.pacman.dot_x % 8 == 0 and self.pacman.dot_y % 8 == 0:
            # 進行方向を確認
            # 壁に行こうとしてたら
            if self.tilemap_state.get(self.pacman.tile_x + self.pacman.x_change_quantity, self.pacman.tile_y + self.pacman.y_change_quantity) == 33:
                # その場所から動かないように値に変える
                self.pacman.x_change_quantity = 0
                self.pacman.y_change_quantity = 0
            # Wキーが押されていた場合に
            elif pyxel.btn(pyxel.KEY_W):
                # 次に移動する先が、背景、クッキー、パワークッキーなら
                if self.tilemap_state.get(self.pacman.tile_x, self.pacman.tile_y - 1) == 5 or self.tilemap_state.get(self.pacman.tile_x, self.pacman.tile_y - 1) == 64 or self.tilemap_state.get(self.pacman.tile_x, self.pacman.tile_y - 1) == 65:
                    # 上に行くように設定
                    self.pacman.x_change_quantity =  0
                    self.pacman.y_change_quantity = -1
                    # 描画する向きを上に設定
                    self.pacman.vectol = 1
            # Sキーが押されていた場合に
            elif pyxel.btn(pyxel.KEY_S):
                # 次に移動する先が、背景、クッキー、パワークッキーなら
                if self.tilemap_state.get(self.pacman.tile_x, self.pacman.tile_y + 1) == 5 or self.tilemap_state.get(self.pacman.tile_x, self.pacman.tile_y + 1) == 64 or self.tilemap_state.get(self.pacman.tile_x, self.pacman.tile_y + 1) == 65:
                    # 下に行くように設定
                    self.pacman.x_change_quantity =  0
                    self.pacman.y_change_quantity =  1
                    # 描画する向きを下に設定
                    self.pacman.vectol = 2
            # Dキーが押されていた場合に
            elif pyxel.btn(pyxel.KEY_D):
                # 次に移動する先が、背景、クッキー、パワークッキーなら
                if self.tilemap_state.get(self.pacman.tile_x + 1, self.pacman.tile_y) == 5 or self.tilemap_state.get(self.pacman.tile_x + 1, self.pacman.tile_y) == 64 or self.tilemap_state.get(self.pacman.tile_x + 1, self.pacman.tile_y) == 65:
                    # 右に行くように設定
                    self.pacman.x_change_quantity =  1
                    self.pacman.y_change_quantity =  0
                    # 描画する向きを右に設定
                    self.pacman.vectol = 3
            # Aキーが押されていた場合に
            elif pyxel.btn(pyxel.KEY_A):
                # 次に移動する先が、背景、クッキー、パワークッキーなら
                if self.tilemap_state.get(self.pacman.tile_x - 1, self.pacman.tile_y) == 5 or self.tilemap_state.get(self.pacman.tile_x - 1, self.pacman.tile_y) == 64 or self.tilemap_state.get(self.pacman.tile_x - 1, self.pacman.tile_y) == 65:
                    # 左にいくように設定
                    self.pacman.x_change_quantity = -1
                    self.pacman.y_change_quantity =  0
                    # 描画する向きを左に設定
                    self.pacman.vectol = 4

            # タイルの座標を進行方向に合わせて変える
            self.pacman.tile_x += self.pacman.x_change_quantity
            self.pacman.tile_y += self.pacman.y_change_quantity

        # 毎フレーム毎に描画する座標を変更していく
        self.pacman.dot_x += self.pacman.x_change_quantity
        self.pacman.dot_y += self.pacman.y_change_quantity

    # ゲーム内で描画されるドット絵の処理をする
    def draw(self):
        # 真っ黒に
        pyxel.cls(0)
        self.draw_tilemap()
        # self.draw_enemy()
        self.draw_pacman()
        self.draw_text()

    # タイルマップの描画処理
    def draw_tilemap(self):
        base_x = 0
        base_y = 0
        tm = 0
        u = 0
        v = 0
        w = 16
        h = 16
        # 指定したtm(template)番号の(u,v)座標から
        # サイズ(w,h)の大きさを(base_x,base_y)座標に描画する
        pyxel.bltm(base_x,base_y,tm,u,v,w,h)

    def draw_pacman(self):
        # 移動しない場合は描画したパックマンの状態をキープ
        if self.pacman.x_change_quantity == 0 and self.pacman.y_change_quantity == 0:
            pass
        else:
            # 口の動きを表現するために、2フレームに１回
            # 丸の状態を表示する
            if pyxel.frame_count % 2 == 0:
                self.pacman.plot_pacman_x_coordinate = 0
            elif self.pacman.vectol == 1:
                # 上向きに開いた口のイメージの座標を設定
                self.pacman.plot_pacman_x_coordinate = 8
            elif self.pacman.vectol == 2:
                # 下向きに開いた口のイメージの座標を設定
                self.pacman.plot_pacman_x_coordinate = 16
            elif self.pacman.vectol == 3:
                # 右向きに開いた口のイメージの座標を設定
                self.pacman.plot_pacman_x_coordinate = 24
            elif self.pacman.vectol == 4:
                # 左向きに開いた口のイメージの座標を設定
                self.pacman.plot_pacman_x_coordinate = 32
        # イメージ０に登録されている(self.pacman.plot_pacman_x_coordinate,0)の座標から
        # 8×8サイズを参照にして、(self.pacman.dot_x,self.pacman.dot_y)の座標に描画する
        pyxel.blt(self.pacman.dot_x,self.pacman.dot_y,0,self.pacman.plot_pacman_x_coordinate,0,8,8)

    def draw_enemy(self):
        pyxel.blt(self.enemy.dot_x,self.enemy.dot_y,0,0,8,8,8)

    def draw_text(self):
        # スコアを表示
        pyxel.text(8,130,"score = {}".format(self.pacman.score),11)

    def update_tilemap(self):
        # ノーマルクッキーはスコア30点追加
        # パワークッキーはスコア100点追加
        # ノーマルクッキーに触れたら
        if self.tilemap_state.get(self.pacman.tile_x,self.pacman.tile_y) == 65:
            self.pacman.score += 30
        # パワークッキーに触れたら
        elif self.tilemap_state.get(self.pacman.tile_x,self.pacman.tile_y) == 64:
            self.pacman.score += 100
        # パックマンがノーマルクッキーとパワークッキーを踏んだら、何もないブロックに変える
        pyxel.tilemap(0).set(self.pacman.tile_x,self.pacman.tile_y,5,refimg=0)



App()
