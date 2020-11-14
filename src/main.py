import search_engine

text = 'The Deaconess of the Favonius Church and a shining starlet adored by all. Although the concept of a starlet is rather novel in a city of bards, the people of Mondstadt love Barbara nonetheless.'
hasil = search_engine.stemming(text)
print(hasil)