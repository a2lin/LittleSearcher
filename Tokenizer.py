import re

class Tokenizer:
	"""The Tokenizer for a Little Search Engine"""

	def __init__(self):
		self.dict = {}

	def load(self, fileDir=""):
		"""loads the file into the tokenizer"""
		if(fileDir == ""):
			raise Exception("Please load with an actual filename")
		self.fileDir = fileDir

	def tokenize_index(self):
		"""tokenizes the file generically. Returns the inverted index."""
		inFile = open(self.fileDir, 'r')
		i = 0
		for line in inFile:
			arr = re.split("[^A-Za-z']+", line)
			for x in arr:
				if(x != ''):
					if x in self.dict:
						self.dict[x] = self.dict[x] + [i]
					else:
						self.dict[x] = [i]
			i += 1
		#print self.dict
		return self.dict


