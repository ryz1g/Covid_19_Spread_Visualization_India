import matplotlib.pyplot as plt
import pickle

f = open('state_wise_daily.csv', 'r')
lines = f.read().strip().split('\n')

data = {
    'Andhra Pradesh': [],
    'Arunachal Pradesh': [],
    'Assam': [],
    'Bihar': [],
    'Chhattisgarh': [],
    'Delhi': [],
    'Goa': [],
    'Gujrat': [],
    'Haryana': [],
    'Himachal Pradesh': [],
    'Jammu and Kashmir': [],
    'Jharkhand': [],
    'Karnataka': [],
    'Kerela': [],
    'Ladakh': [],
    'Madhya Pradesh': [],
    'Maharashtra': [],
    'Manipur': [],
    'Meghalaya': [],
    'Mizoram': [],
    'Nagaland': [],
    'Odisha': [],
    'Punjab': [],
    'Rajasthan': [],
    'Sikkim': [],
    'Tamil Nadu': [],
    'Telangana': [],
    'Tripura': [],
    'Uttar Pradesh': [],
    'Uttarakhand': [],
    'West Bengal': [],
    'Total': []
}

st_code = {
    1: 'Andhra Pradesh',
    2: 'Arunachal Pradesh',
    3: 'Assam',
    4: 'Bihar',
    5: 'Chhattisgarh',
    6: 'Delhi',
    7: 'Goa',
    8: 'Gujrat',
    9: 'Haryana',
    10: 'Himachal Pradesh',
    11: 'Jammu and Kashmir',
    12: 'Jharkhand',
    13: 'Karnataka',
    14: 'Kerela',
    15: 'Ladakh',
    16: 'Madhya Pradesh',
    17: 'Maharashtra',
    18: 'Manipur',
    19: 'Meghalaya',
    20: 'Mizoram',
    21: 'Nagaland',
    22: 'Odisha',
    23: 'Punjab',
    24: 'Rajasthan',
    25: 'Sikkim',
    26: 'Tamil Nadu',
    27: 'Telangana',
    28: 'Tripura',
    29: 'Uttar Pradesh',
    30: 'Uttarakhand',
    31: 'West Bengal',
    0: 'Total'
}

max = {
    'Andhra Pradesh': 0,
    'Arunachal Pradesh': 0,
    'Assam': 0,
    'Bihar': 0,
    'Chhattisgarh': 0,
    'Delhi': 0,
    'Goa': 0,
    'Gujrat': 0,
    'Haryana': 0,
    'Himachal Pradesh': 0,
    'Jammu and Kashmir': 0,
    'Jharkhand': 0,
    'Karnataka': 0,
    'Kerela': 0,
    'Ladakh': 0,
    'Madhya Pradesh': 0,
    'Maharashtra': 0,
    'Manipur': 0,
    'Meghalaya': 0,
    'Mizoram': 0,
    'Nagaland': 0,
    'Odisha': 0,
    'Punjab': 0,
    'Rajasthan': 0,
    'Sikkim': 0,
    'Tamil Nadu': 0,
    'Telangana': 0,
    'Tripura': 0,
    'Uttar Pradesh': 0,
    'Uttarakhand': 0,
    'West Bengal': 0,
    'Total': 0
}

pops = {
    'Andhra Pradesh': 49577103,
    'Arunachal Pradesh': 1383727,
    'Assam': 31205576,
    'Bihar': 104099452,
    'Chhattisgarh': 25545198,
    'Delhi': 16787941,
    'Goa': 1458545,
    'Gujrat': 60439692,
    'Haryana': 25351462,
    'Himachal Pradesh': 6864602,
    'Jammu and Kashmir': 12267032,
    'Jharkhand': 32988134,
    'Karnataka': 61095297,
    'Kerela': 33406061,
    'Ladakh': 274000,
    'Madhya Pradesh': 72626809,
    'Maharashtra': 112374333,
    'Manipur': 2570390,
    'Meghalaya': 2966889,
    'Mizoram': 1097206,
    'Nagaland': 1978502,
    'Odisha': 41974219,
    'Punjab': 27743338,
    'Rajasthan': 68548437,
    'Sikkim': 610577,
    'Tamil Nadu': 72147030,
    'Telangana': 35003674,
    'Tripura': 3673917,
    'Uttar Pradesh': 199812341,
    'Uttarakhand': 10086292,
    'West Bengal': 91276115,
}

days = 0
while days < len(lines):
    line = lines[days]
    if days == 0:
        days = 1
        continue
    dat = line.split(',')
    for i in range(2, 34):
        if max[st_code[i-2]] < int(dat[i]):
            max[st_code[i - 2]] = int(dat[i])
        data[st_code[i-2]].append(int(dat[i]))
    days = days + 3

f = open('data.pkl', 'wb')
pickle.dump(data, f)
f.close()

f = open('max.pkl', 'wb')
pickle.dump(max, f)
f.close()

f = open('codes.pkl', 'wb')
pickle.dump(st_code, f)
f.close()

f = open('pop.pkl', 'wb')
pickle.dump(pops, f)
f.close()


# plt.plot(data['Total'])
# plt.show()


