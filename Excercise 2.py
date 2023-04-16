poem='frequently during my mornings of pain  reflection\nwhen i cannot write\nor articulate my thoughts\nor locate the mindmusic needed\nto complete the poems; essays\nthat are weeks plus days overdue\nforcing me to stop, i cease\nanswering my phone, eating right, running my miles,\nreading my mail, and making love.\n(also, this is when my children do not seek me out\nbecause i do not seek them out.)\ni escape north, to the nearest library or used bookstore.\nthey are my retreats, my quiet energy-givers, my intellectual refuge.\nfor me it is not bluewater beaches, theme parks,\nor silent chapels hidden among forest greens.\nnot multi-stored american malls, corporate book\nsupermarkets, mountain trails, or caribbean hideaways.\nmy sanctuaries are liberated lighthouses of shelved books,\nfeaturing forgotten poets, unread anthropologists of tenure-\nseeking assistant professors, self-published geniuses, remaindered\nfirst novelists, highlighting speed-written bestsellers,\nwise historians; theologians, nobel, pulitzer prize, and american book\naward winners, poets; fiction writers, overcertain political commentators,\nsmall press wunderkinds ; learned academics.\nall are vitamins for my slow brain ; sidetracked spirit in this\nwinter of creating.\ni do not believe in smiling politicians, ama doctors\nzebra-faced bankers, red-jacketed real estate or automobile\nsalespeople, or singing preachers.'
print(poem)
try:
    lines= int(input('How many lines will there be?: '))
    currentCharacter=0
    lastChar=0
    print('Lines:'+str(lines))
    i=0
    cuttedPoem=poem
    while i in range(0,lines):
        currentCharacter=cuttedPoem[currentCharacter:len(cuttedPoem)].find('\n')+2
        lastChar+=currentCharacter
        currentCharacter=0
        cuttedPoem=poem[lastChar:len(poem)]
        i+=1
    print(poem[0:lastChar-2])    
except ValueError:
    print('There was an error with the line number that you input')