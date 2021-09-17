# list of dictionaries to iterate through
covid = [{'state': 'California', 'case': 4522597, 'death': 67672, 'updated': '2021-09-16 18:02:02'}, {'state': 'Texas', 'case': 3891227, 'death': 61309, 'updated': '2021-09-16 18:02:02'}, {'state': 'Florida', 'case': 3509784, 'death': 49257, 'updated': '2021-09-16 18:02:02'}, {'state': 'New York', 'case': 2424888, 'death': 55330, 'updated': '2021-09-16 18:02:02'}, {'state': 'Illinois', 'case': 1582392, 'death': 27061, 'updated': '2021-09-16 18:02:02'}, {'state': 'Georgia', 'case': 1513670, 'death': 24263, 'updated': '2021-09-16 18:02:02'}, {'state': 'Pennsylvania', 'case': 1365049, 'death': 28839, 'updated': '2021-09-16 18:02:02'}, {'state': 'Ohio', 'case': 1319265, 'death': 21265, 'updated': '2021-09-16 18:02:02'}, {'state': 'North Carolina', 'case': 1315427, 'death': 15405, 'updated': '2021-09-16 18:02:02'}, {'state': 'Arizona', 'case': 1055919, 'death': 19333, 'updated': '2021-09-16 18:02:02'}, {'state': 'New Jersey', 'case': 1123364, 'death': 27122, 'updated': '2021-09-16 18:02:02'}, {'state': 'Tennessee', 'case': 1167290, 'death': 14224, 'updated': '2021-09-16 18:02:02'}, {'state': 'Michigan', 'case': 1102957, 'death': 21920, 'updated': '2021-09-16 18:02:02'}, {'state': 'Indiana', 'case': 922320, 'death': 15046, 'updated': '2021-09-16 18:02:02'}, {'state': 'Massachusetts', 'case': 786627, 'death': 18408, 'updated': '2021-09-16 18:02:02'}, {'state': 'Virginia', 'case': 822985, 'death': 12207, 'updated': '2021-09-16 18:02:02'}, {'state': 'Wisconsin', 'case': 764341, 'death': 8666, 'updated': '2021-09-16 18:02:02'}, {'state': 'South Carolina', 'case': 809779, 'death': 11483, 'updated': '2021-09-16 18:02:02'}, {'state': 'Minnesota', 'case': 678978, 'death': 8063, 'updated': '2021-09-16 18:02:02'}, {'state': 'Alabama', 'case': 757893, 'death': 12784, 'updated': '2021-09-16 18:02:02'}, {'state': 'Missouri', 'case': 791832, 'death': 11672, 'updated': '2021-09-16 18:02:02'}, {'state': 'Colorado', 'case': 644419, 'death': 7646, 'updated': '2021-09-16 18:02:02'}, {'state': 'Louisiana', 'case': 721795, 'death': 13318, 'updated': '2021-09-16 18:02:02'}, {'state': 'Oklahoma', 'case': 587687, 'death': 8440, 'updated': '2021-09-16 18:02:02'}, {'state': 'Kentucky', 'case': 639687, 'death': 8144, 'updated': '2021-09-16 18:02:02'}, {'state': 'Maryland', 'case': 515259, 'death': 10238, 'updated': '2021-09-16 18:02:02'}, {'state': 'Utah', 'case': 487351, 'death': 2764, 'updated': '2021-09-16 18:02:02'}, {'state': 'Iowa', 'case': 463376, 'death': 6401, 'updated': '2021-09-16 18:02:02'}, {'state': 'Washington', 'case': 616730, 'death': 7153, 'updated': '2021-09-16 18:02:02'}, {'state': 'Arkansas', 'case': 479110, 'death': 7362, 'updated': '2021-09-16 18:02:02'}, {'state': 'Connecticut', 'case': 381732, 'death': 8416, 'updated': '2021-09-16 18:02:02'}, {'state': 'Nevada', 'case': 407258, 'death': 6789, 'updated': '2021-09-16 18:02:02'}, {'state': 'Mississippi', 'case': 471092, 'death': 9165, 'updated': '2021-09-16 18:02:02'}, {'state': 'Kansas', 'case': 393696, 'death': 5801, 'updated': '2021-09-16 18:02:02'}, {'state': 'US Military', 'case': 278686, 'death': 338, 'updated': '2021-04-20 17:00:47'}, {'state': 'Veteran Affair', 'case': 250417, 'death': 11558, 'updated': '2021-04-20 17:00:47'}, {'state': 'Nebraska', 'case': 255611, 'death': 2365, 'updated': '2021-09-16 18:02:02'}, {'state': 'Puerto Rico', 'case': 217957, 'death': 2207, 'updated': '2021-04-20 17:00:47'}, {'state': 'New Mexico', 'case': 243085, 'death': 4649, 'updated': '2021-09-16 18:02:02'}, {'state': 'Idaho', 'case': 238315, 'death': 2560, 'updated': '2021-09-16 18:02:02'}, {'state': 'Oregon', 'case': 305560, 'death': 3536, 'updated': '2021-09-16 18:02:02'}, {'state': 'West Virginia', 'case': 217119, 'death': 3313, 'updated': '2021-09-16 18:02:02'}, {'state': 'South Dakota', 'case': 139412, 'death': 2096, 'updated': '2021-09-16 18:02:02'}, {'state': 'Rhode Island', 'case': 167653, 'death': 2809, 'updated': '2021-09-16 18:02:02'}, {'state': 'Montana', 'case': 137389, 'death': 1858, 'updated': '2021-09-16 18:02:02'}, {'state': 'North Dakota', 'case': 124620, 'death': 1584, 'updated': '2021-09-16 18:02:02'}, {'state': 'Delaware', 'case': 126050, 'death': 1911, 'updated': '2021-09-16 18:02:02'}, {'state': 'New Hampshire', 'case': 113291, 'death': 1452, 'updated': '2021-09-16 18:02:02'}, {'state': 'Alaska', 'case': 94105, 'death': 453, 'updated': '2021-09-16 18:02:02'}, {'state': 'Wyoming', 'case': 82897, 'death': 918, 'updated': '2021-09-16 18:02:02'}, {'state': 'Federal Bureau of Prisons', 'case': 54863, 'death': 235, 'updated': '2021-04-20 17:00:47'}, {'state': 'Hawaii', 'case': 73268, 'death': 671, 'updated': '2021-09-16 18:02:02'}, {'state': 'Navajo Nation', 'case': 30366, 'death': 1262, 'updated': '2021-04-20 17:00:47'}, {'state': 'Vermont', 'case': 30922, 'death': 294, 'updated': '2021-09-16 18:02:02'}, {'state': 'Guam', 'case': 7859, 'death': 136, 'updated': '2021-04-20 17:00:47'}, {'state': 'US Virgin Islands', 'case': 3005, 'death': 26, 'updated': '2021-04-20 17:00:47'}, {'state': 'Grand Princess', 'case': 103, 'death': 3, 'updated': '2021-04-20 17:00:47'}, {'state': 'Diamond Princess', 'case': 49, 'death': 0, 'updated': '2021-04-20 17:00:47'}, {'state': 'Northern Mariana Islands', 'case': 31, 'death': 2, 'updated': '2021-04-20 17:00:47'}, {'state': 'Wuhan Evacuee', 'case': 4, 'death': 0, 'updated': '2021-04-20 17:00:47'}, {'state': 'District Of Columbia', 'case': 58440, 'death': 1167, 'updated': '2021-09-16 18:02:02'}]

# setting up leaderboard with empty variables
c1 = 0
c1s = ''
c2 = 0
c2s = ''
c3 = 0
c3s = ''
c4 = 0
c4s = ''
c5 = 0
c5s = ''

# for loop that will iterate through each index in the list and compare the value in the key: 'death' with each spot on the leaderboard
for i in range(len(covid)):
    if covid[i]['death'] > c1: # check to see if the current value is larger than the one in the top spot and if so move each value down the list and apply this value as the top
        c5 = c4
        c5s = c4s
        c4 = c3
        c4s = c3s
        c3 = c2
        c3s = c2s
        c2 = c1
        c2s = c1s
        c1 = covid[i]['death']
        c1s = covid[i]['state']
    elif covid[i]['death'] > c2: # if its not larger than the top spot check it against the value of the second spot, and so on
        c5 = c4
        c5s = c4s
        c4 = c3
        c4s = c3s
        c3 = c2
        c3s = c2s
        c2 = covid[i]['death']
        c2s = covid[i]['state']
    elif covid[i]['death'] > c3:
        c5 = c4
        c5s = c4s
        c4 = c3
        c4s = c3s
        c3 = covid[i]['death']
        c3s = covid[i]['state']
    elif covid[i]['death'] > c4:
        c5 = c4
        c5s = c4s
        c4 = covid[i]['death']
        c4s = covid[i]['state']
    elif covid[i]['death'] > c5:
        c5 = covid[i]['death']
        c5s = covid[i]['state']
    else:                       # if the value gets to here then it isn't in the top 5 and we move on
        pass

# once the for loop has reached the end of the covid list, print the leaderboard with state and num of deaths in descending order
print(f"Top 5 COVID Deaths by State\n\n{c1s}:     {c1:,}\n{c2s}:     {c2:,}\n{c3s}:     {c3:,}\n{c4s}:     {c4:,}\n{c5s}:     {c5:,}\n")
# end
