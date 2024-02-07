import openpyxl
import json

# f_sindh = open('./elections-data-main/NA/sindh.json', encoding="utf8")

with open('./elections-data-main/NA/sindh.json', encoding="utf8") as sindh_file:
    sindh_data = json.load(sindh_file)

    for i in range (190, 249):
        print("Constituency No: ", sindh_data[f"NA-{i}"]["Constituency No"])
        print("Constituency Name: ", sindh_data[f"NA-{i}"]["Constituency Name"])

        for j in sindh_data[f"NA-{i}"]["Candidates"]:
            print("SerialNo: ", j["SerialNo"])
            print("Name in English:" , j["Name in English"])
            print("Name in Urdu: ", j["Name in Urdu"])
            print("Address: ", j["Address"])
            print("Symbol: ", j["Symbol"])
            print("Party: ", j["Party"])
            print("SymbolNo: ", j["SymbolNo"])
            print("symbol_url: ", j["symbol_url"])
            print("\n")
            
        print("\n")
