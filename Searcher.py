
class Searcher:
	""" The Searcher for a Little Search Engine """

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
			if x in self.index:
				queriedArray += [self.index[x]]

		return queriedArray

	def intersect(self, tokenArrays):
		""" 
		Takes the intersection of the document arrays 
		to generate final result. This functionality is
		to support multi-term queries.
		"""

		if(len(tokenArrays) == 0):
			return None

		elif(len(tokenArrays) == 1):
			return tokenArrays[0]

		else:
			initial = set(tokenArrays[0])
			for tokenQueryResults in tokenArrays[1:]:
				initial = initial & set(tokenQueryResults)

			toReturn = list(initial)
			toReturn.sort()

			if(len(toReturn) == 0):
				return None
				
			return toReturn










