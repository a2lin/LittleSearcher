
class Searcher:
	""" The searcher for a Little Search Engine """

	def __init__(self, index):
		""" Initialize the searching index to be the passed-in index """
		
		self.index = index

	def search(self, query):
		""" method that returns all elements of a single-element query """

		if (query in self.index):
			return self.index[query]




