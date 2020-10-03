#### A Simple 'SuperHero' Database

---

This program takes in a *'.txt'*  file as a command line parameter, which then serves as a local database.
This particular implementation represents a database of superheroes, however the script can be easily adjusted to process a different set (or amount) of categories. 

---

> ###### To begin,
>
> 1. Download all files including _HeroDB.txt_
> 2. Run: _python3 superhero.py HeroDB.txt_  (can be replaced with your own DB)

> ###### Here, each hero has a total fo 6 attributes:
>
> 1. Name
> 2. location
> 3. income
> 4. powers
> 5. contact
> 6. situations (emergencies)

> ###### The 4 functionalities are:
>
> 1. Generate HeroReport: returns each Hero in the database along with their atts.
> 2. Add Hero: Add a hero (item) to the database along with all attributes 
> 3. Get Hero Info: Returns the attributes of the specified hero
> 4. Find Who To Call: Returns all heroes and their respective contact methods who are equipped to deal with a situation (e.g. Fire, Alien Invasion...)