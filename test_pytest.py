import basketball    # The code to test

import unittest

class helper_methods(unittest.TestCase):
    def test_diceroll(self):
       self.assertIn(basketball.gameMethods.diceRoll(100), range(101))
class player_generation(unittest.TestCase):

    def test_parse_player_height(self):
        seperatedString = list(basketball.playergenerator.parsePlayerHeight(80))
        self.assertEquals(len(seperatedString),3)
        self.assertEquals(seperatedString[0],6)
        self.assertEquals(seperatedString[1],"foot")
        self.assertEquals(seperatedString[2],8)
    def test_archetype_selector(self):
        self.assertEquals(len(basketball.playergenerator.archetypeSelector()),16)
        self.assertNotEquals(len(basketball.playergenerator.archetypeSelector()),range(15) and reversed(range(17)))
    def test_name_generator(self):
        seperatedNames=list(basketball.playergenerator.nameGenerator())
        self.assertEquals(len(seperatedNames),2)
        self.assertNotEquals(len(seperatedNames), range(1) and reversed(range(3)))
    def test_get_rating_names(self):
        ratingNames=basketball.playergenerator.getRatingNames()
        self.assertEquals(len(ratingNames),13)
        self.assertEquals(ratingNames[0],"dribbling")
        self.assertEquals(ratingNames[1],"playmaking")
        self.assertEquals(ratingNames[2],"dunking")
        self.assertEquals(ratingNames[3],"inside shot")
        self.assertEquals(ratingNames[4],"mid range shot")
        self.assertEquals(ratingNames[5], "three point shot")
        self.assertNotEquals(len(ratingNames),range(12) and reversed(range(14)))
    def test_player_generator(self):
        generatedPlayer=basketball.playergenerator.playerGenerator(basketball.playergenerator.archetypeSelector(),basketball.playergenerator.draftPositionAdjuster(basketball.gameMethods.diceRoll(60)))
        self.assertEqual(len(generatedPlayer),13)
        self.assertNotEqual(len(generatedPlayer),range(12) and reversed(range(14)))
        self.assertIn(generatedPlayer[6],range(40,110))
        self.assertNotEqual(generatedPlayer[9],range(40) and reversed(range(111)))
    def test_create_player(self):
        createdPlayer=basketball.playergenerator.createPlayer(False,0,3)
        self.assertEqual(len(createdPlayer),8)
        self.assertNotEqual(len(createdPlayer),range(6)and reversed(range(8)))
    def test_get_player_overall(self):
        import random as r
        listOfRatings=[r.randint(50,100),r.randint(50,100),r.randint(50,100),r.randint(50,100),r.randint(50,100),r.randint(50,100)
                       ,r.randint(50,100),r.randint(50,100),r.randint(50,100),r.randint(50,100),r.randint(50,100),r.randint(50,100),r.randint(50,100)]
        playerOverall=basketball.playergenerator.getOverall(listOfRatings)
        ratingsIndex=0
        sumOfListOfRatings=0
        for i in range(len(listOfRatings)):
            sumOfListOfRatings=listOfRatings[ratingsIndex]+sumOfListOfRatings
            ratingsIndex =ratingsIndex+1
        averageRating=round(sumOfListOfRatings/len(listOfRatings))
        self.assertEquals(playerOverall,averageRating)
    def test_draft_position_adjuster(self):
        adjustedRating=basketball.playergenerator.draftPositionAdjuster(1)
        self.assertIn(adjustedRating,range(11,23))
        self.assertNotEqual(adjustedRating,range(10)and reversed(range(24)))
        self.assertTrue(adjustedRating==int(adjustedRating))
    def test_abbreviated_player(self):
        newPlayer=basketball.playergenerator.createPlayer(False,0,3)
        abbreviatedPlayer=list(basketball.playergenerator.abbreviatedPlayer(newPlayer))
        self.assertEqual(len(abbreviatedPlayer),2)
        self.assertEqual(abbreviatedPlayer[0],(newPlayer[0]))
        self.assertEqual(abbreviatedPlayer[1],newPlayer[6])
    def test_league_initialization(self):
        newLeague=basketball.playergenerator.leagueInitialization()
        self.assertEqual(len(newLeague),2)
        self.assertEqual(len(newLeague[0]),4)
        self.assertEqual(len(newLeague[0][1]),2)
        self.assertEqual(len(newLeague[0][1][1]),5)
        self.assertEqual(len(newLeague[0][1][1][1]),16)
        self.assertEqual(len(newLeague[0][1][1][1][1]),8)
        self.assertEqual(len(newLeague[0][1][1][1][1][5]),13)
        self.assertEqual(newLeague[0][0],"Western Conference")
        self.assertEqual(newLeague[1][1][0],"Southeast Division")
        self.assertEqual(newLeague[1][1][1][1][0],"ORL")
    def test_draft(self):
        import random as r
        draftPositionTester=r.randint(0,59)
        newDraft=basketball.playergenerator.draft()
        self.assertEqual(len(newDraft),60)
        self.assertEqual(newDraft[0][3],1)
        self.assertEqual(newDraft[45][3],46)
        self.assertEqual(newDraft[draftPositionTester][3],draftPositionTester+1)
class game_methods(unittest.TestCase):
    def setUp(self) -> None:
        import copy
        self.newLeague=basketball.playergenerator.leagueInitialization()
       
        self.homeTeam=copy.deepcopy(self.newLeague[0][1][1][3])
        self.awayTeam=copy.deepcopy(self.newLeague[0][1][1][2])
        self.countingStats=[self.homeTeam,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                            ,self.awayTeam,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        self.gameFrame=copy.deepcopy(basketball.gameMethods.getgameFrame(self.newLeague[0][1][1][3],self.newLeague[0][1][1][2]))
        self.sortedGameFrame=copy.deepcopy(basketball.gameMethods.sortPlayers(self.gameFrame))
        self.fiveOnFloor=basketball.gameMethods.getFiveOnFloor(self.sortedGameFrame)
        self.homeTeamFiveOnFloor=self.fiveOnFloor[0]
        self.awayTeamFiveOnFloor=self.fiveOnFloor[1]
        self.listOfOveralls=copy.deepcopy(basketball.gameMethods.getOveralls(basketball.gameMethods.getFiveOnFloor(self.sortedGameFrame)))
        return super().setUp()
    def tearDown(self) -> None:
        self.newLeague=None
        self.gameFrame=None
        self.sortedGameFrame=None
        self.listOfOveralls=None
        return super().tearDown()
    def test_three_pointer(self):
        missedThreePointer=basketball.gameMethods.getThreePointer(-7,-8,10009,1,False)
        self.assertEquals(len(missedThreePointer),5)
        self.assertEquals(missedThreePointer[0],0)
        self.assertEquals(missedThreePointer[1],0)
        self.assertEquals(missedThreePointer[2],0)
        self.assertEquals(missedThreePointer[3],1)
        self.assertEquals(missedThreePointer[4],0)
        madeThreePointer=basketball.gameMethods.getThreePointer(8,7,1,11009,False)
        self.assertEquals(len(madeThreePointer),5)
        self.assertEquals(madeThreePointer[0],3)
        self.assertEquals(madeThreePointer[1],1)
        self.assertEquals(madeThreePointer[2],1)
        self.assertEquals(madeThreePointer[3],1)
        self.assertEquals(madeThreePointer[4],0)
    def test_mid_range(self):
        missedMidRange=basketball.gameMethods.getMidRange(-7,-8,9109,1,False)
        self.assertEquals(len(missedMidRange),5)
        self.assertEquals(missedMidRange[0],0)
        self.assertEquals(missedMidRange[1],0)
        self.assertEquals(missedMidRange[2],0)
        self.assertEquals(missedMidRange[3],1)
        self.assertEquals(missedMidRange[4],0)
        madeMidRange=basketball.gameMethods.getMidRange(8,7,1,1000,False)
        self.assertEquals(len(madeMidRange),5)
        self.assertEquals(madeMidRange[0],2)
        self.assertEquals(madeMidRange[1],1)
        self.assertEquals(madeMidRange[2],1)
        self.assertEquals(madeMidRange[3],1)
        self.assertEquals(madeMidRange[4],0)
    def test_inside_shot(self):
        missedInsideShot=basketball.gameMethods.getInsideShot(-7,-8,9109,1,0,False)
        self.assertEquals(len(missedInsideShot),5)
        self.assertEquals(missedInsideShot[0],0)
        self.assertEquals(missedInsideShot[1],0)
        self.assertEquals(missedInsideShot[2],0)
        self.assertEquals(missedInsideShot[3],1)
        self.assertEquals(missedInsideShot[4],0)
        madeInsideShot=basketball.gameMethods.getInsideShot(8,7,1,9109,1,False)
        self.assertEquals(len(madeInsideShot),5)
        self.assertEquals(madeInsideShot[0],2)
        self.assertEquals(madeInsideShot[1],1)
        self.assertEquals(madeInsideShot[2],1)
        self.assertEquals(madeInsideShot[3],1)
        self.assertEquals(madeInsideShot[4],1)
    def test_free_throw(self):
        self.assertIn(basketball.gameMethods.getFreeThrow(75,2)[0],range(0,2))
        self.assertEqual(basketball.gameMethods.getFreeThrow(0,1)[0],0)
    def test_shot_attempt(self):
        self.assertTrue(basketball.gameMethods.getShotAttempt(0,0,[70,70,70],[70,70,70],0,0,False)==[0,0,0,1,0] or [3,1,1,range(0,1),0])
        self.assertTrue(basketball.gameMethods.getShotAttempt(0,0,[70,70,70],[70,70,70],1,0,False)==[0,0,0,1,0] or [2,1,1,range(0,1),0])
        self.assertTrue(basketball.gameMethods.getShotAttempt(0,0,[70,70,70],[70,70,70],2,0,False)==[0,0,0,1,0] or [2,1,1,range(0,1),range(0,1)])
    def test_block_percentage(self):
        self.assertFalse(basketball.gameMethods.getBlockPecentage(80000,800))
        self.assertTrue(basketball.gameMethods.getBlockPecentage(0,1))
    def test_get_game_frame(self):
        self.assertEqual(basketball.gameMethods.getgameFrame(1,2),[1,2])
        self.assertNotEqual(basketball.gameMethods.getgameFrame(5,3),[4,5])
    def test_sort_players(self):
        self.assertTrue(self.sortedGameFrame[0][1][6]>=self.sortedGameFrame[0][3][6])
        self.assertTrue(self.sortedGameFrame[0][0][6]>=self.sortedGameFrame[0][9][6])
        self.assertFalse(self.sortedGameFrame[1][6][6]>self.sortedGameFrame[0][0][6])
        self.assertFalse(self.sortedGameFrame[1][14][6]>self.sortedGameFrame[0][3][6])
    def test_get_team_role_heirarchies(self):
        sortedStatOverall=basketball.gameMethods.getTeamRoleHeirarchies(self.listOfOveralls[0])
        self.assertEqual(len(sortedStatOverall),5)
        self.assertEqual(sum(sortedStatOverall),100)
        self.assertTrue(sortedStatOverall[0]>5)
    def test_player_shot_agressiveness(self):
        shotAggressiveness=basketball.gameMethods.getShotAggressiveness(self.listOfOveralls[1])
        self.assertEquals(len(shotAggressiveness),5)
    def test_team_shot_tendency(self):
        playerShotTendencies=basketball.gameMethods.getTeamShotTendency(1)
        self.assertEquals(len(playerShotTendencies),3)
        self.assertEquals(playerShotTendencies,[55,70,100])
    def test_get_pass_location(self):
        self.assertIn(basketball.gameMethods.getPassLocation([55,70,100]), range(3))
        self.assertFalse(basketball.gameMethods.getPassLocation([55,70,100])>2)
    def test_get_five_on_floor(self):
        self.assertEqual(len(basketball.gameMethods.getFiveOnFloor(self.gameFrame)),2)
        self.assertEqual(len(basketball.gameMethods.getFiveOnFloor(self.gameFrame)[0]),5)
        self.assertEqual(len(basketball.gameMethods.getFiveOnFloor(self.gameFrame)[0][0]),8)
    def test_get_pass(self):
        self.assertIn(basketball.gameMethods.getPass([23,27,20,20,10],basketball.gameMethods.diceRoll(2))[0],range(5))
        self.assertEqual(len(basketball.gameMethods.getPass([23,27,20,20,10],basketball.gameMethods.diceRoll(2))),2)
    def test_get_time_per_pass(self):
        self.assertIn(basketball.gameMethods.getTimePerPass(),range(1,6))
    def test_get_shot(self):
        self.assertTrue(basketball.gameMethods.getShot(101))
        self.assertFalse(basketball.gameMethods.getShot(-1))
    def test_ball_handling_bonus(self):
        self.assertIn(basketball.gameMethods.getBallHandlingBonus(6,self.gameFrame,1,4,2),range(-20,20))
    def test_get_playmaking_bonus(self):
        self.assertIn(basketball.gameMethods.getPlayMakingBonus(6,self.gameFrame,0,1,2),range(-20,20))
    def test_clear_player_attributes(self):
        clearedGameFrame = basketball.gameMethods.clearPlayerAttributes(self.gameFrame[0])
        self.assertEqual(len(clearedGameFrame[0][5]),0)
        self.assertEqual(len(clearedGameFrame[3][5]),0)
        self.assertIn(clearedGameFrame[0][6],range(40,110))
    def test_get_overalls(self):
        listOfOveralls=basketball.gameMethods.getOveralls(self.gameFrame)
        self.assertEqual(listOfOveralls,self.listOfOveralls)
    def test_set_player_stats(self):
        randomInteger=basketball.gameMethods.diceRoll(30)
        setPlayerStats=basketball.gameMethods.setPlayerStats(basketball.gameMethods.clearPlayerAttributes(self.gameFrame[0]),randomInteger)
        self.assertEqual(len(setPlayerStats[0][5]),randomInteger) 
        self.assertEqual(setPlayerStats[0][5][randomInteger-1],0)
    def test_parse_into_iterable_percentage(self):
        orderedIterablePercentageList=basketball.gameMethods.parseIntoIterablePercentage([34,26,15,13,12])
        self.assertEquals(len(orderedIterablePercentageList),5)
        self.assertEquals(sum(orderedIterablePercentageList),357)
        self.assertTrue(orderedIterablePercentageList[4]>=orderedIterablePercentageList[3]and orderedIterablePercentageList[2]>=orderedIterablePercentageList[0])
        self.assertFalse(orderedIterablePercentageList[1]>orderedIterablePercentageList[3]and orderedIterablePercentageList[0]>orderedIterablePercentageList[1])
    def test_get_primary(self):
        primaryDefender=basketball.gameMethods.getPrimary([30,23,19,14,12])
        self.assertIn(primaryDefender,range(0,5))
    def test_get_stat_overalls(self):
        fiveOnFloor=basketball.gameMethods.getFiveOnFloor(self.gameFrame)
        defenseOveralls=basketball.gameMethods.getStatOveralls(fiveOnFloor[0],6,5)
        self.assertEqual(len(defenseOveralls),5)   
        self.assertIn(defenseOveralls[0],range(40,110)) 
        self.assertIn(defenseOveralls[4],range(40,110))
    def test_game(self): 
        import copy
        game=basketball.gameMethods.game(copy.deepcopy(self.homeTeam),copy.deepcopy(self.awayTeam))
        self.assertEqual(len(game),4)
        self.assertFalse(len(game)!=4)
        self.assertTrue(len(game[0])==len(game[2]))
        self.assertTrue(len(game[1])==len(game[3]))
    def test_possession(self):
        possession=basketball.gameMethods.getPossession(self.countingStats,"shitandpiss",self.homeTeamFiveOnFloor,self.awayTeamFiveOnFloor,2,0,1,[24,1440,480],0,[0,1,2,3,4])
if __name__ == '__main__':
    unittest.main()
