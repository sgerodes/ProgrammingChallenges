class Solution:
    def uniqueMorseRepresentations(self, words):
        eng_morse_map = dict(zip("abcdefghijklmnopqrstuvwxyz", [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]))
        return len({ "".join(eng_morse_map[c] for c in w) for w in words})