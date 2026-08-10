#line 36
#TODO: check if file already exists, and if so, save it with another name

initials = 'CA'
filepath = fr"NBA\stats\{initials}_Stats.json"

try:
    with open (filepath, 'r') as stats:
        pass #check for file

    filepath = fr"NBA\stats\{initials}_Stats1.json"
    with open (filepath, 'w') as stats:
        stats.write() #if exists, write with another name

except: #if doesn't exist
    with open (filepath, 'w') as stats:
        stats.write() #save it with default name