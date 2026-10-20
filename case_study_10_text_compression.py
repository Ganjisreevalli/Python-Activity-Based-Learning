
# Case Study 10: Text Compression Using Character Runs

print("===== TEXT COMPRESSION SYSTEM =====")

text = input("Enter text to compress: ")

if text == "":
    print("Please enter some text.")

else:
    compressed = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed += text[i - 1] + str(count)
            count = 1

    compressed += text[-1] + str(count)

    print("Original Text:", text)
    print("Compressed Text:", compressed)
    print("Original Length:", len(text))
    print("Compressed Length:", len(compressed))

print("====================================")
