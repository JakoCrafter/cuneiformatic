import gmpy2    # for conversion to an arbitrary base

f = open("peano.txt")

##### data to binary conversion code #####
# make sure we always send bytes to make sure to see where a character starts and ends
def bytify(bin_str):
    # print(bin_str)
    if len(bin_str) < 8:
        bin_str = '0' + bin_str
        return bytify(bin_str)
    else:
        return bin_str

# simple binary encoder
def encode(char):
    return bytes(bytify(bin(ord(char))[2:]), 'utf-8')

# sexagesimal encoder for a whole text
def encode60(text):
    return gmpy2.digits(text, 60)

##### main #####
# first make the bit string
string = b''
for line in f.readlines():
    for char in line:
        c_bin = encode(char)
        string += c_bin

# print(string)
# print("size: ", len(string))

# turn into whatever base string we need
res = b''
for c in string:
    if chr(c) == "1":
        res += b'\\'
    else:
        res += b'\''

print("BINARY SANSKRIT REPRESENTATION: ")
print(res)
# print(string)
print("SIZE: ",len(string))

print("SEXAGESIMAL CUNEIFORM REPRESENTATION: ")
res_60 = encode60(int(string,2))
print(res_60)

dirtyset = {}
for i in range(0,60):
    dirtyset[encode60(i)] = i

for e in res_60:
    print(dirtyset[e])



print("SIZE: ", len(res_60))

print("WRITING CUNEIFORM TO FILE")

def decToStr(n):
    if n >= 10 and n < 20:
    	return "ten"
    if n >= 20 and n < 30:
    	return "twenty"
    if n >= 30 and n < 40:
    	return "thirty"
    if n >= 40 and n < 50:
    	return "fourty"	
    if n >= 50 and n <= 60:	
    	return "fifty"
    else:
        print("could not convert", n)

out = open("cuneiform.txt", "a")
s = "\\textcuneiform{\\"
t = "}"

for e in res_60:
    if dirtyset[e] <= 9:
        out.write(s + str(dirtyset[e]) + t + " ")
    elif dirtyset[e] >= 10 and dirtyset[e] % 10 == 0:
        out.write(s + decToStr(dirtyset[e]) + t + " ")
    else:
        out.write(s + str(decToStr(dirtyset[e])) + t + s + str(dirtyset[e] % 10) + t + " ")





f.close()
out.close()
