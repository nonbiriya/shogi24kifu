import Shogi24Lib

class downloadKifu:
    def __init__(self):
        pass
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
        self._shogi24login.doLogin()
        return self._shogi24login.getSession()

    #検索して、ログイン者のIDを取得する
    def setUserId(self,session):
        self._searchUser = Shogi24Lib.searchUser(session,self._shogi24login.getUserName())
        self._searchUser.search()
        return self._searchUSer.getMatchId()
        

    #スクレイピング
    def doScraping(self,session,userID):
        kifulistpage = Shogi24Lib.kifuListPage()
        kifulistpage.setId(userID)
        kifulistpage.getListPage()
        return kifulistpage.scrapingListPage()


    #リストから棋譜をファイル出力
    def makeKifuFile(self,resultList):
        shogi24Lib.kifu(resultList)

if __name__ == "__main__":
    dwnkifu = downloadKifu()
    session = dwnkifu.login()
    userId = dwnkifu.setUserId(session)
    resultList = dwnkifu.doScraping(session,userId)
    makeKifuFile(resultList)
