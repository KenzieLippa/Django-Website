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
class Character extends Sprite{
    //might need to put this in models and bring it here but not sure
    constructor({position, 
        //velocity, 
        color='red', 
        imageSrc, 
        scale = 1, 
        framesMax = 1, 
        offset = {x:0, y:0}, 
        sprites,
        dead = false,
        name,
        adult,
        gender,
        currentInjury = IJ.NONE,
        health = 100,
        injuryChance = 0.02,
        healthLoss = 0,
        deathChance = 0,
        infected = false,
        stomach = 100
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

        //get the height as a property
        this.height = 150;
        this.width = 50;
       // this.offset = offset;

        //add in last key as a property because each sprite will have one

        this.color = color;
    
        this.health = 100

        //could try to refactor later
        this.frameCurr = 0
        this.framesElapsed = 0
        this.framesHold = 50
        this.sprites = sprites
        this.dead = dead

        this.injured = false; //set to false by default
        //set in our attack box
        this.name = name
        this.adult = adult
        this.gender = gender
        this.currentInjury = currentInjury
        this.health = health
        this.injuryChance = injuryChance
        this.healthLoss = healthLoss
        this.deathChance = deathChance
        this.infected = infected
        this.stomach = stomach

        for(const sprite in this.sprites){
            //go through each object and create new images for each
            sprites[sprite].image = new Image()
            sprites[sprite].image.src = sprites[sprite].imageSrc
        }
        console.log(this.sprites)
    }
    get_injured(){
        //get the property
        return this.injured;
    }

    setInjuryStats(){
        //set the injury stats when this is called
        switch(self.currentInjury){

       
            case IJ.NONE:
                if (this.adult){
                    this.injuryChance = 0.01
                    this.hunger = 0.2

                }
                    //set the injury chance back
                else{

                    this.injuryChance = 0.02
                    this.hunger = 0.1
                    this.healthLoss = 0
                    this.restDaysNeeded = 0
                    this.slowHeal = 0
                    this.treated = False
                    this.deathChance = 0
                    this.infected = False
                }
                this.injured = false
                break
            case IJ.CHOLERA:
                this.healthLoss = -0.2
                this.hunger = 0.3
                this.injuryChance = 0.03
                this.restDaysNeeded = 3
                this.slowHeal = 6
                this.deathChance = 10
                this.injured = true
                break
            case IJ.DYSENTERY:
            //'''much more deadly i think'''
                this.healthLoss = -0.5
                this.hunger = 0.4
                this.injuryChance = 0.09
                this.restDaysNeeded = 5
                this.slowHeal = 10
                this.deathChance = 20
                if (this.infected)
                    this.deathChance = 0.5
                this.injured = true
                break
            case IJ.BROKEN_ARM:
            //'''worse than the arm because the player is running on it'''
                this.healthLoss = -0.01
                this.getInfected(self.injuryChance)
                if (this.infected){

                    this.deathChance = 30
                    this.slowHeal = 20
                    this.restDaysNeeded = 10
                    this.healthLoss = -0.1
                }
                else{
                    this.slowHeal = 10
                    this.restDaysNeeded = 5
                    this.deathChance = 1
                }
                this.injured = true
                break
            case IJ.BROKEN_LEG:
                this.healthLoss = -0.03
                this.getInfected(self.injuryChance)
                if (this.infected){

                    this.deathChance = 40
                    this.slowHeal = 25
                    this.restDaysNeeded = 15
                    this.healthLoss = -0.3
                }
                else{

                    this.slowHeal = 15
                    this.restDaysNeeded = 10
                    this.deathChance = 1
                }
                this.injured = true
                break
            case IJ.SNAKE_BITE:
                this.healthLoss = -5
                this.deathChance = 1000
               // # needs to be cured!
                this.slowHeal = 300
                this.restDaysNeeded = 200
                this.injured = true
                break
            case IJ.POSIONED:
                // if was poisoned then everything gets much worse until an andidote is found
                this.healthLoss = -10
                this.deathChance += 1000 //adds 1000 to death chance
                this.slowHeal = 600 //dont let the player heal unless really lucky
                this.restDaysNeeded = 400
                this.injured = true
                break
                
            }
            if (self.treated){
    
                this.slowHeal = 1
                this.restDaysNeeded = 1
                this.deathChance = 7
                this.healthLoss = 0
                this.currentInjury = IJ.NONE // next time stats are set then the sets will all be set back
            }
                //break
    }
    getDead(){
        return this.dead
    }
    eat(){
        self.stomach -= self.hunger
        if (this.stomach < 50){
            // # if less than 50 then double the hunger
             this.hunger += self.hunger

        }
        if (this.stomach < 25){
            this.hunger += this.hunger
            this.injurChance
        }
        if (this.stomach < 10){

            this.hunger += this.hunger
            this.injuryChance += this.injuryChance
        }
        if (this.stomach < 5){
            this.hunger += this.hunger
            this.injuryChance += this.injuryChance

        }
        if (this.stomach < 0){

            this.hunger += this.hunger
            this.injuryChance += this.injuryChance
            this.deathChance += 10
            this.healthLoss += 5
        }
    }

    injure(){
        let injurChance = this.injuryChance * 100

        let getInjury = Math.random() * 100
        if (getInjury >= injurChance){
            return IJ.NONE
        }
        else{
            let boo = Math.ceil(Math.random() * 5)
            switch(boo){
                case 0:
                    return IJ.NONE
                case 1:
                    return IJ.DYSENTERY
                case 2:
                    return IJ.CHOLERA
                case 3:
                    return IJ.BROKEN_ARM
                case 4:
                    return IJ.BROKEN_LEG
                case 5:
                    return IJ.SNAKE_BITE
            }
        }
    }
    snakeEyes(){
        c = Math.ceil(Math.random() * 10)
        if (c===1){
            d = Math.ceil(Math.random() * 10)
            if(d===1){
                e = Math.ceil(Math.random() * 10)
                if(e ===1){
                    this.die()
                }
            }
        }
    }
    hurt(){
        //if we run out of health we run this and also the snake eyes function to see if we die
        if(this.health === 0){
            this.deathChance = 10 + this.deathChance
            for(let i = 0; i < this.deathChance; i++){
                this.snakeEyes()
            }
        }
        else if(self.health < 0)
        {   
            this.deathChance = 100 + self.deathChance
            for(let i = 0; i < this.deathChance; i++){
                this.snakeEyes()
            }
        }
        else{
            for(let i = 0; i < this.deathChance; i++){
                this.snakeEyes()
            }
        }
        self.health += self.healthLoss
    }
    die(){
        self.dead = true
    }
    getInfected(chance){
        //a random function to determine whether or not to get infected
        c = Math.ceil(Math.random()*100) * chance
        if (chance >= 1){
            self.infected = true
        }
    }

    setIJ(injury){
        this.currentInjury = injury
        this.setInjuryStats() //make sure we set the stats
    }
    getIJ(){
        this.treated = true
        this.setInjuryStats()
    }
    finishRest(){
        if(self.restDaysNeeded === 0 || this.slowHeal === 0){
            this.currentInjury = IJ.NONE
            this.setInjuryStats()
        }
    }
    setRest(){
        if(this.restDaysNeeded > 0){
            this.restDaysNeeded -= 1
        }
        else if(this.restDaysNeeded === 0){
            this.finishRest()
        }
    }

    setSlowHeal(){
        if(this.slowHeal > 0){
            this.slowHeal -= 1

        }
        else if(this.slowHeal === 0){
            this.finishRest()
        }
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
        }
    

    switchSprite(sprite){

        // if (this.image === this.sprites.death.image) {
        //     //console.log("this is true")
        //     if(this.frameCurr === this.sprites.death.framesMax -1)
        //         //console.log("dead")
        //         this.dead = true
        //     return //run the attack image fully
        // }
        
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