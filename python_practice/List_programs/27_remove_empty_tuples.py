# 27 Python | Remove empty tuples from a list
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', ''), (), ('', '', '8'),
           (), ('0', '00', '000'), ('birbal', '', '45'), (''), (),  ('', ''), ()
          ]
print(tuples)

# list comprehension
tuples = tuple(t for t in tuples if t)
print(tuples)
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', ''), (), ('', '', '8'),
           (), ('0', '00', '000'), ('birbal', '', '45'), (''), (),  ('', ''), ()
          ]

tuples = tuple(filter(None, tuples))
print(tuples)
