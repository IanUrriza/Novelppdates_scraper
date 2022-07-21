
import sqlalchemy as db
from sqlalchemy_utils import create_database, database_exists
class DatabaseHandler:
    engine = None
    connection = None
    def __init__(self):
        self.initialize()


    def initialize(self):
        username = "user1"
        password = "michael3096"
        dbName   = "novels"
        self.createConnection(username,password)
        self.createDatabase(dbName)
        self.dropConnection()
        self.useDatabase(dbName)
        self.createTables()

    def createConnection(self,username,password):
        self.engine = db.create_engine("mysql+pymysql://user1:michael3096@localhost")
        self.connection = self.engine.connect()

    def createDatabase(self,dbName):
        try:
            self.connection.execute("CREATE DATABASE {}".format(dbName))
        except:
            self.connection.execute("DROP DATABASE {}".format(dbName))
            self.connection.execute("CREATE DATABASE {}".format(dbName))
    def dropConnection(self):
        self.connection.close()
        self.engine.dispose()
    def useDatabase(self,dbName):
            self.engine = db.create_engine("mysql+pymysql://user1:michael3096@localhost/{}?charset=utf8mb4".format(dbName))
            self.connection = self.engine.connect()        
    def createTables(self):

        metadata = db.MetaData()

        Novel = db.Table( 'Novel',metadata,
            db.Column('novelId',                db.Integer(),   primary_key=True),
            db.Column('title',                  db.String(100)),
            db.Column('type',                   db.String(5)),
            db.Column('year',                   db.Integer()),
            db.Column('status',                 db.String(30)),
            db.Column('isLicensed',             db.Boolean()),
            db.Column('isCompletelyTranslated', db.Boolean())
        )

        Novel_Stats = db.Table( 'NovelStats',metadata,
            db.Column('novelId',                        db.Integer(),   db.ForeignKey("Novel.novelId"), nullable = False),
            db.Column('all time rank (Activity)',       db.Integer()),
            db.Column('all time rank (Reading List)',   db.Integer()),
            db.Column('reading list counter',           db.Integer()),
            db.Column('release frequency (Days)',       db.Integer()),
        )

        Releases = db.Table( 'Releases', metadata,
            db.Column('releaseId',                      db.Integer(),   primary_key=True),
            db.Column('novelId',                        db.Integer(),   db.ForeignKey("Novel.novelId"), nullable = False),
            db.Column('groupId',                        db.Integer(),   db.ForeignKey("Group.groupId"), nullable = False),
            db.Column('date',                           db.Date()),
            db.Column('releaseChapter',                 db.String(20))
        )

        Group = db.Table ("Group", metadata,
            db.Column('groupId',                      db.Integer(),   primary_key=True),
            db.Column('groupName',                    db.String(50))            
        )

        Novel_Group = db.Table("Novel_Group", metadata,
            db.Column('novelId',                        db.Integer(),   db.ForeignKey("Novel.novelId"), nullable = False),
            db.Column('groupId',                        db.Integer(),   db.ForeignKey("Group.groupId"), nullable = False),
            db.UniqueConstraint('novelId','groupId', name='uix_1')
        )

        Alternative_Names = db.Table("Alternative_Names", metadata,
            db.Column('novelId',                        db.Integer(),   db.ForeignKey("Novel.novelId"), nullable = False),
            db.Column('altName',                        db.String(100))
        )
        
        Author = db.Table("Author", metadata,
            db.Column('authorId',                      db.Integer(),   primary_key=True),
            db.Column('authorName',                    db.String(50))                   
        )

        Novel_Author = db.Table("Novel_Author", metadata,
            db.Column('novelId',                        db.Integer(),   db.ForeignKey("Novel.novelId"), nullable = False),
            db.Column('authorId',                       db.Integer(),   db.ForeignKey("Author.authorId"), nullable = False),
            db.UniqueConstraint('novelId','authorId', name='uix_2')
        )

        Artist = db.Table("Artist", metadata,
            db.Column('artistId',                      db.Integer(),   primary_key=True),
            db.Column('artistName',                    db.String(50))                   
        )

        Novel_Artist = db.Table("Novel_Artist", metadata,
            db.Column('novelId',                        db.Integer(),   db.ForeignKey("Novel.novelId"), nullable = False),
            db.Column('artistId',                       db.Integer(),   db.ForeignKey("Artist.artistId"), nullable = False),
            db.UniqueConstraint('novelId','artistId', name='uix_3')
        )

        Genre = db.Table("Genre", metadata,
            db.Column('genreId',                      db.Integer(),   primary_key=True),
            db.Column('genreName',                    db.String(50))                   
        )

        Novel_Genre = db.Table("Novel_Genre", metadata,
            db.Column('novelId',                        db.Integer(),   db.ForeignKey("Novel.novelId"), nullable = False),
            db.Column('genreId',                        db.Integer(),   db.ForeignKey("Genre.genreId"), nullable = False),
            db.UniqueConstraint('novelId','genreId', name='uix_4')
        )

        Tag = db.Table("Tag", metadata,
            db.Column('tagId',                      db.Integer(),   primary_key=True),
            db.Column('tagName',                    db.String(50))                   
        )

        Novel_Tag = db.Table("Novel_Tag", metadata,
            db.Column('novelId',                        db.Integer(),   db.ForeignKey("Novel.novelId"), nullable = False),
            db.Column('tagId',                          db.Integer(),   db.ForeignKey("Tag.tagId"), nullable = False),
            db.UniqueConstraint('novelId','tagId', name='uix_5')
        )

        OPub = db.Table("Original_Publisher", metadata,
            db.Column('oPubId',                      db.Integer(),   primary_key=True),
            db.Column('oPubName',                    db.String(50))                   
        )

        Novel_oPublisher = db.Table("Novel_oPublisher", metadata,
            db.Column('novelId',                        db.Integer(),   db.ForeignKey("Novel.novelId"), nullable = False),
            db.Column('oPubId',                         db.Integer(),   db.ForeignKey("Original_Publisher.oPubId"), nullable = False),
            db.UniqueConstraint('novelId','oPubId', name='uix_6')
        )

        EPub = db.Table("English_Publisher", metadata,
            db.Column('ePubId',                      db.Integer(),   primary_key=True),
            db.Column('ePubName',                    db.String(50))                   
        )

        Novel_ePublisher = db.Table("Novel_ePublisher", metadata,
            db.Column('novelId',                        db.Integer(),   db.ForeignKey("Novel.novelId"), nullable = False),
            db.Column('ePubId',                         db.Integer(),   db.ForeignKey("English_Publisher.ePubId"), nullable = False),
            db.UniqueConstraint('novelId','ePubId', name='uix_7')
        )

        Novel_Rating = db.Table("Novel_Rating", metadata,
            db.Column('novelId',                          db.Integer(),   db.ForeignKey("Novel.novelId"), nullable = False),
            db.Column('oneVote',                          db.Integer()),
            db.Column('twoVote',                          db.Integer()),
            db.Column('threeVote',                        db.Integer()),
            db.Column('fourVote',                         db.Integer()),
            db.Column('fiveVote',                         db.Integer()),
            db.Column('totalVote',                        db.Integer()),
            db.Column('averageRating',                    db.Integer())
        )

        metadata.create_all(self.engine)
       
    # def insertNewNovel(self,data):

    # def insertLog(self):

    
DatabaseHandler()