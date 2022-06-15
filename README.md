# findunit

## Introduction

A python CLI tool to find information about the units of study provided by University of Sydney.
This tool is under initial development. The current functionality is gather the academic details, 
enrolment requirements, and overview of the units, then print them to standard output or write to 
a text, mardown, or pdf file.

## Manual

usage: `findunit [-h] [-y YEAR] [-r] [-o OUTPUT] unitcode [unitcode ...]`

Print the academic details, enrolment requirements, and overview of a list of unit of studies at the University of Sydney, or write them to a file

positional arguments:
- unitcode: the unit code to find

options:
-  -h, --help:                  show this help message and exit
-  -y YEAR, --year YEAR         the year of the unit of study
-  -r, --remote                 remote/online delivery mode
-  -o OUTPUT, --output OUTPUT   the output file name (supported format: text, markdown, pdf)