//probably easier to put stuff here and then update them later on the front when saving

function showAlert(msg){
    const dialogueBox = document.getElementById('dialogue-box');
    const dialogueText = document.getElementById('dialogue-text');

    //set the message
    dialogueText.textContent = msg;

    //show the alert by making visible and opaque
    dialogueBox.visibility = 'visible';
    dialogueBox.opacity = '1'

    togglePause();
}

//close the alert
function closeAlert(){
    const dialogueBox = document.getElementById('dialogue-box');

    //hide the alert
    dialogueBox.visibility = 'hidden';
    dialogueBox.style.opacity = '0';
    togglePause();
}