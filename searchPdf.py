import PyPDF2

def searchPdf(keywords):
    
    
    files = ['three.pdf','four.pdf' ]
    
    search_keywords= keywords.split()
    ls = []
    for i,file in enumerate(files):
        
        res = {}
        
    
        pdfFile = open(file,'rb') 
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        totalPages = pdfReader.numPages
        for pageNo in range(totalPages):
            wordCount = 0;
    
            pageObj = pdfReader.getPage(pageNo)
            
            text=(pageObj.extractText())
            #tokens = word_tokenize(text)
            
            text=text.split(",")
            newText = [x.lower() for x in text]
            #print(pageNo, newText)
            
            for sentence in newText:            
    
                lst = []
                for word in search_keywords:
                    if word in sentence:
                        wordCount +=1
            if (wordCount == 0): continue
            else: res[pageNo] = wordCount
        if(len(res) == 0): ls.append([])
        else:
            sortedScores = sorted(res.items(), key=lambda x: x[1], reverse=True)
            ls.append(sortedScores)       
    
    maxVal = 0
    ind = -1
    for i in range(len(ls)):
        if(len(ls[i]) == 0): continue
        if(ls[i][0][1] > maxVal ):
            maxVal = ls[i][0][1]
            ind = i
    if(ind == -1): return ('not found any')
    else: 
        return (files[ind]+' has '+ str(ls[ind][0][1])  + ' results in page no. ' + str(ls[ind][0][0] + 1)  )       


#print(searchPdf('example'))



















