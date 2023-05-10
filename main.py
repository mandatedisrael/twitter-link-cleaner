#!/usr/bin/python3

totalTweets = 0
with open("oldLinks.txt", 'r') as openedFile:
    oldLinks = openedFile.readlines()
with open("newLinks.txt", "w") as newUpdatedLinks:
    for link in oldLinks:
        if link != "\n":
            totalTweets += 1
            shortenedLink = link.split('?')[0]
            newUpdatedLinks.writelines(shortenedLink)
            newUpdatedLinks.write("\n")
        else:
            continue


print(totalTweets,"links has been cleaned up!")
print("All done!")