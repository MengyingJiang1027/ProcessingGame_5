from SpriteAnimated import AnimatedSprite
from Sprite import Sprite
from Button import Button
from Obstacle import Obstacle
import math

alpha = 200


def setup():
    global scr_w, scr_h, frameR
    global bgimg, win_img, lose_img,chest_open_img
    global diamonds, walls, kada, swamp, monsters
    global btns, isGridOn, frameCounter

    # screen and fr init
    size(960, 720)
    scr_w, scr_h = 960, 720
    frameR = 60
    frameRate(frameR)
    isGridOn = False

    # auxiliaries:
    attr_obj_btn = {"btn_x": 4, "btn_y": 180, "btn_w": 80, "btn_h": 90,
                    "msg_x": 100, "msg_y": 150, "msg_w": 550, "msg_h": 150}

    attr_hint_btn = {"btn_x": 4, "btn_y": 380, "btn_w": 80, "btn_h": 90,
                     "msg_x": 100, "msg_y": 400, "msg_w": 500, "msg_h": 300}

    attr_grid_btn = {"btn_x": 4, "btn_y": 20, "btn_w": 80, "btn_h": 50,
                     "msg_x": 0, "msg_y": 0, "msg_w": 0, "msg_h": 0}
    # sprite attributes
    attr_kada = {"x": 100, "y": 395, "w": 70, "h": 90, "speed": 3}
    attr_diamond_1 = {"x": 590, "y": 295, "w": 75, "h": 60}
    attr_diamond_2 = {"x": 640, "y": 245, "w": 75, "h": 60}
    attr_diamond_3 = {"x": 705, "y": 195, "w": 45, "h": 60}
    attr_swamp = {"x":190,"y":0,"w":240,"h":750,"num":-1}

    # enemies
    attr_spider_1 = {"x": 670, "y": 490, "w": 60, "h": 60,
                           "moves_list": ["right", "left"], "arg": 220, "speed": 2}
    attr_spider_2 = {"x": 590, "y": 450, "w": 60, "h": 60,
                           "moves_list": ["down", "up"], "arg": 150, "speed": 1}
    # attr_red_spider = {"x": 94, "y": 72, "w": 60, "h": 60,
    #                    "moves_list": ["right", "left"], "arg": 300, "speed": 3}
    # attr_blue_monster_1 = {"x": 451, "y": 374, "w": 90, "h": 90,
    #                        "moves_list": ["down", "up"], "arg": 175, "speed": 4}
    # attr_blue_monster_2 =   {"x":570,"y":373,"w":80,"h":90,
    #                        "moves_list":["down","up"],"arg":500}

    # walls' attr
    attr_wall_0 = {"x": 0, "y": 0, "w": 180, "h": 80, "num": 0}
    attr_wall_1 = {"x": 4, "y": 157, "w": 130, "h": 280, "num": 1}
    attr_wall_2 = {"x": 0, "y": 521, "w": 194, "h": 200, "num": 2}

    attr_wall_3 = {"x": 445, "y": 0, "w": 320, "h": 115, "num": 3}
    attr_wall_4 = {"x": 446, "y": 125, "w": 85, "h": 210, "num": 4}
    attr_wall_5 = {"x": 541, "y": 120, "w": 110, "h": 110, "num": 5}

    attr_wall_6 = {"x": 651, "y": 555, "w": 310, "h": 170, "num": 6}

    attr_wall_7 = {"x": 668, "y": 381, "w": 300, "h": 110, "num": 7}
    attr_wall_8 = {"x": 755, "y": 255, "w": 200, "h": 60, "num": 8}
    attr_wall_9 = {"x": 830, "y": 190, "w": 130, "h": 60, "num": 9}
    attr_wall_10 = {"x": 710, "y": 320, "w": 250, "h": 60, "num": 10}

    attr_wall_11 = {"x": 490, "y": 550, "w": 90, "h": 170, "num": 11}
    attr_wall_12 = {"x": 803, "y": 0, "w": 150, "h": 45, "num": 12}

    # load btns
    hint_btn = Button(attr=attr_hint_btn,
                      imgs=["/resources/hint_btn.png", "/resources/hint_msg.png"])
    obj_btn = Button(attr=attr_obj_btn,
                     imgs=["/resources/objective_btn.png", "/resources/objective_msg.png"])
    grid_btn = Button(attr=attr_grid_btn,
                      imgs=["/resources/grid_btn.png", "/resources/grid_btn.png"])
    btns = {"hint_btn": hint_btn, "obj_btn": obj_btn, "grid_btn": grid_btn}

    # lose win/lose images:
    win_img = loadImage("/resources/book.png")
    chest_open_img = loadImage("/resources/chest_open.png")
    lose_img = loadImage("/resources/lose.png")

    # load sprite
    kada = AnimatedSprite(x=attr_kada["x"], y=attr_kada["y"],
                          w=attr_kada["w"], h=attr_kada["h"],
                          pics_folder="/resources/kada_moves",
                          scr_w=scr_w, scr_h=scr_h, speed=attr_kada["speed"])
    diamond_1 = Sprite(x=attr_diamond_1["x"], y=attr_diamond_1["y"],
                     w=attr_diamond_1["w"], h=attr_diamond_1["h"],
                     pic="/resources/diamond.png", isVib=False)
    diamond_2 = Sprite(x=attr_diamond_2["x"], y=attr_diamond_2["y"],
                       w=attr_diamond_2["w"], h=attr_diamond_2["h"],
                       pic="/resources/diamond.png", isVib=False)
    diamond_3 = Sprite(x=attr_diamond_3["x"], y=attr_diamond_3["y"],
                       w=attr_diamond_3["w"], h=attr_diamond_3["h"],
                       pic="/resources/book.png", isVib=True)
    swamp = Obstacle(x=attr_swamp["x"], y=attr_swamp["y"],
                     w=attr_swamp["w"], h=attr_swamp["h"], num=-1)

    diamonds = [diamond_1,diamond_2,diamond_3]
    # enemies:
    spider_1 = Sprite(x=attr_spider_1["x"], y=attr_spider_1["y"],
                            w=attr_spider_1["w"], h=attr_spider_1["h"],
                            pic="/resources/spider_1.png",
                            moveList=attr_spider_1["moves_list"],
                            arg=attr_spider_1["arg"], speed=attr_spider_1["speed"])
    spider_2 = Sprite(x=attr_spider_2["x"], y=attr_spider_2["y"],
                            w=attr_spider_2["w"], h=attr_spider_2["h"],
                            pic="/resources/spider_2.png",
                            moveList=attr_spider_2["moves_list"],
                            arg=attr_spider_2["arg"], speed=attr_spider_2["speed"])
    # red_spider = Sprite(x=attr_red_spider["x"], y=attr_red_spider["y"],
    #                     w=attr_red_spider["w"], h=attr_red_spider["h"],
    #                     pic="/resources/red_spider.png",
    #                     moveList=attr_red_spider["moves_list"],
    #                     arg=attr_red_spider["arg"], speed=attr_red_spider["speed"])
    # blue_monster_1 = Sprite(x=attr_blue_monster_1["x"], y=attr_blue_monster_1["y"],
    #                         w=attr_blue_monster_1["w"], h=attr_blue_monster_1["h"],
    #                         pic="/resources/blue_monster.png",
    #                         moveList=attr_blue_monster_1["moves_list"],
    #                         arg=attr_blue_monster_1["arg"], speed=attr_blue_monster_1["speed"])
    # blue_monster_2 = Sprite(x=attr_blue_monster_2["x"], y=attr_blue_monster_2["y"],
    #                     w=attr_blue_monster_2["w"], h=attr_blue_monster_2["h"],
    #                         pic="/resources/blue_monster_2.png")
    monsters = [spider_1, spider_2]

    # walls' init
    wall_0 = Obstacle(x=attr_wall_0["x"], y=attr_wall_0["y"],
                      w=attr_wall_0["w"], h=attr_wall_0["h"], num=attr_wall_0["num"])

    wall_1 = Obstacle(x=attr_wall_1["x"], y=attr_wall_1["y"],
                      w=attr_wall_1["w"], h=attr_wall_1["h"], num=attr_wall_1["num"])

    wall_2 = Obstacle(x=attr_wall_2["x"], y=attr_wall_2["y"],
                      w=attr_wall_2["w"], h=attr_wall_2["h"], num=attr_wall_2["num"])

    wall_3 = Obstacle(x=attr_wall_3["x"], y=attr_wall_3["y"],
                      w=attr_wall_3["w"], h=attr_wall_3["h"], num=attr_wall_3["num"])

    wall_4 = Obstacle(x=attr_wall_4["x"], y=attr_wall_4["y"],
                      w=attr_wall_4["w"], h=attr_wall_4["h"], num=attr_wall_4["num"])

    wall_5 = Obstacle(x=attr_wall_5["x"], y=attr_wall_5["y"],
                      w=attr_wall_5["w"], h=attr_wall_5["h"], num=attr_wall_5["num"])

    wall_6 = Obstacle(x=attr_wall_6["x"], y=attr_wall_6["y"],
                      w=attr_wall_6["w"], h=attr_wall_6["h"], num=attr_wall_6["num"])

    wall_7 = Obstacle(x=attr_wall_7["x"], y=attr_wall_7["y"],
                      w=attr_wall_7["w"], h=attr_wall_7["h"], num=attr_wall_7["num"])

    wall_8 = Obstacle(x=attr_wall_8["x"], y=attr_wall_8["y"],
                      w=attr_wall_8["w"], h=attr_wall_8["h"], num=attr_wall_8["num"])

    wall_9 = Obstacle(x=attr_wall_9["x"], y=attr_wall_9["y"],
                      w=attr_wall_9["w"], h=attr_wall_9["h"], num=attr_wall_9["num"])

    wall_10 = Obstacle(x=attr_wall_10["x"], y=attr_wall_10["y"],
                       w=attr_wall_10["w"], h=attr_wall_10["h"], num=attr_wall_10["num"])

    wall_11 = Obstacle(x=attr_wall_11["x"], y=attr_wall_11["y"],
                       w=attr_wall_11["w"], h=attr_wall_11["h"], num=attr_wall_11["num"])

    wall_12 = Obstacle(x=attr_wall_12["x"], y=attr_wall_12["y"],
                       w=attr_wall_12["w"], h=attr_wall_12["h"], num=attr_wall_12["num"])

    walls = [wall_0, wall_1, wall_2, wall_3, wall_4, wall_5,
             wall_6, wall_7, wall_8, wall_9, wall_10, wall_11,
             wall_12]

    bgimg = loadImage("/resources/bg.png")
    Chinese = createFont("LiSu", 35)
    textFont(Chinese)

    frameCounter = 0

    # $start0
    kada.penup()
    kada.forward(300)
    kada.pendown()
    kada.left(45)
    # kada.forward(400)

    
    
    # $end0


def draw():
    global scr_w, scr_h, frameR
    global bgimg, win_img, lose_img,chest_open_img
    global diamonds, walls, kada, swamp, monsters
    global btns, isGridOn, frameCounter


    # run multiple lines
    kada.runCode()
    updateFrame(kada=kada, frameR=frameR, diamonds=diamonds,
                swamp=swamp, walls=walls, monsters=monsters,
                btns=btns,
                win_img=win_img, lose_img=lose_img)
    frameCounter += 1
    pass


def showMouseXY(scr_w, scr_h, coord_type=0):  # display the current cord of X and Y
    fill(0)
    point(mouseX, mouseY)
    if coord_type == 0:  # origin at the center of the screen
        fill(0)
        textSize(15)
        text("x:" + str(mouseX - scr_w / 2), mouseX + 15, mouseY)
        text("y:" + str(scr_h / 2 - mouseY), mouseX + 60, mouseY)
    else:  # processing's default coord-sys
        fill(255)
        textSize(15)
        text("x:" + str(mouseX), mouseX + 15, mouseY)
        text("y:" + str(mouseY), mouseX + 60, mouseY)


def move_kada(kada, frameR, walls, swamp, diamonds):
    gameCollisionDetect(kada, walls, swamp, diamonds=diamonds, frameR=frameR)
    kada.animationUpdate(frameR=frameR, frameCounter=frameCounter)
    # kada.show()

    # move kada w.r.t the degree parameter
    if kada.isMoving:
        delta_x, delta_y = 0, 0
        if kada.deg >= 0 and kada.deg < 90:
            delta_x = kada.speed * math.cos(radians(kada.deg))
            delta_y = (-1) * kada.speed * math.sin(radians(kada.deg))
        if kada.deg >= 90 and kada.deg < 180:
            delta_x = (-1) * kada.speed * math.cos(radians(180 - kada.deg))
            delta_y = (-1) * kada.speed * math.sin(radians(180 - kada.deg))
        if kada.deg >= 180 and kada.deg < 270:
            delta_x = (-1) * kada.speed * math.cos(radians(kada.deg - 180))
            delta_y = kada.speed * math.sin(radians(kada.deg - 180))
        if kada.deg >= 270 and kada.deg < 360:
            delta_x = kada.speed * math.cos(radians(360 - kada.deg))
            delta_y = kada.speed * math.sin(radians(360 - kada.deg))
        if kada.isBackward:
            kada.x -= int(delta_x)
            kada.y -= int(delta_y)
        else:
            kada.x += int(delta_x)
            kada.y += int(delta_y)
        distance = math.sqrt(math.pow((kada.x - kada.start_x), 2) + math.pow((kada.y - kada.start_y), 2))
        if distance >= kada.stepSize:
            kada.isMoving = False
            kada.start_x = kada.x
            kada.start_y = kada.y

    if kada.isToFly:
        kada.y -= 2
        if abs(kada.y - kada.start_y) > 20:
            kada.isFlying = True
            kada.start_y = kada.y
            kada.isToFly = False
            kada.isMoving = False

    if kada.isToLand:
        kada.y += 2
        if abs(kada.y - kada.start_y) > 20:
            kada.isFlying = False
            kada.start_y = kada.y
            kada.isToLand = False
            kada.isMoving = False


def isCollided(kada, obs):  # collision detection
    # Method: check if the corner touches or within each other.
    kada.rectUpdate()
    obs_corners = obs.corners
    res = []
    # check whether the edges are collided
    if (kada.area["top_left"]["x"] in range(obs_corners["top_left"]["x"], obs_corners["top_right"]["x"])) and \
            (kada.area["top_left"]["y"] in range(obs_corners["top_left"]["y"], obs_corners["bottom_left"]["y"])):
        res.append("top_left")
    if (kada.area["top_right"]["x"] in range(obs_corners["top_left"]["x"], obs_corners["top_right"]["x"])) and \
            (kada.area["top_right"]["y"] in range(obs_corners["top_left"]["y"], obs_corners["bottom_left"]["y"])):
        res.append("top_right")
    if (kada.area["bottom_left"]["x"] in range(obs_corners["top_left"]["x"], obs_corners["top_right"]["x"])) and \
            (kada.area["bottom_left"]["y"] in range(obs_corners["top_left"]["y"], obs_corners["bottom_left"]["y"])):
        res.append("bottom_left")
    if (kada.area["bottom_right"]["x"] in range(obs_corners["top_left"]["x"], obs_corners["top_right"]["x"])) and \
            (kada.area["bottom_right"]["y"] in range(obs_corners["top_left"]["y"], obs_corners["bottom_left"]["y"])):
        res.append("bottom_right")
    return res


def gameCollisionDetect(kada, walls, swamp,diamonds, frameR):
    offset = kada.w // 8
    # kada.show_rect()

    # interaction with walls
    for wall in walls:
        # wall.show(alpha)
        res = isCollided(kada, wall)
        if len(res) != 0:
            kada.isMoving = False
            if ("top_left" in res and "top_right" in res):
                kada.y += offset
            if ("bottom_left" in res and "bottom_left" in res):
                kada.y -= offset
            if ("top_right" in res and "bottom_right" in res):
                kada.x -= offset
            if ("top_left" in res or "bottom_left" in res):
                kada.x += offset

    # losing - monsters
    for monster in monsters:
        if isCollided(kada, monster):
            kada.lose()
            kada.isLose = True

    # losing - swamp
    # swamp.show()
    isLose = isCollided(kada, swamp)
    if ("top_left" in isLose) and ("bottom_left" in isLose) and \
            ("top_right" in isLose) and ("bottom_left" in isLose):
        if kada.isFlying == False:
            kada.isLose = True
            kada.lose()

    # winningdiamonds
    for i,diamond in enumerate(diamonds):
        if kada.isFlying == False:
            if len(isCollided(kada, diamond)) > 0:
                kada.diamond_counter += 1
                diamonds.pop(i)
    if kada.diamond_counter == 3:
        kada.win(frameCounter=frameCounter)

    # screen edge
    if kada.x + kada.w > scr_w:
        kada.isMoving = False
        kada.x -= offset
    if kada.x < 0:
        kada.isMoving = False
        kada.x += offset
    if kada.y < 0:
        kada.isMoving = False
        kada.y += offset
    if kada.y + kada.w > scr_h:
        kada.isMoving = False
        kada.y -= offset


def updateFrame(kada, diamonds, frameR, walls, swamp, monsters,
                btns, win_img, lose_img):
    global isOverGridBtn, isGridOn, frameCounter,chest_open_img
    if kada.isWin:
        # image(chest_open_img, 705,428, 115, 85)

        if kada.win_counter < 2:
            noTint()
            image(bgimg, 0, 0, scr_w, scr_h)
            kada.show()
            kada.win_counter += 1
            pass
        elif kada.win_counter < 20:
            kada.win_counter += 1
            tint(100, 10)
            kada.show()
            image(bgimg, 0, 0, scr_w, scr_h)
            # image(chest_open_img,705,428,115,85)
            kada.win_counter += 1
        else:
            noTint()
            image(win_img, scr_w // 2 - 50, scr_h // 2 - 150, 150, 200)
            fill(255)
            textSize(40)
            text(u"闯关成功！你得到了魔法书！", scr_w // 2 - 250, scr_h // 2 + 125)

    elif kada.isLose:
        if kada.lose_counter < 20:
            kada.lose_counter += 1
            tint(100, 10)
            image(bgimg, 0, 0, scr_w, scr_h)
            kada.show()
            for diamond in diamonds:
                diamond.show_counter(frameCounter)
        else:
            noTint()
            image(lose_img, scr_w // 2 - 50, scr_h // 2 - 150, 200, 200)
            fill(255)
            textSize(40)
            text(u"胜败乃兵家常事，大侠请重新来过！", scr_w // 2 - 250, scr_h // 2 + 125)
    else:
        # --elements to show---
        image(bgimg, 0, 0, scr_w, scr_h)
        stroke(255, 255, 0)

        # line(80, 0, 80, scr_h)  # boarder-seperation

        # grid button
        isOverGridBtn = btns["grid_btn"].showBtn(mouseX, mouseY)
        if isGridOn:
            showGrid(scr_w=960, scr_h=720, isDash=True)

        # direction pointer
        kada.direction(x=40, y=650)
        textSize(15)
        text(u"角度:" + str(kada.deg), 15, 610)

        # show diamonds
        for diamond in diamonds:
            diamond.show_counter(frameCounter)

        # monsters
        for monster in monsters:
            monster.movePath()

        # showMouseXY
        showMouseXY(scr_w - 100, scr_h - 100, coord_type=1)  # 0 for traditional coord; 1 for processing coord

        # move_kada
        move_kada(kada=kada, frameR=frameR, walls=walls, 
                  swamp=swamp, diamonds=diamonds)
        # hint and objective btns
        btns["hint_btn"].show(mouseX, mouseY)
        # btns["obj_btn"].show(mouseX, mouseY)


def showGrid(scr_w, scr_h, isDash=False, interval=5):
    fill(0, 500)
    strokeWeight(1)
    stroke(10)
    for x in range(2, scr_w // 50 + 1):
        if isDash:
            y = 0
            while y < scr_h:
                line(50 * x, y, 50 * x, y + interval)
                y += interval * 2
        else:
            line(50 * x, 0, 50 * x, scr_h)
    for y in range(1, scr_h // 50 + 1):
        if isDash:
            x = 5 * scr_w // 50 + 5
            while x < scr_w:
                line(x, 50 * y, x + interval, 50 * y)
                x += interval * 2
        else:
            line(0, 50 * y, scr_w, 50 * y)
    pass


# **inner event func of processing***
# grid on/off event
def mouseReleased():
    global kada
    global btns, isGridOn, isOverGridBtn
    if isGridOn and isOverGridBtn:
        isGridOn = False
    elif not isGridOn and isOverGridBtn:
        isGridOn = True
    # #-----Testing Purpose Only------
    # if kada.isFlying:
    #     kada.pendown()
    # if not kada.isFlying:
    #     kada.penup()

# ----testing purpose only-----
def keyPressed():
    global kada
    stepSize = 50
    if keyCode == 39: # Right
        kada.right(45)
    if keyCode == 37: # Left
        kada.left(45)
    if keyCode == 40: # Down
        kada.backward(stepSize)
    if keyCode == 38: # UP
        kada.forward(stepSize)
    if keyCode == 85: # letter U
        kada.penup()
    if keyCode == 68: # letter D
        kada.pendown()
