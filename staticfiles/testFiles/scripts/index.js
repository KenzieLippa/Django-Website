const canvas = document.querySelector('canvas'); //select the canvas and store it in here
//seems like this is probably the best way to do stuff as this way we can actually interact with the django side MUCH MUCH easier
const c = canvas.getContext('2d'); //using it alot so we going to make it short
//resize the canvas
canvas.width = 1024;
canvas.height = 576; //16:9 ratio

c.fillRect(0,0,canvas.width, canvas.height);
const gravity = 0.2;
class Sprite {
    //might need to put this in models and bring it here but not sure
    constructor({position, velocity, color='red'}){
        //passing through as an object so it doesnt matter the order
        //create the object, define the properties here
        this.position = position; //probably a vector
        //define field for our thing

        //add velocity property
        this.velocity = velocity;

        //get the height as a property
        this.height = 150;

        //add in last key as a property because each sprite will have one
        this.lastKey;
        this.color = color;

        //set in our attack box
        this.attackBox = {
            //want this to change with us
            position: this.position,
            width: 100,
            height: 50,
        }

    }
    //what do we look like?
    draw(){
        c.fillStyle = this.color //makes the rectangle red
        c.fillRect(this.position.x, this.position.y, 50,this.height);

        let at = this.attackBox
        //draw temp attack box
        c.fillStyle = 'green'
        c.fillRect(at.position.x, at.position.y, at.width, at.height )
    }

    //update so we can continue here
    update(){
        this.draw() //draw our sprite
        //add our gravity to our velocity to speed it up
        
        //over time add our velocity so we can mimic gravity
        this.position.x += this.velocity.x
        this.position.y += this.velocity.y
        //if this hits the bottom then stop the velocity
        if (this.position.y + this.height +this.velocity.y >= canvas.height){
            this.velocity.y = 0; //stop from moving downwards
        }
        else{
             //only call this if the player hasnt hit the floor yet
        this.velocity.y += gravity
        }
    }
}
const player = new Sprite({
    position: {
    x : 0,
    y: 0
    },
    velocity: {
        x: 0,
        y: 1
    }//will need to add delta to help with the craziness
});

const enemy = new Sprite({
    position: {
    x : 400,
    y: 0
    },
    velocity: {
        x: 0,
        y:0
    },
    color: 'blue'
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

function animate(){
    //make an animation function
    window.requestAnimationFrame(animate)
    //console.log('test')
    //will need to clear our canvas
    c.fillStyle = 'black'
    c.fillRect(0,0,canvas.width, canvas.height)
    player.update()
    enemy.update()

    //player movement
    //set the default value and then set if true
    player.velocity.x = 0
    //enemy.velocity.x = 0
    //set the keys based on the values in cost
    if (keys.a.pressed && player.lastKey === 'a'){
        player.velocity.x = -1
    }else if(keys.d.pressed && player.lastKey ==='d'){
        player.velocity.x =1 
    }

    //enemy movement
    //set the default value and then set if true
    enemy.velocity.x = 0
    //set the keys based on the values in cost
    if (keys.ArrowLeft.pressed && enemy.lastKey === 'ArrowLeft'){
        enemy.velocity.x = -1
    }else if(keys.ArrowRight.pressed && enemy.lastKey ==='ArrowRight'){
        enemy.velocity.x =1 
    }
}

animate() //calls the request animation frame and creates a loop

//add an event listener
window.addEventListener('keydown',(event)=>
{
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
        
    }
    console.log(event.key)
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
        console.log(event.key)
    })