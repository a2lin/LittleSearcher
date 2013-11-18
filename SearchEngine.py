import Tokenizer
import Searcher

class SearchEngine:
	""" Main class for the Search Engine"""

	def __init__(self, index={}):
		"""initializes the index & searcher"""

		self.index = index
		self.searcher = []
		self.makeSearcher()

	def makeSearcher(self):
		""" Create a new Searcher to query"""

		self.searcher += [Searcher.Searcher(self.index)]

	def query(self, query):
		""" Make sure that there are available searchers"""

		if (len(self.searcher) == 0):
			self.makeSearcher()
		return self.searcher[0].search(query)

	def createIndex(self, indexLoc):
		""" CreateIndex called to search on an index """

		tok = Tokenizer.Tokenizer()
		tok.load(indexLoc)
		self.index = tok.tokenize_index()






