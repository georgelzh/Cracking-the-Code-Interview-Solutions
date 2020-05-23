# challenge from codesignal
# reference: https://github.com/woodyhoko/codesignal

def hashMap(queryType, query):
    d = {}
    output = []
    for i, j in zip(queryType, query):
        if i == "insert":
            d[j[0]] = j[1]
        elif i == "addToValue":
            for k,v in d.items():
                d[k] += j[0]
        elif i == "addToKey":
            for k, v in d.items():
                d[k+1] = v
                del d[k]
        elif i == "get":
            output.append(j[0])
    return output


queryType = ["insert", "get"]
query = [[1,1], [1]]

print(hashMap(queryType,query))