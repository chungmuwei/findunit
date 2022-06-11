# findunit

## Introduction

A python CLI tool to find information about the units of study provided by University of Sydney.
This tool is under initial development. The current functionality is printing the unit overview.

## Manual

usage: `findunit [-h] [-y YEAR] [-m {CC,RE}] unitcode [unitcode ...]`

Print the overview of an unit of study at the University of Sydney

positional arguments:
- unitcode: the unit code to find

options:
-  -h, --help:                   show this help message and exit
-  -y YEAR, --year YEAR:         the year of the unit of study
-  -m {CC,RE}, --mode {CC,RE}:   the mode of the unit study