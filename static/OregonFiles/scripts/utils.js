//probably easier to put stuff here and then update them later on the front when saving
function showAlert(msg){
    //initially tried using thits but maybe a promise is better?
    return new Promise((resolve)=>{

        console.log("show msg: "+msg)
        const dialogueBox = document.getElementById('dialogue-box');
        const dialogueText = document.getElementById('dialogue-text');
        const okButton = document.getElementById('dialogue-ok-btn');
        //set the message
        dialogueText.textContent = msg;
        

        //show alert
        dialogueBox.classList.add('active');

        //when ok is clicked then resume
        okButton.onclick = () =>{
            dialogueBox.classList.remove('active');
            resolve();
        }
        //show the alert by making visible and opaque
        // dialogueBox.style.visibility = 'visible';
        // dialogueBox.style.opacity = '1'
    })

    // togglePause();
}

//close the alert
// function closeAlert(){
//     const dialogueBox = document.getElementById('dialogue-box');

//     //hide the alert
//     dialogueBox.visibility = 'hidden';
//     dialogueBox.style.opacity = '0';
//     // togglePause();
// }