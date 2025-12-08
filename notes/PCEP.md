# PCEP Points
## Basics
  - Instruction list is machine code
  - High level programming languages extract this to language that is more readable (source code) and is translated through instruction list to machine code
  - Compilation of source code can happen once and then anyone can run
  - Interpretation means source code is interpreted every time the code runs (this is what Python does) aka it is a scripting language
  - Interpreted behavior: read code top to bottom and checks these errors: lexis, syntax, and semantics
  - Lexis - have you used a reserved key word?
  - Syntax - rules for how to construct the python instructions e.g., you must have arguments inside parenthesis after function name
  - Semantics - rules that govern use of functions e.g., number of arguments a given function can take

## Operators 
 - With all mathematical operators except division - if you use 2 integers then you get integer, but a float in any position will produce float
 - Division will always produce a float
 - In Modulo division e.g., x % y, if y > x then the result is always x e.g., 20 % 30 is 20
 - With exponentiation Python actually works from the right to the left instead of left to right
 
## Logical Operators
 - > greater than
 - < less than
 - >= greater than or equal to
 - <= less than or equal to
 - == equal to
 - != not equal to
 - order of operations: not and or

## Data Types
  - Under the hood, everything is really stored as a series of 1s (on) or 0s (off)
  - There is not a binary equivalent for every float number
  - Python makes approximation when storing the floats as binary numbers - close but not exact
 
## Functions
 - The input function always returns a string TBD on how to take other data types as input...
 - Answer is typecasting, see below
 
## Type Casting
 - When using the type casting functions int(), float(), str() - Python will only attempt to convert
 - If user inputs letters and you try to cast as float, the program will fail - this is where exception handling comes into play which we will cover later
 
## Lists
 - There's a distinction between basic data types (where a single value can be stored) vs complex data types (where multiple values can be stored)
 - These are known as collection or container data types
 - Lists, tuples, and dictionaries are examples of this
