country_code = {'India' : '0091',
                'Australia' : '0025',
                'Indonesia' : '0062'
                }

#search dictionary for country code of India
print("Country code for India -")
print(country_code.get('India', 'Not Found'))

print()

#search dictionary for county code of Japan
print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))