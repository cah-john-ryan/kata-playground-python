# Bowling
Taken and modified from https://codingdojo.org/kata/Bowling/ & http://butunclebob.com/ArticleS.UncleBob.TheBowlingGameKata.

## Problem Description
Create a program, which, given a valid sequence of throws for one line of American Ten-Pin Bowling, produces the total score for the game. 

There should be 2 methods accessible from this program:
- throw(pins_knocked_down: int) -> void, which is called each time the player throws a ball. The argument is the number of pins knocked down.
- score() -> int, which is called only at the very end of the game. It returns the total score for that game.

Here are some things that the program will not do:
- We will not check for valid throws.
- We will not check for the correct number of throws and frames.
- We will not provide scores for intermediate frames.

Depending on the application, this might or might not be a valid way to define a complete story, but we do it here for purposes of keeping the kata light. I think you’ll see that improvements like those above would go in readily if they were needed in the real world.

We can briefly summarize the scoring for this form of bowling:
(When displaying scoring - “X” indicates a strike, “/” indicates a spare, “-” indicates a miss)
```                                                                              
 ┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────────┐
 │   1   │   2   │   3   │   4   │   5   │   6   │   7   │   8   │   9   │    10     │
 ├───┬───┼───┬───┼───┬───┼───┬───┼───┬───┼───┬───┼───┬───┼───┬───┼───┬───┼───┬───┬───┤
 │ 1 │ 4 │ 4 │ 5 │ 6 │ / │ 5 │ / │   │ X │ - │ 1 │ 7 │ / │ 6 │ / │   │ X │ 2 │ / │ 6 │
 │   └───┤   └───┤   └───┤   └───┤   └───┤   └───┤   └───┤   └───┤   └───┤   └───┴───┤
 │   5   │  14   │  29   │  49   │  60   │  61   │  77   │  97   │  117  │  133      │
 └───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────────┘                                                              
```
- Each game, or “line” of bowling, includes ten turns, or “frames” for the bowler.
- In each frame, the bowler gets up to two throws to knock down all the pins.
- If in two throws, he fails to knock them all down, his score for that frame is the total number of pins knocked down in his two throws.
- If in two throws he knocks them all down, this is called a “spare” and his score for the frame is ten plus the number of pins knocked down on his next throw (in his next frame).
- If on his first throw in the frame he knocks down all the pins, this is called a “strike”. The frame is complete, and his score for the frame is ten plus the simple total of the pins knocked down in his next two throws.
- If he gets a spare or strike in the last (tenth) frame, the bowler gets to throw one or two more bonus balls, respectively. These bonus throws are taken as part of the same turn. If the bonus throws knock down all the pins, the process does not repeat: the bonus throws are only used to calculate the score of the final frame.
- The game score is the total of all frame scores.
More info on the rules at: [How to Score for Bowling](http://www.topendsports.com/sport/tenpin/scoring.htm)

## Sample input data
The below sample data represents each throw separated by a space

player1: `[9,0,9,0,9,0,9,0,9,0,9,0,9,0,9,0,9,0,9,0]`
(20 throws: 10 pairs of 9 and miss) = 10 frames * 9 points in each frame = 90

player2: `[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]`
(21 throws: 10 pairs of 5 and spare, with a final 5) = 10 frames * 15 points in each frame = 150

player3: `[10,10,10,10,10,10,10,10,10,10,10,10]`
(12 throws: 12 strikes) = 10 frames * 30 points in each frame = 300

## Clues
- What makes this game interesting to score is the lookahead in the scoring for a strike and a spare. At the time we throw a strike or spare, we cannot calculate the frame score: we have to wait one or two frames to find out what the bonus is.
- One interesting point to note is that without counting frames in any way, finding an elegant way to identify the end of the game/last “real” frame becomes difficult.