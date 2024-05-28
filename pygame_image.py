import os
import sys
import random
import pygame as pg

WIDTH, HEIGHT = 1600, 900

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Score:
    """
    正解の工科トンを選択した場合スコアを加算するクラス
    スコアの色が時間経過とともに変わる
    """
    def __init__(self):
        self.font = pg.font.Font(None, 50)
        self.color = pg.Color(0, 0, 255)
        self.value = 0
        self.image = self.font.render(f"Score: {self.value}", 0, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = 10, 850  # 左下に位置するように調整

    def update(self, screen: pg.Surface, time):
        # 色相を時間経過に応じて変化させる
        hue = (time % 360) / 360  # 0から1の範囲にする
        self.color.hsva = (int(hue * 360), 100, 100, 100)  # 色相を変更
        self.image = self.font.render(f"Score: {self.value}", True, self.color)
        self.rect = self.image.get_rect(topleft=(10, 850))
        screen.blit(self.image, self.rect)

    def add_points(self, points):
        self.value += points


def efect(screen):
    """
    正解のこうかとんとフェイクのこうかとんをランダムで表示する機能
    """
    happy = pg.image.load("fig/6.png") #正解のこうかとんの読み込み
    Ans_rct = [random.randint(0, 1600), random.randint(0, 900)] #ランダムに座標を設定
    #Ans_img = pg.transform.rotozoom(happy, 10, random.uniform(0.5, 1.5))
    #Ans_ex_img = pg.transform.rotozoom(happy, 10, 2.0)
    miss_img_lst = ["fig/0.png", "fig/1.png", "fig/2.png", "fig/3.png", "fig/4.png", "fig/5.png", "fig/7.png", "fig/8.png", "fig/9.png"]
    #フェイク画像の読み込み
    
    rct_x=[] #フェイク画像の座標のリスト 
    rct_y=[]
    for i in range(len(miss_img_lst)):
        # screen.blit(pg.image.load(miss_img_lst[i]), [random.randint(0, 1600), random.randint(0, 900)])
        if i<len(miss_img_lst):
            rct_x.append(random.randint(0,1600)) #ランダムに座標を追加
            rct_y.append(random.randint(0,900))
                         
        else:
            pass

    screen.blit(happy, Ans_rct) #正解のこうかとんを関数内で表示
    return happy, Ans_rct, miss_img_lst, rct_x, rct_y  # 必要な情報をタプルで返す


def check_ans(x,y):
     """
     正解のこうかとんにカーソルが合っているかどうかの判定についての関数
     引数：正解のこうかとんの座標x,y
     """
     pos = pg.mouse.get_pos() #カーソル座標の取得
     if (x-10) <= pos[0] <= (x+65): #こうかとんの座標から猶予範囲内なら
         if (y-10) <= pos[1] <= (y+68):
             return 1 #1を返す
         
class Time():
    """
    時間の表示
    """
    def __init__(self):
        self.font = pg.font.Font(None, 50)
        self.tmr = 5
        self.txt = self.font.render(str(self.tmr), True, (255, 255, 255))
    
    def update(self, screen: pg.Surface):
        self.txt = self.font.render(str(self.tmr), True, (255, 255, 255))
        screen.blit(self.txt, [800, 0])


def GameOver(screen: pg.Surface):
    """
    ゲームオーバー画面の表示
    ブラックアウト画面の設定→文字表示の設定→こうかとん表示の設定
    スクリーン表示とディスプレイ更新
    """
    #screen = pg.display.set_mode((WIDTH, HEIGHT))
    #ゲームオーバー画面
    gm_img = pg.Surface((WIDTH,HEIGHT), pg.SRCALPHA, 32)  #ブラックアウト
    gm_img = gm_img.convert_alpha() #半透明
    screen.blit(gm_img, [0, 0]) #変更点（修正するときは消去）

    gm_rct = gm_img.get_rect()
    gm_rct.center = WIDTH/2, HEIGHT/2
    fonto = pg.font.Font(None,100) 
    txt = fonto.render("Game Over",True,(255, 255, 255))
    #ゲームオーバー画面のこうかとん
    gm_kk_img = pg.transform.rotozoom(pg.image.load("fig/2.png"), 0, 2.0)
    gm_kk_img2 = pg.transform.flip(gm_kk_img,True,False) #画像反転
    screen.blit(gm_img,gm_rct)
    screen.blit(txt,[WIDTH/2 - 170, HEIGHT/2 - 40])
    screen.blit(gm_kk_img, (500,370))
    screen.blit(gm_kk_img2, (1050,370))
    pg.display.update()

def main():
    pg.display.set_caption("見つけろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    Fscreen = pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    #kk_img = pg.transform.rotozoom(kk_img,10,1.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    kk_rct.center = 300,200 #こうかとんの初期位置、表示　->こうかとんをランダムで生成する関数の実装後、削除
    
    score = Score()
    time = Time()
    x=0 #判定の初期位置
    y=0 
    start = 0
    #choice = efect(screen)

    tmr = 0
    while True:
        if start == 0: #最初のゲーム説明画面
            kk_happy = pg.image.load("fig/6.png") #正解のこうかとん
            kk_happy = pg.transform.rotozoom(kk_happy,0,2)
            screen.blit(kk_happy,[WIDTH/2, HEIGHT/2 + 40])
            fonto = pg.font.SysFont("hgp創英角ﾎﾟｯﾌﾟ体",50) 
            txt = fonto.render("Happyこうかとんを探せ！",True,(255, 255, 255))
            screen.blit(txt,[WIDTH/2 - 250, HEIGHT/2 - 40])

            pg.display.update()
            pg.time.wait(5000)
            choice = efect(screen)
            start = 10 #スタート画面を抜ける
            
        x = choice[1][0] #正解のこうかとんの座標を取得
        y = choice[1][1]
        
        for event in pg.event.get():

            if event.type == pg.QUIT:
                return 0
            
            if event.type == pg.MOUSEBUTTONUP: #左クリックされたら 
                ans = check_ans(x,y) #正解のこうかとんかどうか判定
                if ans == 1: #合っていたら
                    #print("a") #確認用
                    score.value += 1 #スコア+1 -> のちにスコア関数組み合わせる
                    
                    ###正解のこうかとんを選べた場合、次の問題に遷移###
                    
                    time.tmr = 5 #タイマーを初期値に戻す
                    choice = efect(screen) #正解・フェイクのこうかとんをランダムに更新

        if time.tmr < 0:
            #ブラックアウトと文字、こうかとんの表示
            print("GameOver")
            GameOver(screen)
            pg.time.wait(5000)  #5秒間止める
            return

        screen.blit(bg_img,[0,0])
        
        for i in range(len(choice[3])):
            screen.blit(pg.image.load(choice[2][i]), [choice[3][i], choice[4][i]])
        
        tmr += 25 #scoreの色を変移するために数値を増やす
        
        score.update(screen,tmr)
        screen.blit(choice[0],choice[1])
        screen.blit(kk_img,kk_rct)
        time.update(screen)
        time.tmr -= 1
        pg.display.update()        
        clock.tick(1)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
