import utils

#Association detection of words in messages

message_list = ["merhaba bugün buluşalım",
                "bugün nerede buluşalım",
                "bugün dünden daha çok sıcak",
                "sıcak günler bizi bekliyor",
                "bugün insanlar nerede",
                "bugün insanlar çok çalışıyor "]

dataset = utils.make_message_fit(message_list)
print("###### Message words ######\n", dataset)

minimum_support = 0.3
minimum_frekans = len(dataset) * minimum_support
assosiation_array, frekans_array = utils.get_association_table(dataset, minimum_frekans=minimum_frekans)

print("Words that are often used together in ", len(dataset), " messages.\n")
for index in range(len(frekans_array)):
    print(assosiation_array[index], ":", frekans_array[index], " times used")


###### Coded by Adem YAĞMURLU #######

