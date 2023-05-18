import pygame
import random
import sys

# 重要数据
black = (20,20,20)
red = (255,0,0)
green = (0,200,0)
dark_green = (0,100,0)
rice = (245,222,179)
grey = (150,150,150)
yellow = (240,200,0)
blue = (30,114,255)
light_yellow = (255,227,132)
light_blue = (135,206,235)
theme = 2
orange = (255,97,0)
rock_brown = (138,54,15)

def init():
    print('输入help以显示更多信息')
    start = input('输入start开始游戏：\n')
    if start == 'start':
        main()
    elif start == 'help':
        maze_help()
    else:
        init()

def maze_help():
    print('游戏名:MAZE\n操作方式：awsd或上下左右键\n游戏规则：将人物方块移动至右下角迷宫出口即为胜利\n作者：祁大帅哥')
    print('游戏指令：\n1.输入back回到游戏\n2.输入theme以调整游戏主题')
    command = input('可在此处输入指令:\n')
    if command == 'back':
        init()
    elif command == 'theme':
        theme_ask()
    else:
        maze_help()

def theme_ask():
    print('1-回到游戏\n2-经典\n3-绿野仙踪\n4-大黄系列\n5-深海遨游\n6-炽热熔岩\n7-敬请期待')
    answer =input('请在此处输入主题(数字):\n')
    global theme
    if answer.isdigit():
        game_theme = int(answer)
        if game_theme == 1:
            init()
        elif game_theme == 2:
            print('主题切换成功！')
            theme = 2
            init()
        elif game_theme == 3:
            print('主题切换成功！')
            theme = 3
            init()
        elif game_theme == 4:
            print('主题切换成功！')
            theme = 4
            init()
        elif game_theme == 5:
            print('主题切换成功！')
            theme = 5
            init()
        elif game_theme == 6:
            print('主题切换成功！')
            theme = 6
            init()
        elif game_theme == 7:
            print('别急啊，会更新的')
            init()
        else:
            theme_ask()
    else:
        theme_ask()

def screen_theme(theme_num): #迷宫墙体的颜色
    if theme_num == 2:
        screen_color = grey
    elif theme_num == 3:
        screen_color = dark_green
    elif theme_num == 4:
        screen_color = yellow
    elif theme_num == 5:
        screen_color = blue
    elif theme_num == 6:
        screen_color = orange
    return screen_color

def path_theme(theme_num): #迷宫路径颜色
    if theme_num == 2:
        path_color = black
    elif theme_num == 3:
        path_color = rice
    elif theme_num == 4:
        path_color = light_yellow
    elif theme_num == 5:
        path_color = light_blue
    elif theme_num == 6:
        path_color = rock_brown
    return path_color

def player_theme(theme_num):
    if theme_num == 2:
        player_color= green
    elif theme_num == 3:
        player_color = red
    elif theme_num == 4:
        player_color = blue
    elif theme_num == 5:
        player_color = yellow
    elif theme_num == 6:
        player_color = yellow
    return player_color


def main():
    dif = input('1-简单\n2-中等\n3-困难\n4-地狱\n请选择难度(1/2/3/4)：\n')
    if dif == '1':
        wid = 660
        hei = 660
        a = 20
        running = True
    elif dif == '2':
        wid = 663
        hei = 663
        a = 13
        running = True
    elif dif == '3':
        wid = 657
        hei = 657
        a = 9
        running = True
    elif dif == '4':
        wid = 665
        hei = 665
        a = 7
        running = True
    elif dif == '5':
        print('还是被你发现了啊。不过没事，发现了也玩不过>0<')
        wid = 665
        hei = 665
        a = 5
        running = True
    else:
        init()
        return


    # 界面创建
    pygame.init()
    screen = pygame.display.set_mode((wid, hei))
    pygame.display.set_caption('MAZE')
    screen.fill(screen_theme(theme))
    t = 0

    # 做迷宫路的方块
    class Cube:
        def __init__(self): #一些通用列表及变量的添加
            self.position = [(1,1)]
            self.block = [(1,1)]
            self.around = []
            self.posx = 1
            self.posy = 1

        def update(self):  #更新。其实可以直接引用draw。但是这样好看点。
            self.draw()

        def getaround(self):   #获取当前坐标下上下左右的空坐标
            self.around = []
            check = [(self.posx - 2, self.posy), (self.posx + 2, self.posy), (self.posx, self.posy - 2),
                     (self.posx, self.posy + 2)]    #先添加上下左右全部坐标
            for item in check:
                if item not in self.block:  #再检查空位坐标
                    self.around.append(item)    #添加空位坐标
            return self.around

        def draw(self):
            pygame.draw.rect(screen, path_theme(theme), pygame.Rect(0,a, a, a), 0)
            pygame.draw.rect(screen, path_theme(theme), pygame.Rect(wid-a, hei-2*a, a, a), 0)
            check_list = []
            for i in range(int((wid-a)/a/2-1)):
                for ii in range(int((hei-a)/a/2-1)):
                    check_list.append((i*2+1,ii*2+1))
            for xx in range(int((wid-a)/a/2)):
                self.block.append((xx*2+1,-1))
                self.block.append((xx*2+1,int(wid/a)))
                for yy in range(int((hei-a)/a/2)):
                    self.block.append((-1,yy*2+1))
                    self.block.append((int(hei/a),yy*2+1))
                    pygame.draw.rect(screen,path_theme(theme),pygame.Rect(xx*2*a+a,yy*2*a+a,a,a),0)
            while self.position:
                self.getaround()
                if self.around:
                    target = self.around[random.randint(0, len(self.around) - 1)]
                    x, y = target
                    if x > self.posx:
                        pygame.draw.rect(screen, path_theme(theme), pygame.Rect((self.posx + 1) * a, (self.posy) * a, a, a))
                        self.block.append((self.posx + 1, self.posy))
                        self.posx += 2
                        self.position.append((self.posx,self.posy))
                        self.block.append((self.posx, self.posy))
                    if x < self.posx:
                        pygame.draw.rect(screen, path_theme(theme), pygame.Rect((self.posx - 1) * a, (self.posy) * a, a, a))
                        self.block.append((self.posx - 1, self.posy))
                        self.posx -= 2
                        self.position.append((self.posx, self.posy))
                        self.block.append((self.posx, self.posy))
                    if y > self.posy:
                        pygame.draw.rect(screen, path_theme(theme), pygame.Rect((self.posx) * a, (self.posy + 1) * a, a, a))
                        self.block.append((self.posx, self.posy + 1))
                        self.posy += 2
                        self.position.append((self.posx, self.posy))
                        self.block.append((self.posx, self.posy))
                    if y < self.posy:
                        pygame.draw.rect(screen, path_theme(theme), pygame.Rect((self.posx) * a, (self.posy - 1) * a, a, a))
                        self.block.append((self.posx,self.posy-1))
                        self.posy -= 2
                        self.position.append((self.posx, self.posy))
                        self.block.append((self.posx, self.posy))
                else:
                    for pos in self.position:
                        self.posx,self.posy = pos
                        self.position.remove(pos)
                        self.getaround()
                        if self.around:
                            break
            return self.block

    class Player:
        def __init__(self):
            self.x = 0
            self.y = a

        def update(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_a] or key[pygame.K_LEFT]:
                if self.x > 0:
                    player.left()
            if key[pygame.K_d] or key[pygame.K_RIGHT]:
                player.right()
            if key[pygame.K_w] or key[pygame.K_UP]:
                player.up()
            if key[pygame.K_s] or key[pygame.K_DOWN]:
                player.down()

        def left(self):
            if (self.x/a-1,self.y/a) in cube.block:
                pygame.draw.rect(screen, path_theme(theme), pygame.Rect(player.x, player.y, a, a))
                self.x -= a
        def right(self):
            if (self.x/a + 1, self.y/a) in cube.block or (self.x,self.y) == (wid - 2*a,hei- 2*a):
                pygame.draw.rect(screen, path_theme(theme), pygame.Rect(player.x, player.y, a, a))
                self.x += a
        def up(self):
            if (self.x/a , self.y/a- 1) in cube.block:
                pygame.draw.rect(screen, path_theme(theme), pygame.Rect(player.x, player.y, a, a))
                self.y -= a
        def down(self):
            if (self.x/a , self.y/a+1) in cube.block:
                pygame.draw.rect(screen, path_theme(theme), pygame.Rect(player.x, player.y, a, a))
                self.y += a


    # 运行代码
    cube = Cube()
    player = Player()
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                init()
        player.update()
        if player.x > wid -2*a:
            pygame.quit()
            print('成功!本次用时：'+str(int(t))+'s')
            restart = input('输入restart重新开始游戏：\n')
            if restart == 'restart':
                init()
            else:
                convince = input('不玩了吗靓仔?\n任意输入-不玩了\nrestart-继续玩\n')
                if convince == 'restart':
                    init()
                else:
                    sys.exit()

        t += 1/16
        cube.update()
        pygame.draw.rect(screen,player_theme(theme),pygame.Rect(player.x, player.y, a, a))
        pygame.display.update()
        clock.tick(16)
    pygame.quit()

init()
