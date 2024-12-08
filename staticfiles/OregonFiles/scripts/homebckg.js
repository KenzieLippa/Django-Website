///here we are going to do the parallax for the background
const canvas = document.querySelector('canvas');
const c = canvas.getContext('2d')

let parallax;

//fill the window but may need to fix with the nav bar
//canvas size
canvas.width = 1710
canvas.height = 900

let kidY = 125
// if(p1_currIJ === "IJ.NONE"){





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
   // if(!gamePaused){

        layers.forEach((layer, index)=>{
            const img = images[index];
            const speed = layer.speed;
            const offset = offsets[index]
            
            //draw two copies for the wraparound effect
            c.drawImage(img, offset, 0, canvas.width, canvas.height)
            c.drawImage(img, canvas.width + offset, 0, canvas.width, canvas.height)
            
            //update the offset
            offsets[index] = (offset + speed- canvas.width) % canvas.width;
        })
        

    parallax = requestAnimationFrame(animate);
}


animate()


//TERRIBLE NONSENSE but apparently this is how we do it
