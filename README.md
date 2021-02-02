Fibertree Notebooks
===================

This repository contains various Jupyter notebooks that illustrate the
implemention of various sparse (and dense) computations using the
fibertree abstraction.


Install the fibertree Python package
====================================

See the [fibertree](https://github.com/Fibertree-Project/fibertree)
repo for instructions on installing the fibertree Python package.


Run Ipython notebooks
=====================

To run the Ipython notebooks:

```console
  % cd notebooks
  % jupyter notebook .
```

Browse in the various subdirectories and invoke
a notebook. A good place to start is basic/fibertree.ipynb


See FAQ below for addressing some problems.

FAQ
===

Q: How do I fix font-related errors when displaying graphics?

A: On Ubuntu/Debian systems you can try installing fonts-freefon-ttf with:

```console
   % sudo apt install fonts-freefont-ttf
```

   If you know where the fonts are on your system then you can set the
   environment variable FIBERTREE_FONT in Python code you can do this
   with something like:

```python
   import os

   os.environ['FIBERTREE_FONT'] = 'Pillow/Tests/fonts/FreeMono.ttf'
```

Q: How can I get the Jupyter widgets to work?

A1: For classic Jupyter, try the following command:

```console
  % jupyter nbextension enable --py widgetsnbextension
```

A2: To get widgets to work in Jupyter lab, try the following:

```console
  % curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.6/install.sh | bash
  # restart bash
  % nvm install node
  % jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

