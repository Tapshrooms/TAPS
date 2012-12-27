Taps Agreeable Programming Standards (TAPS) - Revision 1
====

If you want to contribute to the Tapshrooms Tap family, you'll have to conform to these standards.  
__Please note!__ These standards are viable to change at any given time, so 

Taps Agreeable Programming Standards
---
1. Your Tap __must__ have two classes, `Pressure` and `Tap`.
2. Your `Tap` will have a `Pressure` instance available to it (preferably under the name `pressure`).
3. Your Tap and Pressure class will have all of the methods described in the example python file, and no more, unless requird (getters/setters, or other).
4. Your Tap must come with a README, explaining usage.
	+ you should show how to compile the source, if needed
	+ you should briefly show example usage
5. Your Tap class will use the output strings referenced below in the __Strings__ section.

Strings
---
Your Tap must print these strings to standard output when applicable.
Anything following a hash must not be included, and is simply there for explanation's sake.
```
- On initialisation:
I'm a tap!

- In the run() method:
I'm already running! # if the pressure is not zero
Catch me if you can! # if the tap starts running

- In the stop() method:
I'm not running! # if the pressure is zero
I've stopped!    # if the tap has successfully stopped

- In the explode() method:
BANG! # when the pressure is more than the maximum, and the tap explodes
```