from itertools import combinations

def eelOfFortune(secretWord, offWord):
    if not(secretWord and offWord):
        print 'Missing Arguments.'
        return False
        
    if len(offWord) > len(secretWord):
        print 'Invalid Arguments.'
        return False
    
    if secretWord == offWord:
        return True
    
    """ This is to make sure the secret word does not have repeat appearance of any letter of offensive word. """
    tempSecretWord = secretWord
    banned_letters = list(offWord)
    for letter in banned_letters:
        tempSecretWord = tempSecretWord.replace(letter, '',1)
    
    for bl in banned_letters:
        if bl in tempSecretWord:
            return False
    
    """ """
             
    combs = [''.join(p) for p in combinations(secretWord,len(offWord))]
    if offWord in combs:
        return True
    
    return False

if __name__ == '__main__':
    print 'eelOfFortune("synchronized", "snond") -> ' + str(eelOfFortune("synchronized", "snond") )
    print 'eelOfFortune("misfunctioned", "snond") -> ' + str(eelOfFortune("misfunctioned", "snond")) 
    print 'eelOfFortune("mispronounced", "snond") -> ' +str( eelOfFortune("mispronounced", "snond") )
    print 'eelOfFortune("shotgunned", "snond") -> ' + str(eelOfFortune("shotgunned", "snond"))
    print 'eelOfFortune("snond", "snond") -> ' +str(eelOfFortune("snond", "snond") )
    
