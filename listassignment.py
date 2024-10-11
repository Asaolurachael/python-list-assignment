#creating a list of my bestfriends

bestfriends = ["Rejoice", "Bella", "Shalom", "Tumininu", "Glory"]

bestfriends.append("Fola")
print(bestfriends)

bestfriends.insert(1, "Moyo")
print(bestfriends)

bestfriends.sort()
print(bestfriends)

friends = ["Heritage", "Mercy", "Goodness", "Royal"]

bestfriends.extend(friends)
print(bestfriends)

friends.append("Pemisere") 
friends.append("Timisere")
print(friends)

friends.insert(3, "Desere")
print(friends) 

friends.sort()
print(friends)

print("John" in friends)

print(bestfriends)
print(friends)