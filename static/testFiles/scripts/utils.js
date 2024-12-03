function rectangularCollision(
    {
        rectangle1, rectangle2
    }
){
    return( rectangle1.attackBox.position.x + rectangle1.attackBox.width >= 
        rectangle2.position.x && rectangle1.attackBox.position.x <= rectangle2.position.x + rectangle2.width &&
        rectangle1.attackBox.position.y + rectangle1.attackBox.height >= rectangle2.position.y
        && rectangle1.attackBox.position.y <= rectangle2.position.y + rectangle2.height &&
        rectangle1.isAttacking)
        //returns if true or false
}
//end the game
function determineWinner({player, enemy, timerId}){
    clearTimeout(timerId)
     document.querySelector('#displayText').style.display = 'flex'
    if(player.health === enemy.health){
        document.querySelector('#displayText').innerHTML = 'TIE'
        
    }else if(player.health > enemy.health){
         document.querySelector('#displayText').innerHTML = 'Player 1 wins'

    }
    else if(player.health < enemy.health){
        document.querySelector('#displayText').innerHTML = 'Player 2 wins'

   }
}
// function for decreasing time

let timer = 60;
let timerId
function decreaseTimer(){
    timerId = setTimeout(decreaseTimer, 1000)
    //call self after 1000 miliseconds
    if (timer > 0)
    {timer --;
        document.querySelector("#timer").innerHTML = timer
    }
    if(timer === 0){
     
      determineWinner({player, enemy, timerId})  
    }
    //determine who won

}