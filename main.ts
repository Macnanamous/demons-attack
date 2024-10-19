controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(assets.image`Pew Pew`, My_Ship, 0, -50)
    music.play(music.createSoundEffect(WaveShape.Sine, 4213, 1, 255, 0, 50, SoundExpressionEffect.Tremolo, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
})
sprites.onDestroyed(SpriteKind.Enemy, function (sprite) {
    Demon = sprites.create(assets.image`Purple Demon`, SpriteKind.Enemy)
    Demon.setStayInScreen(true)
    Demon.setPosition(randint(10, 160), randint(0, 50))
    animation.runImageAnimation(
    Demon,
    assets.animation`Animated demon`,
    200,
    true
    )
    animation.runMovementAnimation(
    Demon,
    animation.animationPresets(animation.shake),
    2000,
    true
    )
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    music.play(music.melodyPlayable(music.jumpDown), music.PlaybackMode.InBackground)
    sprites.destroy(Demon, effects.fire, 1000)
})
let projectile: Sprite = null
let Demon: Sprite = null
let My_Ship: Sprite = null
effects.starField.startScreenEffect()
info.setScore(0)
My_Ship = sprites.create(assets.image`Player`, SpriteKind.Player)
My_Ship.setPosition(78, 114)
My_Ship.setStayInScreen(true)
controller.moveSprite(My_Ship)
Demon = sprites.create(assets.image`Purple Demon`, SpriteKind.Enemy)
Demon.setStayInScreen(true)
animation.runImageAnimation(
Demon,
assets.animation`Animated demon`,
200,
true
)
animation.runMovementAnimation(
Demon,
animation.animationPresets(animation.shake),
2000,
false
)
Demon.setPosition(randint(10, 160), randint(0, 50))
game.onUpdateInterval(2000, function () {
    Demon = sprites.createProjectileFromSprite(assets.image`Laser`, Demon, 0, 50)
})
