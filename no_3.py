def count_substring(string,sub_string):
    #l=len(sub_string)
    count=0
    count_1 = 0
    string_rev = string[::-1]
    for i in range(len(string)-len(sub_string)+1):
        if(string[i:i+len(sub_string)] == sub_string):      
            count+=1
        if(string_rev[i:i+len(sub_string)] == sub_string):
            count_1+=1
                
    result = count+count_1
    return result

print('ditemukan', count_substring('banananana', 'nana'), 'kali')