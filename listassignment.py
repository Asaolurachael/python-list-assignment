#creating a list of my bestfriends

bestfriends = ["Rejoice"]

bestfriends.append("Fola")
print(bestfriends)

bestfriends.insert(0, "Moyo")
print(bestfriends)

bestfriends.sort()
print(bestfriends)

friends = []

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