#API Key: 6k1nZxqhOx9avPqtfaktM3uXekqb85gS2rLRvJlv# %%import jsonimport requestsimport syssys.argvurl = "https://yfapi.net/v6/finance/quote"stocks = sys.argv[1:]querystring = {"symbols": ','.join(stocks)}headers = {    'x-api-key': "6k1nZxqhOx9avPqtfaktM3uXekqb85gS2rLRvJlv"    }response = requests.request("GET", url, headers=headers, params=querystring)#print(response.text)stock_json = response.json()for i in range(len(stocks)):    print(stock_json['quoteResponse']['result'][i]['longName'] +      ": " + str(stock_json['quoteResponse']['result'][i]['ask']))# %%