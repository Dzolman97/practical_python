acronyms = {'IDK': "I don't know",
            'SMH': "Shaking my Head",}

acronyms['LOL'] = 'Laugh out Loud'
acronyms['TBH'] = 'To Be Honest'

defenition = str(input("What acronym are you trying to figure out?\n"))

print(defenition, "means", acronyms[defenition])