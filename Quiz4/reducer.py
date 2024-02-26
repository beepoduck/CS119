#!/usr/bin/env python3
"""reducer.py"""

import sys

prev_identifier = None
aggregate_sentiment = 0
identifier = None
word_count = 0

for record in sys.stdin:
    record = record.strip()
    identifier, sentiment_score = record.split('\t', 1)
    
    try:
        sentiment_score = float(sentiment_score)
    except ValueError:
        continue
    
    if prev_identifier == identifier:
        aggregate_sentiment += sentiment_score
        word_count += 1
    else:
        if prev_identifier:
            mean_sentiment = aggregate_sentiment / word_count
            print(f'{prev_identifier}\t{mean_sentiment}')
        
        word_count = 1
        prev_identifier = identifier
        aggregate_sentiment = sentiment_score

if prev_identifier == identifier:
    mean_sentiment = aggregate_sentiment / word_count
    print(f'{prev_identifier}\t{mean_sentiment}')
