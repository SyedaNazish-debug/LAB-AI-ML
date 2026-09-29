def compress(text):
    if not text:
        return""
    compressed=""
    count=1

    for i in range (len(text)):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            count +=1
        else:
            compressed += text[i] + str(count)
            count = 1
        return compressed
def decompress(compressed):
    decompressed=""
    i=0

    while i < len(compressed):
        char =  compressed[i]
        i += 1

        count =""
        while i <len(compressed) and compressed[i].isdigit():
            count += compressed[i]

            i += 1
            
    decompressed += char * int(count)
    return decompressed 

text= input("Enter text:")
compressed = compress(text)

print("\n Original text:", text)
print("compressed text:", compressed)

decompressed =decompress(compressed)
print("Decompressedtext:", decompressed)

if len(text)>0:
    ratio =(len(compressed)/len(text)) * 100
    print("compressed size:",len(compressed), "characters")
    print("Original size", len(text),"characters")
    print("compression ratio:", round(ratio,2),"%")