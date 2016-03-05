"""used to save the users settings betwen runs in a file: Settings.json"""
import json

class Settings
		def __init__(self, startLocation, sortByValue, sortByOrder, algorithm):
			self.startLocation = startLocation
			self.sortByValue = sortByValue
			self.sortByOrder = sortByOrder
			self.algorithm = algorithm
			
class SettingsManager:
	#Used to store and save the users settings
#(all in lowercase)Takes the startlocation(eg topleft), sortByValue(eg name), sortByOrder(eg ascending) and algorithm (eg Bubble)  

    #takes a prefsStore Object
    def Save(self, settings):
        with open("Databases\settings.json", 'w') as outfile:
            data = { "startLocation" : settings.StartLocation, "sortByValue" : settings.sortByValue, "sortByOrder" : settings.sortByOrder, "algorithm" : settings.algorithm}
            json.dump(data, outfile)

    #returns a prefsStore Object
    def Load(self):
        with open("Databases\settings.json", 'r') as f:
             data = json.load(f)
             print(data)
             prefs = Settings(data["startLocation"], data["sortByValue"], data["sortByOrder"], data["algorithm"])
             return prefs

#Usage::
#save = prefsSave()
#prefs = prefsStore("topleft", "name", "ascending", "Bubble")
#save.Save(prefs)
#print(save.Load().StartLocation)
