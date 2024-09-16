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

import get_soup as get_soup


tags = {}


def main ():

	with open( sys.argv[1], 'r' ) as file:
		mana = file.read()

	# Gets parsed html from file
	html = get_soup.from_filename( "../basic.html" )

	tags["title"] = "Message";

	element_start = mana.find( "[", 0 )

	element_end = mana.find( "]", element_start + 1 )

	next_element_start = 0

	next_element_end = 0

	while 1 :

		'''
		Gets next element
		'''
		next_element_start = mana.find( "[", element_end + 1 )

		next_element_end = mana.find( "]", next_element_start + 1 )

		if ( next_element_start == -1 ) or ( next_element_end == -1 ) :

			break

		'''
		No operator. Element becomes paragraph
		'''
		if mana.find( "=", element_end, next_element_start ) != -1 :

			element_start = mana.find( "[", next_element_end + 1 )

			element_end = mana.find( "]", element_start + 1 )	

			if ( element_start == -1 ) or ( element_end == -1 ) :

				break

		elif mana.find( "->", element_end, next_element_start ) != -1 :

			element_start = mana.find( "[", next_element_end + 1 )

			element_end = mana.find( "]", element_start + 1 )

			if ( element_start == -1 ) or ( element_end == -1 ) :

				break

		else:

			paragraph = html.new_tag( "p" )

			paragraph.string = mana[ ( element_start + 1 ) : ( element_end ) ]

			html.body.main.append( paragraph )

			element_start = next_element_start

			element_end = next_element_end

	print(html)

	return 0



if __name__ == "__main__":
	main()

