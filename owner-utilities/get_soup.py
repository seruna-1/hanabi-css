from bs4 import BeautifulSoup



'''
[Returns BeautifulSoup document from filename]
'''
def from_filename ( filename ):
	
	with open(filename, 'r') as file:
		string = file.read()

	return from_string( string )



'''
[Returns BeautifulSoup document from string]
'''
def from_string ( string ):

	return BeautifulSoup(string, 'html.parser')
