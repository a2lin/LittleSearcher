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

	def tokenize_index(self, docId):
		"""tokenizes the file generically. Returns the inverted index."""

		inFile = open(self.fileDir, 'r')
		i = 1
		for line in inFile:
			arr = re.split("[^A-Za-z']+", line)
			for x in arr:
				if(x != ''):
					if x in self.dict:
						self.dict[x] = self.dict[x] + [docId+str(i)]
					else:
						self.dict[x] = [docId+str(i)]
			i += 1
		#print self.dict

	def get_index(self):
		"""returns the current index held by this tokenizer"""

		return self.dict

