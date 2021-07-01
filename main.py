import pyramid
import pyramid_lex

result = pyramid_lex.parser.parse("1 2 4 7 p 12")
print(result)