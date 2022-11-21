
def hashStringBad(s, N):
    h = 0
    for c in s:
        h = h + ord(c) # ord is char-to-int
    #print(h)
    return (h % N) # % is modulo (mod)


s1 = "Larissa Bakken"
s2 = "Astrid Bakken"
s3 = "algorithm"

N = 100

# print('hash string bad 1: ', hashStringBad(s1, N))
# print('hash string bad 2: ', hashStringBad(s2, N))
# print('hash string bad 3: ', hashStringBad(s3, N))


class HashedString:

    def __init__(self, N, s):
        self.value = s
        self.size = N
        self.key = 0

    def printHash(self):
        print('key: ', self.key)
        print('value: ', self.value)

        #hash fucntion used in Java
    def hashString(self):
        s = self.value
        h = 0
        for c in s:
            h = (31*h + ord(c)) # ord is char-to-int
        self.key = (h % self.size) # % is modulo (mod)
        return self

hashedTable = {}
for i in range(N):
    hashedTable[i] = {}

streng1 = HashedString(N, s1)
streng1.hashString()
hashedTable[streng1.key] = streng1.value

streng2 = HashedString(N, s2)
streng2.hashString()
hashedTable[streng2.key] = streng2.value

streng1.printHash()
streng2.printHash()

# print(hashedTable)