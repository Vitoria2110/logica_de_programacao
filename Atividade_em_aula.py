lista=[1,3,6,4]
print(str.join( '---',map(  lambda x: str(x) ,filter( lambda x: x > 2 and x < 6 , lista))))
