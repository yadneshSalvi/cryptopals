import codecs

inp1 = '1c0111001f010100061a024b53535009181c'
inp2 = '686974207468652062756c6c277320657965'

inp1_decoded = bytearray(codecs.decode(inp1,"hex"))#converting the hex input first to bytes string then to byte array
inp2_decoded = bytearray(codecs.decode(inp2,"hex"))#the bytes string is nothing but '\x68\x69\x74.....' which in this case is printable ascii

ans = bytearray(len(inp1_decoded))

for i in range(len(inp1_decoded)):
    ans[i] = inp1_decoded[i]^inp2_decoded[i]

ans = codecs.encode(ans.decode("utf-8"),"hex")#converting the byte array first into utf-8 then into hex string
expected_ans = '746865206b696420646f6e277420706c6179'

if ans==expected_ans:
    print("Done.")
else:
    print("Not yet.")

#You can use hexlify and unhexlify from binascii for encoding and decoding hex


