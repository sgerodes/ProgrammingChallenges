def validBraces(string):
    stack=[]
    app=stack.append
    pop=stack.pop
    open_braces='([{'
    closing_braces='}])'
    brace_map={'}':'{', ']':'[', ')':'('}
    for c in string:
        if c in open_braces:
            app(c)
        if c in closing_braces:
            if not stack:
                return False
            if not brace_map[c] == pop():
                return False
    return True if not stack else False