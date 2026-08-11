#line 36
#TODO: check if file already exists, and if so, save it with another name

initials = 'CA'
filepath = fr"NBA\stats\{initials}_Stats.json"

try:
    with open (filepath, 'r') as stats:
        pass #check for file

    for i in range(1, 9999):
        try:
            filepath = fr"NBA\stats\{initials}_Stats{i}.json"
            with open (filepath, 'r') as stats:
                pass #check for file
        except:
            with open (filepath, 'w') as stats:
                stats.write() #if exists, write with another name
            break #if file doesn't exist, break the loop and save it with that name    
        
except: #if doesn't exist
    with open (filepath, 'w') as stats:
        stats.write() #save it with default name

