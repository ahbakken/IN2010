
def hashStringBad(s, N):
    h = 0
    for c in s:
        h = h + ord(c) # ord is char-to-int
    #print(h)
    return (h % N) # % is modulo (mod)

#hash fucntion used in Java
def hashString(v):
    h = 0
    for c in v:
        h = (31*h + ord(c)) # ord is char-to-int
    k = (h % N) # % is modulo (mod)
    return k


s1 = "Larissa Bakken"
s2 = "Astrid Bakken"
s3 = "algorithm"

N = 100

# print('hash string bad 1: ', hashStringBad(s1, N))
# print('hash string bad 2: ', hashStringBad(s2, N))
# print('hash string bad 3: ', hashStringBad(s3, N))


class HashedString:
    LFT = 0.75

    def __init__(self):
        self.n = 0
        self.N = 1
        self.A = [None] * self.N

    def loadfactor(self):
        return self.n/self.N

    def __repr__(self):
        kvsPrint = [f'{k} -> {v}' for k, v in iter(self)]
        return '{' + ', '.join(kvsPrint) + '}'

    def __rehash(self):
        kvs = [(k, v) for k, v in self] #key, value, string
        self.n = 0
        self.N *= 2 #increases the size of the array
        self.A = [None] * self.N
        for k, v in kvs: #put in the 
            self[k] = v

    def capasityCheck(self):
        if self.loadfactor() >= self.LFT: #should not be more that this threshold
            self.__rehash()


class SeparateChainingMap(HashedString):

    def __setitem__(self, k, v): #can set item with d[k] = v when we use __setitem__
        self.capasityCheck()

        i = hash(k) % self.N #use the hash method built into python

        if self.A[i] == None: #see if anything is at the index i
            self.A[i] = []
        
        bucket = self.A[i] #make bucket for this index

        for j in range(len(bucket)):
            kj, vj = bucket[j]
            if kj == k:
                bucket[j] = (k, v)
                return
        
        self.n += 1
        bucket.append((k, v))


    def __getitem__(self, k): #can get item with d[k] when we use __getitem__
        i = hash(k) % self.N
        bucket = self.A[i]

        if bucket == None:
            return

        for j in range(len(bucket)):
            kj, vj = bucket[j]
            if kj == k:
                return bucket[j]
                

    def __delitem__(self, k):
        i = hash(k) % self.N
        bucket = self.A[i]

        if bucket == None:
            return

        self.A[i] = [(ki, v) for ki, v in bucket if ki != k]

    def __iter__(self):
        for bucket in self.A:
            if bucket:
                for kv in bucket:
                    yield kv
                    

s1 = "Larissa Bakken"
s2 = "Astrid Bakken"
s3 = "algorithm"

streng = SeparateChainingMap()
streng[s1] = 0
streng[s2] = 1
streng[s3] = 2

# print(streng)
# del streng[s3]
# print(streng)

# print(hashedTable)

class LinearProbing(HashedString):

    def __setitem__(self, k, v): #can set item with d[k] = v when we use __setitem__
        self.capasityCheck()
        
        i = hash(k) % self.N #use the hash method built into python

        if self.A[i] == None: #see if anything is at the index i
            return

        while self.A[i] != None: # if index i is taken
            ki, _  = self.A[i]
            if k == ki:
                self.A[i] = (k, v)
                return

            i = i + 1 % self.N
        
        self.n += 1
        self.A = (k, v) # if index is available
        

    def __getitem__(self, k): #can get item with d[k] when we use __getitem__
        i = hash(k) % self.N

        while self.A[i] != None: # if index i is taken
            ki, _  = self.A[i]
            if k == ki:
                return self.A[i]

            i = i + 1 % self.N

        return
                

    def __delitem__(self, k):
        i = hash(k) % self.N

        while self.A[i] != None: # if index i is taken
            ki, _  = self.A[i]
            if k == ki:
                self.n -= 1
                self.A[i] = None
                self.__fill_hole(i)
                return
            i = i + 1 % self.N
        
    def __fill_hole(self, i):
        s = 1
        while self.A[(i + s) % self.N] != None: # if index i is taken
            k, v  = self.A[(i + s) % self.N]
            j = hash(k) % self.N
            if not (0 > (j-1) % self.N <= s):
                self.A[i] = (k, v)
                self.A[(i + s) % self.N] = None
                self.__fill_hole((i + s) % self.N)
                return
            s += 1

    def __iter__(self):
        for i in self.A:
            if i:
                yield i


s1 = "Larissa Bakken"
s2 = "Astrid Bakken"
s3 = "algorithm"

streng2 = LinearProbing()
streng2[s1] = 0
streng2[s2] = 1
streng2[s3] = 2
print(streng)

del streng[s3]
print(streng)