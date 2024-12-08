///here we are going to do the parallax for the background
const canvas = document.querySelector('canvas');
const c = canvas.getContext('2d')

let gamePaused = false
let parallax;
let miles = gameMiles
const mile = 5280
const FR = 20
let offsetX = 200
//for if we end up wanting to actually not hard code things
const kidX = 525
const adultX = 400
let wagonHealth = 100

let step = 0;
let gameId = game_id
let food = 100

gsap.to('#food', {
    width: food + '%'
})
gsap.to('#wagon',{
    width: wagonHealth + '%'
})
//fill the window but may need to fix with the nav bar
//canvas size
canvas.width = 1710
canvas.height = 900
console.log(p1_currIJ)
let kidY = 125
// if(p1_currIJ === "IJ.NONE"){
//     console.log("true") //is true passes in as a string instead of an enum
// }
console.log(p1_adult)
//adult is a string

// if(p1_adult=== true){
//     print("is not a string")
// }

function getPythonBool(val){
    switch(val){
        case "True":
           // kidY=0
            return true
        case "False":
          //  kidY=125
            return false
    }
}
function getAdult(val){
    switch(val){
        case "True":
           // kidY=0
            return {adult: true, y:0, x: 0, scale: 1}
        case "False":
          //  kidY=125
            return {adult:false, y:125, x:55, scale: 0.5}
    }
}

function getPythonIJ(val){
    switch(val){
        case "IJ.NONE":
            return IJ.NONE
        case "IJ.DYSENTERY":
            return IJ.DYSENTERY
        case "IJ.CHOLERA":
            return IJ.CHOLERA
        case "IJ.BROKEN_ARM":
            return IJ.BROKEN_ARM
        case "IJ.BROKEN_LEG":
            return IJ.BROKEN_LEG
        case "IJ.SNAKE_BITE":
            return IJ.SNAKE_BITE
        case "IJ.POISONED":
            return IJ.POSIONED
    }
}
console.log(p1_gender)
if(p1_gender)
function getGender(val){
    switch(val){
        case "MALE":
            return {gender:Gender.MALE, idle: MaleIdle, run: MaleWalk}
        case "FEMALE":
            return {gender: Gender.FEMALE, idle: FemaleIdle, run: FemaleWalk}
        default:
            console.log("No genders were detected")
    }
}
console.log(getPythonBool(p1_adult))

//parse the data 
// if(p1_currIJ ==IJ.NONE){
//     console.log("Also True")
// }
const ox = new Sprite({
    position:{
        x:850 + offsetX,
        y:430
    },
    imageSrc: Oxen,
    scale: 1,
    framesMax: 1,

})

const wagon = new Sprite({
    position:{
        x:1050 + offsetX,
        y:400
    },
    imageSrc: Wagon,
    scale: 1,
    framesMax: 1,

})
const MoneyMilesSpr = new Sprite({
    position:{
        x: window.innerWidth - 256,
        y:50
    },
    imageSrc: MoneyMiles,
    scale: 1,
    framesMax: 1,

})


const WagonFood= new Sprite({
    position:{
        x: 0,
        y:50
    },
    imageSrc: WagonFoodBar,
    scale: 1,
    framesMax: 1,

})

const py1_gender = getGender(p1_gender)
const py2_gender = getGender(p2_gender)
const py3_gender = getGender(p3_gender)
const py4_gender = getGender(p4_gender)
const py5_gender = getGender(p5_gender)

const py1_adult = getAdult(p1_adult)
const py2_adult = getAdult(p2_adult)
const py3_adult = getAdult(p3_adult)
const py4_adult = getAdult(p4_adult)
const py5_adult = getAdult(p5_adult)

const py1_dead = getPythonBool(p1_dead)
const py2_dead = getPythonBool(p2_dead)
const py3_dead = getPythonBool(p3_dead)
const py4_dead = getPythonBool(p4_dead)
const py5_dead = getPythonBool(p5_dead)



console.log(py1_gender)
// function getScale(val){
//     if(val){
//         return 1
//     }
//     else{
//         return 0.5
//     }
// }


const player1J = new Character({
    position: {
    x : window.innerWidth/6 *3 + 40,
    y: 400 + py1_adult.y
    },
    
    offset:{
        x: 0,
        y: 0,
    },
    imageSrc: py1_gender.run,
    //set our max frames
    framesMax: 16,
    scale: py1_adult.scale,
    name: p1_name,
    //name:"chad",
    adult: py1_adult.adult,
    gender: py1_gender.gender,
    dead: py1_dead,

    sprites:{
        idle:{
            imageSrc: py1_gender.idle,
            framesMax: 1,
        },
        run:{
            imageSrc: py1_gender.run,
            framesMax: 16,
        },
    
    },
    
});
console.log("p1 fine")
const player2J = new Character({
    position: {
    x : 900 + offsetX  + py2_adult.x,
    y: 400 + py2_adult.y
    },
    
    offset:{
        x: 0,
        y: 0,
    },
    imageSrc: py2_gender.run,
    //set our max frames
    framesMax: 16,
    scale: py2_adult.scale,
    name: p2_name,
    adult: py2_adult.adult,
    gender: py2_gender.gender,
    dead: py2_dead,

    sprites:{
        idle:{
            imageSrc: py2_gender.idle,
            framesMax: 1,
        },
        run:{
            imageSrc: py2_gender.run,
            framesMax: 16,
        },
    
    },
    
});
const player3J = new Character({
    position: {
    x : 1100 + offsetX + py3_adult.x,
    y: 400+ py3_adult.y
    },
    
    offset:{
        x: 0,
        y: 0,
    },
    imageSrc: py3_gender.run,
    //set our max frames
    framesMax: 16,
    scale: py3_adult.scale,
    name: p3_name,
    adult: py3_adult.adult,
    gender: py3_gender.gender,
    dead: py3_dead,

    sprites:{
        idle:{
            imageSrc: py3_gender.idle,
            framesMax: 1,
        },
        run:{
            imageSrc: py3_gender.run,
            framesMax: 16,
        },
    
    },
    
});
const player4J = new Character({
    position: {
    x : 1200 + offsetX + py4_adult.x,
    y: 400 + py4_adult.y
    },
    
    offset:{
        x: 0,
        y: 0,
    },
    imageSrc: py4_gender.run,
    //set our max frames
    framesMax: 16,
    scale: py4_adult.scale,
    name: p4_name,
    adult: py4_adult.adult,
    gender: py4_gender.gender,
    dead: py4_dead,

    sprites:{
        idle:{
            imageSrc: py4_gender.idle,
            framesMax: 1,
        },
        run:{
            imageSrc: py4_gender.run,
            framesMax: 16,
        },
    
    },
    
});
const player5J = new Character({
    position: {
    x : 1300 + offsetX + py5_adult.x,
    y: 400 + py5_adult.y
    },
    
    offset:{
        x: 0,
        y: 0,
    },
    imageSrc: py5_gender.run,
    //set our max frames
    framesMax: 16,
    scale: py5_adult.scale,
    name: p5_name,
    adult: py5_adult.adult,
    gender: py5_gender.gender,
    dead: py5_dead,

    sprites:{
        idle:{
            imageSrc: py5_gender.idle,
            framesMax: 1,
        },
        run:{
            imageSrc: py5_gender.run,
            framesMax: 16,
        },
    
    },
    
});

console.log("p5 fine")
const party = [player1J, player2J, player3J, player4J, player5J]
window.addEventListener('resize', ()=>{
    MoneyMilesSpr.position.x = window.innerWidth -256
    player1J.position.x = window.innerWidth/6 *3 + 40
    //reset when resized
})

//layers for the background
const layers = [
    {src: forest_background, speed:0.05},
    {src: trees, speed:0.1},
    {src: forest_foreground, speed:0.5},
    {src: wind, speed:1},
]

//list of images
const images = []
let offsets = []

layers.forEach((layer, index) =>{
    const img = new Image(); //create a new image
    img.src = layer.src; //populate the src with our saved value
    images.push(img); //add to the list
    offsets.push(0) //start at 0
});
// async function showdead(){
//     await showAlert(str);
// }

//animate the background
function animate(){
    c.clearRect(0,0, canvas.width, canvas.height)
    if(!gamePaused){

        layers.forEach((layer, index)=>{
            const img = images[index];
            const speed = layer.speed;
            const offset = offsets[index]
            
            //draw two copies for the wraparound effect
            c.drawImage(img, offset, 0, canvas.width, canvas.height)
            c.drawImage(img, canvas.width + offset, 0, canvas.width, canvas.height)
            
            //update the offset
            offsets[index] = (offset + speed- canvas.width) % canvas.width;
            step ++;
            if (step % mile ===0){
                miles++
                document.getElementById('miles-display').innerHTML = miles +" M"
                console.log(miles)
                for(let i = 0; i < party.length; i++){
                    if(!party[i].dead){
                        //party[i].die()
                        party[i].eat()
                        party[i].hurt()
                        party[i].injure()
                       // party[i].die()
                      //  console.log(party[i].stomach)
                       if(party[i].getStomach() < 50){
                            if (food >0){
                                food -= 5 //subtract 1 from food
                                party[i].setStomach(100)
                                gsap.to('#food', {
                                    width: food + '%'
                                })
                            }
                            else{
                                wagonHealth -= 5
                                food = 100
                                gsap.to('#wagon', {
                                    width: wagonHealth + '%'
                                })
                            }
                            //console.log("ABOUT TO CALL HURT food is: " + food)
                           
                            
                            }
                        }
                        
                    }
                    //party[1].die()
            }
        })
    }
    
        
    wagon.update()
    ox.update()
    c.fillStyle = 'rgba(255,255,255,0.15)'
    c.fillRect(0,0,canvas.width,canvas.height)
    for(let i = 0; i < party.length; i++){
        if(!party[i].dead){

            party[i].update()
        }
    }
   
    // player1J.update()
    // player2J.update()
    // player3J.update()
    // player4J.update()
    // player5J.update()
    MoneyMilesSpr.update()
    WagonFood.update()
    parallax = requestAnimationFrame(animate);
}

function togglePause(){
    console.log(miles)
    gamePaused = !gamePaused
    const button = document.getElementById('pauseBtn')
    button.textContent = gamePaused ? 'Run': "Stop";
    //console.log("pause")
    //animate()
    if (!gamePaused) {
        player1J.switchSprite('run')
        animate()
    }
    else{
        player1J.switchSprite('idle')
        cancelAnimationFrame(parallax)
    }
}

// for(let j = 0; j < party.length; j++){
//     if(!party[j].alertShown){
//         showAlert(party[j].name +" Has Died!");
//         party[j].showAlert = true
//         togglePause()
        
//     }
// }
// document.addEventListener('keydown', (event) => {
//     if (event.key === 'g') { // Example: Press "P" to pause/unpause
//         console.log(event.key)
//         togglePause();
//     }
// });
//call the toggle pause when we have finished
document.getElementById('pauseBtn').addEventListener('click', togglePause);
//make sure we are loaded in before we animate
// Promise.all(images.map(img => new Promise(resolve => img.onload = resolve))).then(()=>{
//     animate()
// });
animate()

function update_miles(){
    
}

//TERRIBLE NONSENSE but apparently this is how we do it
document.getElementById("saveButton").addEventListener("click", () =>{
    const gameID = gameId
    console.log(gameID)
    console.log(miles)

    fetch(`/update_game/${gameID}/`,{
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({
            miles:miles,
            p1_dead: player1J.dead,
            p2_dead: player2J.dead,
            p3_dead: player3J.dead,
            p4_dead: player4J.dead,
            p5_dead: player5J.dead,
            // add more here if we want to save more
            //player1j.currentInjury: player1j.currentInjury,

        }),
    })
    .then(response => response.json())
    .then(data => {
        if(data.success){
            alert("Miles updated")
        }
        else{
            alert("failed to update miles" + data.error);
        }

    })
    .catch(error=> console.error("Error:", error))
}
    // const miles = document.getElementById("miles-display").textContent //get current milies, will change later
    
);

//could use this to call front end methods or show that we need to call them
//idk if any have been debugged though

//get the cookie
function getCookie(name){
    let cookieVal = null
    if(document.cookie && document.cookie !==""){
        const cookies = document.cookie.split(";").map(c=> c.trim())
        for(const cookie of cookies){
            if(cookie.startsWith(name+"=")){
                cookieVal = decodeURIComponent(cookie.substring(name.length + 1))
                break;
            }
        }
    }
    return cookieVal
}

