def rankResults(results):
    profDict = {}
    # loop through results list
    for prof in results:
        name = prof[0]
        area = prof[1]
        profid = prof[2]
        # check if key is in dictionary
        if name in profDict:
            profDict[name].append(area)
        # if not then create new pair and set value to 0
        else:
            profDict[name] = [profid, area]
    # sort the dictionary based on values
    profDict = sort_by_values_len(profDict)
    # return dictionary
    return(profDict)


#taken from stack overflow
def sort_by_values_len(dict):
    dict_len= {key: len(value) for key, value in dict.items()}
    import operator
    sorted_key_list = sorted(dict_len.items(), key=operator.itemgetter(1), reverse=True)
    sorted_dict = [{item[0]: dict[item [0]]} for item in sorted_key_list]
    return(sorted_dict)

results = [["kolby", "ai", 3], ["aaron", "ml", 1], ["van", "ml", 2], ["aaron", "ai", 1], ["aaron", "compGraphics", 1], ["van", "compGraphics", 2]]

profDict = rankResults(results)

profList = []
for prof in profDict:
    for key in prof:
        profname = key
        areas = prof[profname][1:]
        profid = prof[profname][0]
    info = [profname, areas, profid] #create a list for the prof
    profList.append(info)

print(profList)
