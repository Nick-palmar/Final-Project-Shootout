# Menu
text_instruction = 30
text_play = 30
filler = 255
instruction = False
play = False
hard_mode = False
choose_mode = False

# ball variables
ball_pos = PVector(400, 385)
ball_size = 30
gk_initial_pos = PVector(400, 175)
gk_pos = PVector(400, 175)  # gk is goal keeper
gk_size = 50
gk_radius = gk_size / 2
is_gk_diving = int(random(0, 10))
diving_side = int(random(0, 2))
diving_distance_x = random(1, 74)
diving_height = random(1, 52)
dive_x = diving_distance_x / diving_height
dive_y = diving_distance_x / diving_distance_x

# Power Bar
power_point = PVector(650, 250)
rect_height_point = PVector(power_point.x - 7.5, power_point.y + 15)
rect_height_dim = PVector(15, 265 - power_point.y - 15)
power_change = PVector(0, 0)
# 183 is the y location of where the power will make the ball stop
power_location = 183
distance_to_net = ball_pos.y - power_location
power_miss = 230  # ball power if shot is too short

# Height Bar
bad = color(230, 17, 17)
good = color(17, 230, 34)
height_point = PVector(150, 100)
height_speed = PVector(0, 0)

# Aim Bar
aim_point = PVector(400, 390)
aim_vector = PVector(-50, 0)
rotation_speed = 0
min_aim_point = 350  # minimum x coordinate that the aim line can reach
min_shot_point = 0  # minimum x coordinate that the shot can end up at
max_aim_point = 450  # maximum x coorinate that the aim line can reach
max_shot_point = 800  # maxiumum x cooridnate that the aim line can end up at
good_aim_rect_pos = PVector(388.125, 340)
bad_aim_rect_pos1 = PVector(350, 340)
bad_aim_rect_pos2 = PVector(411.875, 340)


# background variables
grass_pos = PVector(0, 200)
sky_pos = PVector(0, 0)

# status
player_shooting = True
gk_screen_goal = False
gk_screen_miss = False
player_score_once = False
cpu_score_once = False
player_miss_once = False
cpu_miss_once = False
click_number = 0
power_status = False
height_status = False
dive_choice = True
cpu_shooting_status = False
next = False
start_shooting = False
cpu_goal = False
end_game = False

# gk screen variables
cpu_ball_pos = PVector(400, 385)
cpu_ball_size = 30
ball_x_movement_pos = random(290, 510)
ball_y_movement_pos = random(95, 193)
ball_power = int(random(0, 16))
ball_distance = PVector(ball_x_movement_pos - cpu_ball_pos.x,
                        ball_y_movement_pos - cpu_ball_pos.y)
cpu_shot_x = ball_distance.x / ball_distance.y
cpu_shot_y = ball_distance.x / ball_distance.x
dive_pos = PVector(400, 175)

# background variables
grass_pos = PVector(0, 200)
sky_pos = PVector(0, 0)


# Fan variables
red_team = color(230, 17, 17)
blue_team = color(17, 17, 230)
red_fan_pos = PVector(15, 250)
blue_fan_pos = PVector(725, 250)
fan_size = PVector(30, 50)
fan_jump = 210
jump_speed_red = 0
jump_speed_blue = 0
red_fan_head_pos = PVector(15, 215)
blue_fan_head_pos = PVector(725, 215)
head_size = PVector(20, 20)

# score variables
score_player = 0
score_cpu = 0
turn_player = 0
turn_gk = 0

# net
net_pos = PVector(298, 100)

# time bar
time_bar = 150
time_speed = 1
comp_shoot = False

# exit box
exit_box = PVector(0, 425)
exit_game = False


def setup():
    size(800, 500)
    global soccer_background
    soccer_background = loadImage("soccer field.jpg")


def draw():
    # print(time_bar)
    global instruction, text_play, filler
    global text_instruction, play
    global player_shooting, cpu_shooting
    global cpu_shooting_status, hard_mode, choose_mode
    global time_bar, time_speed, go, comp_shoot
    background(255)
    soccer_background.resize(800, 500)
    image(soccer_background, 0, 0)
    fill(255, 255, 255, 160)
    rect(0, 0, 800, 500)
    fill(0)
    textSize(50)
    text("Soccer Shootout", 220, 100)

    textSize(text_instruction)
    text("Instructions", 100, 150)
    textSize(text_play)
    text("Play", 100, 200)

    # instruction
    if mouseX > 100 and mouseX < 270 and mouseY > 100 and mouseY < 150:
        text_instruction = 50
    else:
        text_instruction = 30
    if instruction is True:
        background(255)
        image(soccer_background, 0, 0)
        fill(255, 255, 255, 160)
        rect(0, 0, 800, 500)
        fill(0)
        textSize(30)
        text("Instructions:", 300, 80)
        textSize(20)
        text(
            "Take turns between you and the computer to shoot the ball",
            80, 200)
        text(
            "When it's your turn click when you want the corresponding " +
            "bar to stop", 80, 225)
        text("When it's the computer's turn to shoot tap on the ball", 80, 250)
        text("then tap anywhere on the net to stop the ball", 100, 275)
        fill(255)
        rect(700, 400, 100, 100)
        fill(0)
        if mouseX > 700 and mouseX < 800 and mouseY > 400 and mouseY < 500:
            back = 5
        else:
            back = 0
        textSize(10 + back)
        text("<-- BACK", 720, 450)

    # play
    if mouseX > 100 and mouseX < 160 and mouseY > 150 and mouseY < 200:
        text_play = 50
    else:
        text_play = 30
    # print(play)
    if play is True:
        if choose_mode is False:
            image(soccer_background, 0, 0)
            fill(255, 255, 255, 160)
            rect(0, 0, 800, 500)
            textSize(50)
            fill(0)
            text("Difficulty", 300, 100)

            # mode choice
            if mouseX > 100 and mouseX < 200 and mouseY > 100 and mouseY < 150:
                easy_text = 10
            else:
                easy_text = 0
            textSize(30 + easy_text)
            text("Easy", 100, 150)
            if mouseX > 100 and mouseX < 200 and mouseY > 150 and mouseY < 200:
                hard_text = 10
            else:
                hard_text = 0
            textSize(30 + hard_text)
            textSize(30 + hard_text)

            text("Hard", 100, 200)

            # print(mouseX, mouseY)
        elif choose_mode is True:
            if player_shooting is True:
                background(100, 255, 10)
                global click_number, gk_pos, gk_size, ball_radius, gk_radius
                global power_point, rect_height_point, rect_height_dim
                global power_change, power_location
                global power_status, turn_player, turn_gk
                global ball_pos, ball_size, shot_y, shot_x, play
                global bad, good, height_point, height_speed, height_power
                global height_status
                global net_pos, distance_to_net, aim, dive_x, dive_y
                global aim_point, aim_vector, rotation_speed, bad_aim_rect_pos1
                global good_aim_rect_pos, bad_aim_rect_pos2
                global diving_distance_x, is_gk_diving
                global diving_side, diving_height
                global grass_pos, sky_pos, power_miss, end_game
                global player_score_once, player_miss_once
                global next, score_player, score_cpu, exit_game, exit_box
                ball_to_gk_vect = PVector.sub(gk_pos, ball_pos)
                ball_to_gk_dist = ball_to_gk_vect.mag()
                ball_radius = ball_size / 2

                background(255)

                # grass
                noStroke()
                fill(100, 255, 0)
                rect(grass_pos.x, grass_pos.y, 800, 300)
                # Lines
                fill(255)
                noStroke()
                rectMode(CENTER)
                # inner box
                rect(230, 250, 10, 100)
                rect(570, 250, 10, 100)
                rect(400, 295, 350, 10)
                # outer box
                rect(100, 320, 10, 300)
                rect(700, 320, 10, 300)
                rect(400, 470, 610, 10)
                fill(255, 255, 255, 0)
                stroke(255)
                strokeWeight(10)
                ellipse(400, 470, 200, 130)
                fill(100, 255, 0)
                rectMode(CORNER)
                noStroke()
                rect(250, 400, 300, 65)
                # stroke(0)

                # sky
                noStroke()
                fill(0, 100, 255)
                rect(sky_pos.x, sky_pos.y, 800, 200)

                # exit box
                fill(255)
                stroke(0)
                strokeWeight(1)
                rect(exit_box.x, exit_box.y, 75, 75)
                fill(0)
                textSize(20)
                text("Exit", 15, 470)

                # Power Arrow
                noStroke()
                fill(0)
                textSize(20)
                text("Power(3)", power_point.x - 45, 430)

                fill(0)
                triangle(
                    power_point.x, power_point.y, power_point.x - 25,
                    power_point.y + 15, power_point.x + 25, power_point.y + 15)
                rect(
                    rect_height_point.x, rect_height_point.y,
                    rect_height_dim.x, rect_height_dim.y)

                if power_point.y >= 250 or power_point.y <= 175:
                    power_change = power_change.mult(-1)

                power_point.add(power_change)
                rect_height_dim = PVector(15, -(265 - power_point.y - 15))

                # net
                fill(255)
                stroke(0)
                strokeWeight(2)
                rect(net_pos.x, net_pos.y, 204, 100)

                # goalkeeper
                fill(255, 0, 0)
                noStroke()
                ellipse(gk_pos.x, gk_pos.y, gk_size, gk_size)

                # gk random diving
                if click_number == 3:
                    if is_gk_diving <= 2:  # no movement
                        gk_pos.x = gk_pos.x
                        gk_pos.y = gk_pos.y
                    elif is_gk_diving >= 3:  # movement
                        if diving_side == 0:  # dive left
                            if gk_pos.x >= (gk_initial_pos.x -
                                            diving_distance_x):
                                gk_pos.x -= dive_x
                            if gk_pos.y >= gk_initial_pos.y - diving_height:
                                gk_pos.y -= dive_y

                        elif diving_side == 1:
                            if gk_pos.x <= (gk_initial_pos.x +
                                            diving_distance_x):
                                gk_pos.x += dive_x
                            if gk_pos.y >= gk_initial_pos.y - diving_height:
                                gk_pos.y -= dive_y

                # Height Bar
                fill(0)
                textSize(20)
                text("Height(1)", 125, 430)

                stroke(0)
                strokeWeight(2)
                fill(bad)
                rect(150, 0, 20, 200)

                fill(good)
                rect(150, 200, 20, 200)

                stroke(0)
                strokeWeight(5)
                fill(0)
                line(
                    height_point.x, height_point.y,
                    height_point.x + 20, height_point.y)

                height_point.add(height_speed)

                if height_point.y >= 400:
                    height_speed = height_speed.mult(-1)
                elif height_point.y <= 0:
                    height_speed = height_speed.mult(-1)

                # Aim boundary good
                stroke(0)
                strokeWeight(2)
                fill(good)
                rect(good_aim_rect_pos.x, good_aim_rect_pos.y, 23.75, 60)

                # Aim boundary bad 1
                fill(bad)
                rect(bad_aim_rect_pos1.x, bad_aim_rect_pos1.y, 38.125, 60)

                # Aim boundary bad 2
                fill(bad)
                rect(bad_aim_rect_pos2.x, bad_aim_rect_pos2.y, 38.125, 60)

                # Aim Line
                fill(0)
                textSize(20)
                text("Direction(2)", 360, 430)

                line(
                    aim_point.x, aim_point.y, aim_point.x + aim_vector.x,
                    aim_point.y + aim_vector.y)
                line_angle = degrees(aim_vector.heading())
                if line_angle < -180 or line_angle > 0:
                    rotation_speed = -rotation_speed
                aim_vector.rotate(rotation_speed)

                # ball moving to bottom of net
                if power_point.y < 200:
                    if click_number == 3:
                        if ball_pos.y >= 184:
                            power_status = True
                            if power_location + height_power.y == 185:
                                if ball_pos.y <= 190:
                                    power_status = False
                            if power_status is True:
                                ball_pos.y -= shot_y * 5
                                ball_pos.x += shot_x * 5
                                ball_size = ball_size * 0.98
                                ball_radius = ball_size / 2
                        else:
                            power_status = False
                else:
                    if click_number == 3:
                        if ball_pos.y >= power_miss:
                            power_status = True
                            if power_status is True:
                                ball_pos.y -= shot_y * 5
                                ball_pos.x += shot_x * 5
                                ball_size = ball_size * 0.98
                        else:
                            power_status = False

                # ball moving up the net
                if (ball_pos.y <= 185 and
                    ball_pos.y > power_location + height_power.y and
                        power_status is False):
                    height_status = True
                    if height_status is True:
                        ball_pos.y -= shot_y * 5
                        ball_pos.x += shot_x * 5
                else:
                    height_status = False

                    # goal or miss detection
                    if (ball_pos.x > net_pos.x + ball_radius and
                        ball_pos.x < (net_pos.x + 204) - ball_radius and
                        ball_pos.y > net_pos.y + ball_radius and
                        ball_pos.y < (net_pos.y + 100) - ball_radius and
                        abs(ball_to_gk_dist) > ball_radius + gk_radius and
                        click_number == 3 and height_status is False and
                            power_status is False):
                        textSize(32)
                        text("GOAL", 360, 200)
                        fill(255)
                        text("next", 700, 50)
                        next = True

                        if player_score_once is False:
                            score_player += 1
                            turn_player += 1
                            player_score_once = True
                        else:
                            score_player += 0

                    elif ((ball_pos.x < net_pos.x + ball_radius or
                            ball_pos.x > (net_pos.x + 204) - ball_radius or
                            ball_pos.y < net_pos.y + ball_radius or
                            ball_pos.y > (net_pos.y + 100) - ball_radius or
                            abs(ball_to_gk_dist) < ball_radius + gk_radius) and
                            click_number == 3 and height_status is False and
                            power_status is False):
                        textSize(32)
                        text("MISS", 360, 200)
                        fill(255)
                        text("next", 700, 50)
                        next = True
                        if player_miss_once is False:
                            turn_player += 1
                            player_miss_once = True

                # ball
                fill(0)
                ellipse(ball_pos.x, ball_pos.y, ball_size, ball_size)

                # score
                fill(255)
                textSize(20)
                text("Player:" + str(score_player), 10, 20)

                fill(255)
                textSize(20)
                text("CPU:" + str(score_cpu), 730, 20)

                if turn_player == 4:
                    if abs(score_player - score_cpu) >= 3:
                        winner = max(score_player, score_cpu)
                        end_game = True
                        if max(score_player, score_cpu) is score_cpu:
                            textSize(40)
                            text("You Lose!", 300, 250)
                        elif max(score_player, score_cpu) is score_player:
                            textSize(40)
                            text("You Win!", 300, 250)
                elif turn_player == 5:
                    if abs(score_player - score_cpu) >= 2:
                        winner = max(score_player, score_cpu)
                        end_game = True
                        if max(score_player, score_cpu) is score_cpu:
                            textSize(40)
                            text("You Lose!", 300, 250)
                        elif max(score_player, score_cpu) is score_player:
                            textSize(40)
                            text("You Win!", 300, 250)

            elif player_shooting is not True:
                global turn_player, turn_gk, cpu_miss_once
                global grass_pos, sky_pos, net_pos, gk_size, gk_pos
                global dive_choice, dive_pos, ball_x_movement_pos
                global ball_y_movement_pos, ball_power, ball_distance
                global cpu_shot_x, cpu_shot_y, cpu_shooting_status
                global start_shooting, jump_speed_red, head_size
                global jump_speed_blue, red_fan_head_pos, blue_fan_head_pos
                global gk_screen_goal, gk_screen_miss, click_number, cpu_goal
                global cpu_ball_pos, fan_size, blue_fan_pos, fan_jump
                global red_fan_pos, cpu_ball_size, cpu_ball_radius
                global cpu_score_once, score_player, score_cpu
                global end_game
                global comp_shoot, time_bar, time_speed, exit_box, exit_game

                cpu_ball_radius = cpu_ball_size / 2
                ball_to_gk_vect2 = PVector.sub(cpu_ball_pos, dive_pos)
                ball_to_gk_dist2 = ball_to_gk_vect2.mag()

                background(255)

                # grass
                noStroke()
                fill(100, 255, 0)
                rect(grass_pos.x, grass_pos.y, 800, 300)

                rect(grass_pos.x, grass_pos.y, 800, 300)
                # Lines
                fill(255)
                noStroke()
                rectMode(CENTER)
                # inner box
                rect(230, 250, 10, 100)
                rect(570, 250, 10, 100)
                rect(400, 295, 350, 10)
                # outer box
                rect(100, 320, 10, 300)
                rect(700, 320, 10, 300)
                rect(400, 470, 610, 10)
                fill(255, 255, 255, 0)
                stroke(255)
                strokeWeight(10)
                ellipse(400, 470, 200, 130)
                fill(100, 255, 0)
                rectMode(CORNER)
                noStroke()
                rect(250, 400, 300, 65)

                # sky
                noStroke()
                fill(0, 100, 255)
                rect(sky_pos.x, sky_pos.y, 800, 200)

                # exit box
                fill(255)
                stroke(0)
                strokeWeight(1)
                rect(exit_box.x, exit_box.y, 75, 75)
                fill(0)
                textSize(20)
                text("Exit", 15, 470)

                # net
                fill(255)
                stroke(0)
                strokeWeight(2)
                rect(net_pos.x, net_pos.y, 204, 100)

                # gk blue outline/fill
                if dive_choice is True:
                    fill(255)
                    stroke(0, 0, 200)
                    ellipse(dive_pos.x, dive_pos.y, gk_size, gk_size)
                    fill(0)
                    textSize(20)
                    text("Click(2)", 370, 140)
                elif dive_choice is False:
                    fill(0, 0, 200)
                    ellipse(dive_pos.x, dive_pos.y, gk_size, gk_size)

                # Red, cpu fan sign
                fill(255)
                stroke(0)
                rect(0, 350, 90, 30)
                fill(0)
                textSize(18)
                text("CPU fans", 1, 370)

                # red fans
                fill(red_team)
                noStroke()
                for x in range(0, 61, 30):
                    for y in range(205, 276, 70):
                        ellipse(red_fan_pos.x + x, red_fan_pos.y + y - 205,
                                fan_size.x, fan_size.y)
                        ellipse(red_fan_head_pos.x + x,
                                red_fan_head_pos.y + y - 205,
                                head_size.x, head_size.y)
                red_fan_pos.y += jump_speed_red
                red_fan_head_pos.y += jump_speed_red

                # Blue, player fan sign
                fill(255)
                stroke(0)
                rect(710, 350, 90, 30)
                fill(0)
                textSize(18)
                text("Player fans", 711, 370)

                # blue fan variables
                fill(blue_team)
                noStroke()
                for x in range(710, 771, 30):
                    for y in range(205, 276, 70):
                        ellipse(blue_fan_pos.x + x - 710,
                                blue_fan_pos.y + y - 205, fan_size.x,
                                fan_size.y)
                        ellipse(blue_fan_head_pos.x + x - 710,
                                blue_fan_head_pos.y + y - 205,
                                head_size.x, head_size.y)

                blue_fan_pos.y += jump_speed_blue
                blue_fan_head_pos.y += jump_speed_blue

                fill(0)
                rect(325, 430, 150, 30)
                fill(255)
                rect(325, 430, time_bar, 30)
                if comp_shoot is True:
                    time_bar -= time_speed
                    if time_bar <= 0:
                        time_speed = 0
                        cpu_shooting_status = True
                        start_shooting = True
                        cpu_shooting_status = True

                if start_shooting is True:
                    # cpu random shot generation
                    if cpu_shooting_status is True:
                        if ball_power == 0:
                            ball_y_movement_pos = 250
                            if cpu_ball_pos.y >= ball_y_movement_pos:
                                if hard_mode is True:
                                    cpu_ball_pos.x += (cpu_shot_x * 10)
                                    cpu_ball_pos.y -= (cpu_shot_y * 10)
                                    cpu_ball_size *= 0.97
                                else:
                                    cpu_ball_pos.x += (cpu_shot_x * 5)
                                    cpu_ball_pos.y -= (cpu_shot_y * 5)
                                    cpu_ball_size *= 0.98
                            else:
                                cpu_shooting_status = False
                        elif ball_power >= 1:
                            if cpu_ball_pos.y >= ball_y_movement_pos:
                                if hard_mode is True:
                                    cpu_ball_pos.x += (cpu_shot_x * 10)
                                    cpu_ball_pos.y -= (cpu_shot_y * 10)
                                    cpu_ball_size *= 0.97
                                else:
                                    cpu_ball_pos.x += (cpu_shot_x * 5)
                                    cpu_ball_pos.y -= (cpu_shot_y * 5)
                                    cpu_ball_size *= 0.98
                            else:
                                cpu_shooting_status = False

                    if ((cpu_ball_pos.x > net_pos.x + cpu_ball_radius and
                        cpu_ball_pos.x < (net_pos.x + 204) -
                        cpu_ball_radius and cpu_ball_pos.y > net_pos.y +
                        cpu_ball_radius and cpu_ball_pos.y <
                        (net_pos.y + 100) - cpu_ball_radius and
                        abs(ball_to_gk_dist2) >
                        (cpu_ball_radius + gk_radius) and click_number >= 1 and
                        click_number <= 2 and cpu_shooting_status is False) or
                            cpu_goal is True):
                        fill(0)
                        textSize(32)
                        text("GOAL", 360, 200)
                        gk_screen_goal = True
                        cpu_goal = True
                        if cpu_score_once is False:
                            score_cpu += 1
                            turn_gk += 1
                            cpu_score_once = True
                        else:
                            score_cpu += 0
                    elif ((cpu_ball_pos.x <= net_pos.x + cpu_ball_radius or
                            cpu_ball_pos.x >= (net_pos.x + 204) -
                            cpu_ball_radius or cpu_ball_pos.y <= net_pos.y +
                            cpu_ball_radius or cpu_ball_pos.y >=
                            (net_pos.y + 100) - cpu_ball_radius or
                            abs(ball_to_gk_dist2) <=
                            (cpu_ball_radius + gk_radius)) and
                            click_number >= 1 and click_number <= 2 and
                            cpu_shooting_status is False and
                            cpu_goal is False):
                        textSize(32)
                        fill(0)
                        text("MISS", 360, 200)
                        gk_screen_miss = True
                        if cpu_miss_once is False:
                            turn_gk += 1
                            cpu_miss_once = True
                        # text("next", 700, 50)
                        # next = True

                    # red fan jump
                    if gk_screen_goal is True:
                        if red_fan_pos.y > 250:
                            gk_screen_goal = False
                            jump_speed_red = 0
                            fill(255)
                            text("next", 700, 50)
                            next = True
                        elif red_fan_pos.y >= fan_jump:
                            if jump_speed_red == 0:
                                jump_speed_red = -1
                        elif red_fan_pos.y < fan_jump:
                            if jump_speed_red == -1:
                                jump_speed_red = 1
                    # blue fan jump
                    elif gk_screen_miss is True:
                        if blue_fan_pos.y > 250:
                            gk_screen_miss = False
                            jump_speed_blue = 0
                            fill(255)
                            text("next", 700, 50)
                            next = True
                        elif blue_fan_pos.y >= fan_jump:
                            if jump_speed_blue == 0:
                                jump_speed_blue = -1
                        elif blue_fan_pos.y < fan_jump:
                            if jump_speed_blue == -1:
                                jump_speed_blue = 1

                # cpu ball
                fill(0)
                stroke(0)
                ellipse(cpu_ball_pos.x, cpu_ball_pos.y,
                        cpu_ball_size, cpu_ball_size)
                textSize(20)
                text("Click(1)", 370, 420)

                fill(255)
                textSize(20)
                text("Player:" + str(score_player), 10, 20)

                fill(255)
                textSize(20)
                text("CPU:" + str(score_cpu), 730, 20)

                if play is True:
                    if turn_gk == 3:
                        if abs(score_player - score_cpu) >= 3:
                            winner = max(score_player, score_cpu)
                            end_game = True
                            if max(score_player, score_cpu) is score_cpu:
                                textSize(40)
                                text("You Lose!", 300, 250)
                            elif max(score_player, score_cpu) is score_player:
                                textSize(40)
                                text("You Win!", 300, 250)
                    elif turn_gk == 4:
                        if abs(score_player - score_cpu) >= 2:
                            end_game = True
                            winner = max(score_player, score_cpu)
                            if max(score_player, score_cpu) is score_cpu:
                                textSize(40)
                                text("You Lose!", 300, 250)
                            elif max(score_player, score_cpu) is score_player:
                                textSize(40)
                                text("You Win!", 300, 250)
                    elif turn_gk >= 5:
                        if abs(score_player - score_cpu) >= 1:
                            winner = max(score_player, score_cpu)
                            end_game = True
                            if max(score_player, score_cpu) is score_cpu:
                                textSize(40)
                                text("You Lose!", 300, 250)
                            elif max(score_player, score_cpu) is score_player:
                                textSize(40)
                                text("You Win!", 300, 250)


def mousePressed():
    global bad, good, height_point, height_speed, text_play
    global aim_point, aim_point1, rotation_speed
    global click_number, power, power_point
    global ball_direction, power_change, shot_x, shot_y
    global height_power, power_location, total_y_distance, distance_to_net
    global min_aim_point, min_shot_point, max_shot_point, max_aim_point
    global ball_pos, ball_size
    global gk_pos, next, rotation_speed, hard_mode
    global player_shooting
    global time_bar, time_speed, comp_shoot
    if choose_mode is True:
        if player_shooting is True:
            if click_number == 0:
                height_speed = height_speed.mult(0)
                click_number += 1
                # print(height_point.y)
                if height_point.y >= 391:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 20)))))
                elif height_point.y >= 381:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 19)))))
                elif height_point.y >= 371:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 18)))))
                elif height_point.y >= 361:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 17)))))
                elif height_point.y >= 351:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 16)))))
                elif height_point.y >= 341:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 15)))))
                elif height_point.y >= 331:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 14)))))
                elif height_point.y >= 321:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 13)))))
                elif height_point.y >= 311:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 12)))))
                elif height_point.y >= 301:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 11)))))
                elif height_point.y >= 291:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 10)))))
                elif height_point.y >= 281:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 9)))))
                elif height_point.y >= 271:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 8)))))
                elif height_point.y >= 261:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 7)))))
                elif height_point.y >= 251:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 6)))))
                elif height_point.y >= 241:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 5)))))
                elif height_point.y >= 231:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 4)))))
                elif height_point.y >= 221:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 3)))))
                elif height_point.y >= 211:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 2)))))
                elif height_point.y >= 201:
                    height_power = PVector(
                        0, (-(power_location - (115 + (3.5 * 1)))))
                elif height_point.y == 200:
                    height_power = PVector(0, -80)
                else:
                    height_power = PVector(0, - 100)

                # print(height_power)
                total_y_distance = distance_to_net - height_power.y
                if hard_mode is True:
                    rotation_speed = 0.07
                elif hard_mode is False:
                    rotation_speed = 0.014

            elif click_number == 1:
                rotation_speed = 0
                aim_x = 400 + aim_vector.x
                aim = (
                        (aim_x - min_aim_point) *
                        ((aim_point.x - min_shot_point) /
                            (aim_point.x - min_aim_point)))
                # print(aim)
                relative_aim = aim - 400
                shot_x = relative_aim / total_y_distance
                shot_y = shot_x / shot_x
                click_number += 1
                if hard_mode is True:
                    power_change = PVector(0, 8)
                else:
                    power_change = PVector(0, 3)

            elif click_number == 2:
                power_change = power_change.mult(0)
                power = PVector(0, rect_height_dim.y + 15)
                click_number += 1
        elif player_shooting is False:
            global dive_choice
            global dive_pos
            global start_shooting
            global click_number, cpu_shooting_status
            if start_shooting is False:
                if (mouseX > 385 and mouseX < 415 and
                        mouseY > 370 and mouseY < 400):
                    comp_shoot = True
                    click_number += 1
            if dive_choice is True:
                if (mouseX > 298 and mouseX < 298 + 204 and
                        mouseY > 100 and mouseY < 200):
                    # print(mouseX, mouseY)
                    dive_pos = PVector(mouseX, mouseY)
                    dive_choice = False
                    click_number += 1


def mouseClicked():
    global next, dive_choice, ball_x_movement_pos, ball_y_movement_pos
    global instruction, play, cpu_ball_pos, cpu_ball_size, dive_pos, ball_power
    global ball_distance, aim_vector
    global click_number, power_change, ball_size
    global start_shooting, cpu_shot_x, cpu_shot_y
    global player_shooting, ball_pos, gk_pos, height_speed, rotation_speed
    global player_score_once, cpu_score_once, is_gk_diving, diving_side
    global turn_player, turn_gk
    global diving_distance_x, diving_height, dive_x, dive_y, cpu_goal
    global height_point, end_game, choose_mode
    global gk_screen_goal, gk_screen_miss, jump_speed_red, jump_speed_blue
    global red_fan_head_pos, blue_fan_head_pos, blue_fan_pos, red_fan_pos
    global power_point, rect_height_point, rect_height_dim
    global cpu_miss_once, player_miss_once
    global time_bar, comp_shoot, time_speed
    global score_player, score_cpu, hard_mode, exit_game

    # instructions
    if instruction is False:
        if mouseX > 100 and mouseX < 270 and mouseY > 100 and mouseY < 150:
            instruction = True
    if instruction is True:
        if mouseX > 700 and mouseX < 800 and mouseY > 400 and mouseY < 500:
            instruction = False
    # print(instruction)

    # play
    if play is False:
        if mouseX > 100 and mouseX < 160 and mouseY > 150 and mouseY < 200:
            play = True

    elif choose_mode is False:
        if mouseX > 100 and mouseX < 300 and mouseY > 100 and mouseY < 150:
            hard_mode = False
            choose_mode = True
            click_number = 0
            height_speed = PVector(0, 5)

        elif mouseX > 100 and mouseX < 300 and mouseY > 150 and mouseY < 200:
            hard_mode = True
            choose_mode = True
            click_number = 0
            height_speed = PVector(0, 15)

    if play is True:
        if mouseX > 0 and mouseX < 75 and mouseY > 425 and mouseY < 500:
            exit_game = True

    if (player_shooting is True and next is True and
            mouseX > 700 and mouseX < 800 and mouseY > 0 and mouseY < 100):
        player_shooting = False
        cpu_ball_pos = PVector(400, 385)
        dive_pos = PVector(400, 175)
        cpu_ball_size = 30
        click_number = 0
        cpu_score_once = False
        dive_choice = True
        start_shooting = False
        cpu_shooting_status = False
        ball_x_movement_pos = random(290, 510)
        ball_y_movement_pos = random(95, 193)
        ball_power = int(random(0, 16))
        ball_distance = PVector(ball_x_movement_pos - cpu_ball_pos.x,
                                ball_y_movement_pos - cpu_ball_pos.y)
        cpu_shot_x = ball_distance.x / ball_distance.y
        cpu_shot_y = ball_distance.x / ball_distance.x
        next = False
        cpu_goal = False
        gk_screen_goal = False
        gk_screen_miss = False
        jump_speed_red = 0
        jump_speed_blue = 0
        red_fan_head_pos = PVector(15, 215)
        blue_fan_head_pos = PVector(725, 215)
        red_fan_pos = PVector(15, 250)
        blue_fan_pos = PVector(725, 250)
        cpu_miss_once = False
        comp_shoot = False
        time_bar = 150
        time_speed = 1
        if end_game is True:
            play = False
            end_game = False
            score_player = 0
            score_cpu = 0
            choose_mode = False
            hard_mode = False
            turn_player = 0
            turn_gk = 0
            instrction = False
            player_shooting = True

    elif (player_shooting is False and next is True and mouseX > 700 and
            mouseX < 800 and mouseY > 0 and mouseY < 100):
        player_shooting = True
        click_number = 0
        player_score_once = False
        ball_pos = PVector(400, 385)
        gk_pos = PVector(400, 175)
        height_speed = PVector(0, 10)
        height_point = PVector(150, 100)
        rotation_speed = 0
        power_change = PVector(0, 0)
        ball_size = 30
        next = False
        gk_pos = PVector(400, 175)  # gk is goal keeper
        is_gk_diving = int(random(0, 10))
        diving_side = int(random(0, 2))
        diving_distance_x = random(1, 74)
        diving_height = random(1, 52)
        dive_x = diving_distance_x / diving_height
        dive_y = diving_distance_x / diving_distance_x
        power_point = PVector(650, 250)
        rect_height_point = PVector(power_point.x - 7.5, power_point.y + 15)
        rect_height_dim = PVector(15, 265 - power_point.y - 15)
        player_miss_once = False
        aim_vector = PVector(-50, 0)
        if end_game is True:
            play = False
            end_game = False
            score_player = 0
            score_cpu = 0
            choose_mode = False
            hard_mode = False
            turn_player = 0
            turn_gk = 0
            instruction = False
            player_shooting = True

    if exit_game is True:
        player_shooting = True
        click_number = 0
        player_score_once = False
        ball_pos = PVector(400, 385)
        gk_pos = PVector(400, 175)
        height_speed = PVector(0, 10)
        height_point = PVector(150, 100)
        rotation_speed = 0
        power_change = PVector(0, 0)
        ball_size = 30
        aim_vector = PVector(-50, 0)
        next = False
        gk_pos = PVector(400, 175)  # gk is goal keeper
        is_gk_diving = int(random(0, 10))
        diving_side = int(random(0, 2))
        diving_distance_x = random(1, 74)
        diving_height = random(1, 52)
        dive_x = diving_distance_x / diving_height
        dive_y = diving_distance_x / diving_distance_x
        power_point = PVector(650, 250)
        rect_height_point = PVector(power_point.x - 7.5, power_point.y + 15)
        rect_height_dim = PVector(15, 265 - power_point.y - 15)
        player_miss_once = False
        cpu_ball_pos = PVector(400, 385)
        dive_pos = PVector(400, 175)
        cpu_ball_size = 30
        cpu_score_once = False
        dive_choice = True
        start_shooting = False
        cpu_shooting_status = False
        ball_x_movement_pos = random(290, 510)
        ball_y_movement_pos = random(95, 193)
        ball_power = int(random(0, 16))
        ball_distance = PVector(ball_x_movement_pos - cpu_ball_pos.x,
                                ball_y_movement_pos - cpu_ball_pos.y)
        cpu_shot_x = ball_distance.x / ball_distance.y
        cpu_shot_y = ball_distance.x / ball_distance.x
        cpu_goal = False
        gk_screen_goal = False
        gk_screen_miss = False
        jump_speed_red = 0
        jump_speed_blue = 0
        red_fan_head_pos = PVector(15, 215)
        blue_fan_head_pos = PVector(725, 215)
        red_fan_pos = PVector(15, 250)
        blue_fan_pos = PVector(725, 250)
        cpu_miss_once = False
        comp_shoot = False
        time_bar = 150
        time_speed = 1
        play = False
        end_game = False
        score_player = 0
        score_cpu = 0
        choose_mode = False
        hard_mode = False
        turn_player = 0
        turn_gk = 0
        instruction = False
        exit_game = False
        menu = True