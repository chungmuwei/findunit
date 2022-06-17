# findunit

## Introduction

A python **CLI tool** to find information about the units of study at University of Sydney.
This tool is under initial development. The current functionality is scraping the **overview** 
section of the units outline, which contains **academic details**, **enrolment rules**, and 
**teaching staff and contact details**. There are two option of output. One is printing to 
standard output, and the other one is writing to a file of **text**, **Markdown**, or **PDF** format.

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