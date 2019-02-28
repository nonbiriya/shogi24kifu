import Shogi24Lib

class downloadKifu:
    #ログイン処理
    def login(self):
        iniinfo = Shogi24Lib.inifile()
        self._shogi24login = None
        if iniinfo.readIniFile():
            self._shogi24login = Shogi24Lib.login(iniinfo.getUserName,iniinfo.getUserPass)
        else:
            username = Shogi24Lib.defaultInput.inputID()
            password = Shogi24Lib.defaultInput.inputPass()
            self._shogi24login = Shogi24Lib.login(username,password)
        return shogi24login.getSession()

    #検索して、ログイン者のIDを取得する
    def setUserId(self,session):
        self._searchUser = Shogi24Lib.searchUSer(session)
        self._searchUser.search(self._shogi24login.getUserName())
        return self._searchUSer.getMatchId(self._shogi24login.getUserName())
        

    #スクレイピング
    def doScraping(self,session,userID):
        kifulistpage = Shogi24Lib.kifuListPage()
        kifulistpage.setId(userID)
        kifulistpage.getListPage()
        return kifulistpage.scrapingListPage()



    #棋譜取得
    def getKifu(self):
        pass

if __name__ == "__main__":
    dwnkifu = downloadKifu()
    session = dwnkifu.login()

#kishi = Shogi24Lib.kifuListPage(session)
#kishi.setId("147126")
#page = kishi.getListPage()
#kishi.scrapingListPage()

#print(kishi.getResultList())

su = Shogi24Lib.searchUser(session)
su.search("test")
resultList = su.getMemberSearchResultList()
for result in resultList:
    print(getUserName())