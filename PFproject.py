import json
import requests
from pprint import pprint

try:
    api_string = 'https://www.reddit.com/r/personalfinance/.json?limit=1000000000&after=t3_10omtd/'
    response = requests.get(api_string, headers={'User-agent': 'your bot 0.1'})  # Requests a response from given URL.  Returns the response as an object.
    data = json.loads(response.text)  # Converts the response to Python dictionary ... or "loads" the JSON data into Python. (Using ".text" after response to convert response object from above into a string.)
except Exception as e:
    print('Decoding JSON has failed') #prints the expception if it doesnt' run properly
else:
    print('data:', type(data))  # Printing out type of "data" to show that it is now a Python dictionary
    json_data = json.dumps(data)  # This dumps the Python dictionary data back into JSON format (which is just a really long string)
    print('json_data:', type(json_data))  # Printing type of "json_data" to show it is now JSON format


data2 = data['data']['children']

with open("redditflairdata.csv", "w") as f:  #this opens the file OUTPUT to get it ready to write
    for text in data2:  #for the requested TEXT in the data with the paramaters in the next line
        f.write(text['data']['link_flair_text'] + "\n") #this writes this data to the file specified earlier
    f.close() #finally this closes the file


