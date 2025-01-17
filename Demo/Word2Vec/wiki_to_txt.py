# coding=utf-8
__author__ = "the-Quert (github.com/the-Quert)"
import logging
import sys
import warnings
warnings.filterwarnings(action ='ignore', category = UserWarning, module = 'gensim')
from gensim.corpora import WikiCorpus

# Convert wiki dataset to txt
class Wiki_to_txt(object):

	def __init__(self):
		logging.basicConfig(format = '%(asctime)s : %(levelname)s : %(message)s', level = logging.INFO)

	def set_wiki_to_txt(self, wiki_data_path = None):
		if wiki_data_path == None:
			# Paramenters
			if len(sys.argv) != 2:
				print("Please Usage: python3 " + sys.argv[0] + " wiki_data_path")
				exit()
			else:
				wiki_corpus = WikiCorpus(sys.argv[1], dictionary = {})
		else:
			wiki_corpus = WikiCorpus(wiki_data_path, dictionary = {})
			
		# wiki.xml convert to wiki.txt
		with open("wiki_text.txt", 'w', encoding = 'utf-8') as output:
			text_count = 0
			for text in wiki_corpus.get_texts():
				# save use string(gensim)
				output.write(' '.join(text) + '\n')
				text_count += 1
				if text_count % 10000 == 0:
					logging.info("目前已處理 %d 篇文章" % text_count)
			print("轉檔完畢!")
			
if __name__ == "__main__":
	wiki_to_txt = Wiki_to_txt()
	wiki_to_txt.set_wiki_to_txt()
