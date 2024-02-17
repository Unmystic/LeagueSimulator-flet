# LeagueSimulator-flet
Flet adaptation of  app League Simulator Gui(Qt6 version) 

Using predetermined library of team names (like Ravens, Gorillas, Tornadoes , etc.) and descriptors (Amazing, Marvelous, Glorious, etc.) create a simulation of league tournament. The rules for the tournament are simple:

- Every team plays with others twice: home and away game. There is a minimal advantage for home team.

- 3 points for the victory , 1 point for the draw.

- Currenly, only points total and goal difference sort positions of teams in league table.

- There is option to simulate league round by round.

- No individual statistics , team ratings(attackRating, defenceRating, teamCohesion) generated as a whole.

You also able to add your own team and choose its playstyle. Playstyle affects balance of your team - improves/decreases the chance of stonger offensive/defensive sides. Current match engines takes your attackRating and opponents defenceRating to detrmine the overall goal scoring probability. The third parameter - teamCohesion, also randomly generated and improves slightly with each played game.

You need only flet library to run code. To install , use `pip install flet` command . Distribution packages right now not available, but you can use flet docs to create them yourself.
