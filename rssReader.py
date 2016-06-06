import sys
import chilkat

rss = chilkat.CkRss()

#  Download from the feed URL:
success = rss.DownloadRss("http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml")
if (success != True):
    print(rss.lastErrorText())
    sys.exit()

#  Get the 1st channel.

# rssChannel is a CkRss
rssChannel = rss.GetChannel(0)
if (rssChannel == None ):
    print("No channel found in RSS feed.")
    sys.exit()

#  Display the various pieces of information about the channel:
print("Title: " + rssChannel.getString("title"))
print("Link: " + rssChannel.getString("link"))
print("Description: " + rssChannel.getString("description"))

#  For each item in the channel, display the title, link,
#  publish date, and categories assigned to the post.
numItems = rssChannel.get_NumItems()

for i in range(0,numItems):
    # rssItem is a CkRss
    rssItem = rssChannel.GetItem(i)

    print("----")
    print("Title: " + rssItem.getString("title"))
    print("Link: " + rssItem.getString("link"))
    print("pubDate: " + rssItem.getString("pubDate"))

    numCategories = rssItem.GetCount("category")

    if (numCategories > 0):
        for j in range(0,numCategories):
            print("    category: " + rssItem.mGetString("category",j))
