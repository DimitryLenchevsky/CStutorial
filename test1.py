sample_string = 'To be or not to be'
occurences = {}
for word in sample_string.split():
    occurences[word] = occurences.get(word, 0) + 1
for word in occurences:
    print('The word', word, 'occurs', occurences[word], \
        'times in the string')