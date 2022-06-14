# findunit

## Introduction

A python CLI tool to find information about the units of study provided by University of Sydney.
This tool is under initial development. The current functionality is printing the academic details, 
enrolment requirements, and overview of the units.

## Manual

usage: `findunit [-h] [-y YEAR] [-r] unitcode [unitcode ...]`

Print the academic details, enrolment requirements, and overview of a list of unit of studies at the University of Sydney

positional arguments:
- unitcode: the unit code to find

options:
-  -h, --help:              show this help message and exit
-  -y YEAR, --year YEAR:    the year of the unit of study
-  -r, --remote             remote/online delivery mode