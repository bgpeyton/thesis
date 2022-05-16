`lualatex main.tex` for compilation

to get citations right:
>>> cleantex

# this is a custom command in my .bash_profile, which runs

# `rm *.aux *.lof *.log *.lot *.nlo *.out *.toc *.bbl *.blg`

>>> lualatex main.tex

>>> bibtex main

>>> lualatex main.tex

>>> lualatex main.tex
