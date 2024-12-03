class Sprite {
    //might need to put this in models and bring it here but not sure
    constructor({position, imageSrc, scale = 1, framesMax = 1, offset = {x:0, y:0}}){
        //passing through as an object so it doesnt matter the order
        //create the object, define the properties here
        this.position = position; //probably a vector
        //define field for our thing

        //add velocity property
      

        //get the height as a property
        this.height = 150;
        this.width = 50; 
        this.image = new Image()
        this.image.src = imageSrc;
        this.scale = scale //by default is 1
        this.framesMax = framesMax
        this.frameCurr = 0
        this.framesElapsed = 0
        this.framesHold = 30
        this.offset = offset
        //refactor later 
    }
    //what do we look like?
    draw(){
      c.drawImage(
        this.image, 
        //here we add the crop location and width and height
        this.frameCurr * this.image.width / this.framesMax, //crop x
        0, //crop y
        this.image.width / this.framesMax, //divided by frames
        this.image.height,
        this.position.x - this.offset.x, 
        this.position.y - this.offset.y, 
        this.image.width/this.framesMax * this.scale, //divide this as well to be proper
        this.image.height * this.scale
    ) //draw the image
    }
    animateFrames(){
        this.framesElapsed ++

        if(this.framesElapsed % this.framesHold === 0){
            if(this.frameCurr < this.framesMax - 1){
                this.frameCurr ++
            }
            else{
                this.frameCurr = 0
            }

        }
    }
    //update so we can continue here
    update(){
        this.draw() //draw our sprite
        //add our gravity to our velocity to speed it up
        
        //animation loop
        this.animateFrames()
    }

}

//extends the sprite class if available
class Fighter extends Sprite{
    //might need to put this in models and bring it here but not sure
    constructor({position, 
        velocity, 
        color='red', 
        imageSrc, 
        scale = 1, 
        framesMax = 1, 
        offset = {x:0, y:0}, 
        sprites,
        attackBox = {offset:{}, width:undefined, height:undefined}
    }){

        //add in our new funcs
        super({
            //inheret these from our parents
            position,
            imageSrc,
            scale,
            framesMax,
            offset
        })
        //passing through as an object so it doesnt matter the order
        //create the object, define the properties here
        //this.position = position; //probably a vector
        //define field for our thing

        //add velocity property
        this.velocity = velocity;

        //get the height as a property
        this.height = 150;
        this.width = 50;
       // this.offset = offset;

        //add in last key as a property because each sprite will have one
        this.lastKey;
        this.color = color;
        this.isAttacking = false;
        this.health = 100

        //could try to refactor later
        this.frameCurr = 0
        this.framesElapsed = 0
        this.framesHold = 20
        this.sprites = sprites
        this.dead = false
        //set in our attack box
        this.attackBox = {
            //want this to change with us
            position: {
                x: this.position.x,
                y: this.position.y
            },
            offset: attackBox.offset,
            width:attackBox.width,
            height: attackBox.height,
        }

        for(const sprite in this.sprites){
            //go through each object and create new images for each
            sprites[sprite].image = new Image()
            sprites[sprite].image.src = sprites[sprite].imageSrc
        }
        console.log(this.sprites)
    }
    //what do we look like?
    //no longer rectangles
    // draw(){
    //     c.fillStyle = this.color //makes the rectangle red
    //     c.fillRect(this.position.x, this.position.y, this.width,this.height);

    //     let at = this.attackBox
    //     //draw temp attack box
    //     if (this.isAttacking)
    //     {
    //         c.fillStyle = 'green'
    //         c.fillRect(at.position.x, at.position.y, at.width, at.height )

    //     }
    // }

    //update so we can continue here
   
    update(){
        this.draw() //draw our sprite
        if(!this.dead)
        this.animateFrames()
        //add our gravity to our velocity to speed it up
        this.attackBox.position.x = this.position.x + this.attackBox.offset.x
        this.attackBox.position.y = this.position.y + this.attackBox.offset.y
        // c.fillRect(this.attackBox.position.x, this.attackBox.position.y, this.attackBox.width, this.attackBox.height)
        //over time add our velocity so we can mimic gravity
        this.position.x += this.velocity.x
        this.position.y += this.velocity.y
        //if this hits the bottom then stop the velocity
        if (this.position.y + this.height +this.velocity.y >= canvas.height-96){
            this.velocity.y = 0; //stop from moving downwards
            //console log to get this exact value
            this.position.y = 330
        }
        else{
             //only call this if the player hasnt hit the floor yet
        this.velocity.y += gravity
        }
    }
    attack(){
        this.switchSprite('attack1')
        this.isAttacking = true
        // setTimeout(()=>{
        //     this.isAttacking = false
        // }, 100)

    }
    takeHit(){
        
        this.health -= 20;
        if (this.health <=0){
            //console.log("should die")
            this.switchSprite('death')
        }else{
            this.switchSprite('takeHit')
        }
    }
    switchSprite(sprite){

        if (this.image === this.sprites.death.image) {
            //console.log("this is true")
            if(this.frameCurr === this.sprites.death.framesMax -1)
                //console.log("dead")
                this.dead = true
            return //run the attack image fully
        }
        if (this.image === this.sprites.attack1.image && 
            this.frameCurr <  this.sprites.attack1.framesMax -1) return //run the attack image fully
        
            if (this.image === this.sprites.takeHit.image && 
                this.frameCurr <  this.sprites.takeHit.framesMax -1) return //run the attack image fully
        switch(sprite){
            case 'idle':
                if (this.image !== this.sprites.idle.image){

                    this.image = this.sprites.idle.image
                    this.framesMax = this.sprites.idle.framesMax
                    this.frameCurr = 0
                }
                break
            case 'run':
                if(this.image !== this.sprites.run.image)
                {
                    this.image = this.sprites.run.image
                    this.framesMax = this.sprites.run.framesMax
                    this.frameCurr = 0
                }

                break
            case 'jump':
                if(this.image !== this.sprites.jump.image){
                    this.image = this.sprites.jump.image
                    this.framesMax = this.sprites.jump.framesMax
                    this.frameCurr = 0
                }
                break
            case 'fall':
                if(this.image !== this.sprites.fall.image){
                    this.image = this.sprites.fall.image
                    this.framesMax = this.sprites.fall.framesMax
                    this.frameCurr = 0
                }
                break
            case 'attack1':
                if(this.image !== this.sprites.attack1.image){
                    this.image = this.sprites.attack1.image
                    this.framesMax = this.sprites.attack1.framesMax
                    this.frameCurr = 0
                }
                break
            case 'takeHit':
                if(this.image !== this.sprites.takeHit.image){
                    this.image = this.sprites.takeHit.image
                    this.framesMax = this.sprites.takeHit.framesMax
                    this.frameCurr = 0
                }
                break
            case 'death':
                //console.log("this is true")
                if(this.image !== this.sprites.death.image){
                    this.image = this.sprites.death.image
                    this.framesMax = this.sprites.death.framesMax
                    this.frameCurr = 0
                }
                break
        }
    }
}