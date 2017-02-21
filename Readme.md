##What is this
i'm playing around with anagrams. not sure how much longer this will keep my interest ¯\\\_(ツ)\_/¯, but as long as it does, here's where i'll be doing it.


```python
from pagan_army import AnagramHandler
anagrammer = AnagramHandler(anagramee='py anagram')
next(anagrammer)
> 'pagan army'
```


##things i might continue to iterate on:

###high-level anagram behavior
* enable the handler to have `peek_ahead_n` and `then_yield_n` with super simple internal strategy that penalizes for more words
* extract the strategy to a stateless function
* improve the strategy to consider parts of speech (e.g. adjective+noun > adjective+adverb)
* reorder anagrams on the way out to optimize for readability

###anagram generation performance
* ~~set up a test harness for evaluating the performance of an anagram_generator~~
* ~~get a baseline for what i currently have in a pretty jupyter notebook so i can come back to it later without context~~
* implement letter sorting in words with a new sorted_anagram_generator and sorted_word_trie based on letter frequency in the dictionary (as opposed to alphabetical. write the dictionary to a new file as a dict for faster reads. test it.
* ~~implement a totally different anagram solution by simple dictionary lookups and recursive letters remaining. test it.~~

###accessibility
* put it in a Flask app
* build a front end
