import requests #pip install requests

chk = 1
while chk >= 1:
    chk = chk + 1
    bin = input("Enter BIN: ")
    request = requests.get("https://bins-su-api.now.sh/api/{}".format(bin))
    status = request.status_code
    print("Status Code: ", status)
    result = request.json()['result']
    if result != True:
        print("\nInvalid BIN\n")
    else:
        response = request.json()['data']
        bin1 = response['bin']
        brand = response['vendor']
        binType = response['type']
        level = response['level']
        bank = response['bank']
        country = response['country']
        print("\nValid BIN✅ \nBIN:" + bin1 + "\nBrand: " + brand + "\nBank: " + bank + "\nLevel: " + level + "\nType: " + binType + "\nCounrty: " + country+"\n")
