# Jumper Design Document

## Description

Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.

Jumper is played according to the following rules.

* The puzzle is a secret word randomly chosen from a list.
* The player guesses a letter in the puzzle.
* If the guess is correct, the letter is revealed.
* If the guess is incorrect, a line is cut on the player's parachute.
* If the puzzle is solved the game is over.
* If the player has no more parachute the game is over.

## Classes

- `Director()`
- `Jumper()`
- `Word()`
- `Console()`
- `Parachute()`

**Description**

* Director
The director class administers the gameplay and delegates the turns the player receives. The director inititates the console to display out to the player. The director also initiates the jumper, where differnt phases of the jumper will be displayed via code logic inside the jumper class and a display housed in a parachute class. The director also distrubutes a word from a program that generates a random word from a list.

* Console
The console gets text or numerical input and displays them out to the terminal. The three main functions, are to read input from the user, read each letter of the chosen word, and displays the text.

* Jumper
The jumper class chooses which phase of the jumper themselves gets displayed.
If the player inputs a wrong answer, they lose that round and the next phase of the jumper initiates with them losing a string to their parachute.

* Word
Houses a list of words that will be randomly selected.

* Parachute
Houses our programs icons that will display the different phases of the jumper.


## Assets

### Wordlist

```
import random
list = ["energetic", "teaching", "motionless", "skinny", "cool", "wise", "condition", "axiom",
"difficult", "bagpipes", "rural", "banjo", "remember, "beekeeper", "cumbersome", "blitz", "blizzard", "fruit",
"bookworm", "oven", "boxful", "finger", "buffalo", "trot", "past", "reign", "buzzing",
"fax", "argument", "broad", "flight", "croquet", "crypt", "flavor", "cycle", "political",
"soak", "disavow", "divide", "duplex", "dwarves", "sister", "equip", "allow", "kind",
"instrument", "plane", "jumpy", "economic", "pleasure", "madly", "good", "stir", "night", "relax",
"reflect"]
words = random.choice(list).upper()
```

### Icons

```
 ___
/   \
-----
\   /
 \ /
  o
 /|\
 / \

^^^^^^^
```

```

/   \
-----
\   /
 \ /
  o
 /|\
 / \

^^^^^^^
```

```


-----
\   /
 \ /
  o
 /|\
 / \

^^^^^^^
```

```



\   /
 \ /
  o
 /|\
 / \

^^^^^^^
```

```




 \ /
  o
 /|\
 / \

^^^^^^^
```

```





  x
 /|\
 / \

^^^^^^^
```
