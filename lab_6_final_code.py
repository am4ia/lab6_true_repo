
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
be decoded back to “12345555” after decoding'''

def encoder(list):
    temp_list = []
    for i in list:
        i = int(i)
        i +=3
        i = str(i)
        temp_list.append(i)
        list = ''.join(temp_list)
    return list



def decoder(encoded_string):
    temp_list = []
    for i in encoded_string:
        i = int(i)
        i -= 3
        i = str(i)
        temp_list.append(i)
        decoded_string = ''.join(temp_list)
    return decoded_string



def menu():
    print('Menu\n'
          '-------------\n'
          '1. Encode\n'
          '2. Decode\n'
          '3. Quit\n')

def main():

    while True:
        menu()
        option = int(input('Please enter an option: '))
        if option == 1:
            # encode
            original_str = input('Please enter your password to encode: ')
            encoded_str = encoder(original_str)
            print('Your password has been encoded and stored!')
        if option == 2:
            decoded_str = decoder(encoded_str)
            print(f'The encoded password is {encoded_str}, and the original password is {decoded_str}')
        if option == 3:
            break

if __name__ == '__main__':
    main()
