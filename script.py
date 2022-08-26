import click
import io 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

@click.command()
@click.argument('filename')

def stop_word(filename):
    stop_words = set(stopwords.words('english')) 
    with click.open_file(filename) as file1:
        """ file1 = click.open('filename') """ 
        line = file1.read()
        """ words = line.split()  """
        for r in line: 
            if not r in stop_words: 
                appendFile = open('filteredtext.txt','a')
                
                appendFile.write(r) 
                appendFile.close() 

if __name__ == '__main__':
    stop_word()
