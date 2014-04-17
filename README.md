pycut
=====

Hide an image step-by-step using Gaussian Blur.

Install
=======

`pip install -e .`

If you get an `IOError : decoder jpeg not available.` that means that you don't have the libjpeg, libjpeg-dev, libfreetype6, libfreetype6-dev in your current PATH.

The solution is either to install them or to add them in your current PATH.

Usage
=====

Once you have installed pycut you can use it as a command like that `pycut image.jpg 5x5` or you can use it in python like that :

```python
>>> from pycut import pycut
>>> images = pycut("image.jpg", 5, 5)
>>> for image in images:
...    image.show()
...
>>>
```
