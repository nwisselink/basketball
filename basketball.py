class playergenerator:
    import random as r
    def __init__ (Self,  Name,height, weight, draftPosition, archetype,Ratings,Ovr):#constructor that creates a new player object, with arguments ratings, name, overall and draft positiion, more will be added
        Self.draftPosition = draftPosition
        Self.height = height
        Self.weight = weight
        Self.Ovr = Ovr
        Self.Name = Name
        Self.Ratings = Ratings
        Self.archetype = archetype  
    def parsePlayerHeight(playerHeightInches):
        import math
        playerHeightFeet = math.trunc(playerHeightInches/12)
        playerHeightInches = playerHeightInches%12
        return playerHeightFeet,"foot",playerHeightInches   
    def archetypeSelector():#returns the player archetype
        import random as r
        a = r.randint(0,8)
        unicornChecker= r.randint(1,35)
        if unicornChecker==35:
            a = 9
        trait = ["Facilitator", "Lock Down Perimeter Defender","Combo Guard","shot creator", "3 and D wing", "Athletic Wing finisher","stretch big", "Board Cleaning Big Man", "Rim Protector", "Unicorn"]
        n = [[trait[0],r.randint(67,73),r.randint(150,190),7,8,-2,0,-4,-1,-6,-2,5,-8,5,-5,0]
        ,[trait[1],r.randint(70,75),r.randint(180,220),0,2,2,0,-6,-6,-5,-2,10,2,9,-10,0]
        ,[trait[2],r.randint(69,76),r.randint(165,200),3,2,-1,3,4,4,-6,-6,0,-3,-9,3,0]
        ,[trait[3],r.randint(68,74),r.randint(170,190),5,-9,-6,1,9,11,-7,-8,3,1,-8,-5,0]
        ,[trait[4],r.randint(73,79),r.randint(190,238),-10,-6,-4,-3,0,8,0,0,9,6,2,11,0]
        ,[trait[5],r.randint(73,79),r.randint(185,234),2,-6,12,10,0,-7,2,-5,3,1,-5,-2,0]
        ,[trait[6],r.randint(76,80),r.randint(210,247),-5,3,-6,1,7,10,0,-2,-2,-4,-1,-5,0]
        ,[trait[7],r.randint(77,82),r.randint(220,259),-10,-8,7,8,-5,-19,10,10,-9,7,9,-15,0]
        ,[trait[8],r.randint(78,84),r.randint(230,300),-12,-10,12,9,-10,-10,6,5,-15,15,12,-20,0]
        ,[trait[9],r.randint(80,86),r.randint(220,280),5,10,-5,2,3,12,0,-5,7,3,3,5,-5]]
        return n[a]
    def nameGenerator():
        import random as r
        lastNames = ["Smith", "Jones", "Curry"]
        firstNames = ["John", "Steph", "Jason"]
        lastNameIndex = r.randint(0,2)
        firstNameIndex = r.randint(0,2)
        return firstNames[firstNameIndex], lastNames[lastNameIndex]
    def getRatingNames():
        return ["dribbling", "playmaking", "dunking", "inside shot", "mid range shot", "three point shot", "offensive rebounding",
        "defensive rebounding", "steal", "block","perimeter defense", "inside defense", "clutch"]
    def playerGenerator(archetype, draftPositionBonus):
        import random as r    
        playerTraitBonuses = [archetype[3],archetype[4],archetype[5],archetype[6],archetype[7],archetype[8],archetype[9],archetype[10],archetype[11],archetype[12],archetype[13],archetype[14],archetype[15]]
        return [ r.randint(65,75)+draftPositionBonus + playerTraitBonuses[0], r.randint(65,75) + draftPositionBonus + playerTraitBonuses[1], r.randint(65, 75) +draftPositionBonus+playerTraitBonuses[2],
         r.randint(65,75)+draftPositionBonus + playerTraitBonuses[3], r.randint(65,75)+draftPositionBonus + playerTraitBonuses[4], r.randint(65, 75)+draftPositionBonus + playerTraitBonuses[5],
         r.randint(65,75)+playerTraitBonuses[6]+draftPositionBonus, r.randint(65,75)+playerTraitBonuses[7]+draftPositionBonus, r.randint(65,75)+draftPositionBonus + playerTraitBonuses[8],
        r.randint(65,75)+playerTraitBonuses[9]+draftPositionBonus, r.randint(65,75)+draftPositionBonus + playerTraitBonuses[10], r.randint(65,75)+draftPositionBonus+playerTraitBonuses[11], r.randint(65,75)+draftPositionBonus+playerTraitBonuses[12]]
    def getUserTeam(leagueFrame):#place holder method not included in tests because it is not being used right now
        teams = leagueFrame[5]
        return "To be continued"
    def createPlayer(drafted, draftOrderKeeper,actualPlayerIndex):
        import random as r
        if drafted == True:
            draftPosition = draftOrderKeeper
        else:
            draftPosition = r.randint(0,59)
        playerArchetype = playergenerator.archetypeSelector()
        playerWeight = playerArchetype[2]
        playerHeight = playergenerator.parsePlayerHeight(playerArchetype[1])
        playerRealArchetype =playerArchetype[0]
        draftPositionBonus = playergenerator.draftPositionAdjuster(draftPosition)
        ratings = playergenerator.playerGenerator(playerArchetype,draftPositionBonus)
        actualDraftPosition = draftPosition + 1
        
        newPlayer = playergenerator(playergenerator.nameGenerator(),playerHeight,playerWeight, actualDraftPosition,playerRealArchetype,ratings,playergenerator.getOverall(ratings))
        return [newPlayer.Name,newPlayer.height, newPlayer.weight,newPlayer.draftPosition,newPlayer.archetype,newPlayer.Ratings, newPlayer.Ovr,actualPlayerIndex]
    def simplifyLeagueFrame(leagueFrame):
        simplifiedLeagueFrame=[]
        conferenceIndex=0
        divisionIndex=1
        teamIndex=0
        for i in range(30):
           simplifiedLeagueFrame.append(leagueFrame[conferenceIndex][divisionIndex][1][teamIndex])          
           teamIndex=teamIndex+1
           if teamIndex>4:
              divisionIndex=divisionIndex+1
              teamIndex=0
              if divisionIndex>3:
                  divisionIndex=1
                  conferenceIndex=conferenceIndex+1
                  if conferenceIndex>1:
                      break
        return simplifiedLeagueFrame
    def getOverall(ratings):
        ratings = ratings
        baseoverall = (ratings[0] + ratings[1] + ratings[2] + ratings[3] + ratings[4] + ratings[5] + ratings[6] + ratings[7] + ratings[8] + ratings[9] + ratings[10] + ratings[11] + ratings[12] )/13
        roundedOverall = round(baseoverall)
        return roundedOverall
    def getDraftPosition(draftPosition):#why
        draftPosition = draftPosition 
        return draftPosition
    def draftPositionAdjuster(draftPosition):
        import random as r
        draft = [ r.randint(12,26),r.randint(11,23),r.randint(10,20), r.randint(10,19),r.randint(9,19),r.randint(9,18)
        ,r.randint(9,17),r.randint(8,17),r.randint(8,16),r.randint(8,15),r.randint(7,15),r.randint(7,14),r.randint(7,13),r.randint(6,13),r.randint(5,12),r.randint(5,11)
        ,r.randint(4,11),r.randint(3,10),r.randint(3,9),r.randint(1,9),r.randint(0,8),r.randint(0,7),r.randint(-1,7),r.randint(-1,6),r.randint(-1,3),r.randint(-2,3)
        ,r.randint(-2,4),r.randint(-4,2),r.randint(-4,1),r.randint(-4,0),r.randint(-3,0),r.randint(-5,1),r.randint(-6,1),r.randint(-6,0),r.randint(-7,0),r.randint(-8,-1)
        ,r.randint(-9,-1),r.randint(-9,-2),r.randint(-10,-3),r.randint(-11,-3),r.randint(-11,-4),r.randint(-11,-5),r.randint(-12,-5),r.randint(-12,-6),r.randint(-13,-6),r.randint(-14,-6)
        ,r.randint(-14,-7),r.randint(-15,7),r.randint(-15,-8),r.randint(-16,-8),r.randint(-17,-8),r.randint(-17,-9),r.randint(-18,-9),r.randint(-19,-9),r.randint(-19,-10),r.randint(-20,-10),-r.randint(-20,-12),r.randint(-20,-13),r.randint(-20,5),r.randint(-30,20)]
        return draft[draftPosition]
    def abbreviatedPlayer(player):
        return [player[0],player[6]]
    def leagueInitialization():
        leagueFrame = [["Western Conference",["South West Division",[["DAL"],["HOU"],["MEM"],["NOP"],["SAS"]]]
        , ["Pacific Division",[["LAL"],["LAC"],["GSW"],["SAC"],["PHO"],]]
        , ["Northwest Division",[["POR"], ["OKC"], ["DEN"],["UTA"],["MIN"]]]]
        , ["Eastern Conference",["Southeast Division",[["MIA"],["ORL"],["ATL"],["WSH"],["CHA"]]]
        , ["Atlantic Division",[["TOR"],["BOS"],["PHI"],["NYK"],["BKN"],]]
        , ["Central Division",[["DET"],["CHI"], ["IND"], ["MIL"], ["CLE"],]]]]
        
        conferenceIndex = int(0)
        divisionIndex = int(1)
        teamIndex = int(0)
        playerIndex = int(0)
        for i in range(0,450):
            newPlayer=playergenerator.createPlayer(False, 0,playerIndex)
            leagueFrame[conferenceIndex][divisionIndex][1][teamIndex].insert(1,newPlayer)
            playerIndex = playerIndex+ 1
            if playerIndex > 14:
                teamIndex = teamIndex + 1
                playerIndex = 0
                if teamIndex > 4:
                    divisionIndex=divisionIndex+1
                    teamIndex=0
                    if divisionIndex == 4:
                        conferenceIndex = conferenceIndex + 1
                        divisionIndex = 1
                        if conferenceIndex == 2:
                            break
        return leagueFrame
    def draft():
        draftOrderKeeper = 0
        draft = []
        for i in range (0,60):
            newPlayer=playergenerator.createPlayer(True,draftOrderKeeper,3)
            draft.insert(draftOrderKeeper,newPlayer)
            draftOrderKeeper = draftOrderKeeper + 1
        return draft
class gameMethods():
    def getThreePointer(passBonus,dribblingBonus,defenseShotRating,offenseShotRating,possibleBlock):
        if possibleBlock==True:
           return [0,0,0,1,0]
        if passBonus>dribblingBonus:
            assist=True
        else: assist=False
        totalBonus=passBonus+dribblingBonus
        defenseBonus=(offenseShotRating-defenseShotRating)/10
        attemptedShot=(offenseShotRating/1.99)+(totalBonus*1.2)+defenseBonus
        if attemptedShot>gameMethods.diceRoll(90):
            return [3,assist,1,1,0]#actual points,amount of assists,field goal made, field goal attempted,dunk
        return [0,0,0,1,0]
    def getMidRange(passBonus,dribblingBonus,defenseShotRating,offenseShotRating,possibleBlock):
        if possibleBlock==True:
            return [0,0,0,1,0]
        if passBonus>dribblingBonus:
            assist=1
        else: assist=0
        totalBonus=passBonus+dribblingBonus
        defenseBonus=(offenseShotRating-defenseShotRating)/8
        attemptedShot=(offenseShotRating/1.76)+totalBonus+defenseBonus
        if attemptedShot>gameMethods.diceRoll(95):
            return [2,assist,1,1,0]
        return [0,0,0,1,0]
    def getInsideShot(passBonus,dribblingBonus,defenseShotRating,offenseShotRating,dunk,possibleBlock):
        if possibleBlock==True:
            return [0,0,0,1,0]
        if passBonus>dribblingBonus:
            assist=1
        else: assist=0
        totalBonus=passBonus+dribblingBonus
        defenseBonus=(offenseShotRating-defenseShotRating)/7
        attemptedShot=(offenseShotRating/1.7)+totalBonus+defenseBonus
        if attemptedShot>gameMethods.diceRoll(100):
            return [2,assist,1,1,dunk]
        return [0,0,0,1,0]
    def getFreeThrow(playerFreeThrowRating,amountOfFreeThrows):
        listOfFreeThrows=[]
        for i in range(amountOfFreeThrows):
            if playerFreeThrowRating>92:
                playerFreeThrowRating=92
            if playerFreeThrowRating>gameMethods.diceRoll(96):
                valueOfFreeThrow=1
            else: valueOfFreeThrow=0
            listOfFreeThrows.append(valueOfFreeThrow)
        return listOfFreeThrows
    def getShotAttempt(passBonus,dribblingBonus,defenseShotInformation,offenseShotInformation,passLocation,dunk,possibleBlock):
        if  passLocation==0:
            return gameMethods.getThreePointer(passBonus,dribblingBonus,defenseShotInformation[0],offenseShotInformation[0],possibleBlock)
        elif passLocation==1:
            return gameMethods.getMidRange(passBonus,dribblingBonus,defenseShotInformation[1],offenseShotInformation[1],possibleBlock)
        elif passLocation==2:
            return gameMethods.getInsideShot(passBonus,dribblingBonus,defenseShotInformation[2],offenseShotInformation[2],dunk,possibleBlock)
        else:
            pass
    def getBlockPecentage(teamBlockRating,shotTypeBonus):
        import random as r
        blockPercentage = teamBlockRating/shotTypeBonus
        successfullBlockChecker = r.randint(0,100)
        if blockPercentage > successfullBlockChecker:
            return False
        else:
            return True
    def getgameFrame(homeTeam,awayTeam):
        return [homeTeam, awayTeam]
    def sortPlayers(gameFrame):
        from operator import itemgetter 
        gameMethods.removeFirst(gameFrame)
        gameFrame[0].sort(key = itemgetter(6),reverse = True)
        gameFrame[1].sort(key = itemgetter(6), reverse = True)
        return gameFrame
    def removeFirst(gameFrame):
        gameFrame[0].pop(0)  
        gameFrame[1].pop(0)
        return gameFrame
    def diceRoll(range):
        import random as r
        return r.randint(1,range)
    def getTeamRoleHeirarchies(fiveOnFloorUsage):
        totalUsage = fiveOnFloorUsage[0]+fiveOnFloorUsage[1]+fiveOnFloorUsage[2]+fiveOnFloorUsage[3]+fiveOnFloorUsage[4]
        fiveOnFloorUsageIndex = 0
        deleteIndex = 0
        usageAdjuster = 1
        if totalUsage > 100:
            while totalUsage >101:
                if fiveOnFloorUsage[fiveOnFloorUsageIndex] < 5:
                    usageAdjuster=0
                else: usageAdjuster = 1
                adjustedFiveOnFloorUsage = fiveOnFloorUsage[fiveOnFloorUsageIndex]-usageAdjuster
                totalUsage=fiveOnFloorUsage[0]+fiveOnFloorUsage[1]+fiveOnFloorUsage[2]+fiveOnFloorUsage[3]+fiveOnFloorUsage[4]
                del(fiveOnFloorUsage[deleteIndex])
                fiveOnFloorUsage.insert(fiveOnFloorUsageIndex,adjustedFiveOnFloorUsage)
                fiveOnFloorUsageIndex=fiveOnFloorUsageIndex+1
                deleteIndex = fiveOnFloorUsageIndex
                if fiveOnFloorUsageIndex==5:
                   deleteIndex =0
                   fiveOnFloorUsageIndex=0
                   continue
        elif totalUsage<100:
                while totalUsage <99:
                    adjustedFiveOnFloorUsage = fiveOnFloorUsage[fiveOnFloorUsageIndex]+1
                    totalUsage=fiveOnFloorUsage[0]+fiveOnFloorUsage[1]+fiveOnFloorUsage[2]+fiveOnFloorUsage[3]+fiveOnFloorUsage[4]
                    del(fiveOnFloorUsage[deleteIndex])
                    fiveOnFloorUsage.insert(fiveOnFloorUsageIndex,adjustedFiveOnFloorUsage)
                    fiveOnFloorUsageIndex=fiveOnFloorUsageIndex+1
                    deleteIndex = fiveOnFloorUsageIndex
                    if fiveOnFloorUsageIndex==5:
                        deleteIndex =0
                        fiveOnFloorUsageIndex=0
                        continue
        return fiveOnFloorUsage
    def parseBlockStats(countingStats,defenseIndex,primaryDefender,benchStatCompiler):
        countingStats[defenseIndex][primaryDefender+benchStatCompiler][5][2]=countingStats[defenseIndex][primaryDefender+benchStatCompiler][5][2]+1
        countingStats[defenseIndex+1][2]=countingStats[defenseIndex+1][2]+1
    def getShotAggressiveness(playerOverall):
        primaryShotCreatorAgressiveness=int(playerOverall[0]*1.8)
        secondaryShotCreatorAgressiveness=int(playerOverall[1]*1.8)
        tertiaryShotCreatorAgressiveness=int(playerOverall[2]*1.8)
        quaternaryShotCreatorAgressiveness=int(playerOverall[3]*1.8)
        quinnaryShotCreatorAgressiveness=int(playerOverall[4]*1.8)
        return[primaryShotCreatorAgressiveness,secondaryShotCreatorAgressiveness,
        tertiaryShotCreatorAgressiveness,quaternaryShotCreatorAgressiveness,quinnaryShotCreatorAgressiveness]
    def getTeamShotTendency(teamShotTendency):
        possibleShotTendencies=[[60,72,100],[55,70,100],[50,68,100],[47,70,100],[42,72,100],[40,66,100],[40,60,100],[40,56,100],[38,52,100],[36,48,100]]
        return possibleShotTendencies[teamShotTendency]
    def getPassLocation(teamShotTendency):
        passGetter=gameMethods.diceRoll(100)
        if passGetter <= teamShotTendency[0]:
            return 0
        elif passGetter <= teamShotTendency[1]:
            return 1
        else:
            return 2
    print()
    def getFiveOnFloor(gameFrame):
        return [[gameFrame[0][0],gameFrame[0][1],gameFrame[0][2],gameFrame[0][3],gameFrame[0][4]],
        [gameFrame[1][0],gameFrame[1][1],gameFrame[1][2],gameFrame[1][3],gameFrame[1][4]]]
    def getTeamStats(fiveOnFloor):
        statIndex=6
        playerIndex=0
        teamStatList=[[],[]]
        teamIndex=0
        teamAccess=0
        totalSumofStat=0
        for i in range(0,100):
           totalSumofStat =totalSumofStat+fiveOnFloor[teamIndex][playerIndex][5][statIndex]
           playerIndex=playerIndex+1
           if playerIndex>4:
              averagedStat=totalSumofStat/5
              playerIndex=0
              teamStatList[teamAccess].append(averagedStat)
              totalSumofStat=0    
              statIndex = statIndex+1
              if statIndex > 11:
                teamAccess=teamAccess+1
                teamIndex=teamIndex+1
                statIndex=6
                if teamIndex ==2:
                    break
        return teamStatList
    def getPass(teamUsage, passLocation):
        passLocator=gameMethods.diceRoll(100)
        if passLocator<teamUsage[0]:
            player = 0
        elif passLocator<teamUsage[1]:
            player = 1
        elif passLocator<teamUsage[2]:
            player= 2
        elif passLocator<teamUsage[3]:
            player =3 
        else:
            player = 4
        return [player,passLocation]
    def getTimePerPass():
        import random as r
        return r.randint(2,4)
    def getShot(playerShotAggressiveness):
        shotAttemptSuccessCheck=gameMethods.diceRoll(100)
        if shotAttemptSuccessCheck<playerShotAggressiveness:
            return True
        else:
            return False
    def getBallHandlingBonus(numberOfPasses,gameFrame,team,player,playerLocation):
        return int(gameFrame[team][player][5][0]/10)-numberOfPasses-3-playerLocation
    def getPlayMakingBonus(numberOfPasses,gameFrame,team,player,playerLocation):
        return int(gameFrame[team][player][5][1]/20)+numberOfPasses-5+playerLocation
    def setPlayerCountStatsList():
        return ["Passes","AST","Blk","STL","TO","ORB","DRB","TRB","3PM","3PA"
        ,"MRM","MRA","INM","INA","FTM","FTA","PTS","TOP","FGA","FGM","fouls","ORBA","DRBA","TRBA"]
    def setPlayerAdvancedStatsList():
        return["Usage rate","AST/TO","AST%","AST RATIO","OREB%","DREB%","REB%","PER","DFG","RBMAR",
        "TORATIO","DRATING","ORATING","TS","EFG%","DWS","OWS","VORP","WS","WS/48""D3P%","DMR%","DIN%"]
    def setPlayerFitStatsList():
        return["TeamFitRating",""]
    def clearPlayerAttributes(team):
        statIndex=0
        attributeIndex = 5
        playerIndex= 0
        stat=0
        for i in range(0,295):
            del team[playerIndex][attributeIndex][statIndex]
            stat=stat+1
            if stat>12:
               stat=0
               playerIndex=playerIndex+1
               if playerIndex>14:
                  break
        return team
    def getOveralls(fiveOnFloor):
        return [[fiveOnFloor[0][0][7],fiveOnFloor[0][1][7],fiveOnFloor[0][2][7],fiveOnFloor[0][3][7],fiveOnFloor[0][4][7]],
                [fiveOnFloor[1][0][7],fiveOnFloor[1][1][7],fiveOnFloor[1][2][7],fiveOnFloor[1][3][7],fiveOnFloor[1][4][7]]]
    def setPlayerStats(playerStatsFrame,numberOfStats):
        statIndex = 0
        attributeIndex=5
        playerIndex = 0
        for i in range(0,15*numberOfStats):
            playerStatsFrame[playerIndex][attributeIndex].append(0)
            statIndex=statIndex+1
            if statIndex>numberOfStats-1:
                statIndex=0
                playerIndex = playerIndex +1
                if playerIndex>14:
                    break
        return playerStatsFrame
    def getBlock(blockRating,passLocation,dunk,shotLocationBonus=0):
        if dunk==True:
           shotLocationBonus=2.7
        elif passLocation==0:
            shotLocationBonus=14.3
        elif passLocation==1:
            shotLocationBonus=5
        else:
            shotLocationBonus=3
        percentageOfBlock=(blockRating/63)*shotLocationBonus
        if percentageOfBlock>gameMethods.diceRoll(100):
            return True
        else: return  False
    def parseIntoIterablePercentage(unParsedList):#get better names for this plz
        firstPlayer=unParsedList[0]
        secondPlayer=unParsedList[1]+unParsedList[0]
        thirdPlayer=unParsedList[2]+secondPlayer
        fourthPlayer=unParsedList[3]+thirdPlayer
        fifthPlayer=unParsedList[4]+fourthPlayer
        return[firstPlayer+1,secondPlayer-.25,thirdPlayer-.25,fourthPlayer-.25,fifthPlayer-.25]
    def getPrimary(heirarchy):
        defenderChooser=gameMethods.diceRoll(100)#please pick better name for variable
        defenderList=gameMethods.parseIntoIterablePercentage(heirarchy)
        if defenderChooser<defenderList[0]:
            return 0
        elif defenderChooser<defenderList[1]:
            return 1
        elif defenderChooser<defenderList[2]:
            return 2
        elif defenderChooser<defenderList[3]:
            return 3
        elif defenderChooser<defenderList[4]:
            return 4
        else: return 0
    def getIterableStatOveralls(fiveOnfloor,statIndex):
        playerIndex=0
        iterableStatOveralls=[]
        for i in range(0,5):
            iterableStatOveralls.append(fiveOnfloor[playerIndex][5][statIndex])
            playerIndex=playerIndex+1
        return iterableStatOveralls
    def getStatOveralls(fiveOnFloor,startingIndex,totalNumberOfStats):
        playerIndex=0
        attributeIndex=5
        statIndex=startingIndex
        newOverall=0
        defenseOveralls=[]
        loopCounter=0
        for i in range(totalNumberOfStats*5):
           newOverall = fiveOnFloor[playerIndex][attributeIndex][statIndex]+newOverall
           statIndex=statIndex+1
           loopCounter=loopCounter+1
           if loopCounter>4:
               playerIndex=playerIndex+1
               newOverall=int(newOverall/5)
               defenseOveralls.append(newOverall)
               newOverall=0
               statIndex=7
               loopCounter=0
               if playerIndex>4:
                   break
        return defenseOveralls  
    def game(homeTeam,awayTeam):
        import copy
        gameInformation=[24,1440,480]
        homeTeamFouls=0 
        awayTeamFouls=0
        gameFrame=gameMethods.getgameFrame(homeTeam,awayTeam)
        sortedGameFrame=gameMethods.sortPlayers(gameFrame)
        homeTeam=sortedGameFrame[0]
        awayTeam=sortedGameFrame[1]
        newHomeTeam=copy.deepcopy(homeTeam)
        newAwayTeam=copy.deepcopy(awayTeam)
        possessions=1
        substitution=0
        homeclearedPlayerAttributes=gameMethods.clearPlayerAttributes(homeTeam)
        awayClearedPlayerAttributes=gameMethods.clearPlayerAttributes(awayTeam)
        homeTeam=gameMethods.setPlayerStats(homeclearedPlayerAttributes,25)
        awayTeam=gameMethods.setPlayerStats(awayClearedPlayerAttributes,25)
        fiveOnFloor=gameMethods.getFiveOnFloor([newHomeTeam,newAwayTeam])        
        offenseTeamFiveOnFloor=fiveOnFloor[0]
        defenseTeamFiveOnFloor=fiveOnFloor[1]
        starterFiveOnFloorIndexes=[0,1,2,3,4]
        benchFiveOnFloorIndexes=[5,6,7,8,9]
        reserveFiveOnFloorIndexes=[10,11,12,13,14]
        countingStats=[homeTeam,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],awayTeam,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        fiveOnFloorIndexes=[0,1,2,3,4]
        while gameInformation[1]>0:
             if gameInformation[2]<0:
                offenseTeamFiveOnFloor=gameMethods.getSubstitution(newHomeTeam,benchFiveOnFloorIndexes)
                defenseTeamFiveOnFloor=gameMethods.getSubstitution(newAwayTeam,benchFiveOnFloorIndexes) 
                substitution=1
                fiveOnFloorIndexes=benchFiveOnFloorIndexes
             if gameInformation[2]<-400:
                offenseTeamFiveOnFloor=gameMethods.getSubstitution(newHomeTeam,benchFiveOnFloorIndexes)
                defenseTeamFiveOnFloor=gameMethods.getSubstitution(newAwayTeam,benchFiveOnFloorIndexes)
                substitution=2
                fiveOnFloorIndexes=reserveFiveOnFloorIndexes
             if gameInformation[2]<-500:
                offenseTeamFiveOnFloor=gameMethods.getSubstitution(newHomeTeam,starterFiveOnFloorIndexes)
                defenseTeamFiveOnFloor=gameMethods.getSubstitution(newAwayTeam,starterFiveOnFloorIndexes) 
                substitution=0
                fiveOnFloorIndexes=starterFiveOnFloorIndexes
             gameMethods.getPossession(countingStats,"shitandpiss",offenseTeamFiveOnFloor,defenseTeamFiveOnFloor,0,2,possessions,gameInformation,substitution,fiveOnFloorIndexes)
             gameMethods.getPossession(countingStats,"dickandballs",defenseTeamFiveOnFloor,offenseTeamFiveOnFloor,2,0,possessions,gameInformation,substitution,fiveOnFloorIndexes)  
             possessions=possessions+2
             if possessions>200:
                break
        gameInformation[1]=1440
        gameInformation[2]=480
        while gameInformation[1]>0:
            if gameInformation[2]<0:
                offenseTeamFiveOnFloor=gameMethods.getSubstitution(newHomeTeam,benchFiveOnFloorIndexes)
                defenseTeamFiveOnFloor=gameMethods.getSubstitution(newAwayTeam,benchFiveOnFloorIndexes) 
                substitution=1
                fiveOnFloorIndexes=benchFiveOnFloorIndexes
            if gameInformation[2]<-400:
                offenseTeamFiveOnFloor=gameMethods.getSubstitution(newHomeTeam,benchFiveOnFloorIndexes)
                defenseTeamFiveOnFloor=gameMethods.getSubstitution(newAwayTeam,benchFiveOnFloorIndexes)
                substitution=2
                fiveOnFloorIndexes=reserveFiveOnFloorIndexes
            if gameInformation[2]<-500:
                offenseTeamFiveOnFloor=gameMethods.getSubstitution(newHomeTeam,starterFiveOnFloorIndexes)
                defenseTeamFiveOnFloor=gameMethods.getSubstitution(newAwayTeam,starterFiveOnFloorIndexes) 
                substitution=0
                fiveOnFloorIndexes=starterFiveOnFloorIndexes
            gameMethods.getPossession(countingStats,"shitandpiss",offenseTeamFiveOnFloor,defenseTeamFiveOnFloor,0,2,possessions,gameInformation,substitution,fiveOnFloorIndexes)
            gameMethods.getPossession(countingStats,"dickandballs",defenseTeamFiveOnFloor,offenseTeamFiveOnFloor,2,0,possessions,gameInformation,substitution,fiveOnFloorIndexes)  
            possessions=possessions+2
            if possessions>200:   
                break
        return countingStats
    def getPossession(countingStats,teamAttributes,offenseTeamFiveOnFloor,defenseTeamFiveOnFloor,defenseIndex,offenseIndex,possessions,gameInformation,substitution,fiveOnFloorIndexes):
        shotClock=24
        madeShot=None
        overalls=gameMethods.getOveralls([offenseTeamFiveOnFloor,defenseTeamFiveOnFloor])
        defenseOveralls=overalls[1]
        defenseHeirarchy=gameMethods.getTeamRoleHeirarchies(defenseOveralls)
        offenseOveralls=overalls[0]
        offenseHierarchy=gameMethods.getTeamRoleHeirarchies(offenseOveralls)
        passLocation=gameMethods.diceRoll(2)
        passBonus=0
        defenseTeamCountingStatsIndex=defenseIndex+1
        offenseTeamCountingStatsIndex=offenseIndex+1
        possessions=possessions+1
        teamShotTendency=gameMethods.getTeamShotTendency(gameMethods.diceRoll(9))
        while shotClock > 0:
            import random as r
            timePerPass=gameMethods.getTimePerPass()
            shotClock=shotClock-timePerPass
            if shotClock<0:
                shotClock=0  
            gameInformation[1]=gameInformation[1]-timePerPass
            gameInformation[2]=gameInformation[2]-timePerPass
            primaryDefender=gameMethods.getPrimary(defenseHeirarchy)
            ballHandler=gameMethods.getPrimary(offenseHierarchy)
            benchStatCompiler=5*substitution
            passBonus = passBonus+(offenseTeamFiveOnFloor[ballHandler][5][1]/75+(r.randint(-1,1)))
            dribblingBonus=offenseTeamFiveOnFloor[ballHandler][5][0]/75+(r.randint(-1,1))
            possibleOffensiveRatings=[offenseTeamFiveOnFloor[ballHandler][5][5],offenseTeamFiveOnFloor[ballHandler][5][4],offenseTeamFiveOnFloor[ballHandler][5][3],offenseTeamFiveOnFloor[ballHandler][5][2]]
            possibleDefensiveRatings=[defenseTeamFiveOnFloor[primaryDefender][5][10],(defenseTeamFiveOnFloor[primaryDefender][5][10]+defenseTeamFiveOnFloor[primaryDefender][5][11])/2,defenseTeamFiveOnFloor[primaryDefender][5][11]]  
            oldTurnoverStat= countingStats[offenseTeamCountingStatsIndex][3]
            oldStealStat= countingStats[defenseTeamCountingStatsIndex][4]
            gameMethods.parseTurnoverStats(offenseTeamFiveOnFloor,defenseTeamFiveOnFloor,countingStats,passBonus,defenseIndex,offenseIndex,ballHandler,primaryDefender,benchStatCompiler)
            newTurnoverStat= countingStats[offenseTeamCountingStatsIndex][3]
            newStealStat=countingStats[defenseTeamCountingStatsIndex][4]
            possibleTurnover=gameMethods.gameBooleans(oldTurnoverStat,newTurnoverStat)
            possibleSteal=gameMethods.gameBooleans(oldStealStat,newStealStat)
            if possibleTurnover:  
                break
            if possibleSteal:  
                break
            possibleShotAttempt=gameMethods.getShot(offenseTeamFiveOnFloor[ballHandler][6]*.41111111)
            if possibleShotAttempt:
               dunk=0
               possibleDunk=gameMethods.getDunk(offenseTeamFiveOnFloor[ballHandler][5][2])
               if possibleDunk:
                  dunk=1
               possibleBlock=gameMethods.getBlock(defenseTeamFiveOnFloor[primaryDefender][5][9],passLocation,dunk)
               if possibleBlock:
                   gameMethods.parseBlockStats(countingStats,defenseIndex,primaryDefender,benchStatCompiler)
               possibleFoul=gameMethods.getFoul(defenseTeamFiveOnFloor[primaryDefender][5][12],passLocation)
               amountOfFreeThrows=2
               if passLocation==0:
                   amountOfFreeThrows=3
               offensiveRebound=None
               import copy
               oldNumberOfPoints=copy.deepcopy(countingStats[offenseTeamCountingStatsIndex][16]) 
               gameMethods.parseShootingStats(countingStats,offenseTeamCountingStatsIndex-1,defenseTeamCountingStatsIndex-1,ballHandler,passBonus,passLocation,dribblingBonus,possibleDefensiveRatings,possibleOffensiveRatings,possibleBlock,dunk,madeShot,offenseTeamCountingStatsIndex,defenseTeamCountingStatsIndex,benchStatCompiler)
               newNumberOfPoints=countingStats[offenseTeamCountingStatsIndex][16]
               madeShot=gameMethods.gameBooleans(oldNumberOfPoints,newNumberOfPoints)
               if madeShot:
                   amountOfFreeThrows=1  
               if possibleFoul:
                   gameMethods.parseFoulShots(countingStats,amountOfFreeThrows,offenseTeamFiveOnFloor[ballHandler][5][12],ballHandler,offenseIndex,offenseTeamCountingStatsIndex,defenseIndex,defenseTeamCountingStatsIndex,primaryDefender,benchStatCompiler)
                   break
               if madeShot:
                   break
               else:
                   oldOffensiveReboundStat=copy.deepcopy(countingStats[offenseTeamCountingStatsIndex][5])
                   gameMethods.parseRebound(offensiveRebound,countingStats,offenseTeamFiveOnFloor,defenseTeamFiveOnFloor,offenseIndex,defenseIndex,offenseTeamCountingStatsIndex,defenseTeamCountingStatsIndex,primaryDefender,benchStatCompiler)
                   newOffensiveReboundStat=countingStats[offenseTeamCountingStatsIndex][5]
                   offensiveRebound=gameMethods.gameBooleans(oldOffensiveReboundStat,newOffensiveReboundStat)
                   if offensiveRebound==True:
                       shotClock=14
                       continue
                   else:
                       break
            passLocation=gameMethods.getPassLocation(teamShotTendency)
            countingStats[offenseIndex][ballHandler+benchStatCompiler][5][0]=countingStats[offenseIndex][ballHandler][5][0]+1
            countingStats[offenseIndex+1][0]=countingStats[offenseIndex+1][0]+1
        gameMethods.parseMinutesAndPossessions(countingStats,shotClock,fiveOnFloorIndexes)        
    def parseShootingStats(countingStats,offenseIndex,defenseIndex,ballHandler, passBonus,passLocation,dribblingBonus,possibleDefensiveRatings,possibleOffensiveRatings,possibleBlock,dunk,madeShot,offenseTeamCountingStatsIndex,defenseTeamCountingStatsIndex,benchStatCompiler):
        newShotInformation=gameMethods.getShotAttempt(passBonus,dribblingBonus,possibleDefensiveRatings,possibleOffensiveRatings,passLocation,dunk,possibleBlock)
        countingStats[offenseIndex][ballHandler+benchStatCompiler][5][18]=countingStats[offenseIndex][ballHandler+benchStatCompiler][5][18]+newShotInformation[3]
        countingStats[offenseIndex][ballHandler+benchStatCompiler][5][9+2*passLocation]=countingStats[offenseIndex][ballHandler+benchStatCompiler][5][9+2*passLocation]+newShotInformation[3]
        countingStats[offenseIndex][ballHandler+benchStatCompiler][5][19]=countingStats[offenseIndex][ballHandler+benchStatCompiler][5][19]+newShotInformation[2]
        countingStats[offenseIndex][ballHandler+benchStatCompiler][5][16]=countingStats[offenseIndex][ballHandler+benchStatCompiler][5][16]+newShotInformation[0]
        countingStats[offenseIndex][ballHandler+benchStatCompiler][5][1]=countingStats[offenseIndex][ballHandler+benchStatCompiler][5][1]+newShotInformation[1]
        countingStats[offenseIndex][ballHandler+benchStatCompiler][5][8+2*passLocation]=countingStats[offenseIndex][ballHandler+benchStatCompiler][5][8+2*passLocation]+newShotInformation[2]
        countingStats[offenseTeamCountingStatsIndex][18]=countingStats[offenseTeamCountingStatsIndex][18]+newShotInformation[3]
        countingStats[offenseTeamCountingStatsIndex][9+2*passLocation]=countingStats[offenseTeamCountingStatsIndex][9+2*passLocation]+newShotInformation[3]
        countingStats[offenseTeamCountingStatsIndex][19]=countingStats[offenseTeamCountingStatsIndex][19]+newShotInformation[2]
        countingStats[offenseTeamCountingStatsIndex][16]=countingStats[offenseTeamCountingStatsIndex][16]+newShotInformation[0]
        countingStats[offenseTeamCountingStatsIndex][1]=countingStats[offenseTeamCountingStatsIndex][1]+newShotInformation[1]
        countingStats[offenseTeamCountingStatsIndex][8+2*passLocation]=countingStats[offenseTeamCountingStatsIndex][8+2*passLocation]+newShotInformation[2]
        madeshot=madeShot
        if int(newShotInformation[0])>int(1):
            madeShot=True      
    def gameBooleans(oldStat,newStat):
        if newStat>oldStat:
            return True
        return False
    def moreCustomizableDiceRoll(lowerBound,upperBound):
        import random as r
        return r.randint(lowerBound,upperBound)
    def parseMinutesAndPossessions(countingStats, shotClock,fiveOnFloorIndexes):
        if shotClock<0:
            shotClock=0 
        secondsPlayed= abs(shotClock-24)
        defenseSwitcher=0
        fiveOnFloor=0
        for i in range(10):
            if i >4:
                defenseSwitcher=2
                fiveOnFloor=5       
            countingStats[0+defenseSwitcher][fiveOnFloorIndexes[i-1-fiveOnFloor]][5][24]=countingStats[0+defenseSwitcher][fiveOnFloorIndexes[i-1-fiveOnFloor]][5][24]+secondsPlayed/60
            countingStats[0+defenseSwitcher][fiveOnFloorIndexes[i-1-fiveOnFloor]][5][17]=countingStats[0+defenseSwitcher][fiveOnFloorIndexes[i-1-fiveOnFloor]][5][17]+1
            countingStats[0+defenseSwitcher+1][25]=countingStats[0+defenseSwitcher+1][25]+secondsPlayed/60
            countingStats[0+defenseSwitcher+1][17]=countingStats[0+defenseSwitcher+1][17]+1
    def parseRebound(offensiveRebound,countingStats,offenseTeamFiveOnFloor,defenseTeamFiveOnFloor,offenseIndex,defenseIndex,offenseTeamCountingStatsIndex,defenseTeamCountingStatsIndex,primaryDefender,benchStatCompiler):
        rebound=gameMethods.getRebound(offenseTeamFiveOnFloor,defenseTeamFiveOnFloor,offenseIndex,defenseIndex)
        countingStats[offenseIndex][rebound[1]+benchStatCompiler][5][21]=countingStats[offenseIndex][rebound[1]+benchStatCompiler][5][21]+1
        countingStats[offenseIndex][rebound[1]+benchStatCompiler][5][23]=countingStats[offenseIndex][rebound[1]+benchStatCompiler][5][23]+1
        countingStats[defenseIndex][rebound[2]+benchStatCompiler][5][22]=countingStats[defenseIndex][rebound[2]+benchStatCompiler][5][22]+1
        countingStats[defenseIndex][rebound[2]+benchStatCompiler][5][23]=countingStats[defenseIndex][rebound[2]+benchStatCompiler][5][23]+1
        countingStats[offenseTeamCountingStatsIndex][21]=countingStats[offenseTeamCountingStatsIndex][21]+1
        countingStats[offenseTeamCountingStatsIndex][23]=countingStats[offenseTeamCountingStatsIndex][23]+1
        countingStats[defenseTeamCountingStatsIndex][22]=countingStats[defenseTeamCountingStatsIndex][22]+1
        countingStats[defenseTeamCountingStatsIndex][23]=countingStats[defenseTeamCountingStatsIndex][22]+1
        if rebound[0]==True:
            countingStats[offenseIndex][rebound[1]+benchStatCompiler][5][5]=countingStats[offenseIndex][rebound[1]+benchStatCompiler][5][5]+1
            countingStats[offenseIndex][rebound[1]+benchStatCompiler][5][7]=countingStats[offenseIndex][rebound[1]+benchStatCompiler][5][7]+1
            countingStats[offenseTeamCountingStatsIndex][7]=countingStats[offenseTeamCountingStatsIndex][7]+1
            countingStats[offenseTeamCountingStatsIndex][5]=countingStats[offenseTeamCountingStatsIndex][5]+1
        else:
            countingStats[defenseIndex][rebound[2]+benchStatCompiler][5][6]=countingStats[defenseIndex][rebound[2]+benchStatCompiler][5][6]+1
            countingStats[defenseIndex][rebound[2]+benchStatCompiler][5][7]=countingStats[defenseIndex][rebound[2]+benchStatCompiler][5][7]+1
            countingStats[defenseTeamCountingStatsIndex][6]=countingStats[defenseTeamCountingStatsIndex][6]+1
            countingStats[defenseTeamCountingStatsIndex][7]=countingStats[defenseTeamCountingStatsIndex][7]+1
    def getRebound(offenseTeamFiveOnFloor,defenseTeamFiveOnFloor,offenseIndex,defenseIndex):
        sortedOffensiveReboundOverallList=gameMethods.getIterableStatOveralls(offenseTeamFiveOnFloor,6)
        sortedDefenseReboundOverallList=gameMethods.getIterableStatOveralls(defenseTeamFiveOnFloor,7)
        offenseReboundRoleHeirarchy=gameMethods.getTeamRoleHeirarchies(sortedOffensiveReboundOverallList)
        defenseReboundRoleHeirachy=gameMethods.getTeamRoleHeirarchies(sortedDefenseReboundOverallList)
        prospectiveOffensiveRebounderIndex=gameMethods.getPrimary(offenseReboundRoleHeirarchy)
        prospectiveDefensiveRebounderIndex=gameMethods.getPrimary(defenseReboundRoleHeirachy)
        offensiveReboundRating=offenseTeamFiveOnFloor[prospectiveOffensiveRebounderIndex][5][6]
        defensiveReboundRating=defenseTeamFiveOnFloor[prospectiveDefensiveRebounderIndex][5][7]
        differenceInReboundingStats=offensiveReboundRating-defensiveReboundRating
        offensiveReboundBonus=differenceInReboundingStats/2
        chanceOfOffensiveRebound=27+offensiveReboundBonus
        if chanceOfOffensiveRebound>gameMethods.diceRoll(100):
            return [True,prospectiveOffensiveRebounderIndex,prospectiveDefensiveRebounderIndex]
        return [False,prospectiveOffensiveRebounderIndex,prospectiveDefensiveRebounderIndex]
    def parseFoulShots(countingStats,amountOfFreeThrows,playerFreeThrowRating,ballHandler,offenseIndex,offenseTeamCountingStats,defenseIndex,defenseTeamCountingStats,primaryDefender,benchStatCompiler):
        foulShotInformation=gameMethods.getFreeThrow(playerFreeThrowRating,amountOfFreeThrows)
        for foulCounter in range(len(foulShotInformation)):
            countingStats[defenseIndex][primaryDefender+benchStatCompiler][5][20]=countingStats[defenseIndex][primaryDefender][5][20]+1
            countingStats[defenseTeamCountingStats][20]=countingStats[defenseTeamCountingStats][20]+1
            countingStats[offenseTeamCountingStats][14]=countingStats[offenseTeamCountingStats][14]+foulShotInformation[foulCounter]
            countingStats[offenseTeamCountingStats][15]=countingStats[offenseTeamCountingStats][15]+1
            countingStats[offenseTeamCountingStats][16]=countingStats[offenseTeamCountingStats][16]+foulShotInformation[foulCounter]
            countingStats[offenseIndex][ballHandler+benchStatCompiler][5][14]=countingStats[offenseIndex][ballHandler+benchStatCompiler][5][14]+foulShotInformation[foulCounter]
            countingStats[offenseIndex][ballHandler+benchStatCompiler][5][15]=countingStats[offenseIndex][ballHandler+benchStatCompiler][5][15]+1
            countingStats[offenseIndex][ballHandler+benchStatCompiler][5][16]=countingStats[offenseIndex][ballHandler+benchStatCompiler][5][16]+foulShotInformation[foulCounter]
    def getFoul(playerIQ,passLocation):
        if passLocation==0:
            locationBonus=1
        elif passLocation==1:
            locationBonus=7
        else: locationBonus=15
        probabilityOfFoul=(70/playerIQ)*locationBonus
        if probabilityOfFoul>gameMethods.diceRoll(100):
            return True
        return False
    def getDunk(dunkRating):
        probabilityOfDunk=(dunkRating/70)*5
        if probabilityOfDunk>gameMethods.diceRoll(100):
            return True
        return False
    def getSubstitution(team, substitutedPlayersIndex):
        newFiveOnFloor=[]
        for i in range(5):
            newFiveOnFloor.append(team[substitutedPlayersIndex[i-1]])
        return newFiveOnFloor
    def getTurnover(stealRating,passingRating,base): 
        probabilityOfTurnover=base+(passingRating/2)
        turnoverChecker=gameMethods.diceRoll(1000)
        turnover=0
        steal=0
        if turnoverChecker<probabilityOfTurnover:
            turnover=1
            probabilityOfSteal=stealRating/2.5
            if probabilityOfSteal>gameMethods.diceRoll(100):
                steal = 1
        else: 
            turnover=0
            steal = 0
        return [steal, turnover]
    def parseTurnoverStats(offenseFiveOnFloor, defenseFiveOnFloor, countingStats,base,defenseIndex, offenseIndex, ballHandler, primaryDefender, benchStatCompiler):
        turnover=gameMethods.getTurnover(defenseFiveOnFloor[primaryDefender][5][9],offenseFiveOnFloor[ballHandler][5][1],base)
        countingStats[offenseIndex][ballHandler+benchStatCompiler][5][3]=countingStats[offenseIndex][ballHandler+benchStatCompiler][5][3]+turnover[0]
        countingStats[defenseIndex][primaryDefender+benchStatCompiler][5][4]=countingStats[defenseIndex][primaryDefender+benchStatCompiler][5][4]+turnover[1]
        countingStats[offenseIndex+1][3]=countingStats[offenseIndex+1][3]+turnover[0]
        countingStats[defenseIndex+1][4]=countingStats[defenseIndex+1][4]+turnover[1]     
leagueFrame = playergenerator.leagueInitialization()
s=playergenerator.leagueInitialization()
gameFrame=gameMethods.getgameFrame(s[0][1][1][3],s[0][1][1][2])
#print(len(s[0][1][1][3]))
sortedGameFrame=gameMethods.sortPlayers(gameFrame)
homeTeam=sortedGameFrame[0]
awayTeam=sortedGameFrame[1]
homeclearedPlayerAttributes=gameMethods.clearPlayerAttributes(homeTeam)
awayClearedPlayerAttributes=gameMethods.clearPlayerAttributes(awayTeam)
homeTeam=gameMethods.setPlayerStats(homeclearedPlayerAttributes,20)
awayTeam=gameMethods.setPlayerStats(awayClearedPlayerAttributes,20)
fiveOnFloor=gameMethods.getFiveOnFloor([homeTeam,awayTeam])
homeTeamFiveOnFloor=fiveOnFloor[0]
awayTeamFiveOnFloor=fiveOnFloor[1]
aggregatedOveralls=[[homeTeamFiveOnFloor],[awayTeamFiveOnFloor]]
countingStats=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[homeTeamFiveOnFloor],[awayTeamFiveOnFloor]]
#print(gameMethods.getPossession(countingStats,0,homeTeamFiveOnFloor,awayTeamFiveOnFloor,1,2))
#gameMethods.parseShootingStats(countingStats,1,2,2,3,0,3,[76,56,43],[10000,1394,23939])
#print(countingStats)
#print(gameMethods.getOveralls([[homeTeamFiveOnFloor],[awayTeamFiveOnFloor]]))
#for i in range (100):
    #gameMethods.parseShootingStats(countingStats,1,2,2,3,0,3,[76,56,93],[100,90,67])

def getThreePointerPercentage(passBonus,dribblingBonus,offenseShotRating,defenseShotRating):
    totalBonus=passBonus+dribblingBonus
    defenseBonus=(offenseShotRating-defenseShotRating)/8
    attemptedShot=(offenseShotRating/2.25)+totalBonus+defenseBonus
    return attemptedShot
class FrontEndMethods():
    def GetUserTeam(leagueFrame,conferenceIndex,divisionIndex,userTeamIndex):
        return leagueFrame[conferenceIndex][divisionIndex][1][userTeamIndex]


            
#print(countingStats)
#print(gameMethods.getSubstitution([y[0][0],y[0][1],y[0][2],y[0][3],y[0][4]],[y[0][5],y[0][6],y[0][7],y[0][8],y[0][9]]))
#print(gameMethods.gethomeTeamStats(y))
#for i in rane(0,34):
   #print(gameMethods.getPassLocation([34,87,100]))
#for i in range(1000):
   # passBonus=r.randint(-5,5)
    #dribblingBonus=r.randint(-5,5)
   # offenseShotRating=r.randint(50,95)
   # defenseShotRating=r.randint(50,95)
    #threePointPercentage=getThreePointerPercentage(passBonus,dribblingBonus,offenseShotRating,defenseShotRating)
   # newList=[threePointPercentage,passBonus,dribblingBonus,offenseShotRating,defenseShotRating]
   #threePointerData.append(newList)
#df = pd.DataFrame (threePointerData, columns = ['chance_of_make','pass_bonus','dribbling_bonus','offense_rating','defense_rating'])
#print (df)
#import numpy as np
#path=r'C:\Users\nwiss\miscealinous python projects\basketball_app/df.csv'
#with open(path,'a') as f:
   # df_string=df.to_string(header=False,index=False)
   # f.write(df_string)
#print(gameMethods.sortPlayers(gameMethods.getgameFrame(leagueFrame[0][1][1][3],leagueFrame[0][1][1][2])))
#for i in range(0,30):
#print(gameMethods.parseIntoIterablePercentage([34,26,15,13,12]))  
   # print(gameMethods.game(leagueFrame[0][1][1][3],leagueFrame[0][1][1][2]))
#print(playergenerator.simplifyLeagueFrame(playergenerator.leagueInitialization())[29])
class statKeeping():
    def getUserTeam(teamNumber):
        import basketball
        newLeague=basketball.playergenerator.leagueInitialization()
        conferenceIndex=0
        divisionIndex=0
        teamIndex=0
        for i in range (0,teamNumber):
            teamIndex=teamIndex+1
            if teamIndex>4:
               teamIndex=0
               divisionIndex=divisionIndex+1
               if divisionIndex>3:
                   divisionIndex=1
                   conferenceIndex=conferenceIndex+1
                   if conferenceIndex>1:
                       break
        userTeam=newLeague[conferenceIndex][divisionIndex][1][teamIndex]
        return userTeam
    import copy
    import pandas as pd
    import random as r
    import basketball
    leagueFrame = basketball.playergenerator.leagueInitialization()
    def getListOfTeams(self):
            import basketball
            newLeague=basketball.playergenerator.leagueInitialization()
            conferenceIndex=0
            divisionIndex=1
            teamIndex=0
            possibleUserTeams=[]
            for i in range (0,30):
                possibleUserTeams.append(newLeague[conferenceIndex][divisionIndex][1][teamIndex])
                teamIndex=teamIndex+1
                if teamIndex>4:
                    teamIndex=0
                divisionIndex=divisionIndex+1
                if divisionIndex>3:
                    divisionIndex=1
                    conferenceIndex=conferenceIndex+1
                    if conferenceIndex>1:
                        break     
            return possibleUserTeams
    #print(homeTeamFiveOnFloor)

    #for i in range(100):print(basketball.gameMethods.getRebound(newhomeTeam,newAwayTeam,4,3))
    #print(newhomeTeam)
    #print(newAwayTeam)
    timePerPass=10
    #print(homeTeamFiveOnFloor)
    #print(basketball.gameMethods.getIterableStatOveralls(homeTeamFiveOnFloor,0)
    #for i in range(100):
        
    # basketball.gameMethods.getPossession(countingStats,3,newAwayTeam,newhomeTeam,0,2,1,copy.deepcopy(timePerPass))
    # timePerPass=
    # basketball.gameMethods.getPossession(countingStats,3,newAwayTeam,newhomeTeam,2,0,1,timePerPass)
    # timePerPass=timePerPass
        #print('gkgfktrm: ',timePerPass)#fix problem with time not going down
        #if timePerPass<1:
            # break

    def addAllCountingStats(countingStatOne,countingStatTwo,teamIndex):
        playerIndex=0
        statIndex=0
        for i in range(2):
            for i in range(375):
                countingStatTwo[0][teamIndex][playerIndex][5][statIndex]=countingStatTwo[0][teamIndex][playerIndex][5][statIndex]+countingStatOne[0][teamIndex][playerIndex][5][statIndex]
                statIndex=statIndex+1 
            if statIndex>24:
                playerIndex=playerIndex+1
                statIndex=0
                if playerIndex>14:
                    break
            for i in range(25):
                countingStatTwo[1][statIndex]=countingStatOne[1][statIndex]+countingStatTwo[1][statIndex]
        return countingStatTwo
    def dataCollection(gameOne,gameTwo):
        for j in range(480):
            for i in range(25):
                gameOne[j-1][i+7]=gameOne[j-1][i+7]+gameTwo[j-1][i+7]       
    def listPlayerRatings(listIndex, team):
        from operator import itemgetter
        import copy
        if listIndex==0:
            team.pop(0)
        team.sort(key = itemgetter(6),reverse = True)
        listedPlayerRatings=[]
        team=copy.deepcopy(team)
        ratingIndex=0
        for i in range(13):
            listedPlayerRatings.append(team[listIndex][5][ratingIndex])
            ratingIndex= ratingIndex+1
        return listedPlayerRatings
    def getStatOveralls(listedPlayerOverall):
        sumOfOveralls=0
        for i in range(len(listedPlayerOverall)):
            sumOfOveralls=sumOfOveralls+listedPlayerOverall[i-1]
        averagedOverall=int(sumOfOveralls/len(listedPlayerOverall))
        return averagedOverall
    def elongateGameData(game,teamOne, teamTwo):
        game=list(game)
        statIndex=0
        playerIndex=0
        teamIndex=0
        homeTeamTotals=game.pop(1)
        awayTeamTotals=game.pop(2)
        totals=[]
        for i in range(2):
            for k in range(15):
                gameStats=[]
                for l in range(25):
                    gameStats.append(game[teamIndex][playerIndex][5][l])
                game[teamIndex][playerIndex].extend(gameStats)
                if i<1:
                    playerRatingsList=statKeeping.listPlayerRatings(playerIndex,teamOne)
                else: playerRatingsList=statKeeping.listPlayerRatings(playerIndex,teamTwo)
                game[teamIndex][playerIndex].extend(playerRatingsList)
                playerIndex=playerIndex+1 
                playerOverall=statKeeping.getStatOveralls(playerRatingsList)
                if i==0:
                    totals=homeTeamTotals
                else: totals= awayTeamTotals
                totals.append(playerOverall)   
            for h in range(7):
                totals.insert(h,"N/A")
            for j in range(15):
                del game[teamIndex][j-1][5] 
            playerIndex=0
            teamIndex=teamIndex+1
            del totals[47]
            del totals[46]
            del totals[31]
            totals=[totals]
            game.append(totals)     
        appendedGame=[item for sublist in game for item in sublist]
        return appendedGame
    def addLists(oldGame,newGame):
        oldGame.extend(newGame)
    def createDataFrameFromGame(game):
        import pandas as pd
        gameDataFrame=pd.DataFrame(game,columns=["Name","Height","Weight","Draft Position","Archetype","Overall","Player Index",
        "Passes","AST","Blk","STL","TO","ORB","DRB","TRB","3PM","3PA",
        "MRM","MRA","INM","INA","FTM","FTA","PTS","TOP","FGA","FGM","fouls","ORBA","DRBA","TRBA","secondsPlayed","dribbling","playmaking","dunk","inside shot","mid range","three pointer","offensive rebound","defensive rebound","steal rating","block rating","perimeter defense","inside defense","IQ"])
        return gameDataFrame
    def elongateAndExtend(oldGame,newGame,homeTeam,awayTeam):
        newGame=statKeeping.elongateGameData(newGame,homeTeam,awayTeam)
        statKeeping.addLists(oldGame,newGame)
    def everyonePlaysOneGame(league):
        import copy
        conferenceIndex=0
        divisionIndex=3
        teamIndex=1
        crossoverConferenceGame=gameMethods.game(copy.deepcopy(league[conferenceIndex][divisionIndex][1][teamIndex]),copy.deepcopy(league[conferenceIndex+1][divisionIndex][1][teamIndex]))
        crossoverConferenceGame=statKeeping.elongateGameData(crossoverConferenceGame,copy.deepcopy(league[conferenceIndex][divisionIndex][1][teamIndex]),copy.deepcopy(league[conferenceIndex+1][divisionIndex][1][teamIndex]))
        
        conferenceIndex=0
        divisionIndex=1
        for i in range(12):
            mainBlockOfGames=gameMethods.game(copy.deepcopy(league[conferenceIndex][divisionIndex][1][teamIndex]),copy.deepcopy(league[conferenceIndex][divisionIndex][1][teamIndex+1]))
            statKeeping.elongateAndExtend(crossoverConferenceGame,mainBlockOfGames,copy.deepcopy(league[conferenceIndex][divisionIndex][1][teamIndex]),copy.deepcopy(league[conferenceIndex][divisionIndex][1][teamIndex]))
            teamIndex=teamIndex+2
            
            if teamIndex>4:
                divisionIndex=divisionIndex+1
                teamIndex=1
                if divisionIndex>3:
                    conferenceIndex=conferenceIndex+1
                    divisionIndex=1
                    if conferenceIndex>1:
                        conferenceIndex=0
                        divisionIndex=1
                        teamIndex=4
                        break
        for i in range(2):
            interDivisionGames=gameMethods.game(copy.deepcopy(league[conferenceIndex][divisionIndex][1][teamIndex]),copy.deepcopy(league[conferenceIndex][divisionIndex+1][1][teamIndex]))
            statKeeping.elongateAndExtend(crossoverConferenceGame,interDivisionGames,copy.deepcopy(league[conferenceIndex][divisionIndex][1][teamIndex]),copy.deepcopy(league[conferenceIndex][divisionIndex+1][1][teamIndex]))
            conferenceIndex=conferenceIndex+1
        return crossoverConferenceGame
    def toCSV(df,filename):
        import pandas as pd
        df.to_csv(filename)
    def season(leagueFrame):
        game=statKeeping.everyonePlaysOneGame(leagueFrame)
        for i in range(82):
            games = statKeeping.everyonePlaysOneGame(leagueFrame)
            statKeeping.dataCollection(game,games)
        statKeeping.getAverages(82,game)
        game=statKeeping.createDataFrameFromGame(game)
    def getAverages(numberOfGames,list):
        for i in range(480):
            for j in range(25):
                list[i-1][j+7]=round(list[i-1][j+7]/numberOfGames,1)
print(len(playergenerator.leagueInitialization()[0][1][1][0]),playergenerator.leagueInitialization()[0][1][1][0][0])