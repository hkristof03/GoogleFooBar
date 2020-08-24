import base64

#The encrypted key
message='E0wBHBAXChVDFEhRUk4UBgoHRBRES1UKHBgDA1FUHQ5VSUlUSANDRw0OHwwXU0NGF1YODR0bBwdI RgoTTwIcCgERCw9SXw1MXklUFQwOWVYeDh8MHQBIRgoTTx4cBRwXBANUFERLVRsSFg0PREBPS0hJ VAcOAFUUREtVDxwbSEYKE08cGwdSUxI='

#Your Google username
key='hkristof03'

decrypted_message=[]

#decode the key to base64 bytes
dec_bytes=base64.b64decode(message)

#XOR with Username
for a,b in enumerate(dec_bytes):
    decrypted_message.append(chr(b ^ ord(key[a%len(key)])))

#The encypted message
print("".join(decrypted_message))
