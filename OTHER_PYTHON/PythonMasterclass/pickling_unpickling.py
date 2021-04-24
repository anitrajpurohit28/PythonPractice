# import pickle
#
# should always unpickle in same order as pickled
# imelda = ('More Mayhem',
#           'IMelda May',
#           '2011',
#           ((1, 'Pulling the Rug'),
#            (2, 'Psycho'),
#            (3, 'Mayhem'),
#            (4, 'Kentish Town Waltz')))
#
# print("Before pickling:\n", imelda)
# # 1. storing the pickled contents in file imelda.pickle
# with open("imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file)
#
# # 2. fetch the pickled entry by pickle.load
# with open("imelda.pickle", "rb") as imelda_pickled:
#     unpickled_imelda = pickle.load(imelda_pickled)
#
# print("After unpickling:\n", unpickled_imelda)
# album, artist, year, track_list = unpickled_imelda
# print("Album: {}\nArtist: {}\nYear: {}".format(album, artist, year))
# for track in track_list:
#     print("{}: {}".format(track[0], track[1]))


import pickle

imelda = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))
random_number = 987654321

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump(random_number, pickle_file)

with open("imelda.pickle", "rb") as pickled_file:
    imelda_unpickled = pickle.load(pickled_file)
    even_unpickled = pickle.load(pickled_file)
    odd_unpickled = pickle.load(pickled_file)
    random_number_unpickled = pickle.load(pickled_file)

print("Unpickled files are:")
print("Imdlda: {}\neven: {}\nodd: {}\nRandomNumber: {}".format(
    imelda_unpickled, even_unpickled, odd_unpickled, random_number_unpickled))

