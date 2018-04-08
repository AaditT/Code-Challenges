# prints the fibonacci series with the given number of terms

def fibonacci(num_terms):
    terms = [0,1]
    counter = 2
    while (counter < num_terms):
        terms.insert(counter, (terms[counter-1] + terms[counter-2]))
        counter = counter + 1
    print(terms)