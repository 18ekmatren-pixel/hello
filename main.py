def on_start():
    dino3.set_stay_in_screen(True)
    dino3.set_position(15, 100)
    dino3.ay = 250
    floor2.image.fill(14)
    floor2.bottom = 123
    info.set_score(0)
    scene.set_background_image(assets.image("""
        forest
        """))

def on_a_pressed():
    if dino3.overlaps_with(floor2):
        dino3.vy = -150
        animation.run_image_animation(dino3,
            [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
            150,
            False)
        timer.after(1150, animate_bike)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(dino, cactus):
    game.over(False)
sprites.on_overlap(Player, Enemy, on_on_overlap)

def animate_bike():
    animation.run_image_animation(dino3,
        [img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """)],
        150,
        True)

def on_on_overlap2(dino2, floor):
    dino2.vy = 0
    dino2.bottom = floor.top
    dino2.y += 1
sprites.on_overlap(Player, floor2, on_on_overlap2)

cactus2: Sprite = None
floor2: Sprite = None
dino3: Sprite = None
Enemy = 0
Player = 0
# on start code
Player = SpriteKind.player
Enemy = SpriteKind.enemy
Floor = SpriteKind.create()
dino3 = sprites.create(assets.image("""
    dino
    """), Player)
floor2 = sprites.create(image.create(160, 10), floor2)
x_vel = -75
# end of on start code
on_start()
animate_bike()

def on_on_update():
    info.change_score_by(1)
game.on_update(on_on_update)

def on_update_interval():
    global cactus2
    cactus2 = sprites.create(assets.image("""
        cactus
        """), Enemy)
    cactus2.set_position(160, 105)
    cactus2.set_velocity(x_vel, 0)
    cactus2.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(2000, on_update_interval)
