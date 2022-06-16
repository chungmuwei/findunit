'''
Include function regarding parsing and validating command line arguments
'''

import argparse
from datetime import date

def get_args():
    '''
    Parse the argument using argparse library and return the corresponding Namespace object
    '''

    parser = argparse.ArgumentParser(description='Print the overview of an unit of study at the University of Sydney')
    parser.add_argument('unitcode', type=str.upper, nargs='+', help='the unit code to find')
    parser.add_argument('-y', '--year', type=int, default=date.today().year, help='the year of the unit of study')
    parser.add_argument('-r', '--remote', action='store_true', help='remote/online delivery mode')
    parser.add_argument('-o', '--output', type=str, help='the output file name (supported format: text, markdown, pdf)')
    
    return parser.parse_args()

##########################
### Checking Arguments ###
##########################

def valid_unitcode(string: str) -> bool:
	"""
	Check if the input string satisfies the structure of the unit code of the University of Sydney
	A valid unit code consists of 8 characters. The first 4 are alphabets and the last 4 are numbers.
	"""
	return len(string) == 8 and string[:4].isalpha() and string[4:].isnumeric()

def valid_filename(filename: str) -> bool:
	"""
	Check if the input file name is valid
	"""
	extention = filename.split(".")[-1]
	return extention == "txt" or extention == "md" or extention == "pdf"
	