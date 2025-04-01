class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        # split the sentence into words
        words = sentence.split()

        # list to store the transformed words
        transformed_words = []

        # iterate through each word in the sentence
        for i, word in enumerate(words):
            # check if the word starts with a vowel
            if word[0].lower() in 'aeiou':
                # If it starts with a vowel, add "ma" to the end of the word
                word = word + 'ma'
            else:
                # If it starts with a consonant, 
                # move the first letter to the end and add "ma"
                word = word[1:] + word[0] + 'ma'

            # Add (i + 1) 'a's based on the position of the word
            word = word + 'a' * (i + 1)

            # append the transformed word to the list
            transformed_words.append(word)

        # join the transformed words into a single string and return
        return ' '.join(transformed_words)
        