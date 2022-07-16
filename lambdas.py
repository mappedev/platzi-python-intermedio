# def palindrome(string):
#     return string == string[::-1]


palindrome = lambda string: string == string[::-1]
print(palindrome("radar"))

# * definition = lambda parameters: expression
# * Las lambdas son funciones anónimas que deben definirse en una sola línea.
