#customize your sim settings here. you can customize your readout settings below. you can customize other settings below, but know this was poorly coded and you could upset the spaghetti


simTitle = "my simulation" # this will optionally print above your data print out, so you can easily copy/paste the output and it will have a title


adrenalineRushBehaviour = 0 # 0: never cast, 1: cast on pull after slice, 2: cast as soon as you can without capping

bladeFlurryBehaviour = 0 # 0: never cast, 1: cast on pull after slice and after optional adrenaline rush

openingSliceBehaviour = 1 # number of cp to cast first slice at. type a number greater than 5 to never slice

thistleTeaBehaviour = 0 # 0: never cast, 1: cast when <40 energy and off gcd


hastePotionBehaviour = 0 # 0: cast with blade flurry, 1: cast on pull

shivBehaviour = 0 # number of shivs to cast



#time is in 0.1s ticks in this sim, so a weapon speed of 14 is 1.4 seconds, lust activating at 100 means 10.0 seconds

#sim settings
iterations = 50000
adrenalineRushMaxEnergyToCast = 85 # this includes the refund you would get if you cast it
bladeFlurryMaxEnergyToCast = 85
ruthlessnessBehaviour = 2 # 0: guaranteed off, 1: guaranteed on, 2: random like in game
relentlessBehaviour = 2 # 0: guaranteed off, 1: guaranteed on, 2: random like in game
combatPotencyBehaviour = 2 # 0: guaranteed off, 1: guaranteed 3 on each swing, 2: random 15 like in game
sliceSafetyBehaviour = 0 # 0: cast slice no matter your energy situation, 1: cast slice only if getting a relentless proc wouldn't put you in overcapping danger
sliceMaxEnergyToCast = 85 # sim won't case slice if 1. the above setting is on, and 2. your energy + energy tick in next 1s is less/equal than this value
lustActivatesAt = 400 # large number to default to not cast these buffs
drumsActivatesAt = 300
firstEnergyTickBehaviour = 1 # 0: average middle of next tick on pull, 1: random like in game
maxSimTime = 400 # just a failsafe to stop the sim from an infinite loop - if you are running into 30s opener times somehow you might want to increase this
dstEquipped = True
glaivesEquipped = False # you might want to adjust weapon speed
mongooseMHEquipped = True
mongooseOHEquipped = True
customRatingEquipped = False
customMultiEqupped = False
parryOnOpener = True
parryOnOpenerTime = 15

#readout settings
#these settings can change what the sim spits out for the final readout, in case you want/don't want certain information
printTitle = True
printVersion = True
printIterations = True
printSteadyStateTime = True #this prints the time until you got expose AND slice up - intending to paint a better picture of your slice downtime
printExposeTime = True
printSliceDropTime = True
printEnergyFromPotency = True
printSlowestExpose = True
printFastestExpose = True
printSlowestOpener = True
printFastestOpener = True
printCooldownBehaviour = True
printOvercappedEnergy = False
printMostOvercappedEnergy = False
printPPMReadout = True
PPMreadoutBehaviour = 0 # 0: Show % of trials that has dst proc before a certain time, 1: show % of trials dst procced at most x seconds before casting expose
PPMReadoutMaximumTime = -1 # -1 for % of procs before opener ends, put any other number for % of procs before that time in ticks (eg. 60 to see % of procs before 6 seconds)
PPMReadoutTimeSubtraction = 40 #how many ticks you want to see if dst procced before opener ends (25 to see what % of trials had dst proc 2.5 seconds before opener ends, or later - but not earlier)
printDecimalPlaces = 2
printLoadingBarSteps = 450
loadingBarCharacter = "█"
debugMode = False #turning this on will make the sim print out basically every action it takes: what time it is every frame, when auto attacks lands etc. significantly slows the sim down

#custom tracking proc - does actually give haste too, if configured to do so
customTrackingProcName = "default dst clone tracker" #this is just a title that gets printed in the readout
customTrackingProcEquipped = True
customTrackingProcBehaviour = 0 # 0: PPM mode, use the PPM defined below, 1: Chance mode, use the flat percent chance below
customTrackingProcPPM = 1
customTrackingProcChance = 10 #in raw percent, so 10 for 10%
customTrackingProcOnSpecialsOnly = False #set to true for warp-spring-like behaviour, only proccing on specials
customTrackingProcBuffDuration = 100
customTrackingProcICDDuration = 200
customTrackingProcHasteRating = 0 #the sim uses both this rating and the multi below, so make sure to set to 0 and 1.0 for no benefit from either
customTrackingProcHasteMulti = 1.0

#char givens
weaponSpeedOHBase = 14
weaponSpeedMHBase = 27
dodgeChance = 25 # exactly 1 decimal, so 32 for 3.2% dodge, 100 for 10% dodge. both autos and specials
missChance = 0 # exactly 1 decimal, so 32 for 3.2% miss, 100 for 10% miss. only for auto attacks
parryChance = 100 # only during the first few seconds, if the setting for parryOnOpener is on
energyTickLength = 20
maxEnergy = 100
gcdLength = 10

#ability givens
sliceMulti = 1.35
bfMulti = 1.2
lustMulti = 1.3
hastePotionBonus = 400
drumsBonus = 80
dstBonus = 325
dstPPM = 1
glaiveBonus = 450
glaivePPM = 1
mongooseMulti = 1.02
mongoosePPM = 1
customHasteRatingBonus = 0
customHasteRatingPPM = 1
customHasteMultiBonus = 1.0
customHasteMultiPPM = 1
hasteRatingCoefficient = 1577
sliceTable = {1: 130.5, 2: 174.0, 3: 217.5, 4: 261.0, 5: 304.5}
energyFromPotencyProc = 15
energyFromPotencyAvg = 3
energyFromRelentlessProc = 25
cpFromRuthlessnessProc = 1
energyFromThistleTea = 40
shivEnergyCost = weaponSpeedOHBase + 20
sinisterCost = 40
bladeFlurryDuration = 150
lustDuration = 400
drumsDuration = 300
mongooseDuration = 150
hastePotionDuration = 150
dstDuration = 100
dstICDDuration = 200
glaivesDuration = 100
glaivesICDDuration = 450
customRatingDuration = 100
customRatingICDDuration = 0
customMultiDuration = 100
customMultiICDDuration = 0

#internal givens
timeTick = 1
ticksPerSecond = 10
simVersion = 5.0
inactiveTime = -1

#internal sim variables
iterationCount = 0
mainHandIdentifier = "mh"
offHandIdentifier = "oh"
ppmBaseProcChanceMH = 0
ppmBaseProcChanceOH = 0
procsToCheck = []
loadingBarStepsTaken = 1 #bad name i guess, but it should start at 1 so first bar tick is at stepsPerTick * 1 - because i check iterations vs steps taken after i increment the iteration
havePrintedLoadingTitle = False


#below here get changed and saved, proceed with caution

#char stats to start the sim with
hasteRating = 0
energy = 100
comboPoints = 0
sliceDuration = 0
energyPerTick = 20

#interal variables
nextEnergyTickAt = 10 # avg 1s after pull
currentTickTime = 0
currentOHSwingTimer = 0
currentMHSwingTimer = 0
currentOHSwingSpeed = weaponSpeedOHBase
currentMHSwingSpeed = weaponSpeedMHBase
nextGCDEnds = inactiveTime
wasSliceCast = False
wasExposeCast = False
finishedOpener = False
wasARCast = False
wasBFCast = False
wasLustCast = False
wasDrumsCast = False
wasHastePotCast = False
wasThistleTeaCast = False
shivsCast = 0
sliceActive = False
sliceFallsAt = inactiveTime
bfActive = False
bladeFlurryFallsAt = inactiveTime
lustActive = False
lustFallsAt = inactiveTime
drumsActive = False
drumsFallsAt = inactiveTime
mongooseMHActive = False
mongooseMHFallsAt = inactiveTime
mongooseOHActive = False
mongooseOHFallsAt = inactiveTime
hastePotionActive = False
hastePotionFallsAt = inactiveTime
dstActive = False
dstFallsAt = inactiveTime
dstICDFallsAt = inactiveTime
glaivesActive = False
glaivesFallsAt = inactiveTime
glaivesICDFallsAt = inactiveTime
customRatingActive = False
customRatingFallsAt = inactiveTime
customRatingICDFallsAt = inactiveTime
customMultiActive = False
customMultiFallsAt = inactiveTime
customMultiICDFallsAt = inactiveTime
customTrackingProcActive = False
customTrackingProcFallsAt = inactiveTime
customTrackingProcICDFallsAt = inactiveTime

#tracking
totalPotencyProcs = 0
totalRuthlessnessProcs = 0
totalRelentlessProcs = 0
totalCappedEnergy = 0
totalDodgedSinisters = 0
timeWithoutSlice = 0
trackingProcActivatedAt = inactiveTime
exposeAppliedAt = 0




import random

#~~~~~~~~~~~~
#game logic
#~~~~~~~~~~~~

def autoAttack():
    global currentOHSwingTimer
    global currentMHSwingTimer
    
    currentOHSwingTimer -= timeTick
    currentMHSwingTimer -= timeTick

    if currentOHSwingTimer <= 0:
        currentOHSwingTimer = currentOHSwingSpeed

        if not rollToHitAuto():
            if debugMode: print("failed oh auto :( at", currentTickTime/ticksPerSecond)

        else:
            if debugMode: print("attack oh! at ", currentTickTime/ticksPerSecond)
            rollPotencyProc()
            checkForProcs(offHandIdentifier)

    if currentMHSwingTimer <= 0:
        currentMHSwingTimer = currentMHSwingSpeed

        if not rollToHitAuto():
            if debugMode: print("failed mh auto :( at", currentTickTime/ticksPerSecond)

        else:
            if debugMode: print("attack mh! at ", currentTickTime/ticksPerSecond)
            checkForProcs(mainHandIdentifier)

def castAbilities():

    #if i can tea, tea
    if thistleTeaBehaviour == 1:
        if not onGCD():
            if energy < sinisterCost and thistleTeaBehaviour == 1 and wasThistleTeaCast == False: # < sinister cost cause it's my most expensive ability... could be smarter
                castThistleTea()

    #if i can expose, expose
    if not onGCD():
        if wasExposeCast == False and comboPoints >= 5 and energy >= 25:
            castExpose()

    #if haste pot forced to activate asap, activate asap
    if hastePotionBehaviour == 1 and wasHastePotCast == False:
        castHastePotion()

    #if no slice, slice
    if not onGCD():
        if sliceActive == False: #no need to refresh
            #print("expose:", wasExposeCast, "slice:", wasSliceCast, "behaviour:", openingSliceBehaviour)
            if (openingSliceBehaviour < 5 and wasExposeCast == True) or (openingSliceBehaviour < 5 and wasExposeCast == False and wasSliceCast == False) or (openingSliceBehaviour > 5 and wasExposeCast == True): #either supposed to cast slice once before expose, or only after expose
                if comboPoints >= openingSliceBehaviour or wasExposeCast == True: #am i allowed by rotation to cast slice at my current cp
                    if energy >= 25 and comboPoints >= 1: #am i allowed by game to cast slice
                        if sliceSafetyBehaviour > 0:
                            energyIn1Second = energy
                            if nextEnergyTickAt - currentTickTime < gcdLength:
                                energyIn1Second += energyPerTick
                            if energyIn1Second <= sliceMaxEnergyToCast:
                                castSlice()
                        else:
                            castSlice()

    #if no ar but slice is rolling, ar
    if not onGCD():
        if (adrenalineRushBehaviour == 1 and wasARCast == False and wasSliceCast == True) or (adrenalineRushBehaviour == 2 and wasARCast == False):

            energyAfterCastingAdrenalineRush = energy + calculateRefundThisTick()

            if energyAfterCastingAdrenalineRush <= adrenalineRushMaxEnergyToCast:
                castAdrenalineRush()

    #if slice is rolling, bf
    if not onGCD():
        if (bladeFlurryBehaviour == 1 and wasBFCast == False and sliceActive) and energy <= bladeFlurryMaxEnergyToCast:
            if energy >= 25:
                castBladeFlurry()

    #otherwise, cast a builder

    #if i was told to cast shiv
    if shivBehaviour > 0:
        if not onGCD():
            if energy >= shivEnergyCost and shivsCast < shivBehaviour:
                castShiv()

    #otherwise sinister
    if not onGCD():
        if energy >= sinisterCost:
            castSinister()

def castSlice():
    global sliceDuration
    global comboPoints
    global wasSliceCast
    global sliceFallsAt
    global sliceActive

    comboPointsCastAt = comboPoints    

    sliceDuration = sliceTable[comboPoints]
    sliceFallsAt = currentTickTime + sliceDuration
    updateFallingBuffs("slice", sliceFallsAt)


    if wasSliceCast == False:
        wasSliceCast = True
    
    
    updateEnergy(-25)
    sliceActive = True
    comboPoints = 0


    if debugMode: print("cast slice for ", sliceDuration/ticksPerSecond, " until ", sliceFallsAt/ticksPerSecond )
    updateHaste()

    startGCD()

    rollProcsOnFinisher(comboPointsCastAt)


def rollProcsOnFinisher(comboPointsCastAt):
    global totalRuthlessnessProcs
    global totalRelentlessProcs
    global comboPoints

    if ruthlessnessBehaviour != 0:
        if ruthlessnessBehaviour == 1:
            comboPoints += cpFromRuthlessnessProc
            totalRuthlessnessProcs += 1
            if debugMode: print("ruthlessness proc! cp is now", comboPoints)

        if ruthlessnessBehaviour == 2:
            if random.randint(1,10) <= 6: # 60% chance
                    comboPoints += cpFromRuthlessnessProc
                    totalRuthlessnessProcs += 1
                    if debugMode: print("ruthlessness proc! cp is now", comboPoints)

    if relentlessBehaviour != 0:
        if relentlessBehaviour == 1:
            updateEnergy(energyFromRelentlessProc)
            totalRelentlessProcs += 1
            if debugMode: print("relentless proc! energy is now", energy)

        if relentlessBehaviour == 2:
            if random.randint(1,5) <= comboPointsCastAt:
                    updateEnergy(energyFromRelentlessProc)
                    totalRelentlessProcs += 1
                    if debugMode: print("relentless proc! energy is now", energy)

def rollToHitSpecial():
    return _rollToHit(0)

def rollToHitAuto():
    return _rollToHit(1)

def _rollToHit(isAuto):

    parryChanceThisAttack = 0
    if parryOnOpener:
        if parryOnOpenerTime >= currentTickTime:
            parryChanceThisAttack = parryChance

    totalFailureChance = dodgeChance + (isAuto*missChance) + parryChanceThisAttack

    if random.randint(1,1000) <= totalFailureChance:
        return False
    else:
        return True

def rollPotencyProc():
    global totalPotencyProcs

    if combatPotencyBehaviour != 0:
        if combatPotencyBehaviour == 1:
            updateEnergy(energyFromPotencyAvg)
            totalPotencyProcs += 1
            if debugMode: print("potency proc for" , energyFromPotencyAvg, "energy! energy is now", energy)

        if combatPotencyBehaviour == 2:
            if random.randint(1,5) == 1: # 20% chance
                updateEnergy(energyFromPotencyProc)
                totalPotencyProcs += 1
                if debugMode: print("potency proc for" , energyFromPotencyProc, "energy! energy is now", energy)

def energyTick():

    if currentTickTime >= nextEnergyTickAt:
        updateEnergy(energyPerTick)

        resetEnergyTick()

        if debugMode: print("energy tick at ", currentTickTime/ticksPerSecond, "  energy now at ", energy)

def resetEnergyTick():
    global nextEnergyTickAt

    nextEnergyTickAt = currentTickTime + energyTickLength

def startGCD():
    global nextGCDEnds

    nextGCDEnds = currentTickTime + gcdLength

def onGCD():
    amIOnGCD = nextGCDEnds > currentTickTime
    return amIOnGCD

def updateHaste():
    global currentOHSwingSpeed
    global currentOHSwingTimer
    global currentMHSwingSpeed
    global currentMHSwingTimer

    oldOHSwingSpeed = currentOHSwingSpeed
    oldOHSwingTimer = currentOHSwingTimer
    oldMHSwingSpeed = currentMHSwingSpeed
    oldMHSwingTimer = currentMHSwingTimer
    
    hasteMulti = 1

    if sliceActive:
        hasteMulti *= sliceMulti
    if bfActive:
        hasteMulti *= bfMulti
    if lustActive:
        hasteMulti *= lustMulti
    if mongooseMHActive:
        hasteMulti *= mongooseMulti
    if mongooseOHActive:
        hasteMulti *= mongooseMulti
    if customMultiActive:
        hasteMulti *= customHasteMultiBonus
    if customTrackingProcActive and customTrackingProcHasteMulti > 1.0:
        hasteMulti *= customTrackingProcHasteMulti

    hasteRating = 0

    if drumsActive:
        hasteRating += drumsBonus
    if hastePotionActive:
        hasteRating += hastePotionBonus
    if dstActive:
        hasteRating += dstBonus
    if glaivesActive:
        hasteRating += glaiveBonus
    if customRatingActive:
        hasteRating += customHasteRatingBonus
    if customTrackingProcActive and customTrackingProcHasteRating > 0:
        hasteRating += customTrackingProcHasteRating

    hasteMulti *= 1 + (hasteRating / hasteRatingCoefficient)

    if debugMode: print("~~updating haste~~")

    newOHSwingSpeed = weaponSpeedOHBase / hasteMulti
    currentOHSwingSpeed = newOHSwingSpeed
    newMHSwingSpeed = weaponSpeedMHBase / hasteMulti
    currentMHSwingSpeed = newMHSwingSpeed
    if debugMode: print("oh swing speed was", ticksToSecond(oldOHSwingSpeed), ": now is", ticksToSecond(newOHSwingSpeed), " | ", "mh swing speed was", ticksToSecond(oldMHSwingSpeed), ": now is", ticksToSecond(newMHSwingSpeed))

    swingOHSpeedDiff = oldOHSwingSpeed / newOHSwingSpeed
    swingMHSpeedDiff = oldMHSwingSpeed / newMHSwingSpeed
    newOHSwingTimer = currentOHSwingTimer / swingOHSpeedDiff
    newMHSwingTimer = currentMHSwingTimer / swingMHSpeedDiff

    currentOHSwingTimer = newOHSwingTimer
    currentMHSwingTimer = newMHSwingTimer
    if debugMode: print("oh swing timer was", ticksToSecond(oldOHSwingTimer), "; now is", ticksToSecond(newOHSwingTimer), " | ", "mh swing timer was", ticksToSecond(oldMHSwingTimer), "; now is", ticksToSecond(newMHSwingTimer))

def updateEnergy(delta):
    global energy
    global totalCappedEnergy

    energy += delta

    if energy > maxEnergy:
        cappedEnergy = energy-maxEnergy
        if debugMode: print("oh no! capped energy by", cappedEnergy)
        totalCappedEnergy += cappedEnergy
        energy = maxEnergy

    if energy < 0:
        print("bug! i have", energy, "energy now, somehow")

def calculateRefundThisTick():
    timeUntilNextTick = nextEnergyTickAt - currentTickTime
    tickPortionElapsed = energyTickLength - timeUntilNextTick
    tickRefund = int((tickPortionElapsed/energyTickLength) * energyPerTick)

    return tickRefund

def initializePpmSettings():
    global ppmBaseProcChanceMH
    global ppmBaseProcChanceOH

    # 1ppm * (weaponspeed/10) / 60 = proc chance decimal, *100%, *10 for 1 more decimal for randomint rolls ; weaponspeed/10 for ticks->seconds
    ppmBaseProcChanceMH = (((1*weaponSpeedMHBase/10) / 60)*100)*10
    ppmBaseProcChanceOH = (((1*weaponSpeedOHBase/10) / 60)*100)*10

def checkForProcs(hand, isSpecial=False):
    if dstEquipped:
        if rollPpmProcChance(dstPPM, hand):
            castDst()
    if glaivesEquipped:
        if rollPpmProcChance(glaivePPM, hand):
            castGlaivesProc()
    if mongooseMHEquipped and hand == mainHandIdentifier:
        if rollPpmProcChance(mongoosePPM, hand):
            castMongoose(hand)
    if mongooseOHEquipped and hand == offHandIdentifier:
        if rollPpmProcChance(mongoosePPM, hand):
            castMongoose(hand)
    if customRatingEquipped:
        if rollPpmProcChance(customHasteRatingPPM, hand):
            castCustomHasteRating()
    if customMultiEqupped:
        if rollPpmProcChance(customHasteMultiPPM, hand):
            castCustomHasteMulti()
    if customTrackingProcEquipped:
        if (customTrackingProcOnSpecialsOnly and isSpecial) or (customTrackingProcOnSpecialsOnly == False):
            if customTrackingProcBehaviour == 0:
                if rollPpmProcChance(customTrackingProcPPM, hand):
                    castCustomTrackingProc()
            elif customTrackingProcBehaviour == 1:
                if rollFlatChance(customTrackingProcChance*10): #*10 for 1 more decimal for randomint rolls
                    castCustomTrackingProc()
 
def rollPpmProcChance(ppm, hand):

    procChance = 0

    if hand == mainHandIdentifier:
        procChance = ppm * ppmBaseProcChanceMH
    if hand == offHandIdentifier:
        procChance = ppm * ppmBaseProcChanceOH

    return rollFlatChance(procChance)

def rollFlatChance(chance):

    if random.randint(1, 1000) <= chance: #1000 for 100% * 10 for an extra decimal place
        return True
    else:
        return False
    
def castAdrenalineRush():
    global wasARCast
    global energyPerTick


    wasARCast = True
    startGCD()

    if debugMode: print("casting adrenaline rush")

    refund = calculateRefundThisTick()
    updateEnergy(refund)
    if debugMode: print("refunding", refund, "energy")

    resetEnergyTick()

    energyPerTick = 40

def castSinister():
    global comboPoints
    global totalDodgedSinisters

    startGCD()

    if not rollToHitSpecial():
        updateEnergy(-8)
        if debugMode: print("sinister failed :(")
        totalDodgedSinisters += 1
    else:
        updateEnergy(-sinisterCost)
        comboPoints += 1

        if debugMode: print("cast sinister at ", currentTickTime/ticksPerSecond, "  now at " , comboPoints, " cp")
        checkForProcs(mainHandIdentifier, isSpecial = True)

def castShiv():
    global comboPoints
    global shivsCast

    startGCD()

    updateEnergy(-shivEnergyCost)
    comboPoints += 1
    shivsCast += 1

    if debugMode: print("cast shiv at ", currentTickTime/ticksPerSecond, "  now at " , comboPoints, " cp")

    rollPotencyProc()

    checkForProcs(offHandIdentifier, isSpecial = True)

def castExpose():
    global wasExposeCast
    global comboPoints
    global exposeAppliedAt

    comboPointsCastAt = comboPoints
    
    updateEnergy(-25)
    comboPoints = 0

    wasExposeCast = True
    exposeAppliedAt = currentTickTime
    if debugMode: print ("!! cast expose at ", currentTickTime/ticksPerSecond, "!!")

    startGCD()

    rollProcsOnFinisher(comboPointsCastAt)

def castBladeFlurry():
    global wasBFCast
    global bfActive
    global bladeFlurryFallsAt

    wasBFCast = True
    startGCD()

    if debugMode: print("casting blade flurry")

    updateEnergy(-25)
    bfActive = True
    bladeFlurryFallsAt = currentTickTime + bladeFlurryDuration
    updateFallingBuffs("blade flurry", bladeFlurryFallsAt)

    if hastePotionBehaviour == 0:
        castHastePotion()
    else:
        updateHaste()

def castHastePotion():
    global wasHastePotCast
    global hastePotionActive
    global hastePotionFallsAt

    wasHastePotCast = True

    hastePotionActive = True
    hastePotionFallsAt = currentTickTime + hastePotionDuration
    updateFallingBuffs("haste potion", hastePotionFallsAt)

    if debugMode: print("casting haste potion")

    updateHaste()

def castThistleTea():
    global wasThistleTeaCast
    
    wasThistleTeaCast = True

    updateEnergy(energyFromThistleTea)

    if debugMode: print("casting thistle tea")

def castDst():
    global dstActive
    global dstFallsAt
    global dstICDFallsAt

    if dstICDFallsAt <= currentTickTime:
        dstActive = True
        dstFallsAt = currentTickTime + dstDuration
        dstICDFallsAt = currentTickTime + dstICDDuration
        updateFallingBuffs("dst", dstFallsAt)

        if debugMode: print("dst activated!")
        updateHaste()

def castGlaivesProc():
    global glaivesActive
    global glaivesFallsAt
    global glaivesICDFallsAt

    if glaivesICDFallsAt <= currentTickTime:
        glaivesActive = True
        glaivesFallsAt = currentTickTime + glaivesDuration
        glaivesICDFallsAt = currentTickTime + glaivesICDDuration
        updateFallingBuffs("glaives", glaivesFallsAt)

        if debugMode: print("glaives activated!")

        updateHaste()

def castMongoose(hand):
    global mongooseMHActive
    global mongooseOHActive
    global mongooseMHFallsAt
    global mongooseOHFallsAt

    shouldRecalculateHaste = False

    if hand == mainHandIdentifier:
        if not mongooseMHActive:
            shouldRecalculateHaste = True

        mongooseMHActive = True
        mongooseMHFallsAt = currentTickTime + mongooseDuration
        updateFallingBuffs("mongoose MH", mongooseMHFallsAt)

        if debugMode: print("mongoose MH activated!")

        if shouldRecalculateHaste:
            updateHaste()

    if hand == offHandIdentifier:
        if not mongooseOHActive:
            shouldRecalculateHaste = True

        mongooseOHActive = True
        mongooseOHFallsAt = currentTickTime + mongooseDuration
        updateFallingBuffs("mongoose OH", mongooseOHFallsAt)

        if debugMode: print("mongoose OH activated!")

        if shouldRecalculateHaste:
            updateHaste()

def castCustomHasteRating():
    global customRatingActive
    global customRatingFallsAt
    global customRatingICDFallsAt

    if customRatingICDFallsAt <= currentTickTime:
        customRatingActive = True
        customRatingFallsAt = currentTickTime + customRatingDuration
        customRatingICDFallsAt = currentTickTime + customRatingICDDuration
        updateFallingBuffs("custom rating", customRatingFallsAt)

        if debugMode: print("custom rating activated!")

        updateHaste()

def castCustomHasteMulti():
    global customMultiActive
    global customMultiFallsAt
    global customMultiICDFallsAt

    if customMultiICDFallsAt <= currentTickTime:
        customMultiActive = True
        customMultiFallsAt = currentTickTime + customMultiDuration
        customMultiICDFallsAt = currentTickTime + customMultiICDDuration
        updateFallingBuffs("custom multi", customMultiFallsAt)

        if debugMode: print("custom multi activated!")

        updateHaste()

def castCustomTrackingProc():
    global customTrackingProcActive
    global customTrackingProcFallsAt
    global customTrackingProcICDFallsAt
    global trackingProcActivatedAt

    if customTrackingProcICDFallsAt <= currentTickTime:
        customTrackingProcActive = True
        customTrackingProcFallsAt = currentTickTime + customTrackingProcBuffDuration
        customTrackingProcICDFallsAt = currentTickTime + customTrackingProcICDDuration
        updateFallingBuffs("custom tracker", customTrackingProcFallsAt)

        if debugMode: print("custom tracker:", customTrackingProcName, "activated!")
        trackingProcActivatedAt = currentTickTime

        if customTrackingProcHasteRating > 0 or customTrackingProcHasteMulti > 1.0:
            updateHaste()

def checkExternals():
    global wasLustCast
    global wasDrumsCast
    global lustActive
    global drumsActive
    global lustFallsAt
    global drumsFallsAt

    shouldUpdateHaste = False

    if currentTickTime >= lustActivatesAt and wasLustCast == False:
        wasLustCast = True
        lustActive = True
        lustFallsAt = currentTickTime + lustDuration

        shouldUpdateHaste = True
        if debugMode: print("casting lust")

    if currentTickTime >= drumsActivatesAt and wasDrumsCast == False:
        wasDrumsCast = True
        drumsActive = True
        drumsFallsAt = currentTickTime + drumsDuration

        shouldUpdateHaste = True
        if debugMode: print("casting drums")

    if shouldUpdateHaste:
        updateHaste()

def trackBuffUptime():
    global timeWithoutSlice

    if not sliceActive:
        timeWithoutSlice += 1

hasteBuffs = {
    "slice":sliceFallsAt,
    "blade flurry":bladeFlurryFallsAt,
    "lust":lustFallsAt,
    "drums":drumsFallsAt,
    "mongoose MH":mongooseMHFallsAt,
    "mongoose OH":mongooseOHFallsAt,
    "haste potion":hastePotionFallsAt,
    "dst":dstFallsAt,
    "glaives":glaivesFallsAt,
    "custom rating":customRatingFallsAt,
    "custom multi":customMultiFallsAt,
    "custom tracker":customTrackingProcFallsAt,
}

def updateFallingBuffs(buff, fallTime):
    hasteBuffs[buff] = fallTime

def checkFallingBuffs():
    for buff in hasteBuffs:
        if hasteBuffs[buff] != inactiveTime and hasteBuffs[buff] <= currentTickTime:
            deactivateBuff(buff)

def deactivateBuff(buff):
    global sliceActive
    global sliceFallsAt
    global bfActive
    global bladeFlurryFallsAt
    global lustActive
    global lustFallsAt
    global drumsActive
    global drumsFallsAt
    global mongooseMHActive
    global mongooseMHFallsAt
    global mongooseOHActive
    global mongooseOHFallsAt
    global hastePotionActive
    global hastePotionFallsAt
    global dstActive
    global dstFallsAt
    global glaivesActive
    global glaivesFallsAt
    global customRatingActive
    global customRatingFallsAt
    global customMultiActive
    global customMultiFallsAt
    global customTrackingProcActive
    global customTrackingProcFallsAt

    if debugMode: print("deactivating", buff)

    if buff == "slice":
        sliceActive = False
        sliceFallsAt = inactiveTime
        updateFallingBuffs(buff, sliceFallsAt)
    elif buff == "blade flurry":
        bfActive = False
        bladeFlurryFallsAt = inactiveTime
        updateFallingBuffs(buff, bladeFlurryFallsAt)
    elif buff == "lust":
        lustActive = False
        lustFallsAt = inactiveTime
        updateFallingBuffs(buff, lustFallsAt)
    elif buff == "drums":
        drumsActive = False
        drumsFallsAt = inactiveTime
        updateFallingBuffs(buff, drumsFallsAt)
    elif buff == "mongoose MH":
        mongooseMHActive = False
        mongooseMHFallsAt = inactiveTime
        updateFallingBuffs(buff, mongooseMHFallsAt)
    elif buff == "mongoose OH":
        mongooseOHActive = False
        mongooseOHFallsAt = inactiveTime
        updateFallingBuffs(buff, mongooseOHFallsAt)
    elif buff == "haste potion":
        hastePotionActive = False
        hastePotionFallsAt = inactiveTime
        updateFallingBuffs(buff, hastePotionFallsAt)
    elif buff == "dst":
        dstActive = False
        dstFallsAt = inactiveTime
        updateFallingBuffs(buff, dstFallsAt)
    elif buff == "glaives":
        glaivesActive = False
        glaivesFallsAt = inactiveTime
        updateFallingBuffs(buff, glaivesFallsAt)
    elif buff == "custom rating":
        customRatingActive = False
        customRatingFallsAt = inactiveTime
        updateFallingBuffs(buff, customRatingFallsAt)
    elif buff == "custom multi":
        customMultiActive = False
        customMultiFallsAt = inactiveTime
        updateFallingBuffs(buff, customMultiFallsAt)
    elif buff == "custom tracker":
        customTrackingProcActive = False
        customTrackingProcFallsAt = inactiveTime
        updateFallingBuffs(buff, customTrackingProcFallsAt)
    else:
        if debugMode: print("send help: called to disactivate buffs but no buffs deactivated")
    
    updateHaste()

def checkIfFinishedOpener():
    global finishedOpener

    if wasExposeCast and sliceActive:
        finishedOpener = True

#~~~~~~~~~~
#sim logic
#~~~~~~~~~~

#these are settings i want to save/reset between sims
#1. define a save state for variable
#2. declare variable as global
#3. revert variable to save state

#header
s_hasteRating = hasteRating
s_energy = energy
s_comboPoints = comboPoints
s_sliceDuration = sliceDuration
s_energyPerTick = energyPerTick
#header
#header
s_nextEnergyTickAt = nextEnergyTickAt
s_currentTickTime = currentTickTime
s_currentOHSwingTimer = currentOHSwingTimer
s_currentMHSwingTimer = currentMHSwingTimer
s_currentOHSwingSpeed = currentOHSwingSpeed
s_currentMHSwingSpeed = currentMHSwingSpeed
s_nextGCDEnds = nextGCDEnds
s_wasSliceCast = wasSliceCast
s_wasExposeCast = wasExposeCast
s_finishedOpener = finishedOpener
s_wasARCast = wasARCast
s_wasBFCast = wasBFCast
s_wasLustCast = wasLustCast
s_wasDrumsCast = wasDrumsCast
s_wasHastePotCast = wasHastePotCast
s_wasThistleTeaCast = wasThistleTeaCast
s_shivsCast = shivsCast
s_sliceActive = sliceActive
s_sliceFallsAt = sliceFallsAt
s_bfActive = bfActive
s_bladeFlurryFallsAt = bladeFlurryFallsAt
s_lustActive = lustActive
s_lustFallsAt = lustFallsAt
s_drumsActive = drumsActive
s_drumsFallsAt = drumsFallsAt
s_mongooseMHActive = mongooseMHActive
s_mongooseMHFallsAt = mongooseMHFallsAt
s_mongooseOHActive = mongooseOHActive
s_mongooseOHFallsAt = mongooseOHFallsAt
s_hastePotionActive = hastePotionActive
s_hastePotionFallsAt = hastePotionFallsAt
s_dstActive = dstActive
s_dstFallsAt = dstFallsAt
s_dstICDFallsAt = dstICDFallsAt
s_glaivesActive = glaivesActive
s_glaivesFallsAt = glaivesFallsAt
s_glaivesICDFallsAt = glaivesICDFallsAt
s_customRatingActive = customRatingActive
s_customRatingFallsAt = customRatingFallsAt
s_customRatingICDFallsAt = customRatingICDFallsAt
s_customMultiActive = customMultiActive
s_customMultiFallsAt = customMultiFallsAt
s_customMultiICDFallsAt = customMultiICDFallsAt
s_customTrackingProcActive = customTrackingProcActive
s_customTrackingProcFallsAt = customTrackingProcFallsAt
s_customTrackingProcICDFallsAt = customTrackingProcICDFallsAt
#header
#header
s_totalPotencyProcs = totalPotencyProcs
s_totalRuthlessnessProcs = totalRuthlessnessProcs
s_totalRelentlessProcs = totalRelentlessProcs
s_totalCappedEnergy = totalCappedEnergy
s_totalDodgedSinisters = totalDodgedSinisters
s_timeWithoutSlice = timeWithoutSlice
s_trackingProcActivatedAt = trackingProcActivatedAt
s_wasThistleTeaCast = wasThistleTeaCast
s_shivsCast = shivsCast
s_sliceActive = sliceActive
s_sliceFallsAt = sliceFallsAt
s_bfActive = bfActive
s_bladeFlurryFallsAt = bladeFlurryFallsAt
s_lustActive = lustActive
s_lustFallsAt = lustFallsAt
s_drumsActive = drumsActive
s_drumsFallsAt = drumsFallsAt
s_mongooseMHActive = mongooseMHActive
s_mongooseMHFallsAt = mongooseMHFallsAt
s_mongooseOHActive = mongooseOHActive
s_mongooseOHFallsAt = mongooseOHFallsAt
s_hastePotionActive = hastePotionActive
s_hastePotionFallsAt = hastePotionFallsAt
s_dstActive = dstActive
s_dstFallsAt = dstFallsAt
s_dstICDFallsAt = dstICDFallsAt
s_glaivesActive = glaivesActive
s_glaivesFallsAt = glaivesFallsAt
s_glaivesICDFallsAt = glaivesICDFallsAt
s_customRatingActive = customRatingActive
s_customRatingFallsAt = customRatingFallsAt
s_customRatingICDFallsAt = customRatingICDFallsAt
s_customMultiActive = customMultiActive
s_customMultiFallsAt = customMultiFallsAt
s_customMultiICDFallsAt = customMultiICDFallsAt
#header
#header
s_totalPotencyProcs = totalPotencyProcs
s_totalRuthlessnessProcs = totalRuthlessnessProcs
s_totalRelentlessProcs = totalRelentlessProcs
s_totalCappedEnergy = totalCappedEnergy
s_totalDodgedSinisters = totalDodgedSinisters
s_timeWithoutSlice = timeWithoutSlice
s_trackingProcActivatedAt = trackingProcActivatedAt
s_exposeAppliedAt = exposeAppliedAt

def resetSim():
    #header
    global hasteRating
    global energy
    global comboPoints
    global sliceDuration
    global energyPerTick
    #header
    #header
    global nextEnergyTickAt
    global currentTickTime
    global currentOHSwingTimer
    global currentMHSwingTimer
    global currentOHSwingSpeed
    global currentMHSwingSpeed
    global nextGCDEnds
    global wasSliceCast
    global wasExposeCast
    global finishedOpener
    global wasARCast
    global wasBFCast
    global wasLustCast
    global wasDrumsCast
    global wasHastePotCast
    global wasThistleTeaCast
    global shivsCast
    global sliceActive
    global sliceFallsAt
    global bfActive
    global bladeFlurryFallsAt
    global lustActive
    global lustFallsAt
    global drumsActive
    global drumsFallsAt
    global mongooseMHActive
    global mongooseMHFallsAt
    global mongooseOHActive
    global mongooseOHFallsAt
    global hastePotionActive
    global hastePotionFallsAt
    global dstActive
    global dstFallsAt
    global dstICDFallsAt
    global glaivesActive
    global glaivesFallsAt
    global glaivesICDFallsAt
    global customRatingActive
    global customRatingFallsAt
    global customRatingICDFallsAt
    global customMultiActive
    global customMultiFallsAt
    global customMultiICDFallsAt
    global customTrackingProcActive
    global customTrackingProcFallsAt
    global customTrackingProcICDFallsAt
    #header
    #header
    global totalPotencyProcs
    global totalRuthlessnessProcs
    global totalRelentlessProcs
    global totalCappedEnergy
    global totalDodgedSinisters
    global timeWithoutSlice
    global trackingProcActivatedAt
    global wasThistleTeaCast
    global shivsCast
    global sliceActive
    global sliceFallsAt
    global bfActive
    global bladeFlurryFallsAt
    global lustActive
    global lustFallsAt
    global drumsActive
    global drumsFallsAt
    global mongooseMHActive
    global mongooseMHFallsAt
    global mongooseOHActive
    global mongooseOHFallsAt
    global hastePotionActive
    global hastePotionFallsAt
    global dstActive
    global dstFallsAt
    global dstICDFallsAt
    global glaivesActive
    global glaivesFallsAt
    global glaivesICDFallsAt
    global customRatingActive
    global customRatingFallsAt
    global customRatingICDFallsAt
    global customMultiActive
    global customMultiFallsAt
    global customMultiICDFallsAt
    #header
    #header
    global totalPotencyProcs
    global totalRuthlessnessProcs
    global totalRelentlessProcs
    global totalCappedEnergy
    global totalDodgedSinisters
    global timeWithoutSlice
    global trackingProcActivatedAt
    global exposeAppliedAt

    #~~~~~~~~~~~~~~~~~~~~~~~
    #reset to saved state
    if firstEnergyTickBehaviour == 1:
        nextEnergyTickAt = random.randint(1,20)
    #~~~~~~~~~~~~~~~~~~~~~~~

    #header
    hasteRating = s_hasteRating
    energy = s_energy
    comboPoints = s_comboPoints
    sliceDuration = s_sliceDuration
    energyPerTick = s_energyPerTick
    #header
    #header
    nextEnergyTickAt = s_nextEnergyTickAt
    currentTickTime = s_currentTickTime
    currentOHSwingTimer = s_currentOHSwingTimer
    currentMHSwingTimer = s_currentMHSwingTimer
    currentOHSwingSpeed = s_currentOHSwingSpeed
    currentMHSwingSpeed = s_currentMHSwingSpeed
    nextGCDEnds = s_nextGCDEnds
    wasSliceCast = s_wasSliceCast
    wasExposeCast = s_wasExposeCast
    finishedOpener = s_finishedOpener
    wasARCast = s_wasARCast
    wasBFCast = s_wasBFCast
    wasLustCast = s_wasLustCast
    wasDrumsCast = s_wasDrumsCast
    wasHastePotCast = s_wasHastePotCast
    wasThistleTeaCast = s_wasThistleTeaCast
    shivsCast = s_shivsCast
    sliceActive = s_sliceActive
    sliceFallsAt = s_sliceFallsAt
    bfActive = s_bfActive
    bladeFlurryFallsAt = s_bladeFlurryFallsAt
    lustActive = s_lustActive
    lustFallsAt = s_lustFallsAt
    drumsActive = s_drumsActive
    drumsFallsAt = s_drumsFallsAt
    mongooseMHActive = s_mongooseMHActive
    mongooseMHFallsAt = s_mongooseMHFallsAt
    mongooseOHActive = s_mongooseOHActive
    mongooseOHFallsAt = s_mongooseOHFallsAt
    hastePotionActive = s_hastePotionActive
    hastePotionFallsAt = s_hastePotionFallsAt
    dstActive = s_dstActive
    dstFallsAt = s_dstFallsAt
    dstICDFallsAt = s_dstICDFallsAt
    glaivesActive = s_glaivesActive
    glaivesFallsAt = s_glaivesFallsAt
    glaivesICDFallsAt = s_glaivesICDFallsAt
    customRatingActive = s_customRatingActive
    customRatingFallsAt = s_customRatingFallsAt
    customRatingICDFallsAt = s_customRatingICDFallsAt
    customMultiActive = s_customMultiActive
    customMultiFallsAt = s_customMultiFallsAt
    customMultiICDFallsAt = s_customMultiICDFallsAt
    customTrackingProcActive = s_customTrackingProcActive
    customTrackingProcFallsAt = s_customTrackingProcFallsAt
    customTrackingProcICDFallsAt = s_customTrackingProcICDFallsAt
    #header
    #header
    totalPotencyProcs = s_totalPotencyProcs
    totalRuthlessnessProcs = s_totalRuthlessnessProcs
    totalRelentlessProcs = s_totalRelentlessProcs
    totalCappedEnergy = s_totalCappedEnergy
    totalDodgedSinisters = s_totalDodgedSinisters
    timeWithoutSlice = s_timeWithoutSlice
    trackingProcActivatedAt = s_trackingProcActivatedAt
    wasThistleTeaCast = s_wasThistleTeaCast
    shivsCast = s_shivsCast
    sliceActive = s_sliceActive
    sliceFallsAt = s_sliceFallsAt
    bfActive = s_bfActive
    bladeFlurryFallsAt = s_bladeFlurryFallsAt
    lustActive = s_lustActive
    lustFallsAt = s_lustFallsAt
    drumsActive = s_drumsActive
    drumsFallsAt = s_drumsFallsAt
    mongooseMHActive = s_mongooseMHActive
    mongooseMHFallsAt = s_mongooseMHFallsAt
    mongooseOHActive = s_mongooseOHActive
    mongooseOHFallsAt = s_mongooseOHFallsAt
    hastePotionActive = s_hastePotionActive
    hastePotionFallsAt = s_hastePotionFallsAt
    dstActive = s_dstActive
    dstFallsAt = s_dstFallsAt
    dstICDFallsAt = s_dstICDFallsAt
    glaivesActive = s_glaivesActive
    glaivesFallsAt = s_glaivesFallsAt
    glaivesICDFallsAt = s_glaivesICDFallsAt
    customRatingActive = s_customRatingActive
    customRatingFallsAt = s_customRatingFallsAt
    customRatingICDFallsAt = s_customRatingICDFallsAt
    customMultiActive = s_customMultiActive
    customMultiFallsAt = s_customMultiFallsAt
    customMultiICDFallsAt = s_customMultiICDFallsAt
    #header
    #header
    totalPotencyProcs = s_totalPotencyProcs
    totalRuthlessnessProcs = s_totalRuthlessnessProcs
    totalRelentlessProcs = s_totalRelentlessProcs
    totalCappedEnergy = s_totalCappedEnergy
    totalDodgedSinisters = s_totalDodgedSinisters
    timeWithoutSlice = s_timeWithoutSlice
    trackingProcActivatedAt = s_trackingProcActivatedAt
    exposeAppliedAt = s_exposeAppliedAt

def finishIteration():
    global iterationCount

    if debugMode: print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if debugMode: print("total potency procs:", totalPotencyProcs, "total ruthlessness procs:", totalRuthlessnessProcs, "total relentless procs:", totalRelentlessProcs, "\ntime without slice", timeWithoutSlice/ticksPerSecond, "total capped energy:", totalCappedEnergy, "total dodged ss:", totalDodgedSinisters,)
    if debugMode: print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    iterationCount += 1
    aggregateData(totalTime=currentTickTime, exposeTime=exposeAppliedAt, sliceMissingTime=timeWithoutSlice, potencyProcs=totalPotencyProcs, cappedEnergy=totalCappedEnergy, trackingProcProccedAt=trackingProcActivatedAt)
    if debugMode: print("~~ finished iteration", iterationCount, "~~\n")

def initializeSim():
    initializePpmSettings()
    resetSim()

def simOneTick():
    global currentTickTime

    if debugMode: print("current time:  ", (currentTickTime/ticksPerSecond), " current energy: ", energy)

    checkExternals()

    castAbilities()
    autoAttack()

    energyTick()

    castAbilities() # checking again in case i got more energy


    checkIfFinishedOpener()
    if finishedOpener == True:
        finishIteration()
        return

    trackBuffUptime()

    checkFallingBuffs()

    if currentTickTime >= maxSimTime:
        print("send help sim ran too long")
        finishIteration()

    currentTickTime += timeTick

def runSim():

    initializeSim()

    while iterationCount < iterations:
        updateHaste()

        while currentTickTime <= maxSimTime and finishedOpener == False:
            simOneTick()
        
        if not debugMode: printLoadingBar()

        resetSim()

def printLoadingBar():
    global loadingBarStepsTaken
    global havePrintedLoadingTitle

    if not havePrintedLoadingTitle:
        totalSteps = (iterations // printLoadingBarSteps) + 1

        print("Preparing...  [-", totalSteps*loadingBarCharacter, "-]", sep="") #i legitimatally want to put a like 0.2s fake delay in here somewhere... UX
        print("Simulating... [-", end="")
        havePrintedLoadingTitle = True

    if iterationCount == (printLoadingBarSteps*loadingBarStepsTaken):
        loadingBarStepsTaken += 1
        print(loadingBarCharacter, end="", flush = True)

    if iterationCount == iterations:
        print(loadingBarCharacter, "-]\n", sep="") #2 new lines to end loading bar


#~~~~~~~~~~~~~~~
# output logic
#~~~~~~~~~~~~~~~

iterationsCount = 0
dataTotalExposeTime = 0
dataTotalSliceDropTime = 0
dataTotalPotencyProcs = 0
dataFastestExpose = inactiveTime
dataSlowestExpose = inactiveTime
dataOvercappedEnergy = 0
dataMostOvercappedEnergy = 0
dataTotalTrackingProcAtTime = 0
dataTrackingProcsBeforeTime = 0
dataTotalTimeBeforeSteadyState = 0
dataFastestOpener = inactiveTime
dataSlowestOpener = inactiveTime

def aggregateData(totalTime, exposeTime, sliceMissingTime, potencyProcs, cappedEnergy, trackingProcProccedAt):
    global iterationsCount
    global dataTotalExposeTime
    global dataTotalSliceDropTime
    global dataTotalPotencyProcs
    global dataFastestExpose
    global dataSlowestExpose
    global dataOvercappedEnergy
    global dataMostOvercappedEnergy
    global dataTotalTrackingProcAtTime
    global dataTrackingProcsBeforeTime
    global dataTotalTimeBeforeSteadyState
    global dataFastestOpener
    global dataSlowestOpener

        #make this a function later instead of copy pasting
    if exposeTime > dataSlowestExpose or dataSlowestExpose == inactiveTime:
        dataSlowestExpose = exposeTime
    if exposeTime < dataFastestExpose or dataFastestExpose == inactiveTime:
        dataFastestExpose = exposeTime

    if totalTime > dataSlowestOpener or dataSlowestOpener == inactiveTime:
        dataSlowestOpener = totalTime
    if totalTime < dataFastestOpener or dataFastestOpener == inactiveTime:
        dataFastestOpener = totalTime

    if cappedEnergy > 0:
        dataOvercappedEnergy += cappedEnergy

        if cappedEnergy > dataMostOvercappedEnergy:
            dataMostOvercappedEnergy = cappedEnergy


    iterationsCount += 1
    dataTotalExposeTime += exposeTime
    dataTotalSliceDropTime += sliceMissingTime
    dataTotalPotencyProcs += potencyProcs
    dataTotalTimeBeforeSteadyState += totalTime

    if trackingProcProccedAt == inactiveTime:
        dataTotalTrackingProcAtTime += 0
    else: dataTotalTrackingProcAtTime += trackingProcProccedAt

    if PPMreadoutBehaviour == 0:
        if PPMReadoutMaximumTime == -1:
            if (trackingProcProccedAt != inactiveTime): #as long as it procced at all, it procced before opener ended
                dataTrackingProcsBeforeTime += 1

        else:
            if (trackingProcProccedAt != inactiveTime) and trackingProcProccedAt <= PPMReadoutMaximumTime:
                dataTrackingProcsBeforeTime += 1
    else:
        if (trackingProcProccedAt >= totalTime - PPMReadoutTimeSubtraction) or (trackingProcProccedAt == inactiveTime):
            dataTrackingProcsBeforeTime += 1

def returnData():
    averageExposeTime = (dataTotalExposeTime/iterationsCount)
    averageSliceDropTime = (dataTotalSliceDropTime/iterationsCount)
    averageOpenerTime = (dataTotalTimeBeforeSteadyState/iterationsCount)
    averagePotencyProcs = dataTotalPotencyProcs/iterationsCount
    slowestExposeTime = dataSlowestExpose
    fastestExposeTime = dataFastestExpose
    slowestOpenerTime = dataSlowestOpener
    fastestOpenerTime = dataFastestOpener
    averageOvercappedEnergy = dataOvercappedEnergy/iterationsCount

    energyFromPotencyProcThisSim = 0
    if combatPotencyBehaviour == 1:
        energyFromPotencyProcThisSim = 3
    elif combatPotencyBehaviour == 2:
        energyFromPotencyProcThisSim = 15
    averageEnergyFromPotency = averagePotencyProcs * energyFromPotencyProcThisSim

    if printTitle:
        print("title:", simTitle)
    if printVersion:
        print("version:", simVersion)
    if printIterations:
        print("iterations:", iterationsCount)

    if printCooldownBehaviour:
        print(createCooldownReadout())
    if printPPMReadout and customTrackingProcEquipped:
        print(createPpmReadout())

    print("") #new line for spacing

    if printSteadyStateTime:
        print("average time to finish opener:", ticksToSecond(averageOpenerTime), "seconds")
    if printExposeTime:
        print("average time to expose:", ticksToSecond(averageExposeTime), "seconds")
    if printSliceDropTime:
        print("average time without slice:", ticksToSecond(averageSliceDropTime), "seconds")
    if printSlowestExpose:
        print("slowest expose:", ticksToSecond(slowestExposeTime), "seconds")
    if printFastestExpose:
        print("fastest expose:", ticksToSecond(fastestExposeTime), "seconds")
    if printSlowestOpener:
        print("slowest opener:", ticksToSecond(slowestOpenerTime), "seconds")
    if printFastestOpener:
        print("fastest opener:", ticksToSecond(fastestOpenerTime), "seconds")
    if printEnergyFromPotency:
        print("average energy from combat potency:", round(averageEnergyFromPotency, printDecimalPlaces), "|", round(averageEnergyFromPotency/ticksToSecond(averageOpenerTime), printDecimalPlaces), "energy/second")
    if printOvercappedEnergy:
        print("average over capped energy:", round(averageOvercappedEnergy, printDecimalPlaces))
    if printMostOvercappedEnergy: #not rounding to catch errors, since it should never not be a whole number (this is wrong if i ever go to 2.02s ticks)
        print("most capped energy in one sim:", dataMostOvercappedEnergy)

def ticksToSecond(timeInTicks):
    return round(timeInTicks/ticksPerSecond, printDecimalPlaces)

def createCooldownReadout():
    firstSliceReadout = ""
    adrenalineRushReadout = ""
    bladeFlurryReadout = ""
    teaReadout = ""
    hastePotionReadout = ""
    shivReadout = ""

    if openingSliceBehaviour >= 5:
        firstSliceReadout = "First Slice after expose"
    else:
        firstSliceReadout = "First Slice at " + str(openingSliceBehaviour) + " cp"

    if adrenalineRushBehaviour == 1:
        adrenalineRushReadout = "Adrenaline Rush: After Slice"
    elif adrenalineRushBehaviour == 2:
        adrenalineRushReadout = "Adrenaline Rush: On pull"
    else:
        adrenalineRushReadout = "Adrenaline Rush: Never"

    if bladeFlurryBehaviour == 1:
        bladeFlurryReadout = "Blade Flurry: On pull"
    else:
        bladeFlurryReadout = "Blade Flurry: Never"

    if thistleTeaBehaviour == 1:
        teaReadout = "Tea: Yes"
    else:
        teaReadout = "Tea: No"
    
    if hastePotionBehaviour == 1:
        hastePotionReadout = "Haste Potion on Pull"

    if shivBehaviour > 0:
        shivReadout = "Shivs cast: " + str(shivBehaviour)

        
    readouts = [firstSliceReadout, adrenalineRushReadout, bladeFlurryReadout, teaReadout, hastePotionReadout, shivReadout]

    
    finalReadout = ""
    readoutSeperator = " | "
    for readout in readouts:
        if readout: # isn't blank
            finalReadout += readout
            finalReadout += readoutSeperator
    
    return finalReadout

def createPpmReadout():
    
    percentofTrackingProcsBefore = str(round((dataTrackingProcsBeforeTime/iterationsCount) * 100, printDecimalPlaces))

    readout = ""

    if PPMreadoutBehaviour == 0:
        if PPMReadoutMaximumTime == -1:
            readout += "% of sims where " + customTrackingProcName + " procs before opener completed: " + percentofTrackingProcsBefore + "%"
        else:
            readout += "% of sims where " + customTrackingProcName + " procs before " + str(PPMReadoutMaximumTime) + ": " + percentofTrackingProcsBefore + "%"
    else:
        readout += "% of sims where " + customTrackingProcName + " didn't proc, or procs at most " + str(ticksToSecond(PPMReadoutTimeSubtraction)) + "s before opener completed: " + percentofTrackingProcsBefore + "%"

    return readout

runSim()
returnData()

endingScreen = input("\nhappy simming!")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#TO DO

#fix finisher check to accomodate 0.05s left on slice and 0 energy/0cp - somehow check for (slice active AND [energy to cast slice OR time to not need to cast slice])
#clean up trinket readout.. make it better too... use it to see what you need

#known issues
#energy ticks are every 2s not every 2.02s, and so you always get 20 energy not sometimes 21. not sure exactly how this works in game, esp with ar, and i figure it's minor in such a short time frame
#expose isn't a timed aura - this will only matter if you somehow put up expose and then don't get a slice up before expose falls...

#~~here be feature creep~~
#random seeds : D for debug and to help me make new versions and double check findings
#have "auto failed" return why it failed
#comment everything better : D
#change the huge code blocks at the top into tuple lists or something better maybe
#fix haste buffs to refer to set strings instead of magic strings; maybe have a list constructor that checks all...
#fix haste procs to not check unequipped procs every time.. it's called very often so it should be as cheap as possible
#probably make some sort of class for procs - with their name, equipped state, bonus/multi, ppm, etc
#change all ticks to real time lmao enough
#make all the comparision from checkTime <= currentTime consistent in direction; some are currenttime >= checkTime
#streamline 'not' and '== False'
#instead of checking to end sim every tick, check to end sim every finisher? would save perf but be less flexible
#unhardcode all ability energy/cp costs in abilities function
#bf: should make this smarter - only not cast bf if tick < gcd and energy after tick > energy+bf cost; but this will like never matter
#tea: maybe have it check for all abilities, then tea, then abilities again; and can even print how many trials actually used tea.. but my perf
#for performance have functions not define their own variables.. lol
#display energy from all procs relentless+ruthless... maybe?
#darkmantle????????
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~