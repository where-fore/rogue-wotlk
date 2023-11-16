import random

# every reference to seconds, time, is multiplied by 10, so my tenth-of-a-second-sim-ticks can be a whole integer

# sim settings
timeBetweenEnemyAttack = 20

parryDuringRiposteRefreshes = True
parryChance = 5+5+10+7 # 5 base + 5 talent + 10 gauche + 7 avg blade dance

totalSimIterations = 10000
fightLength = 300

riposteDuration = 60

# initialize counters. copy paste these in the resetSim() function if you change
currentEnemySwingTimer = 0
currentRiposteDuration = 0
uptimeSecondsThisIteration = 0
elapsedTimeInIteration = 0
# except me don't copy me
elapsedIterations = 0
uptimeSecondsTotal = 0

def enemyAttack():
    global currentRiposteDuration
    roll = random.randint(1,100)
    print("rolled a ", roll)
    if roll < parryChance: #if you roll a parry
        print("parried")

        if parryDuringRiposteRefreshes:
            currentRiposteDuration = riposteDuration

        elif not parryDuringRiposteRefreshes:
            if currentRiposteDuration <= 0: #if you have no riposte active
                currentRiposteDuration = riposteDuration

def simTick():
    global currentEnemySwingTimer
    global currentRiposteDuration
    global elapsedTimeInIteration
    global uptimeSecondsThisIteration

    if currentRiposteDuration > 0:
        uptimeSecondsThisIteration += 1
        currentRiposteDuration -= 1
    
    if currentEnemySwingTimer <= 0:
        enemyAttack()
        currentEnemySwingTimer = timeBetweenEnemyAttack
    currentEnemySwingTimer -= 1

    elapsedTimeInIteration += 1
    #print("time is now", elapsedTimeInIteration)

def resetSim():
    global currentEnemySwingTimer
    global currentRiposteDuration
    global uptimeSecondsThisIteration
    global elapsedTimeInIteration

    # save results
    global uptimeSecondsTotal
    uptimeSecondsTotal += uptimeSecondsThisIteration

    # reset counters
    currentEnemySwingTimer = 0
    currentRiposteDuration = 0
    uptimeSecondsThisIteration = 0
    elapsedTimeInIteration = 0

#run the sim
while elapsedIterations < totalSimIterations:

    while elapsedTimeInIteration < fightLength:
        simTick()
        #print("-----")

    print("-----")
    resetSim()
    elapsedIterations += 1

totalFightLength = fightLength*totalSimIterations
totalRiposteUptime = uptimeSecondsTotal / totalFightLength *100
print("total uptime was", totalRiposteUptime, "%:", uptimeSecondsTotal/10, "seconds, out of", totalFightLength/10, "seconds fighting")