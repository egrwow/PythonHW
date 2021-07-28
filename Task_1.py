tr_dict = {"zero": "ноль", 'one': 'один', 'two':'два','three':'три','four':'четрые', 'five':"пять",
           'six': 'шесть', 'seven':'семь','eight':'восемь','nine':'девять', 'ten':'десять'}

def num_translate(word):
    return tr_dict.get(word)


print(num_translate(input("enter ur number to translate")))