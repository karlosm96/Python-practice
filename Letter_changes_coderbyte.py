def StringChallenge(strParam):
    clean_str = ""
    for i in range(len(strParam)):
        if strParam[i] == "M":
            if i < 1:
                clean_str += strParam[i].replace("M", "")
            else:
                clean_str += strParam[i].replace("M", strParam[i - 1])
                
                
        elif strParam[i] == "N":
            if i < len(strParam) or i < 1:
                clean_str += strParam[i].replace("N", "")
            else:
                clean_str += strParam[i].replace("N", "")
            
        else:
            clean_str += strParam[i]
        
        
    return clean_str
                
        
  

# keep this function call here 
print(StringChallenge(StringChallenge("oMoMkkNrrN")))