#Question 1
print("Question 1")
import re
emails="zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"
k=re.findall(r'([a-z]+\d+)@([a-z]+).([a-z]+m)',emails)
print(k)
#Question 2
print("Question 2")
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
l=re.findall(r'[bB]\w+',text)
print(l)
#Question 3
print("Question 3")
sentence = "A, very very; irregular_sentence"
# Delete Python-style comments
sen= re.sub(r'[\W_]', " ", sentence)
print("Sentence : ", sen)
#Optional Question
print("Optional Question")
tweet ="Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"
print(tweet)
p=re.sub(r'! .*Web:'," ",tweet)
q=re.sub(r'http.*'," ",p)
print(q)