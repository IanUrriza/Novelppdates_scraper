
## Scraper
    # Series Finder with Latest Update as sort
    # Start from the last novel
    # Catch non-english characters (probably non utf-8)
    # Limit to 5 simultaneous novel requests
    # multiple requests to browse the uploaded chapters (check if there's one call that shows everything and bypass pagination)
    # How to add failsafes
## Pandas processing 
    # is this really required?
    # just create an object to hold everything? then pass to SQLalchemy?
# SQL alchemy for saving
    # Connect app to db
    # Separate file for initialization
    # Separate file for credentials? such as dbname uname pass
    # Create tables
    # Create inserts that catches the data available
##   - Data available
    #       - Novel
        #       - Title
        #       - Description
        #       - Type *
        #       - Language *
        #       - Year *
        #       - Status in COO (Full Text)
        #       - isLicensed
        #       - isCompletelyTranslated
#       - Novel_Stats
    #       - novelId
    #       - All Time Rank (Activity)
    #       - All Time Rank (Reading List)
    #       - Reading List Counter
    #       - Release Frequency
#       - Releases
    #       - releaseId
    #       - novelId
    #       - groupId
    #       - Date
    #       - releaseChapter

#       - Alternative Names
    #       - novelId
    #       - altName

#       - Author
    #       - authorId
    #       - authorName

#       - Novel-Author
    #       - novelId
    #       - authorId

#       - Artist
    #       - novelId
    #       - artistName

#       - Novel-Artist
    #       - novelId
    #       - artistId

#       - Group
    #       - groupId
    #       - groupName

#       - Novel-Group
    #       - novelId
    #       - groupId

#       - Genre
    #       - genreId
    #       - genreName

#       - Novel-Genre
    #       - novelId
    #       - genreId

#       - Tag
    #       - tagId
    #       - tagName

#       - Novel-Tag
    #       - novelId
    #       - tagId


#       - Original Publisher
    #       - oPubId
    #       - oPubName

#       - Novel-oPublisher
    #       - novelId
    #       - oPubId

#       - English Publisher
    #       - ePubId
    #       - ePubName

#       - Novel-ePublisher
    #       - novelId
    #       - ePubId

#       - Novel-Rating
    #       - novelId
    #       - oneVotes
    #       - twoVotes
    #       - threeVotes
    #       - fourVotes
    #       - fiveVotes
    #       - totalVotes
    #       - averageRating
