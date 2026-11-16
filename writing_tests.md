# Designing Test Situations

Testing a program means choosing inputs or actions and checking whether the program behaves as expected. Use these four categories to help you choose tests.
> **Categories can overlap.** For example, a score of 101 is both an invalid input and a boundary test when scores must be between 0 and 100. Focus on choosing useful tests and explaining your reasoning.

<br>

## Four Categories of Tests

| Category | Guiding question |
|---|---|
| **Typical cases** | Does the program work with ordinary, expected inputs? |
| **Invalid inputs** | Does the program respond appropriately to invalid or incorrectly formatted input and/or user error? |
| **Boundary cases** | Does the program work at, just below, and just above important limits or cutoffs? |
| **Unusual situations** | Does the program handle special circumstances? |

<br>
<hr>

### Typical Cases
| Subcategory | Example |
|---|---|
|Representative inputs | In a py5 drawing program, click in several places on the canvas to check that shapes appear where you click. |
| Different paths through the program | Test a shipping calculator with an order that qualifies for free shipping and one that does not. |

<br>

### Invalid Inputs
| Subcategory | Example |
|---|---|
| Values outside the allowed range | Enter −1 or 101 when quiz scores must be between 0 and 100. |
| Incorrect type or format | Enter “hello” when the program asks for an age. |
| Missing required input | Leave a required username field blank. |

<br>

### Boundary Cases
| Subcategory | Example |
|---|---|
| Minimum and maximum values | If a py5 program lets users choose a brush size from 1 to 50, test sizes of 0, 1, 2, 49, 50, and 51. |
| Decision cutoffs | If a py5 game ends when a timer reaches zero, check its behavior just before, exactly at, and just after zero. |
| Spatial boundaries | In a py5 program, click just inside, exactly on, and just outside a rectangular button’s edges. |
| Size limits | If a username must contain 3–20 characters, test lengths of 2, 3, 4, 19, 20, and 21. |

<br>

### Unusual Situations
| Subcategory | Example |
|---|---|
| Empty or single-item collections | In a py5 animation, check what happens when the list of moving objects is empty or contains only one object. |
| Repeated values or ties | Find the highest score when several players tie for highest. |
| Unexpected patterns in valid data | Find the largest number in a list containing only negative numbers. |
| Calculation details | In a program that is deals with whole-number quantities, like people, what happens when you divide and get a fraction of a person? |


