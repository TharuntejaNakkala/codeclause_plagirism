from collections import Counter
def read_docu(file):
    
    all_words = []
    
    with open(file, "r", encoding = "utf-8") as input_file:
        for line in input_file:
            line = line.lower()
            line = line.strip().split()
            all_words += line
        return(all_words)
#Codes by Jay Lee https://www.kaggle.com/jayaos/basic-nlp-preprocessing-of-corpus-and-zipf-s-law/notebook

def word_counter(all_words):
    
    word_count = Counter()
    for word in all_words:
        word_count[word] += 1
    return(word_count.values())
def draw_zipfian_curve(word_count):
    plt.plot(sorted(word_count, reverse = True), marker = "o")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("log(Rank)")
    plt.ylabel("log(Frequency)")
    plt.show()

#Codes by Jay Lee https://www.kaggle.com/jayaos/basic-nlp-preprocessing-of-corpus-and-zipf-s-law/notebook

def zipfian_plot(file):
    word_corpus = read_docu(file)
    counts = word_counter(word_corpus)
    draw_zipfian_curve(counts)
zipfian_plot("../input/mit-plagairism-detection-dataset/train_snli.txt")

df= pd.read_csv('../input/mit-plagairism-detection-dataset/train_snli.txt', sep='\t', error_bad_lines=False)
df.head()

df.isnull().sum()

#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# lets create a text
text = "Two blond women are hugging one another"

# length of text ( includes spaces)
print("length of text: ",len(text))

# split the text
splitted_text = text.split() # default split methods splits text according to spaces
print("Splitted text: ",splitted_text)    # splitted_text is a list that includes words of text sentence
# each word is called token in text maning world.

#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# find specific words with list comprehension method
specific_words = [word for word in splitted_text if(len(word)>2)]
print("Words which are more than 3 letter: ",specific_words)

# capitalized words with istitle() method that finds capitalized words
capital_words = [ word for word in splitted_text if word.istitle()]
print("Capitalized words: ",capital_words)

# words which end with "o": endswith() method finds last letter of word
words_end_with_o =  [word for word in splitted_text if word.endswith("o")]
print("words end with o: ",words_end_with_o) 

# words which starts with "w": startswith() method
words_start_with_w = [word for word in splitted_text if word.startswith("w")]
print("words start with w: ",words_start_with_w) 

#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# unique with set() method
print("unique words: ",set(splitted_text))  # actually the word "no" is occured twice bc one word is "no" and others "No" there is a capital letter at first letter

# make all letters lowercase with lower() method
lowercase_text = [word.lower() for word in splitted_text]

# then find uniques again with set() method
print("unique words: ",set(lowercase_text))

#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# check words includes or not includes particular substring or letter
print("Is w letter in women word:", "w" in "women")

# check words are upper case or lower case
print("Is word uppercase:", "WOMEN".isupper())
print("Is word lowercase:", "hugging".islower())

# check words are made of by digits or not
print("Is word made of by digits: ","12345".isdigit())

# get rid of from white space characters like spaces and tabs or from unwanted letters with strip() method
print("00000000Two blond: ","00000000Two blond".strip("0"))

# find particular letter from front 
print("Find particular letter from back: ","one another".find("r"))  # at index 1

# find particular letter from back  rfind = reverse find
print("Find particular letter from back: ","one another".rfind("r"))  # at index 8

# replace letter with number
print("Replace o with 4 ", "one another".replace("r","4"))

# find each letter and store them in list
print("Each letter: ",list("Two blond"))

# Cleaning text
text1 = "    The kids are frowning    "
print("Split text: ",text1.split(" "))   # as you can see there are unnecessary white space in list

# get rid of from these unnecassary white spaces with strip() method then split
print("Cleaned text: ",text1.strip().split(" "))


library.an.edu

from collections import Counter
#Codes by Jay Lee https://www.kaggle.com/jayaos/basic-nlp-preprocessing-of-corpus-and-zipf-s-law/notebook

def read_docu(file):
    
    all_words = []
    
    with open(file, "r", encoding = "utf-8") as input_file:
        for line in input_file:
            line = line.lower()
            line = line.strip().split()
            all_words += line
        return(all_words)
#Codes by Jay Lee https://www.kaggle.com/jayaos/basic-nlp-preprocessing-of-corpus-and-zipf-s-law/notebook

def word_counter(all_words):
    
    word_count = Counter()
    for word in all_words:
        word_count[word] += 1
    return(word_count.values())
def draw_zipfian_curve(word_count):
    plt.plot(sorted(word_count, reverse = True), marker = "o")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("log(Rank)")
    plt.ylabel("log(Frequency)")
    plt.show()
#Codes by Jay Lee https://www.kaggle.com/jayaos/basic-nlp-preprocessing-of-corpus-and-zipf-s-law/notebook

def zipfian_plot(file):
    word_corpus = read_docu(file)
    counts = word_counter(word_corpus)
    draw_zipfian_curve(counts)
zipfian_plot("../input/mit-plagairism-detection-dataset/train_snli.txt")

df= pd.read_csv('../input/mit-plagairism-detection-dataset/train_snli.txt', sep='\t', error_bad_lines=False)
df.head()
A person on a horse jumps over a broken down airplane.	A person is at a diner, ordering an omelette.	0
0	A person on a horse jumps over a broken down a...	A person is outdoors, on a horse.	1
1	Children smiling and waving at camera	There are children present	1
2	Children smiling and waving at camera	The kids are frowning	0
3	A boy is jumping on skateboard in the middle o...	The boy skates down the sidewalk.	0
4	A boy is jumping on skateboard in the middle o...	The boy does a skateboarding trick.	1
df.isnull().sum()
A person on a horse jumps over a broken down airplane.    0
A person is at a diner, ordering an omelette.             4
0                                                         0
dtype: int64
Basic Text Mining Methods
Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining
#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# lets create a text
text = "Two blond women are hugging one another"

# length of text ( includes spaces)
print("length of text: ",len(text))

# split the text
splitted_text = text.split() # default split methods splits text according to spaces
print("Splitted text: ",splitted_text)    # splitted_text is a list that includes words of text sentence
# each word is called token in text maning world.
length of text:  39
Splitted text:  ['Two', 'blond', 'women', 'are', 'hugging', 'one', 'another']
One blond and one brunette hugging


#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# find specific words with list comprehension method
specific_words = [word for word in splitted_text if(len(word)>2)]
print("Words which are more than 3 letter: ",specific_words)

# capitalized words with istitle() method that finds capitalized words
capital_words = [ word for word in splitted_text if word.istitle()]
print("Capitalized words: ",capital_words)

# words which end with "o": endswith() method finds last letter of word
words_end_with_o =  [word for word in splitted_text if word.endswith("o")]
print("words end with o: ",words_end_with_o) 

# words which starts with "w": startswith() method
words_start_with_w = [word for word in splitted_text if word.startswith("w")]
print("words start with w: ",words_start_with_w) 
Words which are more than 3 letter:  ['Two', 'blond', 'women', 'are', 'hugging', 'one', 'another']
Capitalized words:  ['Two']
words end with o:  ['Two']
words start with w:  ['women']
#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# unique with set() method
print("unique words: ",set(splitted_text))  # actually the word "no" is occured twice bc one word is "no" and others "No" there is a capital letter at first letter

# make all letters lowercase with lower() method
lowercase_text = [word.lower() for word in splitted_text]

# then find uniques again with set() method
print("unique words: ",set(lowercase_text))
unique words:  {'blond', 'another', 'women', 'hugging', 'one', 'are', 'Two'}
unique words:  {'blond', 'another', 'two', 'women', 'hugging', 'one', 'are'}
#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# check words includes or not includes particular substring or letter
print("Is w letter in women word:", "w" in "women")

# check words are upper case or lower case
print("Is word uppercase:", "WOMEN".isupper())
print("Is word lowercase:", "hugging".islower())

# check words are made of by digits or not
print("Is word made of by digits: ","12345".isdigit())

# get rid of from white space characters like spaces and tabs or from unwanted letters with strip() method
print("00000000Two blond: ","00000000Two blond".strip("0"))

# find particular letter from front 
print("Find particular letter from back: ","one another".find("r"))  # at index 1

# find particular letter from back  rfind = reverse find
print("Find particular letter from back: ","one another".rfind("r"))  # at index 8

# replace letter with number
print("Replace o with 4 ", "one another".replace("r","4"))

# find each letter and store them in list
print("Each letter: ",list("Two blond"))
Is w letter in women word: True
Is word uppercase: True
Is word lowercase: True
Is word made of by digits:  True
00000000Two blond:  Two blond
Find particular letter from back:  10
Find particular letter from back:  10
Replace o with 4  one anothe4
Each letter:  ['T', 'w', 'o', ' ', 'b', 'l', 'o', 'n', 'd']
# Cleaning text
text1 = "    The kids are frowning    "
print("Split text: ",text1.split(" "))   # as you can see there are unnecessary white space in list

# get rid of from these unnecassary white spaces with strip() method then split
print("Cleaned text: ",text1.strip().split(" "))
Split text:  ['', '', '', '', 'The', 'kids', 'are', 'frowning', '', '', '', '']
Cleaned text:  ['The', 'kids', 'are', 'frowning']
The kids are frowning
bckonline.com

dogtrainingobedienceschool.com

memecreator.org

#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# reading files line by line
f = open("../input/mit-plagairism-detection-dataset/train_snli.txt","r")

# read first line
print(f.readline())

# length of text
text3=f.read()
print("Length of text: ",len(text3))

# Number of lines with splitlines() method
lines = text3.splitlines()
print("Number of lines: ",len(lines))

df = df.rename(columns={'A person on a horse jumps over a broken down airplane.':'person', 'A person is at a diner, ordering an omelette.': 'omelette'})

df.head()
# find which entries contain the word 'appointment'
print("In this text, the rate of occuring boy word is: ",sum(df.person.str.contains('boy'))/len(df))
# text
text = df.person[1]
print(text)

#I´m saving that snippet since there is No callout that started with @.  

# find regular expression on text
# import regular expression package
import re
# find callouts that starts with @
callouts = [word for word in text.split(" ") if re.search("@[A-Za-z0-9_]+",word)]
print("callouts: ",callouts)

#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# find specific characters like "w"
print(re.findall(r"[w]",text))
# "w"ith, "w"indo"w", sho"w"ing, s"w"itches 

# do not find specific character like "w". We will use "^" symbol
print(re.findall(r"[^w]",text))

#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# import natural language tool kit
import nltk as nlp

# counting vocabulary of words
text = df.person[1]
splitted = text.split(" ")
print("number of words: ",len(splitted))

# counting unique vocabulary of words
text = df.person[1]
print("number of unique words: ",len(set(splitted)))

# print first five unique words
print("first 5 unique words: ",list(set(splitted))[:5])

# frequency of words 
dist = nlp.FreqDist(splitted)
print("frequency of words: ",dist)

# look at keys in dist
print("words in person: ",dist.keys())

# count how many time a particalar value occurs. Lets look at "box"
print("the word box is occured how many times:",dist["box"])

#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# normalization
words = "task Tasked tasks tasking"
words_list = words.lower().split(" ")
print("normalized words: ",words_list)

# stemming
porter_stemmer = nlp.PorterStemmer()
roots = [porter_stemmer.stem(each) for each in words_list]
print("roots of task Tasked tasks tasking: ",roots)

#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# stemming
stemming_word_list = ["baseball","airplane","restaurant","drinking","outdoors"]
porter_stemmer = nlp.PorterStemmer()
roots = [porter_stemmer.stem(each) for each in stemming_word_list]
print("result of stemming: ",roots)

# lemmatization
lemma = nlp.WordNetLemmatizer()
lemma_roots = [lemma.lemmatize(each) for each in stemming_word_list]
print("result of lemmatization: ",lemma_roots)

#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

text_t = "Two groups of rival gang members flipped each other off."
print("split the sentence: ", text_t.split(" "))  # 5 words

# tokenization with nltk
print("tokenize with nltk: ",nlp.word_tokenize(text_t))

# categorical features with missing values
categorical_nan = [feature for feature in df.columns if df[feature].isna().sum()>0 and df[feature].dtypes=='O']
print(categorical_nan)

# replacing missing values in categorical features
for feature in categorical_nan:
    df[feature] = df[feature].fillna('None')

df[categorical_nan].isna().sum()


library.an.edu

from collections import Counter
#Codes by Jay Lee https://www.kaggle.com/jayaos/basic-nlp-preprocessing-of-corpus-and-zipf-s-law/notebook

def read_docu(file):
    
    all_words = []
    
    with open(file, "r", encoding = "utf-8") as input_file:
        for line in input_file:
            line = line.lower()
            line = line.strip().split()
            all_words += line
        return(all_words)
#Codes by Jay Lee https://www.kaggle.com/jayaos/basic-nlp-preprocessing-of-corpus-and-zipf-s-law/notebook

def word_counter(all_words):
    
    word_count = Counter()
    for word in all_words:
        word_count[word] += 1
    return(word_count.values())
def draw_zipfian_curve(word_count):
    plt.plot(sorted(word_count, reverse = True), marker = "o")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("log(Rank)")
    plt.ylabel("log(Frequency)")
    plt.show()
#Codes by Jay Lee https://www.kaggle.com/jayaos/basic-nlp-preprocessing-of-corpus-and-zipf-s-law/notebook

def zipfian_plot(file):
    word_corpus = read_docu(file)
    counts = word_counter(word_corpus)
    draw_zipfian_curve(counts)
zipfian_plot("../input/mit-plagairism-detection-dataset/train_snli.txt")

df= pd.read_csv('../input/mit-plagairism-detection-dataset/train_snli.txt', sep='\t', error_bad_lines=False)
df.head()
A person on a horse jumps over a broken down airplane.	A person is at a diner, ordering an omelette.	0
0	A person on a horse jumps over a broken down a...	A person is outdoors, on a horse.	1
1	Children smiling and waving at camera	There are children present	1
2	Children smiling and waving at camera	The kids are frowning	0
3	A boy is jumping on skateboard in the middle o...	The boy skates down the sidewalk.	0
4	A boy is jumping on skateboard in the middle o...	The boy does a skateboarding trick.	1
df.isnull().sum()
A person on a horse jumps over a broken down airplane.    0
A person is at a diner, ordering an omelette.             4
0                                                         0
dtype: int64
Basic Text Mining Methods
Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining
#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# lets create a text
text = "Two blond women are hugging one another"

# length of text ( includes spaces)
print("length of text: ",len(text))

# split the text
splitted_text = text.split() # default split methods splits text according to spaces
print("Splitted text: ",splitted_text)    # splitted_text is a list that includes words of text sentence
# each word is called token in text maning world.
length of text:  39
Splitted text:  ['Two', 'blond', 'women', 'are', 'hugging', 'one', 'another']
One blond and one brunette hugging


#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# find specific words with list comprehension method
specific_words = [word for word in splitted_text if(len(word)>2)]
print("Words which are more than 3 letter: ",specific_words)

# capitalized words with istitle() method that finds capitalized words
capital_words = [ word for word in splitted_text if word.istitle()]
print("Capitalized words: ",capital_words)

# words which end with "o": endswith() method finds last letter of word
words_end_with_o =  [word for word in splitted_text if word.endswith("o")]
print("words end with o: ",words_end_with_o) 

# words which starts with "w": startswith() method
words_start_with_w = [word for word in splitted_text if word.startswith("w")]
print("words start with w: ",words_start_with_w) 
Words which are more than 3 letter:  ['Two', 'blond', 'women', 'are', 'hugging', 'one', 'another']
Capitalized words:  ['Two']
words end with o:  ['Two']
words start with w:  ['women']
#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# unique with set() method
print("unique words: ",set(splitted_text))  # actually the word "no" is occured twice bc one word is "no" and others "No" there is a capital letter at first letter

# make all letters lowercase with lower() method
lowercase_text = [word.lower() for word in splitted_text]

# then find uniques again with set() method
print("unique words: ",set(lowercase_text))
unique words:  {'blond', 'another', 'women', 'hugging', 'one', 'are', 'Two'}
unique words:  {'blond', 'another', 'two', 'women', 'hugging', 'one', 'are'}
#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# check words includes or not includes particular substring or letter
print("Is w letter in women word:", "w" in "women")

# check words are upper case or lower case
print("Is word uppercase:", "WOMEN".isupper())
print("Is word lowercase:", "hugging".islower())

# check words are made of by digits or not
print("Is word made of by digits: ","12345".isdigit())

# get rid of from white space characters like spaces and tabs or from unwanted letters with strip() method
print("00000000Two blond: ","00000000Two blond".strip("0"))

# find particular letter from front 
print("Find particular letter from back: ","one another".find("r"))  # at index 1

# find particular letter from back  rfind = reverse find
print("Find particular letter from back: ","one another".rfind("r"))  # at index 8

# replace letter with number
print("Replace o with 4 ", "one another".replace("r","4"))

# find each letter and store them in list
print("Each letter: ",list("Two blond"))
Is w letter in women word: True
Is word uppercase: True
Is word lowercase: True
Is word made of by digits:  True
00000000Two blond:  Two blond
Find particular letter from back:  10
Find particular letter from back:  10
Replace o with 4  one anothe4
Each letter:  ['T', 'w', 'o', ' ', 'b', 'l', 'o', 'n', 'd']
# Cleaning text
text1 = "    The kids are frowning    "
print("Split text: ",text1.split(" "))   # as you can see there are unnecessary white space in list

# get rid of from these unnecassary white spaces with strip() method then split
print("Cleaned text: ",text1.strip().split(" "))
Split text:  ['', '', '', '', 'The', 'kids', 'are', 'frowning', '', '', '', '']
Cleaned text:  ['The', 'kids', 'are', 'frowning']
The kids are frowning
bckonline.com

dogtrainingobedienceschool.com

memecreator.org

#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# reading files line by line
f = open("../input/mit-plagairism-detection-dataset/train_snli.txt","r")

# read first line
print(f.readline())

# length of text
text3=f.read()
print("Length of text: ",len(text3))

# Number of lines with splitlines() method
lines = text3.splitlines()
print("Number of lines: ",len(lines))
A person on a horse jumps over a broken down airplane.	A person is at a diner, ordering an omelette.	0

Length of text:  38743027
Number of lines:  367372
df = df.rename(columns={'A person on a horse jumps over a broken down airplane.':'person', 'A person is at a diner, ordering an omelette.': 'omelette'})
df.head()
person	omelette	0
0	A person on a horse jumps over a broken down a...	A person is outdoors, on a horse.	1
1	Children smiling and waving at camera	There are children present	1
2	Children smiling and waving at camera	The kids are frowning	0
3	A boy is jumping on skateboard in the middle o...	The boy skates down the sidewalk.	0
4	A boy is jumping on skateboard in the middle o...	The boy does a skateboarding trick.	1
# find which entries contain the word 'appointment'
print("In this text, the rate of occuring boy word is: ",sum(df.person.str.contains('boy'))/len(df))
# text
text = df.person[1]
print(text)
In this text, the rate of occuring boy word is:  0.07259943599403329
Children smiling and waving at camera
#I´m saving that snippet since there is No callout that started with @.  

# find regular expression on text
# import regular expression package
import re
# find callouts that starts with @
callouts = [word for word in text.split(" ") if re.search("@[A-Za-z0-9_]+",word)]
print("callouts: ",callouts)
callouts:  []
#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# find specific characters like "w"
print(re.findall(r"[w]",text))
# "w"ith, "w"indo"w", sho"w"ing, s"w"itches 

# do not find specific character like "w". We will use "^" symbol
print(re.findall(r"[^w]",text))
['w']
['C', 'h', 'i', 'l', 'd', 'r', 'e', 'n', ' ', 's', 'm', 'i', 'l', 'i', 'n', 'g', ' ', 'a', 'n', 'd', ' ', 'a', 'v', 'i', 'n', 'g', ' ', 'a', 't', ' ', 'c', 'a', 'm', 'e', 'r', 'a']
# Regular expressions for Dates
#date = "15-10-2000\n09/10/2005\n15-05-1999\n05/05/99\n\n05/05/199\n\n05/05/9"
#re.findall(r"\d{1,2}[/-]\d{1,2}[/-]\d{1,4}",date)
Natural Language Process (NLP)
#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# import natural language tool kit
import nltk as nlp

# counting vocabulary of words
text = df.person[1]
splitted = text.split(" ")
print("number of words: ",len(splitted))

# counting unique vocabulary of words
text = df.person[1]
print("number of unique words: ",len(set(splitted)))

# print first five unique words
print("first 5 unique words: ",list(set(splitted))[:5])

# frequency of words 
dist = nlp.FreqDist(splitted)
print("frequency of words: ",dist)

# look at keys in dist
print("words in person: ",dist.keys())

# count how many time a particalar value occurs. Lets look at "box"
print("the word box is occured how many times:",dist["box"])
number of words:  6
number of unique words:  6
first 5 unique words:  ['at', 'smiling', 'Children', 'and', 'camera']
frequency of words:  <FreqDist with 6 samples and 6 outcomes>
words in person:  dict_keys(['Children', 'smiling', 'and', 'waving', 'at', 'camera'])
the word box is occured how many times: 0
Normalization and Stemming words
Normalization is different forms of the same word like have and having.

Stemming is finding a root of the words like having => have.

#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# normalization
words = "task Tasked tasks tasking"
words_list = words.lower().split(" ")
print("normalized words: ",words_list)

# stemming
porter_stemmer = nlp.PorterStemmer()
roots = [porter_stemmer.stem(each) for each in words_list]
print("roots of task Tasked tasks tasking: ",roots)
normalized words:  ['task', 'tasked', 'tasks', 'tasking']
roots of task Tasked tasks tasking:  ['task', 'task', 'task', 'task']
Lemmatization
#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

# stemming
stemming_word_list = ["baseball","airplane","restaurant","drinking","outdoors"]
porter_stemmer = nlp.PorterStemmer()
roots = [porter_stemmer.stem(each) for each in stemming_word_list]
print("result of stemming: ",roots)

# lemmatization
lemma = nlp.WordNetLemmatizer()
lemma_roots = [lemma.lemmatize(each) for each in stemming_word_list]
print("result of lemmatization: ",lemma_roots)
result of stemming:  ['basebal', 'airplan', 'restaur', 'drink', 'outdoor']
result of lemmatization:  ['baseball', 'airplane', 'restaurant', 'drinking', 'outdoors']
Tokenization
Splitting a sentence into words(tokens)

#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

text_t = "Two groups of rival gang members flipped each other off."
print("split the sentence: ", text_t.split(" "))  # 5 words

# tokenization with nltk
print("tokenize with nltk: ",nlp.word_tokenize(text_t))
split the sentence:  ['Two', 'groups', 'of', 'rival', 'gang', 'members', 'flipped', 'each', 'other', 'off.']
tokenize with nltk:  ['Two', 'groups', 'of', 'rival', 'gang', 'members', 'flipped', 'each', 'other', 'off', '.']
# categorical features with missing values
categorical_nan = [feature for feature in df.columns if df[feature].isna().sum()>0 and df[feature].dtypes=='O']
print(categorical_nan)
['omelette']
# replacing missing values in categorical features
for feature in categorical_nan:
    df[feature] = df[feature].fillna('None')
df[categorical_nan].isna().sum()
omelette    0
dtype: int64
m.quickmeme.com

#https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html

# %% creating bag of words model
from sklearn.feature_extraction.text import CountVectorizer  # for bag of words 
max_features = 150 # max_features dimension reduction 
count_vectorizer = CountVectorizer(stop_words = "english",max_features = max_features) 
review_list = df.iloc[:,1] #fixed by Billa comment @skbilla

# stop_words parameter = automatically remove all stopwords 
# lowercase parameter 
# token_pattern removing other karakters like .. !

sparce_matrix = count_vectorizer.fit_transform(review_list).toarray() # sparce matrix yaratir bag of words model = sparce matrix

print("Most used {} words: {}".format(max_features,count_vectorizer.get_feature_names()))

y = df.iloc[:,0].values  # positive or negative comment

#sparce matrix includes independent variable
# train test split
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(sparce_matrix,y,test_size = 0.1,random_state = 0)

#That snippet take hours to provide GaussianNB ()??? . 

# %% naive bayes
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(sparce_matrix,y)

#%%
from sklearn.metrics import confusion_matrix

#Code by Datai https://www.kaggle.com/kanncaa1/applying-text-mining

import matplotlib.pyplot as plt
import seaborn as sns
f,ax = plt.subplots(figsize=(5, 5))
sns.heatmap(cm, annot=True, linewidths=0.5,linecolor="red", fmt= '.1f',ax=ax)
plt.show()
plt.savefig('graph.png')
