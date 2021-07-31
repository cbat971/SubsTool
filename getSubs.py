from youtube_transcript_api import YouTubeTranscriptApi
import urlexpander

subWordList = []
print('ready')
#https://www.youtube.com/watch?v=R2XaBhsB2mE&ab_channel=BadFriends
#https://youtu.be/R2XaBhsB2mE

#https://www.youtube.com/watch?v=tEdRBA588V8&ab_channel=TigerBelly


def isolateVidID(input):
    try:
        z = urlexpander.expand(input)
        z = z.split('v=')
        z = z[1].split('&ab')
        z = z[0]
    except:
        z = input
    return z
videoId = "This is the ID of the youtube video you are searching for"
fullSubs = ""
def getSubs(videoURL):
    global fullSubs
    global videoID
    videoID = isolateVidID(videoURL)
    try:
        fullSubs = YouTubeTranscriptApi.get_transcript(videoID)   
        for x in fullSubs:
            for y in x:
                if type(x[y]) == str:
                    subWordList.append(x[y])
        subParagraph = ''              
        for x in subWordList:
            subParagraph = subParagraph + ' ' + x
        return (subParagraph)
    except:
        print("Subs for this are not possible")




resultsString = []
def getResultsString(new_addition):
    global resultsString
    if len(resultsString) < 30:
        resultsString.append(new_addition)
    else:
        resultsString.append(new_addition)
        resultsString = resultsString[1:]
    results_in_string = ' '.join(resultsString)
    return results_in_string


# url is https://www.youtube.com/watch?v=UccTT8bKmc0&t=2712s
url = input("Enter URL of YouTube video you would like to search.")
# url = 'https://www.youtube.com/watch?v=AHYm2uDtGIs&ab_channel=ComicsExplained'
url = str(url)
subs = (getSubs(url))
# print(subs)
def getSearchTerms(term):
    subs_broken = subs.split(' ')
    placement=0
    findAny = False
    for each in subs_broken:
        phraseToReturn = getResultsString(each)
        placement+=1
        if str(term) in each:
            findAny = True
            print(phraseToReturn)
            print('searching...')
            print('searching...')
            print('searching...')
            result = (' '.join(subs_broken[placement-30:placement+20]))
            print(result)
            test1 = (result[0:11])
            test2 = (result[11:22])
            test3 = (result[25:37])

            for each in fullSubs:
                if test1 in each['text']:
                    print(each)
                    print("https://youtu.be/" + str(videoID) + "?t=" + str(int(each['start'])))
                elif  test2 in each['text']:
                    print(each)
                    print("https://youtu.be/" + str(videoID) + "?t=" + str(int(each['start'])))
                elif  test3 in each['text']:
                    print(each)
                    print("https://youtu.be/" + str(videoID) + "?t=" + str(int(each['start'])))

    if findAny == False:
        print("Sorry, but nothing was found.")

            


# print(subParagraph)
# END getSubs()

getSearchTerms(input("What would you like to look for?  "))

print(videoID)
#find words or phrases in the subs (possibly subParagraph so that the entire thing is available)

