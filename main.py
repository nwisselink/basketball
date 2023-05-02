import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager as sm, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from functools import partial
import basketball
class SettingsScreen(Screen):
    pass
class MenuScreen(Screen):
    pass

      
class ScreenManager(sm):
    pass 
class Account(Screen):
    pass
class About(Screen):
    pass
class Privacy(Screen):
    pass
class NewGameScreen(Screen):
    pass
class SelectTeamScreen(Screen):
    pass
class EmbedSelectTeamScreen(Screen):
    def __init__(self,**kwargs):
        super(EmbedSelectTeamScreen,self).__init__(**kwargs)
        self.newLeague=basketball.playergenerator.leagueInitialization()
        newSimplifiedLeague=basketball.playergenerator.simplifyLeagueFrame(self.newLeague)
        teamIndex=0
        positionChanger=0
        self.listOfTeamNamesIndexes=[]
        self.listOfTeams=self.getListOfTeams(self.newLeague)
        layout = BoxLayout(orientation='vertical')
        self.teamIndex=6
        self.userTeam=3
        for i in range(30):
            button = Button(text=str(self.listOfTeams[i][0]))
            button.bind(on_press=lambda instance, index=i: self.getUserTeam(index))
            layout.add_widget(button)
        self.add_widget(layout)
    def getUserTeam(self,index):
        self.my_variable = self.listOfTeams[index]
        print(self.my_variable)
   # def getUserTeamIndex(self,buttonIndex,instance):
       # print(self.teamIndex)
    def getListOfTeams(self,newLeague):
        import basketball
        
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
class HomeScreen(Screen):
    def __init__(self,**kwargs):
        super(HomeScreen,self).__init__(**kwargs)
        self.team=[]
        screen_manager=ScreenManager()
        welcomeLabel=Label(text="Welcome to the Association",pos_hint={'center_x':.5,'center_y':.95},
        size_hint=(.6,8),color=(1,0,0))
        self.add_widget(welcomeLabel)
        
        self.financeInformation=["salary cap","Overall","Dead Money",2000000,5000000,0]
        financeLayout=GridLayout(cols=3, rows=2, size_hint=(.3,.1),pos_hint={"center_x":.5,"center_y":.8})
        for i in range(6):
            financeButtons=Button(text=str(self.financeInformation[i]))
            financeButtons.bind(on_press=self.change_screen_to_finance)
            financeLayout.add_widget(financeButtons)
        self.add_widget(financeLayout)
        screen_manager.add_widget(EmbedSelectTeamScreen(name='embed_select_team_screen')) 
        newTeam=Button(text="Next Game",size_hint=(.2,.2),pos_hint={'center_x':.5,'center_y':.5})
        self.add_widget(newTeam)
        newTeam.bind(on_press=self.change_screen_to_game)       
    def change_screen_to_game(self,instance):
        screen_manager=ScreenManager()
        screen_manager.add_widget(GameScreen(name="game_screen"))
        self.parent.current="game_screen"
    def change_screen_to_finance(self,instance):
        screen_manager=ScreenManager()
        screen_manager.add_widget(SalaryCapExplanationScreen(name="salary_cap_explanation_screen"))
        self.parent.current="salary_cap_explanation_screen"
class GameScreen(Screen):
    def __init__(self,**kwargs):
        super(GameScreen,self).__init__(**kwargs)
        import copy
        screen_manager=ScreenManager()
        screen_manager.add_widget(EmbedSelectTeamScreen(name="select_team_screen"))
        selectTeamScreen=screen_manager.get_screen("select_team_screen")
        league=copy.deepcopy(selectTeamScreen.newLeague)
        game=basketball.gameMethods.game(copy.deepcopy(league[0][1][1][3]),copy.deepcopy(league[0][1][1][2]))
        awayTeamStatSummarizationlayout=BoxLayout(orientation="vertical")
        
            
        homeTeamStatSummarizationLayout=BoxLayout(orientation="vertical")

        gameSummarizationLayout=BoxLayout()
        awayTeam=Button(text=league[0][1][1][3][0], pos_hint={"center_x":.25,"center_y":.95},size_hint=(.1,.2),background_color=(0,1,0,1),color=(1,0,0,1))
        homeTeam=Button(text=league[0][1][1][2][0], pos_hint={"center_x":.75,"center_y":.95},size_hint=(.1,.2),color=(0,1,0,1),background_color=(1,0,0,1))
        gameSummarizationLayout.add_widget(homeTeam)
        gameSummarizationLayout.add_widget(awayTeam)
        self.add_widget(gameSummarizationLayout)
        advancedStatsLayout=BoxLayout()
        recentPlaysLayout=ScrollView()
        teamLayout=BoxLayout()
class TeamScreen(Screen):
    def __init__(self,**kwargs):
        super(TeamScreen,self).__init__(**kwargs)
        backButton=Button(text="back")
        self.add_widget(backButton) 
        backButton.bind(on_press=self.changeScreen)
    def changeScreen(self,instance):
        Screen_manager=ScreenManager()
        Screen_manager.add_widget(GameScreen(name='game_screen'))
        self.parent.current='game_screen'
class LeagueScreen(Screen):
    def __init__(self,**kwargs):
        super(LeagueScreen,self).__init__(**kwargs)
class FinanceScreen(Screen):
    def __init__(self,**kwargs):
        super(FinanceScreen,self).__init__(**kwargs)
class SalaryCapExplanationScreen(Screen):
    def __init__(self,**kwargs):
        super(SalaryCapExplanationScreen, self).__init__(**kwargs)
        screen_manager=ScreenManager()
        financeWidget=screen_manager.add_widget(HomeScreen)
        
class StatsScreen(Screen):
    def __init__(self,**kwargs):
        super(StatsScreen,self).__init__(**kwargs)
class LeagueStandingsScreen(Screen):
    def __init__(self,**kwargs):
        super(LeagueStandingsScreen,self).__init__(**kwargs)
class PlayerStatsScreen(Screen):
    def __init__(self,**kwargs):
        super(PlayerStatsScreen,self).__init__(**kwargs)
class TeamStatsScreen(Screen):
    def __init__(self,**kwargs):
        super(TeamStatsScreen,self).__init__(**kwargs)
class BasketballApp(App):
    pass
       
BasketballApp().run()