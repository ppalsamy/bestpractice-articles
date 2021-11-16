## Test Driven Development
### Requirement - Bowling Game (Ten Pin Bowling)
The game consists of 10 frames. In each frame the player has two rolls to knock down 10 pins. The score for the frame is the total number of pins knocked down, plus bonuses for strikes and spares.

A **spare** is when the player knocks down all 10 pins in two rolls. The bonus for that frame is the number of pins knocked down by the next roll.

A **strike** is when the player knocks down all 10 pins on his first roll. The frame is then completed with a single roll. The bonus for that frame is the value of the next two rolls.

In the tenth frame a player who rolls a spare or strike is allowed to roll the extra balls to complete the frame. However no more than three balls can be rolled in tenth frame.

Reference - https://kata-log.rocks/bowling-game-kata

### Pre-requisite
* Java 8
* Junit 5
* Gradle/Maven
* IntelliJ / Eclipse
### Approach
#### Red
- Always start with failing test. Failure can be a compilation issue, and a test.
#### Green
- Make the failed test case to pass by fixing compilation issue and/or test. use `Keep It Simple Stupid (KISS)` design principle.
#### Refactor
- Is there anything to refactor? Use `Don't Repeat Yourself (DRY) or Duplicate Is Evil (DIE)` design principle.
### Running Tests
To execute the tests either run `./gradlew test`, `mvn test` or run the tests from the IDE you are using.
### Implementation
Let's start implementing the requirement using Test-Driven development in the step-by-step process.

#### 1. Getting started
**Red:**

Write a failing test and make it **Red**.
Below code does not compile because there is no class BowlingGame exist.
~~~
package com.tdd;
import org.junit.jupiter.api.Test;

public class BowlingGameTest {

    @Test
    void createGame(){
        BowlingGame game = new BowlingGame();
    }
}
~~~
**Green:**

Fix the failing test by creating class BowlingGame. No additional code is required to make the test pass. Now, we
made it **Green**
````
package com.tdd;
public class BowlingGame{

}
````

 **Refactor:**

Is there any opportunity to clean/refactor the code? NO
Since we did not have any implementation. We don't have to do any refactoring.

#### 2. Understand how to roll
**Red:**

let's try to roll the pins and see what happens.  Below code will not compile because there is no roll method in the class.
~~~
package com.tdd;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

public class BowlingGameTest {

    @Test
    void createGame(){
        BowlingGame game = new BowlingGame();
    }
    @Test
    void canRoll(){
        BowlingGame game = new BowlingGame();
        game.roll(1);
    }
    
}
~~~

**Green:**

Fix the code by adding roll method to the implementation class like below

````
package com.tdd;

public class BowlingGame {
    public void roll(int pins) {
        // do nothing
    }
}
````
let's run the Test, Woo-hoo!!! we got our first method implemented successfully!

**Refactor:**

Can we refactor the code?
Oh! Yes there is a code duplication in the Test.
````
BowlingGame game = new BowlingGame();
````
let's remove the duplicate code.

~~~
package com.tdd;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

public class BowlingGameTest {
    private BowlingGame game =  new BowlingGame();

    @Test
    void canRoll(){
        game.roll(1);
    }
}

~~~

#### 3. Start the first Great game
**Red:**

let's see what's the score for the gutter game :wink: After 20 rounds of roll we still scored 0 :worried:

~~~
package com.tdd;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

public class BowlingGameTest {
    private BowlingGame game =  new BowlingGame();

    @Test
    void canRoll(){
        game.roll(1);
    }

    @Test
    void gutterGame(){
        for(int i =0;i<20;i++>){
            game.roll(0);
        }
        Assertions.assertEquals(0, game.score());
    }
}

~~~
Code will not compile because of `game.score()`, there is no score() method exists.
##### Green:
So let's fix the compilation.

````
package com.tdd;

public class BowlingGame {
    public void roll(int pins) {
        // do nothing
    }
     public int score() {
        return 0;
    }
}
````
let's run the test. Yes test is success.
##### Refactor:
Is the implementation make sense? `score()` method always return 0. Remember `KISS` principle. So for our test simple implementation is enough.

#### 4. Second game
**Red:**

let's add our next test, For each roll one pin knock down

~~~
package com.tdd;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

public class BowlingGameTest {
    private BowlingGame game =  new BowlingGame();

    @Test
    void gutterGame(){
        for(int i =0;i<20;i++>){
            game.roll(0);
        }
        Assertions.assertEquals(0, game.score());
    }
    
    @Test
    public void forEachRoll_onePinDown(){
            for(int i =0;i<20;i++>){
            game.roll(1);
        }
        Assertions.assertEquals(20,game.score());
    }
}

~~~
Test will fail with the below exception
~~~
expected: <20> but was: <0>
Expected :20
Actual   :0

org.opentest4j.AssertionFailedError: expected: <20> but was: <0>
	at org.junit.jupiter.api.AssertionUtils.fail(AssertionUtils.java:55)
	at org.junit.jupiter.api.AssertionUtils.failNotEqual(AssertionUtils.java:62)
	at org.junit.jupiter.api.AssertEquals.assertEquals(AssertEquals.java:150)
	at org.junit.jupiter.api.AssertEquals.assertEquals(AssertEquals.java:145)
	at org.junit.jupiter.api.Assertions.assertEquals(Assertions.java:510)

~~~
**Green:**

So let's fix the test by adding some meaningful code.

````
package com.tdd;

public class BowlingGame {
    private int score =0;
    public void roll(int pins) {
        score +=pins;
    }
     public int score() {
        return this.score;
    }
}
````
let's run the test. Yes, test is success.

**Refactor:**

Is there anything we can refactor. any design pattern or design principles can apply?
Yes, duplicate for loop in the test. we can move the for loop to rollMany method.

~~~
package com.tdd;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

public class BowlingGameTest {
    private BowlingGame game =  new BowlingGame();

    @Test
    public void gutterGame(){
        // Arrange
        int noOfRolls = 20;
        int noOfPins = 0;
        //Act
        rollMany(noOfRolls, noOfPins);
        //Assert
        Assertions.assertEquals(0,game.score());
    }
    
    @Test
    public void eachRoll_onePin_game(){
        rollMany(20, 1);
        Assertions.assertEquals(20,game.score());
   }

    private void rollMany(int noOfRolls, int noOfPins) {
        for (int i = 0; i < noOfRolls; i++) {
            game.roll(noOfPins);
        }
    }
}
~~~

When we write test, always remember to follow
* `Arrange` - prepare and initialize
* `Act`- call the method
* `Assert`- Assert what is expected against actual

#### 5. Repeat
Repeat for other scenarios like below.
* First Spare game 
  - e.g. frame1 - roll(5), roll(5), frame2 - roll(3) and rest of the rolls are 0 pins down
  - Expected score = 16
* One Strike game 
   - e.g. frame1 - roll(10), frame2-roll(3), roll(4)  
   - Expected score = (10+3+4)+3+4 = 24 
* Double strike 
  - e.g frame1 - roll(10), frame2 - roll(10), frame3 - roll(3), roll(4) 
  - Expected score = (10+10+3)+(10+3+4)+3+4 = 47
* Triple strike 
  - e.g frame1 - roll(10), frame2 - roll(10), frame3 - roll(10), frame4-roll(3), roll(4) 
  - Expected score = (10+10+10)+(10+10+3)+(10+3+4)+3+4 = 77
* Tenth Frame Strike or Spare, if we Strike or Spare in tenth frame, we will get one extra chance to roll.
* Perfect Game
  - If everything is strike, maximum possible rolls are 12
  - Expected score = 300
* You can add more cases

Happy Test Driven Development :smiley: 
