from django.db import models
from django.contrib.auth.models import User
from enum import Enum
import random
# Create your models here.
class IJ(Enum):
    '''use a switch case here to determine problem chance'''
    NONE = 0
    DYSENTERY = 1
    CHOLERA = 2
    BROKEN_ARM = 3
    BROKEN_LEG = 4
    SNAKE_BITE = 5
    POSIONED = 6
class Gender(Enum):
    '''to use text choices for gender field'''
    MALE = "Male"
    FEMALE = "Female"

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]
    
class Deal(Enum):
    '''starts with good deals but if evil will reroll good deal into bad one'''
    NONE =0
    GIVE_MONEY = 1
    TAKE_MONEY = 2
    GIVE_CURE = 3
    GIVE_POISON = 4

class Day(Enum):
    WALKING = 0 
    REST = 1
# class Hunger(Enum):
#     '''Use switch here as well to determine what will go wrong with the character'''
#     STARVING = 1
#     HUNGRY = 2
#     NEUTRAL = 3
#     FULL = 4

class Season(Enum):
    SPRING = "Spring"
    SUMMER = "Summer"
    FALL = "Fall"
    WINTER = "Winter"
    
    @classmethod
    def choices1(cls):
        return [(choice.name, choice.value) for choice in cls]

class Profile(models.Model):
    '''store the information for the player and the relevant information'''
    name = models.TextField(blank=False)
    age = models.IntegerField(blank=True, null=True)
    # currentGame = models.ForeignKey('Game',
    #                                 null=True,
    #                                 blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name = "oregon_profile", on_delete=models.CASCADE)
    bestScore = 0 #will have a setter function for this


    def setBestScore(self, score):
        '''set the best score if our new score is better than our last one'''
        self.bestScore = score

    def get_games(self):
        '''return all games assosciated with this profile'''
        game = Game.objects.filter(profile = self)
        return game

    def __str__(self):
        return f'{self.name}'

# base model rn for the game, oh man this one might get huge but idk
class Game(models.Model):
    '''include details of the game'''
    # player_id = models.ForeignKey('Profile', on_delete=models.CASCADE)
    # last_name = models.TextField(blank=False)
    # city = models.TextField(blank=False)
    # email_address = models.EmailField(blank=False)
    # for profile url
    # profile_img = models.URLField(blank=False)

    # add user field
    # associate game with a user

    active = True #set to true by default
    profile = models.ForeignKey('Profile', related_name='profileg', on_delete=models.CASCADE)
    player1 = models.ForeignKey('Character', related_name='player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey('Character', related_name='player2',on_delete=models.CASCADE)
    player3 = models.ForeignKey('Character', related_name='player3',on_delete=models.CASCADE)
    player4 = models.ForeignKey('Character', related_name='player4', on_delete=models.CASCADE)
    player5 = models.ForeignKey('Character', related_name='player5',on_delete=models.CASCADE)

    party = [player1, player2, player3, player4, player5]
    miles = models.IntegerField(default=0) #how many miles has the player gone
    days = models.IntegerField(default=0)
    # will be figured out later as different seasons will have different properties,
    #probably will make seasons their own model
    # currentSeason = models.CharField(
    #     max_length=10,
    #     choices=Season.choices1(),
    #     blank=False
    # )
    season = models.CharField(
        max_length=10,
        choices=Season.choices1(),
        blank=False
    )
    playersAlive = models.IntegerField(default=5)
    dayState = Day.WALKING #default

    currDay = 0 #incramented each day
    speed = 10 # TODO make it modifiable based on injuries in the party
    def move(self):
        '''a function to calculate current miles, again not sure what we going to do here'''
        if Day.WALKING:
            anyInjured = False
            # TODO fix the reverse accessor error
            for member in self.party:
                if member.getInjured() == True:
                    anyInjured = True
            
            if anyInjured:
                miles +=0.1
            else:
                miles +=0.2
        
    def advanceDay(self):
        '''a function to move everything forward and update everything'''
        # TODO figure out how to call all methods from players, might get moved to js file
        self.currDay += 1

    def setScore(self, score):
        self.score = score

    daysLeft = 28 #days before season switches
    healPenalty = 0 # what is the rest day penalty, will be added to rest days and days left
    foodPenalty = 0 #added to the food storage to see if harder to get food
    speedPenalty = 0 #slows the player down

    def setDefault(self, season):
        self.daysLeft = 28 #days before season switches
        self.healPenalty = 0 # what is the rest day penalty, will be added to rest days and days left
        self.foodPenalty = 0 #added to the food storage to see if harder to get food
        self.speedPenalty = 0 #slows the player down
        self.setCurrentSeason(season)

    def setCurrentSeason(self, season):
        '''set the current season'''
        self.currenSeason = season
        self.setSeasonStats()

    def incramentSeason(self):
        '''maybe will refactor later to make less terrible
        didnt end up being too much code tho'''
        match(self.currenSeason):
            case Season.SPRING:
                self.currenSeason = Season.SUMMER
            case Season.SUMMER:
                self.currenSeason = Season.FALL
            case Season.FALL:
                self.currenSeason = Season.WINTER
            case Season.WINTER:
                self.currenSeason = Season.SPRING

    def setDaysLeft(self, days):
        self.daysLeft = days

    def setHealPenalty(self, val):
        self.healPenalty = val
    def setFoodPenalty(self, food):
        self.foodPenalty = food

    def setSpeedPenalty(self, speed):
        self.speedPenalty = speed

    def setSeasonStats(self):
        match(self.currentSeason):
            case Season.SPRING:
                # could have just had it automatically been 28
                self.setDaysLeft(28) # set back to full
                self.setHealPenalty = 2
                self.setFoodPenalty = 1
                self.setSpeedPenalty = 1
            case Season.SUMMER:
                self.setDaysLeft(28) # set back to full
                self.setHealPenalty = 0
                self.setFoodPenalty = 0
                self.setSpeedPenalty = 0
            case Season.FALL:
                self.setDaysLeft(28) # set back to full
                self.setHealPenalty = 3
                self.setFoodPenalty = 3
                self.setSpeedPenalty = 2
            case Season.WINTER:
                self.setDaysLeft(28) # set back to full
                self.setHealPenalty = 10
                self.setFoodPenalty = 10
                self.setSpeedPenalty = 10
            

    def progressDay(self):
        if self.daysLeft > 0:
            self.daysLeft -= 1
        else:
            self.incramentSeason()
            self.setSeasonStats()

    def __str__(self):
        return f'{self.player1}'
    
class Season(models.Model):
    '''Will set the current enviroment buffs based on what season it is'''
    # TODO figure out how to use season buffs to hurt or help the player, can always make it a method in player
    # not sure exactly since i stupidly am setting everything without methods but i could still probably leave it and continue forward with methods
    # will probably refactor though
    name = models.TextField(blank=False)
    currentSeason = models.CharField(
        max_length=10,
        choices=Season.choices1(),
        blank=False
    )
    daysLeft = 28 #days before season switches
    healPenalty = 0 # what is the rest day penalty, will be added to rest days and days left
    foodPenalty = 0 #added to the food storage to see if harder to get food
    speedPenalty = 0 #slows the player down

    def setDefault(self, season):
        self.daysLeft = 28 #days before season switches
        self.healPenalty = 0 # what is the rest day penalty, will be added to rest days and days left
        self.foodPenalty = 0 #added to the food storage to see if harder to get food
        self.speedPenalty = 0 #slows the player down
        self.setCurrentSeason(season)

    def setCurrentSeason(self, season):
        '''set the current season'''
        self.currenSeason = season
        self.setSeasonStats()

    def incramentSeason(self):
        '''maybe will refactor later to make less terrible
        didnt end up being too much code tho'''
        match(self.currenSeason):
            case Season.SPRING:
                self.currenSeason = Season.SUMMER
            case Season.SUMMER:
                self.currenSeason = Season.FALL
            case Season.FALL:
                self.currenSeason = Season.WINTER
            case Season.WINTER:
                self.currenSeason = Season.SPRING

    def setDaysLeft(self, days):
        self.daysLeft = days

    def setHealPenalty(self, val):
        self.healPenalty = val
    def setFoodPenalty(self, food):
        self.foodPenalty = food

    def setSpeedPenalty(self, speed):
        self.speedPenalty = speed

    def setSeasonStats(self):
        match(self.currentSeason):
            case Season.SPRING:
                # could have just had it automatically been 28
                self.setDaysLeft(28) # set back to full
                self.setHealPenalty = 2
                self.setFoodPenalty = 1
                self.setSpeedPenalty = 1
            case Season.SUMMER:
                self.setDaysLeft(28) # set back to full
                self.setHealPenalty = 0
                self.setFoodPenalty = 0
                self.setSpeedPenalty = 0
            case Season.FALL:
                self.setDaysLeft(28) # set back to full
                self.setHealPenalty = 3
                self.setFoodPenalty = 3
                self.setSpeedPenalty = 2
            case Season.WINTER:
                self.setDaysLeft(28) # set back to full
                self.setHealPenalty = 10
                self.setFoodPenalty = 10
                self.setSpeedPenalty = 10
            

    def progressDay(self):
        if self.daysLeft > 0:
            self.daysLeft -= 1
        else:
            self.incramentSeason()
            self.setSeasonStats()
    
    def __str__(self):
        return f"{self.name}"
    
class Character(models.Model):
    '''this will be the main character class where models of this will be created
    to reflect the players party, will be maxed to 5 though Im not sure how to do this yet'''
    # TODO: max to five possible players
    name = models.TextField(blank=False)
    # choose if adult or child
    adult = models.BooleanField(blank=False)
    # select the gender of the player
    gender = models.CharField(
        max_length=10,
        choices=Gender.choices(),
        blank=False
    )
    #will need to check this to determine whether to run any of these or not
    dead = models.BooleanField(default=False)
    #TODO: figure out how to populate the sprite, maybe through character creation on the js side

    #TODO: figure out the injury if we want to use enum or string rep, i think strings still fine as long as its consistent and might be easier with scope
    #also might end up being an object with propertiesnot sure
    # currentInjury = "None" #assign to a string or an enum, enum might be easier idk, im not sure where i would define it anyway
    currentInjury = models.TextField(default="IJ.NONE")
    health = models.IntegerField(default=100)
    injuryChance = models.FloatField(default=0.02)
    hunger = models.FloatField(default=0.01)
    healthLoss = models.IntegerField(default=0)
    restDaysNeeded = models.IntegerField(default=0)
    treated = models.BooleanField(default=False)
    #if no effort is put into healing the disease how long will it take till it is healed
    slowHeal = models.IntegerField(default=0)
    deathChance = models.IntegerField(default=0)
    infected = models.BooleanField(default=False)
    stomach = models.IntegerField(default=100)
    if adult:
        # if the character is an adult then the hurt chance is lower
        health = 150
        injuryChance = 0.01
        hunger = 0.2
        # TODO: test and tweak values


    def reset(self):
        '''reset so the character is no longer dead when a new game is started'''
        self.dead = False
        self.health = 100
        self.stomach = 100
        self.save()

    def setInjuryStats(self):
        '''setting stats based on injury
        SUBJECT TO CHANGE WITH TESTING'''
        match(self.currentInjury):
            case IJ.NONE:
                if self.adult:
                    #set the injury chance back
                    self.injuryChance = 0.01
                    self.hunger = 0.2
                else:
                    self.injuryChance = 0.02
                    self.hunger = 0.1
                self.healthLoss = 0
                self.restDaysNeeded = 0
                self.slowHeal = 0
                self.treated = False
                self.deathChance = 0
                self.infected = False
          
            case IJ.CHOLERA:
                self.healthLoss = -0.2
                self.hunger = 0.3
                self.injuryChance = 0.03
                self.restDaysNeeded = 3
                self.slowHeal = 6
                self.deathChance = 10
            case IJ.DYSENTERY:
                '''much more deadly i think'''
                self.healthLoss = -0.5
                self.hunger = 0.4
                self.injuryChance = 0.09
                self.restDaysNeeded = 5
                self.slowHeal = 10
                self.deathChance = 20
                if self.infected:
                    self.deathChance = 0.5
            case IJ.BROKEN_ARM:
                '''worse than the arm because the player is running on it'''
                self.healthLoss = -0.01
                self.getInfected(self.injuryChance)
                if self.infected:
                    self.deathChance = 30
                    self.slowHeal = 20
                    self.restDaysNeeded = 10
                    self.healthLoss = -0.1
                else:
                    self.slowHeal = 10
                    self.restDaysNeeded = 5
                    self.deathChance = 1
            case IJ.BROKEN_LEG:
                self.healthLoss = -0.03
                self.getInfected(self.injuryChance)
                if self.infected:
                    self.deathChance = 40
                    self.slowHeal = 25
                    self.restDaysNeeded = 15
                    self.healthLoss = -0.3
                else:
                    self.slowHeal = 15
                    self.restDaysNeeded = 10
                    self.deathChance = 1
            case IJ.SNAKE_BITE:
                self.healthLoss = -5
                self.deathChance = 1000
                # needs to be cured!
                self.slowHeal = 300
                self.restDaysNeeded = 200
            case IJ.POSIONED:
                # if was poisoned then everything gets much worse until an andidote is found
                self.healthLoss = -10
                self.deathChance += 1000 #adds 1000 to death chance
                self.slowHeal = 600 #dont let the player heal unless really lucky
                self.restDaysNeeded = 400
        if self.treated:
            self.slowHeal = 1
            self.restDaysNeeded = 1
            self.deathChance = 7
            self.healthLoss = 0
            self.currentInjury = IJ.NONE # next time stats are set then the sets will all be set back

    def getDead(self):
        '''see if the player is dead'''
        return self.dead
    def eat(self):
        self.stomach -= self.hunger
        if self.stomach < 50:
            # if less than 50 then double the hunger
            self.hunger += self.hunger
        if self.stomach < 25:
            self.hunger += self.hunger
        if self.stomach < 10:
            self.hunger += self.hunger
            self.injuryChance += self.injuryChance
        if self.stomach < 5:
            self.hunger += self.hunger
            self.injuryChance += self.injuryChance
        if self.stomach < 0:
            self.hunger += self.hunger
            self.injuryChance += self.injuryChance
            self.deathChance += 10
            self.healthLoss += 5

    def injure(self):
        '''run this function with our injury chance and decide which injury to have'''
        injureChance = self.injuryChance * 100
        getInjury = random.randint(0,100)
        if getInjury >= injureChance:
            return IJ.NONE
        else:
            injuryType = random.randint(0,5)
            match(injuryType):
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

    # TODO: figure out how often to run these functions
    def hurt(self):
        '''if we ran out of health then we run this
        if we are out of health then we want to run snake eyes, 
        if we are worse than out of health then we want to do it multiple times'''
        if self.health == 0:
            deathChance = 10 + self.deathChance
            for i in range(deathChance):
                self.snakeEyes()
        elif self.health < 0:
            deathChance = 100 + self.deathChance
            for i in range(deathChance):
                self.snakeEyes()
        else:
            for i in range(deathChance):
                self.snakeEyes()

        self.health += self.healthLoss


                
    def getInfected(self, chance):
        c = random.randint(0,100) * chance
        if chance >= 1:
            self.infected = True

    def snakeEyes(self):
        '''to calculate whether the player should die in a turn'''
        # roll = [death, death, death]
        # tested in the shell, seems to proc very rarely when you run 10000 trials will run 9 times
        #this will start running when health hits zero
        c = random.randint(0,10)
        if c == 1:
            d = random.randint(0,10)
            if d == 1:
                e = random.randint()
                if e == 1:
                   self.die() 

            

    def setHealth(self, health):
        self.health = health

    def setInjury(self, injury):
        self.currentInjury = injury
        self.setInjuryStats()

    def getTreated(self):
        self.treated = True
        # treat self
        # self.currentInjury = IJ.NONE
        self.setInjuryStats()

    def die(self):
        self.dead = True
    
    def getInjured(self):
        if self.currentInjury != IJ.NONE:
            return True
        else:
            return False
    
    def setRest(self):
        if self.restDaysNeeded >0:
            self.restDaysNeeded -=1
        elif self.restDaysNeeded == 0:
            self.finishRest()
    def setSlowHeal(self):
        if self.slowHeal > 0:
            self.slowHeal -= 1
        elif self.slowHeal == 0:
            self.finishRest()
    
    def finishRest(self):
        '''player has finished rest days'''
        if self.restDaysNeeded == 0 or self.slowHeal == 0:
            self.currentInjury = IJ.NONE
            self.setInjuryStats()
    def __str__(self):
        return f"{self.name}"

class NPC(models.Model):
    '''class for sellers or deal makers'''
    evilChance = models.IntegerField(blank=False)
    name = models.TextField(blank=False)
    deal = Deal.NONE
    fakeDeal = Deal.NONE
    isEvil = False
    Dialogue = models.ForeignKey("Dialogue", null=True,blank=True, on_delete=models.CASCADE)

    def setEvil(self):
        '''set the evil value based on evil chance'''
        roll = random.randint(0,10)
        if roll > self.evilChance:
            self.isEvil = True

    def setDeal(self):
        if self.isEvil:
            roll = random.randint(0,1)
            if roll == 0:
                self.deal = Deal.GIVE_MONEY
                self.fakeDeal = Deal.GIVE_MONEY
            else:
                self.deal = Deal.GIVE_CURE
                self.fakeDeal = Deal.GIVE_CURE
        else:
            roll = random.randint(0,1)
            if roll == 0:
                self.deal = Deal.TAKE_MONEY
                self.fakeDeal = Deal.GIVE_MONEY
            else:
                self.deal = Deal.GIVE_POISON
                self.fakeDeal = Deal.GIVE_CURE

    def getDeal(self):
        return self.deal
    def getFakeDeal(self):
        return self.fakeDeal
    
    def __str__(self):
        return f"{self.name}"
    


        
class Dialogue(models.Model):
    '''a class for dialogue creation for the game, either player notifications triggered
    by events or npc dialogue'''
    # TODO: add more fields
    # npc = models.ForeignKey("NPC", null = True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    # TODO add some kind of time period or event trigger
    # time = models.IntegerField(blank=True)

    # TODO make text boxes
    # TODO decide if i want to read in json files for this
    def __str__(self):
        return self.text

# TODO: FIX LATER
# class GameStats(models.Model):
#     # probably will have these populated automatically when the game is over but will send a json or text post to the backend
#     deathSeason = models.CharField(
#         max_length=10,
#         choices=Season.choices1(),
#         blank=False
#     )
#     daysLived = models.IntegerField
#     milesTraveled = models.IntegerField
#     illnessesObtained = models.IntegerField
#     strangersTrusted = models.IntegerField
#     moneyLeft = models.IntegerField
#     foodLeft = models.IntegerField
#     game = models.ForeignKey("Game", on_delete=models.CASCADE)
