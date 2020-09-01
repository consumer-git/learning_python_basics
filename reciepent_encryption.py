import string as s


encode=s.punctuation[0:26]+' '
decode=s.ascii_lowercase[0:26]+' '
dict_decode=dict(zip(encode, decode))


enter_text_recipient=str(input('enter your received text '))


for r_letter in enter_text_recipient:
    print(dict_decode[r_letter], end='')








