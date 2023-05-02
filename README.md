# basketball
This includes the front end and back end for a basketball general manager simulator as well as unit tests for both.
It is a still an in progress program with lots of bugs and as a new programmer I would welcome any and all constructive criticism.
# Basketball file- description of each methods purpose and implementation 
  # Player Generation class
      **Player Constructor-**
				The constructor for all players in the team. When called it defines each players attributes including name, height, weight, draft position, archetype, ratings and overall.
			This is done through the methods specified below in the player generation class.
 		  **Parse Player Height-**
				This method is used for getting realistic player height. It takes one integer that is the players height in inches. It then uses the math.trunc function to get the rounded quotient of the player height divided by 12 and stores it in the playerHeightFeet variable. The next line gets the modulo of that same function and stores it in the playerHeightInches variable. It then returns a tuple (playerHeightFeet, 'foot', playerHeightInches).
			**Archetype Selector-**
					This method is used to determine the archetype for a player of which their are ten choices. Instead of the normal positions in basketball pg, sg, sf, etc, this game uses archetypes to give the user increased flexibility in terms of selecting which players are in the court. This also allows for more streamlined team building as the user will not be hindered by two highly rated players that play the same position. Each archetype has different strengths and weaknesses. The exact specifications will not be revealed to the user. As for the actual method it takes in one parameter that contains a integer from 0-9. Within the method a two dimensional array with 10 columns and 13 rows. The columns specify a list of archetype stat bonuses while the rows specify each stat bonuses within the chosen archypte. It returns a single dimensional list with 13 elements. This list comes from the afore-mentioned two dimensional list with the index being the only parameter passed through the method. 
				
				
