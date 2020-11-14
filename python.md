

## python wierdness

```
# check paths that are available
python3 -m site

# The top one from the list is CWD. 
# If you run your code with `python3 path/to/script.py`, it will change to `.../path/to/`.
# To create a stable path that doesn't change, do followings:
export PYTHONPATH=$PYTHONPATH:/path/to/your/root_contains_modules

# IF your module.py has main defined, you can run your module.py by:
python3 -m module

# check a module's path
python3 -c 'import site as _; print(_.__file__)
python3 -c 'from yourpkg import yourmod as _; print(_.__file__)

```
