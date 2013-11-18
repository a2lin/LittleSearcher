import Searcher
import Importer
import SearchEngine
import sys

importer = Importer.Importer()
importer.load('shakespeare/')
curIndex = importer.index_dir()

searchers = Searcher.Searcher(curIndex)
se = SearchEngine.SearchEngine(curIndex)

while True:
	print "Please Enter a Query:"
	q = sys.stdin.readline()
	print se.query(q.strip())
