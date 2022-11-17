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

*The purpose of the game, Jumper, is to guess letters for every turn . Similar to the game, Hangman, if the chosen letter is not in the secret word, the parachute will lose a line. The player continues to guess until either the puzzle is solved or the jumper falls to his gruesome death.*

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
