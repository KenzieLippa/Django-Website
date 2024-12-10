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
        injuryChance = 0.05,
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
        //set the animation properties
        this.frameCurr = 0
        this.framesElapsed = 0
        this.framesHold = 15
        //populate the sprite and deaths fields
        this.sprites = sprites
        this.dead = dead
        //something i was going to use to help fix the double dead popup but it didnt help
        //double dead only happens sometimes its probably because of how the snake eyes func works
        //if the player dies twice then its called twice
        this.alertShown = false

        this.injured = false; //set to false by default
        

        //set our personal stats from the db
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
        this.hunger = 5

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
        switch(this.currentInjury){

       
            case IJ.NONE:
                if (this.adult){
                    this.injuryChance = 0.1
                    this.hunger = 2

                }
                    //set the injury chance back
                else{

                    this.injuryChance = 0.1
                    this.hunger = 1
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
                this.hunger = 3
                this.injuryChance = 0.1
                this.restDaysNeeded = 3
                this.slowHeal = 6
                this.deathChance = 10
                this.injured = true
                break
            case IJ.DYSENTERY:
            //'''much more deadly i think'''
                this.healthLoss = -0.5
                this.hunger = 4
                this.injuryChance = 0.45
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
                this.getInfected(this.injuryChance)
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
                this.getInfected(this.injuryChance)
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
            if (this.treated){
    
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
    getStomach(){
        return this.stomach
    }
    setStomach(val){
        this.stomach = val
    }
    eat(){
        //prevent from being too negative
        if(this.stomach > -100)
            this.stomach -= this.hunger
       console.log(this.stomach)
        if (this.stomach < 50){
            // # if less than 50 then double the hunger
             this.hunger += this.hunger

        }
        if (this.stomach < 25){
            this.hunger += this.hunger
           // this.injurChance
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

    async injure(){
        if(this.currentInjury === IJ.NONE){

       
        let injurChance = this.injuryChance * 100

        let getInjury = Math.random() * 100
        if (getInjury >= injurChance){
            return IJ.NONE
        }
        else{
            let boo = Math.ceil(Math.random() * 5)
            switch(boo){
                case 0:
                    this.currentInjury = IJ.NONE
                    break
                case 1:
                    let str = this.name + " HAS DYSENTERY!"
                    await showAlert(str);
                    this.currentInjury = IJ.DYSENTERY
                    break
                case 2:
                    let str1 = this.name + " HAS CHOLERA"
                    await showAlert(str1);
                    this.currentInjury = IJ.CHOLERA
                    break
                case 3:
                    let str2 = this.name + " HAS A BROKEN ARM!"
                    await showAlert(str2);
                    this.currentInjury = IJ.BROKEN_ARM
                    break
                case 4:
                    let str3 = this.name + " HAS A BROKEN LEG!"
                    await showAlert(str3);
                    this.currentInjury = IJ.BROKEN_LEG
                    break
                case 5:
                    let str4 = this.name + " HAS DIED!"
                    await showAlert(str4);
                    this.currentInjury = IJ.SNAKE_BITE
                    break
            }
            //set the new injury stats
            this.setInjuryStats()
        }
    }
    }
    snakeEyes(){
        console.log("snake eyes called")
        let b = Math.ceil(Math.random() * 10)
        if (b===1){
            let d = Math.ceil(Math.random() * 10)
            if(d===1){
                let e = Math.ceil(Math.random() * 10)
                if(e ===1){
                    this.die()
                }
            }
        }
    }
    hurt(){
        console.log("CALLED THE HURT METHOD")
        //if we run out of health we run this and also the snake eyes function to see if we die
        if(this.health === 0){
            this.deathChance = 10 + this.deathChance
            for(let i = 0; i < this.deathChance; i++){
                this.snakeEyes()
            }
        }
        else if(this.health < 0)
        {   
            this.deathChance = 100 + this.deathChance
            for(let i = 0; i < this.deathChance; i++){
                this.snakeEyes()
            }
        }
        else{
            for(let i = 0; i < this.deathChance; i++){
                this.snakeEyes()
            }
        }
        if(this.health> 0)
            this.health -= this.healthLoss
        console.log(this.stomach)
        console.log(this.health)
    }
    
    async die(){
        // alert(this.name+ " HAS DIED!")
        if(!this.dead){

            this.dead = true
            let str = this.name + " HAS DIED!"
            await showAlert(str);
           // console.log("YOU HAVE DIED! "+ this.name)
        }
    }
    async getInfected(chance){
        //a random function to determine whether or not to get infected
        let d = Math.ceil(Math.random()*100)
        let chance2 = chance * 100
        if (chance2 >= d){
            let str = this.name + "'s INJURY IS INFECTED!"
            await showAlert(str);
            this.infected = true
        }
    }

    setIJ(injury){
        this.currentInjury = injury
        this.setInjuryStats() //make sure we set the stats
    }
    getIJ(){
        switch(this.currentInjury){
            case IJ.NONE:
                return this.name + "Has no injury, Congrats!"
            case IJ.CHOLERA:
                return this.name + "Has Cholera!"
            case IJ.DYSENTERY:
                return this.name + "Has Dysentery!"
            case IJ.BROKEN_ARM:
                return this.name + "Has a broken arm!"
            case IJ.BROKEN_LEG:
                return this.name + "Has a broken leg!"
            case IJ.SNAKE_BITE:
                return this.name + "Has a snake bite!"
        }
    }
    healIJ(){
        this.treated = true
        this.setInjuryStats()
    }
    finishRest(){
        if(this.restDaysNeeded === 0 || this.slowHeal === 0){
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