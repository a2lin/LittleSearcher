import SearchEngine
import sys
"""A simple command-line client for SearchEngine"""

se = SearchEngine.SearchEngine()
se.createIndex("twogentverona.txt")

while True:
	print "Please Enter a Query:"
	q = sys.stdin.readline()
	print se.query(q.strip())

# tok = Tokenizer.Tokenizer()
# tok.load('twogentverona.txt')
# tok.tokenize()