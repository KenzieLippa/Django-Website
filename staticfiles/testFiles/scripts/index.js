const canvas = document.querySelector('canvas'); //select the canvas and store it in here
//seems like this is probably the best way to do stuff as this way we can actually interact with the django side MUCH MUCH easier
const c = canvas.getContext('2d'); //using it alot so we going to make it short
//resize the canvas
canvas.width = 1024;
canvas.height = 576; //16:9 ratio

c.fillRect(0,0,canvas.width, canvas.height);
const gravity = 0.2;

const background = new Sprite({
    position:{
        x:0,
        y:0
    },
    imageSrc: backgroundImg

})
const shop = new Sprite({
    position:{
        x:600,
        y:128
    },
    imageSrc: shopImg,
    scale: 2.75,
    framesMax: 6,

})
const player = new Fighter({
    position: {
    x : 0,
    y: 0
    },
    velocity: {
        x: 0,
        y: 1
    }//will need to add delta to help with the craziness
    ,
    offset:{
        x: 0,
        y: 0,
    },
    imageSrc: mackIdle,
    //set our max frames
    framesMax: 8,
    scale: 2.5,
    offset:{
        x:215,
        y:157,
    },
    sprites:{
        idle:{
            imageSrc: mackIdle,
            framesMax: 8,
        },
        run:{
            imageSrc: mackRun,
            framesMax: 8,
        },
        jump:{
            imageSrc: mackJump,
            framesMax: 2,
        },
        fall:{
            imageSrc: mackFall,
            framesMax: 2,
        },
        attack1:{
            imageSrc: mackAttack1,
            framesMax: 6,
        },
        takeHit:{
            imageSrc: mackTakeHit,
            framesMax: 4,
        },
        death:{
            imageSrc: mackDeath,
            framesMax: 6,
        },
    },
    attackBox:{
        offset:{
            x:100,
            y: 50

        },
        width: 160,
        height: 50,
    }
});

const enemy = new Fighter({
    position: {
    x : 400,
    y: 0
    },
    velocity: {
        x: 0,
        y:0
    },
    color: 'blue'
    ,
    offset:{
        x: -50,
        y: 0,
    },
    imageSrc: kenjiIdle,
    //set our max frames
    framesMax: 4,
    scale: 2.5,
    offset:{
        x:215,
        y:167,
    },
    sprites:{
        idle:{
            imageSrc: kenjiIdle,
            framesMax: 4,
        },
        run:{
            imageSrc: kenjiRun,
            framesMax: 8,
        },
        jump:{
            imageSrc: kenjiJump,
            framesMax: 2,
        },
        fall:{
            imageSrc: kenjiFall,
            framesMax: 2,
        },
        attack1:{
            imageSrc: kenjiAttack1,
            framesMax: 4,
        },
        takeHit:{
            imageSrc: kenjiTakeHit,
            framesMax: 3
        },
        death:{
            imageSrc: kenjiDeath,
            framesMax: 7
        }
    },
    attackBox:{
        offset:{
            x: -170,
            y:50

        },
        width: 170,
        height: 50,
    }
   
})
// player.draw()
// enemy.draw()
console.log(player)

const keys = {
    a : {
        pressed: false
    },
    d : {
        pressed: false
    },
    w: {
        pressed: false
    },
    ArrowRight:{
        pressed: false
    },
    ArrowLeft:{
        pressed: false
    }

}
//let lastKey;

decreaseTimer() //call the func
function animate(){
    //drawn first, reference background
    
    //make an animation function
    window.requestAnimationFrame(animate)
    //console.log('test')
    //will need to clear our canvas
    c.fillStyle = 'black'
    c.fillRect(0,0,canvas.width, canvas.height)
    background.update()
    shop.update()
    //slight white overlay
    c.fillStyle = 'rgba(255,255,255,0.15)'
    c.fillRect(0,0, canvas.width, canvas.height)
    player.update()
    enemy.update()

    //player movement
    //set the default value and then set if true
    player.velocity.x = 0

    enemy.velocity.x = 0

    //player.switchSprite('idle')
    //set the keys based on the values in cost
    if (keys.a.pressed && player.lastKey === 'a'){
        player.velocity.x = -1
       player.switchSprite('run')
    }else if(keys.d.pressed && player.lastKey ==='d'){
        player.velocity.x =1 
        player.switchSprite('run')
    }else{
        player.switchSprite('idle')
    }
    if(player.velocity.y < 0){
        player.switchSprite('jump')
    }else if(player.velocity.y > 0){
        player.switchSprite('fall')
    }
    //enemy movement
    //set the default value and then set if true
    enemy.velocity.x = 0
    //set the keys based on the values in cost
    if (keys.ArrowLeft.pressed && enemy.lastKey === 'ArrowLeft'){
        enemy.velocity.x = -1
        enemy.switchSprite('run')
    }else if(keys.ArrowRight.pressed && enemy.lastKey ==='ArrowRight'){
        enemy.velocity.x =1 
        enemy.switchSprite('run')
    }else{
        enemy.switchSprite('idle')
    }
    if(enemy.velocity.y < 0){
        enemy.switchSprite('jump')
    }else if(enemy.velocity.y > 0){
        enemy.switchSprite('fall')
    }

    //detect for collision here
    if (rectangularCollision({
        rectangle1: player,
        rectangle2: enemy,
    }) && player.isAttacking && player.frameCurr === 4
    ){
        // console.log('HIT')
        enemy.takeHit()
        player.isAttacking = false
        
        //document.querySelector('#enemyHealth').style.width = enemy.health +'%'
        gsap.to('#enemyHealth', {
            width: enemy.health + '%'
        })
    }

    //if player misses
    if(player.isAttacking && player.frameCurr === 4){
        player.isAttacking = false
    }
    if (rectangularCollision({
        rectangle1: enemy,
        rectangle2: player,
    }) && enemy.isAttacking && enemy.frameCurr === 2
    ){
        //console.log('HIT')
        player.takeHit()
        enemy.isAttacking = false
       
        //document.querySelector('#playerHealth').style.width = player.health +'%'
        gsap.to('#playerHealth', {
            width: player.health + '%'
        })
    }

    //if enemy misses
    if(enemy.isAttacking && enemy.frameCurr === 2){
        enemy.isAttacking = false
    }

    // end game based on health
    if(enemy.health <=0 || player.health <=0){
        determineWinner({player, enemy, timerId})
    }
}

animate() //calls the request animation frame and creates a loop

//add an event listener
window.addEventListener('keydown',(event)=>
{
    if(!player.dead){

    
    //fired when we press down on a key
    switch(event.key){
        case 'd':
            keys.d.pressed = true
            player.lastKey = 'd'
            break
        case 'a':
            // player.velocity.x = -1
            keys.a.pressed = true
            player.lastKey = 'a'
            break
        case 'w':
            // player.velocity.x = -1
            keys.w.pressed = true
            player.velocity.y = -10
            break

        case ' ':
            player.attack()
            break
    }
    }
    if(!enemy.dead){
        switch(event.key){
    
        case 'ArrowRight':
            keys.ArrowRight.pressed = true
            enemy.lastKey = 'ArrowRight'
            break
        case 'ArrowLeft':
            // player.velocity.x = -1
            keys.ArrowLeft.pressed = true
            enemy.lastKey = 'ArrowLeft'
            break
        case 'ArrowUp':
            // player.velocity.x = -1
            //keys.ArrowUp.pressed = true
            enemy.velocity.y = -10
            break
        case 'ArrowDown':
            // player.velocity.x = -1
            //keys.ArrowUp.pressed = true
            enemy.attack()
            //enemy.isAttacking = true
            break
        }
    }
    // console.log(event.key)
})

window.addEventListener('keyup',(event)=>
    {
        //fired when we press down on a key
        switch(event.key){
            case 'd':
                keys.d.pressed = false
                lastKey = 'a'
                break
            case 'a':
                keys.a.pressed = false
                lastKey = 'd'
                break

            case 'w':
                // player.velocity.x = -1
                keys.w.pressed = false
                //lastKey = 'a'
                break

            case 'ArrowRight':
                keys.ArrowRight.pressed = false
                enemy.lastKey = 'ArrowLeft'
                break
            case 'ArrowLeft':
                // player.velocity.x = -1
                keys.ArrowLeft.pressed = false
                enemy.lastKey = 'ArrowRight'
                break
            
        }
        // console.log(event.key)
    })