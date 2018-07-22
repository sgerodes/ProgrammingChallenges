function firstNonRepeatingLetter(s) {
    for (let i = 0; i < s.length; ++i){
        if (s.toLowerCase().split(s[i].toLowerCase()).length-1 == 1) {return s[i]}
    }
    return ""
}