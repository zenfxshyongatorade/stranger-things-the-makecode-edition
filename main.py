@namespace
class SpriteKind:
    collectable = SpriteKind.create()
    collectible = SpriteKind.create()
    fake = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    game.splash("This is fake!")
    page.destroy(effects.spray, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.fake, on_on_overlap)

def on_on_destroyed(sprite2):
    global page
    page = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . d f d d d . . . . . 
                    . . . . . . 6 f f 8 8 . . . . . 
                    . . . . . . 6 6 f 8 8 . . . . . 
                    . . . . . . d 6 f 8 d . . . . . 
                    . . . . . . d 6 f d d . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.collectible)
    page.set_position(112, 26)
    page = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . d f d d d . . . . . 
                    . . . . . . 6 f f 8 8 . . . . . 
                    . . . . . . 6 6 f 8 8 . . . . . 
                    . . . . . . d 6 f 8 d . . . . . 
                    . . . . . . d 6 f d d . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.fake)
    page.set_position(61, 20)
    page = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . d f d d d . . . . . 
                    . . . . . . 6 f f 8 8 . . . . . 
                    . . . . . . 6 6 f 8 8 . . . . . 
                    . . . . . . d 6 f 8 d . . . . . 
                    . . . . . . d 6 f d d . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.fake)
    page.set_position(39, 79)
    page = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . d f d d d . . . . . 
                    . . . . . . 6 f f 8 8 . . . . . 
                    . . . . . . 6 6 f 8 8 . . . . . 
                    . . . . . . d 6 f 8 d . . . . . 
                    . . . . . . d 6 f d d . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.fake)
    page.set_position(88, 9)
sprites.on_destroyed(SpriteKind.collectable, on_on_destroyed)

def on_on_overlap2(sprite3, otherSprite2):
    info.change_score_by(1)
    music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
            5000,
            1,
            255,
            213,
            500,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LOGARITHMIC),
        SoundExpressionPlayMode.UNTIL_DONE)
    page.destroy(effects.disintegrate, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.collectible, on_on_overlap2)

def on_on_score():
    game.over(True, effects.clouds)
info.on_score(2, on_on_score)

def on_on_overlap3(sprite4, otherSprite3):
    info.change_score_by(1)
    music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
            5000,
            1,
            255,
            213,
            500,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LOGARITHMIC),
        SoundExpressionPlayMode.UNTIL_DONE)
    page.destroy(effects.disintegrate, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.collectable, on_on_overlap3)

page: Sprite = None
info.set_score(0)
scene.set_background_color(11)
scene.set_background_image(img("""
    ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        .............................................................................................................................fff................................
        ...........................................................................................................................fffff................................
        .........................................................................................................................fffffff................................
        ........................................................................................................................ffffffff................................
        ......................................................ffffff..ffffff...................................................fffffffff................................
        ......................................................ffffffffffffffff.................................................ffff..fff................................
        ......................................................fffffffffffffffffff.............................................ffff...fff................................
        ......................................................ffffffffffffffffffffff.........................................fffff...fff................................
        ......................................................ffffffffffffffffffffffffff...................................ffffff....fff................................
        .......................................................ffffffffffffffffffffffffff...............................fffffffff....fff................................
        ..........................ffff...........................ffffffffffffffffffffffff..............................ffffffff......fff................................
        ..........................ffffff............................ffffffffffffffffffffff............................fffffff........fff................................
        ..........................ffffffff............................fffffffffffffffffffff.........................fffffff..........fff................................
        ..........................ffffffffffff..........................ffffffffffffffffffff.......................ffffff............fff................................
        ..........................fff.fffffffffff...........................ffffffffffffffff......................ffffff.............fff................................
        ..........................ffff..fffffffffff.........................ffffffffffffffff....................ffffffff.............fff................................
        ..........................ffff......fffffffff........................fffffffffffffff..................fffffffffff............fff................................
        ...........................fff.........fffffffff.......................fffffffffffff...............fffffffff.ffff............fff................................
        ...........................ffff..........ffffffffff......................fffffffffff......ffffffffffffffff...ffff............fff................................
        ...........................ffff..........fffffffffffffffff................ffffffffff...fffffffffffffffff.....ffff............ffff...............................
        ............................fff..........fff..ffffffffffffffff............fffffffffff.fffffffffffffff.........fff............ffff...............................
        ............................fff..........fff.....fffffffffffffff.........ffffffffffff.ffffff..................ffff............fff...............................
        ............................fff..........fff............ffffffffff......ffffffffffffffffff....................ffff..............................................
        ............................fff..........fff................ffffffff...ffffffffffffffffffff....................fff..............................................
        ............................fff..........fff..................ffffffffffffffffffffffffffffff...................fff..............................................
        ............................fff..........ffff...................fffffffffffffffffffff...ffff...................fff..............................................
        ............................fff..........ffff..................ffffffffffffffffffffff...ffff...................fff..............................................
        ..........................................fff.................fffffffffffffffffffffff....ffff..................fff..............................................
        ..........................................fff................ffffffffffffffffffffffff....ffff..................fff..............................................
        .............................................................fffffffffffffffffffffff......ffff.................ffff.............................................
        .............................................................fffffffffffffffffffffff......fffff................ffff.............................................
        .............................................................fffffffffffffffffffffff.......ffffff..............ffff.............................................
        .............................................................fffffffffffffffffffffff........fffffff.............................................................
        .............................................................fffffffffffffffffffffff.........ffffff.............................................................
        .............................................................ffffffffffffffffffffff............fffff............................................................
        .............................................................ffffffffffffffff...................ffffff..........................................................
        ...............................................................fffffffffffff..................fffffffff.........................................................
        ...............................................................fff............................fff.fffffff.......................................................
        ...............................................................fff............................fff...fffff.......................................................
        ...............................................................fff............................fff....ffffff.....................................................
        ...............................................................fff............................fff.....fffff.....................................................
        ...............................................................fff............................fff......ffff.....................................................
        ..............................................................ffff............................fff.......fff.....................................................
        ..............................................................ffff............................fff.......fff.....................................................
        ..............................................................fff.............................ffff......fff.....................................................
        ..............................................................fff.............................ffff......fff.....................................................
        ..............................................................fff..............................fff......fff.....................................................
        ..............................................................fff..............................fff......fff.....................................................
        ..............................................................fff..............................fff......fff.....................................................
        ..............................................................fff..............................fff......fff.....................................................
        ..............................................................fff..............................fff......fff.....................................................
        .............................................................ffff..............................fff......fff.....................................................
        ............................................................fffff..............................fff......fff.....................................................
        ..........................................................ffffff..............................ffff......fff.....................................................
        ......................................................fffffffff...............................ffff...ffffff.....................................................
        ...................................................fffffffffff................................fff....ffffff.....................................................
        .................................................fffffffffff................................fffff....fffff......................................................
        ...............................................fffffffff.fff................................fffff....fffff......................................................
        ...............................................ffffff....fff................................ffff......fff.......................................................
        ...............................................ffff......fff................................ffff......fff.......................................................
        ...............................................fff.......fff................................fff.......fff.......................................................
        ...............................................fff.......fff....................................................................................................
        ...............................................ffff......fff....................................................................................................
        ...............................................ffff......fff....................................................................................................
        ...............................................ffff......fff....................................................................................................
        ...............................................ffff......fff....................................................................................................
        ...............................................ffff......fff....................................................................................................
        .........................................................fff....................................................................................................
        .........................................................fff....................................................................................................
        .........................................................fff....................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
"""))
game.show_long_text("An attack from a weird shadow monster is haunting will, can you find the correct pages before the shadow lets us meet our doom? (this is not based on the series, only the characters ",
    DialogLayout.BOTTOM)
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffff22222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffff222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffff222222ffffffffffffff222222222fffffffffffffff222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffff222fffffffffffffffff222222222222ffffffffffff22222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffff2222fffffffffffffffff222222222222ffffffffffff2222222ffffffffffffff2222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffff2222fffffffffffffffffff222ff22222ffffffffffff22222222fffffffffffff222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffff222ffffffffffffffffffff222fffffffffffffffffff222222222ffffffffffff22222222fffffffffffffffffffff222ffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffff222ffffffffffffffffffff222fffffffffffffffffff222ff22222fffffffffff22222222fffffffffffffffffffff222ffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffff2222fffffffffffffffffff222fffffffffffffffffff222ff22222fffffffffff222f2222ffffffffffffffffffff2222fffffffffffff2222fffffffffffffffffffffffffff
        fff22222ffffffffff22222ffffffffffffffffff222fffffffffffffffffff222f222222fffffffffff222ff222ffffffffffffffffffff2222ffff222ffff222222fffffffffffffffffffffffffff
        fff2222222222222222222222ffffffffffffffff222fffffffffffffffffff222222222ffffffffffff222ff222fffffffffffffffffff22222ffff222ff22222222ffffffffff222ffffffffffffff
        fff22222222222222222222222fffffffffffffff222ffffffffffffffffff22222222ffffffffffffff222ff2222ffffffffffffffffff22222ffff222ff222222fffffffffff2222ffffffffffffff
        ffffff222222222222222222222ffffffffffffff222ffffffffffffffffff2222222fffffffffffffff222ff2222fffffffffffffffff222222ffff222ff2222ffffffffffff22222ffffffffffffff
        fffffffffffffffffffffff222222ffffffffffff222ffffffffffffffffff222222ffffffffffffffff222fff222fffffffffffffffff222222ffff222f2222ffffffffffff222222ffffffffffffff
        ffffffffffffffffffffffff22222ffffffffffff222ffffffffffffffffff222222ffffffffffffffff222fff222ffffffffffffffff2222222fff2222f2222fffffffffff2222222ffffffffffffff
        fffffffffffffffffffffffff2222fffffffffff2222ffffffffffffffffff2222222fffffffffffffff222222222fffffffffffffff22222222fff22222222ffffffffffff2222222ffffffffffffff
        fffffffffffffffff222ffffff222fffffffffff2222ffffffffffffffffff2222222fffffffffffffff22222222222fffffffffffff2222f222ff2222f2222fffffffffff22222222fff222ffffffff
        fffffffffffffffff222ffffff222fffffffffff222fffffffffffffffffff222f2222ffffffffffffff22222222222222fffffffff2222ff222ff2222f222ffffffffffff2222222ffff222fff222ff
        fffffffffffffffff222fffff2222fffffffffff222fffffffffffffffffff222f22222fffffffffffff222ff222222222fffffffff2222ff222f2222f2222ffffffffffff2222222ffff222f22222ff
        fffffffffffffffff222222222222fffffffffff222ffffffffffffffffff2222ff222222fffffffffff222fffff222222ffffffff2222ff222222222f2222fffffff222ff222222fffff222222222ff
        fffffffffffffffff22222222222ffffffffffff222ffffffffffffffffff2222fff2222222fffffffff222fffff22222fffffffff2222ff22222222ff222fffffff2222ff222222fffff22222222fff
        fffffffffffffffff2222222222fffffffffffff222fffffffffffffffff2222fffff222222fffffffff222ffffff2222ffffffff2222fff2222222fff2222ffffff2222ff222222fffff2222222222f
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222fffffff222222fffffff222fffffff2222ffffff22222fff222222ffff2222fffff22222ff22222ffffff22222f22222
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222fffffffff22222fffffff222fffffff2222ffffff2222ffff222222fffff22222f2222222ff22222ffffff22222f22222
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222ffffffffff2222fffffff222ffffffff222fffff2222fffff22222ffffff2222222222222ff2222fff222f2222ffff222
        ffffffffff2222222222222222222222222fffffffffffffffffffffffff222fffffffffffffffffffff222ffffffff2222ffff2222ffffff222ffffffff222222222222ff22222f2222f2222fffffff
        ffffffffff2222222222222222222222222222ffffffffffffffffffffffffffffffffffffffffffffff222ffffffff2222ffff222ffffffffffffffffffff22222ff222fff222222222ffffffffffff
        ffffffffff2222222222222222222222222222222222ffffffffffffffffffffffffffffffffffffffff222fffffffff222ffffffffffffffffffffffffffffffffff222ffff2222222fffffffffffff
        fffffffffffffffffffffffffffffffff222222222222222222222222222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222fffff222222fffffffffffff
        ffffffffffffffffffffffffffffffffffff22222222222222222222222222222222222ffffffffffffffffffffffff2222222fffffffffffffffffffffffffffffffffffffffffffff2222222ffffff
        ffffffffffffffffffffffffffffffffffffffffff2222222222222222222222222222222222222ffffffff222222222222222222fffffffffffffffffffffffffffffff222222222222222222222fff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222222222222222222222222222222222222222222222fffffffffffffffffffffffff2222222222222222222222222fff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222222222222222222222222222fff222222222fffffffffffffffffff222222222222222222222fff22222fff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222222222ffffffffffffff222222222222fffffffff22222222222222ffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222222222222222222222222222ffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222222222222222222222ffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222222222222ffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffff222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffff222ffffffff222ffffff222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffff222ffffffff222ffffff222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffff222ffffffff222ffffff222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffff22222222222222222ffff222ffffffff222fffffffffffffffffffffffffffffffffffffffffffffffffff2222ffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffff22222222222222222ffff222ffffffff222ffffffffffffffffffffffffffffffffffffffffffffffffff2222222ffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffff22222222222222222ffff222ffffffff222fffffffffffffffffffffffffffffffffffffffffffffffff2222222222ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffff222fffffffff222ffffffff222ffffffffffffffffffffffffffffffffffffffffffffffff22222222222222ffffff222222fffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffff222fffffffff222ffffffff222fffffff222fffffffff222fffffffffffffffffffffff2222222fff2222222fffff2222222fffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffff222fffffffff222ffffffff222fffffff222fffffffff222fffffffffffffffffffffff222222ffffff22222fffff2222222fffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffff222fffffffff222ffffffff222fffffff222fffffffff222ffffffffffffffffffffff222222fffffffffffffffff222fffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffff222fffffffff222ffffffff222fffffff222fffffffff222fffff22222ffffffffffff22222ffffffffffffffffff222fffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffff222fffffffff22222222222222fffffff222fffffffff222ffff2222222fffffffffff2222ffffffffffffffffff2222fffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffff222fffffffff22222222222222fffffff222fffffffff222fff222222222ffffffffff2222ffffffffffffffffff2222fffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffff222fffffffff22222222222222fffffff222fffffffff222ff22222f2222ffffffffff222fffffffffffffffffff222ffffffffffffffffffffffffffffffffffffff
        fffffffffffffffff2222222222222fffffffff2222fffffff222fffffff222fffffffff222ff2222fff222fffffffff2222fffffffffffffffffff222ffffffffffffffffffffffffffffffffffffff
        fffffffffffffffff2222222222222ffffffffff222fffffff2222fffff2222fffffffff222f2222ffff2222ffffffff2222fffffffffffffffffff222ffffffff22222222ffffffffffffffffffffff
        fffffffffffffffff2222222222222ffffffffff222fffffff2222fffff2222fffffffff22222222ffff2222ffffffff2222fffffffffffffffffff222fff2222222222222222222222222222fffffff
        fffffffffffffffffffffffffff2222fffffffff222ffffffff222fffff222ffffffffff2222222ffffff2222fffffff2222fffffffffffffffffff2222222222222222222222222222222222fffffff
        fffffffffffffffffffffffffff2222fffffffff222ffffffff222fffff222ffffffffff222222fffffff2222ffffffff2222fffffff222ffffffff2222222222222ffff22222222222222222fffffff
        ffffffffffffffffffffffffffff222fffffffff222ffffffff222fffff222ffffffffff222222ffffffff222ffffffff22222fffff2222ffffffff22222222fffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffff222fffffffff222ffffffff222ffff2222ffffffffff22222fffffffff222fff222fff2222ffff22222ffffffff222ffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffff222fffffffff222ffffffff222ffff2222ffffffffff2222ffffffffff222fff222ffff2222ff222222ffffffff2222fffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffff222fffffffff222ffffffff222ffff2222ffffffffff2222ffffffffff222fff222ffff2222f2222222ffffffff22222ffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffff222ffffffff2222ffffffff222ffff2222ffffffffff222fffffffffff22222f222fffff22222222222fffffffff22222fffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffff222ffffffff2222ffffffff222ffff2222ffffffffffffffffffffffff222222222fffff2222222f222ffffffffff2222fffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffff222ffffffff2222ffffffff222ffff222fffffffffffffffffffffffff222222222ffffff222222f222fffffffffff222fffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffff222ffffffff2222ffffffff222fffffffffffffffffffffffffffffffffff222222fffffff2222ff222fffffffffff222fffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffff222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222fffffffffff222fffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222fffffffffff2222ffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222ffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222ffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222fff222222ffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222222222222ffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222222222ffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222222ffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222ffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222222222222fffffff
        ffffffffffffffffffffff2222222222222222222222222222222222222222222222222222ffffffffffffffffffffffffffffffffffffffffffffffffffffff2222222222222222222222222fffffff
        ffffffffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222ffffffff22222222222222222222222222222222222222222222222222222222222fffffff
        ffffffffffffffffffffff222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222ffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222222222222222222222222222222222222222222222222222222222ffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
"""))
for index in range(4):
    music.play_melody("E F G A B A G F ", 285)
info.start_countdown(10)
scene.set_background_image(img("""
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbddddbbbbfbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbfdfddddddfddbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbdddddddfffdddbbbbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbddddddfdfdfddbbbbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbdddddddffdddbbbbbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbdddddddbbbbbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddffffffffffffdddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddddddddddddddddddddddddddddddddd
        ddddffffffffffffffffdddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddddddddddddddddddddddddddddddd
        dddfffffffffffffffffddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddddddddddddddddddddddddddddd
        dddfffffffffffffffffddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddddddddddddddddddddddddddddd
        dddfffffffffffffffffddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddddddddddddddddddddddddddddd
        dddfffffffffffffffffddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbdddddddddddddddddddddddddddddddbbbbbbbbdddddddddddddddddddddddddddddddddddddddddddd
        dddfffffffffffffffffddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbdddddddfffdddddddddddddddddddddddddddbbbbbbdddddddddddddddddddddddddddddddddddddddddddd
        dddfffffffffffffffffddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbddddddddfffddfffdddfffdddddddfffddddddbbbbbbdddddddddddddddddddddddddddddddddddddddddddd
        ddffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddddddbbbbbbddddddddfffddfffdddfffdddddddfffddddbbbbbbbbdddddddddddddddddddddddddddddddddddddddddddd
        ddfffffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddbbbbbbbdddddddddddddfffdddfffdddddddfffdbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddd
        ddfffffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddbbbbbbbbdddbbbbbbbbbbbbbbdddddddddbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddd
        ddfffffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddd
        ddfffffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddd
        dffffffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddddddddddddddddddddddddddddd
        dffffffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbdddddddddddddddddddddddddddddddddddddddddddd
        fffffffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbddddddbbbbbbbbbbbbbbbbbdddddddbbbbbbdddddddddddddddddddddddddddddddddddddddddddd
        fffffffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddbbbbbddddddddddddddddddddddddddddddddddddddddbbbbbbdddddddddddddddddddddddddddddddddddddddddddd
        fffffffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddbbbbbddddddddddddddddddddddddddddddddddddddddbbbbbbdddddddddddddddddddddddddddddddddddddddddddd
        fffffffffffffffffffffffdddddddddddddddddddddddddddddddddddddddddbbbbbbdddddddddddddddddddddddddddddddddddddddbbbbbbbdddddddddddddddddddddddddddddddddddddddddddd
        ffffffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddbbbbbbdddddddddddddddddddddddddddddddddddddddbbbbbbbdddddddddddddddddddddddddddddddddddddddddddd
        fffffffffffffffffffffdddddddddddddddddddddddddddddddddddddddddddbbbbbbdddddddddddddddddddddddddddddddddddddddbbbbbbddddddddddddddddddddddddddddddddddddddddddddd
        fffffffffffffffffffffdddddddddddddddddddddddddddddddddddddddddddbbbbbbdddddddddddddddddddddddddddddddddddddddbbbbbbddddddddddddddddddddddddddddddddddddddddddddd
"""))
lucas = sprites.create(assets.image("""
    lucas
"""), SpriteKind.player)
controller.move_sprite(lucas)
scaling.scale_to_percent(lucas, 150, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
lucas.set_bounce_on_wall(True)
page = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . d f d d d . . . . . 
            . . . . . . 6 f f 8 8 . . . . . 
            . . . . . . 6 6 f 8 8 . . . . . 
            . . . . . . d 6 f 8 d . . . . . 
            . . . . . . d 6 f d d . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.collectable)
page.set_position(20, 36)