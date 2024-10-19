def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        Pew Pew
    """), My_Ship, 0, -50)
    music.play(music.create_sound_effect(WaveShape.SINE,
            4213,
            1,
            255,
            0,
            50,
            SoundExpressionEffect.TREMOLO,
            InterpolationCurve.CURVE),
        music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_destroyed(sprite):
    global Demon, Laser
    Demon = sprites.create(assets.image("""
        Purple Demon
    """), SpriteKind.enemy)
    Demon.set_stay_in_screen(True)
    Demon.set_position(randint(10, 160), randint(0, 50))
    Laser = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 4 4 . . . . . . . 
                    . . . . . . 4 5 5 4 . . . . . . 
                    . . . . . . 2 5 5 2 . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        Demon,
        0,
        100)
    animation.run_image_animation(Demon,
        assets.animation("""
            Animated demon
        """),
        200,
        True)
    animation.run_movement_animation(Demon,
        animation.animation_presets(animation.bobbing),
        2000,
        True)
sprites.on_destroyed(SpriteKind.enemy, on_on_destroyed)

def on_on_overlap(sprite2, otherSprite):
    info.change_score_by(1)
    sprites.destroy(Demon, effects.fire, 250)
    music.play(music.melody_playable(music.big_crash),
        music.PlaybackMode.IN_BACKGROUND)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

projectile: Sprite = None
Laser: Sprite = None
Demon: Sprite = None
My_Ship: Sprite = None
My_Ship = sprites.create(assets.image("""
    Player
"""), SpriteKind.player)
My_Ship.set_position(78, 114)
My_Ship.set_stay_in_screen(True)
effects.star_field.start_screen_effect()
controller.move_sprite(My_Ship)
info.set_score(0)
Demon = sprites.create(assets.image("""
    Purple Demon
"""), SpriteKind.enemy)
Demon.set_stay_in_screen(True)
Demon.set_position(randint(10, 160), randint(0, 50))
Laser = sprites.create_projectile_from_sprite(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . 4 4 . . . . . . . 
            . . . . . . 4 5 5 4 . . . . . . 
            . . . . . . 2 5 5 2 . . . . . . 
            . . . . . . . 2 2 . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    Demon,
    0,
    100)
animation.run_image_animation(Demon,
    assets.animation("""
        Animated demon
    """),
    200,
    True)
animation.run_movement_animation(Demon,
    animation.animation_presets(animation.shake),
    2000,
    False)

def on_update_interval():
    global Laser
    Laser = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 4 4 . . . . . . . 
                    . . . . . . 4 5 5 4 . . . . . . 
                    . . . . . . 2 5 5 2 . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        Demon,
        0,
        100)
game.on_update_interval(2500, on_update_interval)
