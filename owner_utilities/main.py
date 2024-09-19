# To get arguments to the program
import sys

# To manage files
import os

# To find files
from pathlib import Path

# To manipulate html files
from bs4 import BeautifulSoup

# To get class [Manipulator]
import classes

# To get parsed html object from filenames and strings
import get_soup as get_soup


'''
[base_dir] ~ [absolute path] to top directory
[returns a list of html pages found in [base_dir]]
'''
def get_pages ( base_dir ):

	#Return error if [base_dir] is not absolute path
	if ( base_dir[0] != '/' ):
		print(base_dir[1])
		print("Path syntax error. Must begin with \"/\".")
		return -1
	
	# List of html pages
	pages = []

	# Find html files and append to list [pages]
	for file in Path(base_dir).rglob('*.html'):
		pages.append(file.absolute())

	return pages;




	

	
'''
[program entry point]

[arguments] ~
[
	[1] ~ [absolute path to top domain]
	[2] ~ [optional] ~ [file inside domain to be updated]
]
'''
def main():

	domain_path = sys.argv[1]
	file_relative_path = sys.argv[2]

	# Gets parsed html from file
	html = get_soup.from_filename( sys.argv[1] + '/' + sys.argv[2] )
	
	'''
	# Gets header string from file
	with open(domain_path + '/' + "templates/header.html", "r") as file:
	header = get_soup.from_filename( sys.argv[2] )
	'''

	newManipulator = classes.Manipulator(html)
	# newManipulator.import_template(header, "header")

	'''
	# Rename old html file
	os.rename(
		domain_path + '/' + file_relative_path,
		domain_path + '/' + '.' + file_relative_path + '.old'
	)

	# Write html string as new file
	new_file = open(domain_path + '/' + file_relative_path, "w")
	new_file.write(html)
	new_file.close()
	'''

	print(newManipulator.output(0, 0))

	return 0

if __name__ == "__main__":
	main()
