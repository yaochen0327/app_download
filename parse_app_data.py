import json





f = open("app_ranking_list_json", "r")

soup = json.load(f)



f.close()

print(soup)


