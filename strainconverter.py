import csv
import json
import urllib2
f = open("strains.json")
j = json.load(f)


with open('strains_plus.csv', 'wb') as csvfile:
     writer = csv.DictWriter(csvfile, ["Id", "Key", "Name", "Category", "Symbol", "Abstract", "Url", "DetailUrl", "RateUrl", "Rating", "TopEffect", "TopMedical", "TopActivity", "Anxiety", "Depression", "Fatigue", "Insomnia", "Lack of appetite", "Migraines", "Muscle Spasms", "Nausea", "Pain", "PMS", "Seizures", "Stress", "Aroused", "Creative", "Energetic", "Euphoric", "Focused", "Giggly",  "Happy", "Hungry", "Lazy", "Sleepy", "Talkative", "Tingly", "Uplifted", "Meditate", "Dry Mouth", "Get outdoors", "Create art", "Study", "Listen to music", "Paranoia", "Watch a movie", "Dizziness", "Relax at home", "Hang with friends", "Go to a party", "Play video games", "Headaches", "Dry Eyes"])
     writer.writeheader()
     for row in j: 
     	key = row["Key"]
     	data = urllib2.urlopen('http://www.leafly.com/api/details/'+key)
     	k = json.load(data)
     	for category in ["Effects", "Medical", "Activities", "Negative"]:
     		for attribute in k[category]:
     			row[attribute["Name"]] = attribute["Score"]
     	writer.writerow(row)
