letters={
    1:"",
    2:["a","b","c"],
    3:["d","e","f"],
    4:["g","h","i"],
    5:["j","k","l"],
    6:["m","n","o"],
    7:["p","q","r","s"],
    8:["t","u","v"],
    9:["w","x","y","z"]
}
digits="2237"
def letterCombinaton(letters,digits):
    numbers=list(map(int,digits))
    wantedLetters=[]
    for i in numbers:
        wantedLetters.append(letters[i])
    combination=[]
    print(wantedLetters)
    #["ad","ae","af","bd","be","bf","cd","ce","cf"]
letterCombinaton(letters,digits)