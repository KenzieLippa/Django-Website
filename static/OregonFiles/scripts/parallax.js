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

let step = 0;
let gameId = game_id
//fill the window but may need to fix with the nav bar
//canvas size
canvas.width = 1710
canvas.height = 900

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
const player1J = new Character({
    position: {
    x : 700 + offsetX,
    y: 400
    },
    
    offset:{
        x: 0,
        y: 0,
    },
    imageSrc: MaleWalk,
    //set our max frames
    framesMax: 16,
    scale: 1,
    name: "Chad",
    adult: true,
    gender: Gender.MALE,

    sprites:{
        idle:{
            imageSrc: MaleIdle,
            framesMax: 1,
        },
        run:{
            imageSrc: MaleWalk,
            framesMax: 16,
        },
    
    },
    
});
const player2J = new Character({
    position: {
    x : 900 + offsetX,
    y: 400
    },
    
    offset:{
        x: 0,
        y: 0,
    },
    imageSrc: FemaleWalk,
    //set our max frames
    framesMax: 16,
    scale: 1,
    name: "Fema",
    adult: true,
    gender: Gender.FEMALE,

    sprites:{
        idle:{
            imageSrc: FemaleIdle,
            framesMax: 1,
        },
        run:{
            imageSrc: FemaleWalk,
            framesMax: 16,
        },
    
    },
    
});
const player3J = new Character({
    position: {
    x : 1100 + offsetX,
    y: 525
    },
    
    offset:{
        x: 0,
        y: 0,
    },
    imageSrc: FemaleWalk,
    //set our max frames
    framesMax: 16,
    scale: 0.5,
    name: "Mingus",
    adult: false,
    gender: Gender.FEMALE,

    sprites:{
        idle:{
            imageSrc: FemaleIdle,
            framesMax: 1,
        },
        run:{
            imageSrc: FemaleWalk,
            framesMax: 16,
        },
    
    },
    
});
const player4J = new Character({
    position: {
    x : 1200 + offsetX,
    y: 525
    },
    
    offset:{
        x: 0,
        y: 0,
    },
    imageSrc: MaleWalk,
    //set our max frames
    framesMax: 16,
    scale: 0.5,
    name: "RayRay",
    adult: false,
    gender: Gender.MALE,

    sprites:{
        idle:{
            imageSrc: MaleIdle,
            framesMax: 1,
        },
        run:{
            imageSrc: MaleWalk,
            framesMax: 16,
        },
    
    },
    
});
const player5J = new Character({
    position: {
    x : 1300 + offsetX,
    y: 525
    },
    
    offset:{
        x: 0,
        y: 0,
    },
    imageSrc: MaleWalk,
    //set our max frames
    framesMax: 16,
    scale: 0.5,
    name: "Boo Jenkins",
    adult: false,
    gender: Gender.MALE,

    sprites:{
        idle:{
            imageSrc: MaleIdle,
            framesMax: 1,
        },
        run:{
            imageSrc: MaleWalk,
            framesMax: 16,
        },
    
    },
    
});

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

//animate the background
function animate(){
    c.clearRect(0,0, canvas.width, canvas.height)

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
        wagon.update()
        ox.update()
        c.fillStyle = 'rgba(255,255,255,0.15)'
        c.fillRect(0,0,canvas.width,canvas.height)
        player1J.update()
        player2J.update()
        player3J.update()
        player4J.update()
        player5J.update()
        if (step % mile ===0){
            miles++
            document.getElementById('miles-display').innerHTML = miles
            console.log(miles)
        }
    })
    parallax = requestAnimationFrame(animate);
}
function togglePause(){
    console.log(miles)
    gamePaused = !gamePaused
    const button = document.getElementById('pauseBtn')
    button.textContent = gamePaused ? 'Run': "Stop";
    //console.log("pause")
    if (!gamePaused) {
        player1J.switchSprite('run')
        animate()
    }
    else{
        player1J.switchSprite('idle')
        cancelAnimationFrame(parallax)
    }
}
// document.addEventListener('keydown', (event) => {
//     if (event.key === 'g') { // Example: Press "P" to pause/unpause
//         console.log(event.key)
//         togglePause();
//     }
// });
//call the toggle pause when we have finished
document.getElementById('pauseBtn').addEventListener('click', togglePause);
//make sure we are loaded in before we animate
Promise.all(images.map(img => new Promise(resolve => img.onload = resolve))).then(()=>{
    animate()
});

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
        body: JSON.stringify({miles:miles}),
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

