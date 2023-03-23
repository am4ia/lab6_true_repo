# amaia modolo

'''
Encoder
The password encoder should take in an 8-digit password in string format containing only integers. After
passing the password into the encoder, the encoder stores the encoded password to a new variable, with each
digit being shifted up by 3 numbers.
Examples:
“12345555” will become “45678888” after encoding.
“00009962” will become “33332295” after encoding.
Decoder
The password decoder takes in the encoded password and returns the original password. “45678888” needs to
be decoded back to “12345555” after decoding
'''



def encoder(list):
    temp_list = []
    for i in list:
        i = int(i)
        i +=3
        i = str(i)
        temp_list.append(i)
        list = ''.join(temp_list)
    return list

