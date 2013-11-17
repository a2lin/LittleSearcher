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

	def tokenize(self):
		"""tokenizes the file generically. Returns the dict of word counts."""
		inFile = open(self.fileDir, 'r')
		for line in inFile:
			arr = re.split("[^A-Za-z']+", line)
			for x in arr:
				if(x != ''):
					if x in self.dict:
						self.dict[x] = self.dict[x] + 1
					else:
						self.dict[x] = 1
		#print self.dict
		return self.dict


