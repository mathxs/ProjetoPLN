#!/usr/bin/env python
import sys
import re
from nltk import word_tokenize, pos_tag, ne_chunk


regex = r"[-'a-zA-ZÀ-ÖØ-öø-ÿ]+|[.,!?;]"

if __name__ == '__main__':
    
    sentence = "Mark and John are working at Google."
    #sentence = "Carlos and Maria are students of the Federal University of ABC"

    print ( word_tokenize(sentence) )

    print ( pos_tag( word_tokenize(sentence) ))

    print ( ne_chunk( pos_tag( word_tokenize(sentence) )))
