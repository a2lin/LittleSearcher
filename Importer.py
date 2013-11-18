import Tokenizer
import os

class Importer:
	"""Importer for directory-level indexing"""

	def __init__(self):
		"""initializes the tokenizer, and directory"""

		self.curDir = ""
		self.tokenizer = Tokenizer.Tokenizer()

	def load(self, curDir=""):
		"""load a current directory to recursively traverse"""

		self.curDir = curDir

	def index_dir(self):
		"""Indexes the directory, traversing recursively"""

		for dirname, dirnames, filenames in os.walk(self.curDir):
			#for subdirname in dirnames:
				#print os.path.join(dirname, subdirname)

			for filename in filenames:
				self.tokenizer.load(os.path.join(dirname,filename))
				self.tokenizer.tokenize_index(filename+'-')

			if '.git' in dirnames:
				dirnames.remove('.git')

		return self.tokenizer.get_index()

	

