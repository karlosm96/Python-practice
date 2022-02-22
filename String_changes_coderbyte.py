def modification(string):
    mod_str = ""
    dic = dict(zip('abcdefghijklmnopqrstuvwxyz', ["1","2","3","4","5","6","7","8","9","10","11","12","13","15","16","17","18","19","20","21","22","23","24","25","26"]))
    
    for i in range(len(string)):
        if string[i] in dic:
            mod_str += dic[string[i]]
        else:
            mod_str += string[i]
    
    return mod_str

string = "jaj-a"

print(modification(string))