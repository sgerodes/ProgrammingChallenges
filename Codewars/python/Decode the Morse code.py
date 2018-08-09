def decodeMorse(morse_code):
    morse_words=morse_code.strip().split('   ')
    words_by_letter=[ word.split(' ') for word in morse_words]
    return ' '.join([''.join([ MORSE_CODE[c] for c in word]) for word in words_by_letter])