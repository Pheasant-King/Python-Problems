def word_smith( string , check ):
    length = 0
    mylist = []
    words = string.split();
    for word in words:
        for letter in word:
            if len(word) > 3 and letter in check and letter not in '!@#$%^&*()~<>?[]|{}=_+-.':
                mylist.append(word)
                break
        if word[0].lower() in 'aeiouy' and len(word) > 3 and word not in mylist:
            mylist.append(word)
    length = len(mylist)
    return length

def base_builder( n ):
    def get_Quaterary( n ):
        if (n < 4):
            return str(int(n))
        return str(get_Quaterary(n/4)) + str((int(n%4)))
    def get_Sum( n ):
        s = 0
        while n:
            n, remainder = divmod(n, 10)
            s += remainder
        return s
    quaterary = int(get_Quaterary(n))
    sum = get_Sum(quaterary)
    
    return(sum, quaterary)
