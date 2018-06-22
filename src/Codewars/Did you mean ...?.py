import difflib

class Dictionary:
    def __init__(self,words):
        print(words)
        self.words=words
    def find_most_similar(self,term):
        if not self.words:
            return None
        most_similar=self.words[0]
        dfference_score=self.calculate_differences(self.words[0],term)
        for word in self.words:
            curr_score=self.calculate_differences(word,term)
            if curr_score < dfference_score:
                most_similar=word
                dfference_score=curr_score
        return most_similar

    def calculate_differences(self,w1,w2):
        #return self.calculate_differences_difflib(w1,w2)
        return self.calculate_differences_Levenshtein(w1,w2)

    def calculate_differences_difflib(self,w1,w2):
        print(w1,w2)
        return sum(1 for diff in self.differences_between_two_words(w1,w2) if not diff.startswith(' '))

    def differences_between_two_words(self,w1,w2):
        return list(difflib.ndiff(w1, w2))

    def calculate_differences_Levenshtein(self,w1,w2):
        return self.l_distance(w1, w2)

    def l_distance(self,a, b):
        "Calculates the Levenshtein distance between a and b."
        n, m = len(a), len(b)
        if n > m:
            # Make sure n <= m, to use O(min(n,m)) space
            a, b = b, a
            n, m = m, n

        current_row = range(n+1) # Keep current and previous row, not entire matrix
        for i in range(1, m+1):
            previous_row, current_row = current_row, [i]+[0]*n
            for j in range(1,n+1):
                add, delete, change = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
                if a[j-1] != b[i-1]:
                    change += 1
                current_row[j] = min(add, delete, change)

        return current_row[n]
