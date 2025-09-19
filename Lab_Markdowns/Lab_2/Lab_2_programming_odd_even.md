## Learning goals

- Create a simple script in Blockly

- Learn and practice some of the programming basics:

  - Defining a variable

  - If statement for logical comparison

  - Loop

  - Function

## Software and hardware

- BlocklyProp Solo

- Activity Board

- Parallax USB programming cable

# Programming 

- Create a script that:

  1.  Gets a number from users, and

  2.  Identifies if the number is odd or even.

  3.  Prints the outcome in the terminal (e.g., this is an EVEN number!)

- Save your code on your computer periodically.

- Submit your code saved as a \*.svg file.

<!-- -->

- Submit your code saved as a \*.svg file.

# Instructions and hints

- The script should have two main blocks:

  - Main block, in which there are:

    - A continuous loop (use *repeat forever* block) asking users to enter a number (use terminal receive block).

    - Call a function that identifies if this is an even or odd number.

    - At the beginning of this block, you may want to add a new line (use terminal new line block) and a text block that prompts users to enter a number (use terminal print text block).

  - Your function block, which

    - Identifies if this is an odd or even number.

    - Prints the outcome in the terminal (e.g., "this is an ODD/EVEN number.").

HINTS:

- To identify if a number is odd or even, you need to check the remainder when you divide the number by 2. If a number is evenly divisible by 2 with no remainder (the remainder is equal to zero), then it is even, otherwise, it is odd (the remainder is not equal to zero). You can use the math operation block and change it to *remainder after division* in the mutation window (gear icon):

![Graphical user interface, application Description automatically generated](media/image1.png)

- Use \`if\` statement to check if the remainder is equal to zero or not:

  - If remainder = 0 🡺 this is an even number.

  - If remainder ≠ 0 🡺 this is an odd number.

- You may want to add comments to your code to make your code more readable, make code maintenance much easier, and help others better understand your code.

# Useful resources

Propeller BlocklyProp Block Reference

<https://learn.parallax.com/support/reference/propeller-blocklyprop-block-reference>

- [**Variable Blocks**](https://learn.parallax.com/tutorials/language/blocklyprop/simple-blocklyprop-programs-propeller-boards/variable-blocks)

- [**Terminal Talk**](https://learn.parallax.com/tutorials/language/blocklyprop/simple-blocklyprop-programs-propeller-boards/terminal-talk)

- [**Values and Math Blocks**](https://learn.parallax.com/tutorials/language/blocklyprop/simple-blocklyprop-programs-propeller-boards/values-and-math-blocks)

- [**Making Decisions**](https://learn.parallax.com/tutorials/language/blocklyprop/simple-blocklyprop-programs-propeller-boards/making-decisions)

- [**Blocks that Repeat**](https://learn.parallax.com/tutorials/language/blocklyprop/simple-blocklyprop-programs-propeller-boards/blocks-repeat)

- [**Functions**](https://learn.parallax.com/support/reference/propeller-blocklyprop-block-reference/functions)
