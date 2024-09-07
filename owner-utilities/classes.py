# To parse html
from bs4 import BeautifulSoup, NavigableString, Tag



class Domain:

	def __init__ ( self, path ) :
		self.path = path;
		return

	'''
	[finds file]
	[fragment] ~ [path fragment]
	'''
	def find (fragment) :
		return

	'''
	[finds all files]
	[fragment] ~ [path fragment]
	'''
	def find_all (fragment) :
		return



class Manipulator:

	def __init__ ( self, parsed ) :
		
		# BeautifulSoup document (parsed html file)
		self.pacient = parsed


	'''
	[template] ~ [string that will be inserted in]
	'''
	def import_template ( self, template, selector ) :

		# [template will become an parsed object]
		template = BeautifulSoup(template, 'html.parser')
		
		element = self.pacient.find(selector)
		
		element.clear()
		
		element.append(template)


	def output_attributes ( self, element ) :

		attributes = ''
		
		return attributes



	def ignorable_content ( string ) :
		return
		
		

	'''
	[outputs as string]
	'''
	def output ( self, element, level ) :

		output = ''

		if element == 0:
			element = self.pacient.html

		name = element.name
			
		attributes = ''
		
		if type(element) is Tag:
			
			for key, value in element.attrs.items():

				if type(value) is list:
					value = ''.join(value)
					
				attributes += ' ' + key + '=\"' + value + '\"'
				
		opener = '<' + name + attributes + '>'

		closer = '</' + name + '>'

		identation = '\t'

		output += (identation * level) + opener
			
		if (not element.contents) :
			output += closer + '\n'
			return output

		elif (len(element.contents) == 1) and (type(element.contents[0] is NavigableString)) and (element.contents[0] != '\n') :
			output += element.string + closer + '\n'
			return output

		else:

			output += '\n'
			
			for child in element.contents:

				#print(type(child))

				if child == '\n':
					continue

				elif type(child) is NavigableString:
					output += '\n' + (identation * (level + 1)) + child

				elif type(child) is Tag:
					output += '\n' + self.output(child, (level + 1)) 

			output += '\n' + (identation * level) + closer + '\n'
			return output

