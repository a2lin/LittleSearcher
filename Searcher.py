
class Searcher:
	""" The searcher for a Little Search Engine """

	def __init__(self, index):
		""" Initialize the searching index to be the passed-in index """
		
		self.index = index

	def search(self, query):
		""" 
		Method that returns all elements of a query. 
		Supports multi-element queries
		"""

		tokenArrays = self.tokenize_query(query)
		return self.intersect(tokenArrays)

	def tokenize_query(self, toTok):
		""" simple tokenizer for queries. Queries and returns. """

		tokens = toTok.split(" ")
		queriedArray = []
		for x in tokens:
			queriedArray += self.index[x]

		return queriedArray

	def intersect(self, tokenArrays):
		""" 
		Takes the intersection of the document arrays 
		to generate final result. This functionality is
		to support multi-term queries.
		"""

		intersection = {}

		for singleTokenResult in tokenArrays:
			for singleTokenElement in singleTokenResult:
				intersection[singleTokenElement] = 1

		return intersection.keys










