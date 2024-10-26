def all_variants(text):
    len_ = 1
    while len_ < len(text) + 1:
        for start in range(len(text) + 1):
            result = text[start:start + len_]
            if len(result) == len_:
                yield result
        len_ += 1


a = all_variants("abc")
for i in a:
    print(i)
