import shelve
shelfFile = shelve.open(r'saves\mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()