import os
import re

wordLengths = []
sentenceLengths = []

with open(os.path.join("PyParagraph", "raw_data", "paragraph_2.txt"), 'r') as txtFile:
    paragraph = txtFile.read()
    words = paragraph.replace('\n', " ").split(" ")
    sentences = re.split("(?<=[.!?]) +", paragraph.replace('\n', " "))

    # For each word in the paragraph
    for word in words:
        wordFormatted = ''.join(e for e in word if e.isalpha())

         # if its actually a word, add to the list of word lengths
        if len(wordFormatted) > 0:
            wordLengths.append(len(wordFormatted))
    
    #For each sentence in the paragraph
    for sentence in sentences:

        # Split the sentence into words
        sentenceWords = sentence.split(" ")
        wordCount = 0

        #for each wo
        for word in sentenceWords:
            wordFormatted = ''.join(e for e in word if e.isalpha())

            # if its actually a word, add to the word count
            if len(wordFormatted) > 0:
                wordCount += 1

        # add the length of the sentence (in words) to the list of sentence lengths
        sentenceLengths.append(wordCount)

print(f'Approximate Word Count: {len(wordLengths)}')
print(f'Approximate Sentence Count: {len(sentences)}')
print(f'Average Letter Count: {round(sum(wordLengths)/len(wordLengths), 1)}')
print(f'Average Sentence Length: {round(sum(sentenceLengths)/len(sentenceLengths), 1)}')


