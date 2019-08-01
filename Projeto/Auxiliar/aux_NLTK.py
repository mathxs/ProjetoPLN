#!/usr/bin/env python

import re
from nltk import word_tokenize, pos_tag, ne_chunk

class aux_NLTK:

    def __init__(self,sentence):

    regex = r"[-'a-zA-ZÀ-ÖØ-öø-ÿ]+|[.,!?;]"

    print ( word_tokenize(sentence) )

    print ( pos_tag( word_tokenize(sentence) ))

    print ( ne_chunk( pos_tag( word_tokenize(sentence) )))
