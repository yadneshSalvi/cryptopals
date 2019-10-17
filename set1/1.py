import codecs 

inp = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

b64 = codecs.encode(codecs.decode(inp,"hex"),"base64").decode().strip()#even without the outer decode it is fine, without the outer decode the type is string, with it the type is unicode

expected_out = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

if (b64==expected_out):
    print('Done.')
else:
    print('Not yet.')
