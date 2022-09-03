import requests
import csv

def write_to_csv(data):
    with open('data.csv', 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)

HEADER = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
}
write_to_csv(['id', 'location_address', 'TotalAssessedValue', 'owners', 'BillingAddress', 'State', 'ZipCode', 'Neighborhood'])

url = 'https://property.spatialest.com/nc/mecklenburg/api/v1/recordcard/{}'

for index in range(1, 101):
    r = requests.get(url.format(index), headers=HEADER)
    res = r.json()
    try:
        if 'error' in res:
            continue
        id = res['id']
        location_address = res['parcel']['header']['location_address']
        TotalAssessedValue = res['parcel']['header']['TotalAssessedValue']
        owners = res['parcel']['header']['owners']
        BillingAddress = res['parcel']['header']['BillingAddress']
        State = res['parcel']['header']['State']
        ZipCode = res['parcel']['header']['ZipCode']
        Neighborhood = res['parcel']['header']['Neighborhood']
        data = [id, location_address, TotalAssessedValue, owners, BillingAddress, State, ZipCode, Neighborhood]
        write_to_csv(data)
        print('Success: ', id)
    except Exception as e:
        print(index, e)
        continue
