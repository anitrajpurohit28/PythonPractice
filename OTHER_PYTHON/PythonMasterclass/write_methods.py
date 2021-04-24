# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("cities.txt", "w") as city_file_obj:
#     for city in cities:
#         print(city, file=city_file_obj)



# cities = []
# with open("cities.txt", "r") as city_file_obj:
#     for city in city_file_obj:
#         cities.append(city.strip())
#
# print(cities)
# for city in cities:
#     print(city)




# imelda = "More Mayhem", "Imelda MAy", "2011", (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# with open("imelda_text.txt", "w") as imelda_file_obj:
#     print(imelda, file=imelda_file_obj)




# with open("imelda_text.txt", "r") as imelda_file_obj:
#     contents = imelda_file_obj.read()
# print(contents)
#
# recreated_obj = eval(contents)
# print(recreated_obj)
# print(type(recreated_obj))
#
# title, artist, year, tracks = recreated_obj
# print(f"Title: {title} Artist: {artist} Year: {year}")
# for each_track in tracks:
#     print(f"{each_track[0]}: {each_track[1]}")
