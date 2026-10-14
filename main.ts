function on_start () {
    dino.setStayInScreen(true)
    dino.setPosition(15, 100)
    dino.ay = 250
    floor.image.fill(14)
    floor.bottom = 123
    info.setScore(0)
    scene.setBackgroundImage(assets.image`forest`)
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (dino.overlapsWith(floor)) {
        dino.vy = -150
        animation.runImageAnimation(
        dino,
        [img`
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
            `],
        150,
        false
        )
        timer.after(1150, animate_bike)
    }
})
sprites.onOverlap(Player, Enemy, function (dino, cactus) {
    game.over(false)
})
function animate_bike () {
    animation.runImageAnimation(
    dino,
    [img`
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
        `],
    150,
    true
    )
}
sprites.onOverlap(Player, floor, function (dino, floor) {
    dino.vy = 0
    dino.bottom = floor.top
    dino.y += 1
})
let cactus: Sprite = null
let floor: Sprite = null
let dino: Sprite = null
let Enemy = 0
let Player = 0
// on start code
Player = SpriteKind.Player
Enemy = SpriteKind.Enemy
let Floor = SpriteKind.create()
dino = sprites.create(assets.image`dino`, Player)
floor = sprites.create(image.create(160, 10), floor)
let x_vel = -75
// end of on start code
on_start()
animate_bike()
game.onUpdate(function () {
    info.changeScoreBy(1)
})
game.onUpdateInterval(2000, function () {
    cactus = sprites.create(assets.image`cactus`, Enemy)
    cactus.setPosition(160, 105)
    cactus.setVelocity(x_vel, 0)
    cactus.setFlag(SpriteFlag.AutoDestroy, true)
})
