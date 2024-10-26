def all_variants(text):
    l = 1
    while l < len(text) + 1:
        for i in range(len(text) + 1):
            result = text[i:i + l]
            if len(result) == l:
                yield text[i:i + l]
        l += 1


a = all_variants("abc")
for i in a:
    print(i)
