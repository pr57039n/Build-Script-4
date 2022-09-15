from pip._vendor import requests
import pandas as pd
import json

# Drink name for user to input
print("Hello! Thank you for using this application, I'll be glad to tell you about any cocktail drink!")
print("Please input the name of the drink you would like to know about.")
drinkname = input()

# Next checks if the user wishes to also know how strong the drink is for the request.
while(True):
    drinkstrength = input("Would you like to know the strength of the drink? Yes or no: ").lower()
    if drinkstrength == "yes":
        print("I will keep that in mind")
        break
    elif drinkstrength =="no":
        print("I will keep that in mind.")
        break
    else:
        print("Please input yes or no.")
        continue
# Lastly it will check if the user wants to know the type of glass that should be used.
while (True):
        glasstype = input("Would you like to know what glass is used for this drink? SImilarly; yes or no only:").lower()
        if glasstype == "yes":
            print("I will keep that in mind")
            break
        elif glasstype =="no":
            print("I will keep that in mind.")
            break
        else:
            print("Yes or no is the only accepted respone.")
            continue
print("Please wait while I process this information")

# Now that the user has specified what data they need, requests can be more specific to get
gateway = str("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=")+str(drinkname)

# If the user said yes to checking the drink strength then this paramater is used
if drinkstrength =="yes":
    drinkstrength = "strAlcoholic"
else:
    drinkstrength = "null"

# Similarly if the user said yes to checking the glass type, this paramater will be used or dropped.
if glasstype == "yes":
    glasstype = "strGlass"
else:
    glasstype = "null"
# Now the paramaters can be set
drinkparam = {glasstype:drinkstrength}

# Finally the request will be made.

drinkrequest = requests.get(url=gateway,params=drinkparam)

# Taking the info in as json
drinkdata = drinkrequest.json()

#Storing a local form of the json as a csv
with open('personaldrink.json', "w") as file:
    json.dump(drinkdata, file)

drinklist = pd.read_json('personaldrink.json')
drinklist.to_csv('personaldrink.csv', index = None)

#Attemtping to format the data
formatstrength = drinkdata['drinks'][0]['strAlcoholic']
formatglass = drinkdata['drinks'][0]['strGlass']

if drinkstrength =="null" and glasstype == "null":
    print("The drink name is",drinkname)
elif drinkstrength == "strAlcoholic" and glasstype == "null":
    print("The drink name is",drinkname,"The strength is",formatstrength)
elif drinkstrength == "null" and glasstype == "strGlass":
    print("The drink name is",drinkname,"It should be stored in",formatglass)
else:
    print("The drink name is",drinkname,"The strength is",formatstrength,"It should be stored in",formatglass)

