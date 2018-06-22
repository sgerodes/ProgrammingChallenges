class Calculator(object):
def evaluate(self, string):
    def calculate_operators(expression,*operators):
        i=0
        while True:
            if i >= len(expression)-1:
                return expression
            if expression[i] in operators:
                expression=expression[:i-1] + [str(eval(expression[i-1] + expression[i] + expression[i+1]))] + expression[i+2:]
                i-=1
            i+=1

    expression=string.split()
    e1=calculate_operators(expression,'*','/')
    e2=calculate_operators(e1,'+','-')
    return eval(e2[0])