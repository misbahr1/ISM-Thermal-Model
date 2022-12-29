# About

This project aims to provide a simple framework to create a thermal model. *More details to be added when ready.*

This is still **WORK IN PROGRESS**. The files in [thermalmodel](./thermalmodel) contain all the classes for the implementation.

The general structure of the various elements is described with the following class diagram.
![Class Diagram](./class-diagram/output.png)

A sample implementation can be found in [the example file](./example.py).

# TODO

You will find many comments saying `TODO`. Please look for those to identify any missing elements. Here are the general aspects still missing, in order of priority.

-[ ] Add ability to see *missing links* (i.e. those that were not specifically specified). Please refer to comments in the code for more information.
-[ ] Generate new links for the set of *missing links*. Use the `links.ManualLink` type for these; here the heat exchange is "computed" with a user-defined function. For simplicity, make this function compute the heat exchange using the inverse link (i.e. for link `(j,i)`, compute using `(i.j)`)
<!-- -[ ] Make it such that the HSN first only computes the heat exchange for links that are defined. In a second pass, "compute" the heat exchange for links that were not defined (and generated by the code (i.e. they should be identifiable because they only have the `ManualLink` link type; a more robust approach would be to add an attributed indicating whether the links was generated because it was missing or not)). Suggestion: split the `computeHeatExchange()` functions into 2 subfunctions for this task. This is necessary, because you cannot get the heat exchange value of the inverse link if it was not computed yet. Alternatively, run the compute function twice: the first time it might have "missing values" for the inverse links; the second time it will fill up what is missing (but recalculate everything). -->
-[ ] Implement `AmbientLink`'s `computeHeatExchange()` function
-[ ] Implement `VacuumChamberLink`'s `computeHeatExchange()` function
-[ ] Are temperatures the only relevant thing at the end of the simulation? With the current implementation, there is most likely no need to incorporate complicated matrices (i.e. since the links are now defined both ways (if the above points have been tackled)). If temperatures are all, then store those into arrays for later use, no need for matrices.
-[ ] Implement `save()` function
