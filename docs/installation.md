# How to Install tac-hep-coding-jam

## For Users

You will need to git clone the repository from github:

```
git clone https://github.com/ckoraka/tac-hep-coding-jam.git
```

From there, move into the gi directory and use pip install.

```
cd tac-hep-coding-jam
pip install .
```

The package is now installed and ready for use.

## For Developer

### To Get Started

```

git clone https://github.com/ckoraka/tac-hep-coding-jam.git

git checkout -b yourname/jam  # to make your own branch

pip install .   # to install a bunch of stuff you need

```

### Testing Your Code

`pre-commit run --all-files`

### Making Docs

You can add docs by adding an new.md file to directory docs and adding new to
the list under the toctree statement

build your docs by doing:

`nox -s docs -- --serve`

which will create a link that you can look at in a browser

`http://127.0.0.1:8000`