//putting the model funcs in here instead
const Season = Object.freeze({
    SPRING: 0,
    SUMMER: 1, 
    FALL: 2,
    WINTER: 3
})
const Gender = Object.freeze({
    MALE:0,
    FEMALE:1
})

const Day = Object.freeze({
    STANDING :0,
    WALKING: 1
})

const IJ = Object.freeze({
    NONE: 0,
    DYSENTERY: 1,
    CHOLERA: 2,
    BROKEN_ARM: 3,
    BROKEN_LEG: 4,
    SNAKE_BITE: 5,
    POSIONED: 6,
})

//if end up having time
const Deal = Object.freeze({
    NONE: 0,
    GIVE_MONEY: 1,
    TAKE_MONEY: 2,
    GIVE_CURE: 3,
    GIVE_POISON: 4,
})
function move(miles, party){
    //move function, here we will update the miles
    //might want to change the frequency here
    anyInjured = false;
    for(let i = 0; i < party.length; i++){
        //for everyone in the party see if anyone is injured, if they are then walk slower
        if(party[i].getInjured() === true){
            anyInjured = true;
        }
    }
    if(anyInjured){
        miles += 0.1
    }else{
        miles += 0.2
    }
    return miles //just in case we need it

}

function advanceDay(day, daysLeft, season){
    //probably would add more here
    day++;
    if(daysLeft>0){

        daysLeft --;
    }
    else{
        incramentSeason(season)
        setSeasonStats(season)
    }
    return {day: day, daysLeft: daysLeft}
}

function incramentSeason(season){
    //incraments the current season
    switch(season){
        case Season.SPRING:
            return Season.SUMMER
           // break
        case Season.SUMMER:
            return Season.FALL
            //break
        case Season.FALL:
            return Season.WINTER
            //break
        case Season.WINTER:
            return Season.SPRING

    }
}

function setSeasonStats(season){
    switch(season){
        case Season.SPRING:
            return{
                daysLeft: 28,
                healPenalty: 2,
                foodPenalty: 1,
                speedPenalty: 1
            }
           // break

        case Season.SUMMER:
            return{
                daysLeft: 28,
                healPenalty: 0,
                foodPenalty: 0,
                speedPenalty: 0
            }
           // break

        case Season.FALL:
            return{
                daysLeft: 28,
                healPenalty: 3,
                foodPenalty: 3,
                speedPenalty: 2
            }
           // break

        case Season.WINTER:
            return{
                daysLeft: 28,
                healPenalty: 10,
                foodPenalty: 10,
                speedPenalty: 10
            }
           // break
    }
}



function advanceDay(day, daysLeft, season){
    //probably would add more here
    day++;
    if(daysLeft>0){

        daysLeft --;
    }
    else{
        season = incramentSeason(season)
        setSeasonStats(season)
    }
    return {day: day, daysLeft: daysLeft}
}

