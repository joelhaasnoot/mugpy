Mugpy: A Mugsy client for python
=======

_MIT License_

What?
----
An API wrapper to brew coffee with the Mugsy Robotic Coffee maker by Matthew Oswald. In his own words:

> Mugsy is the world's first hackable, customizable, dead simple, robotic coffee maker.

Usage
-----

```
from mugpy.api import Mugpy

mugsy = Mugpy("a", "b", "c")
result = mugsy.coffee_now()
print(result)  # Boolean
```

Notes
-----
I don't actually have a machine yet and the API isn't live _quite_ yet.
