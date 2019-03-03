import Shogi24Lib

class downloadKifu:
    def __init__(self):
        pass
    #ログイン処理
    def login(self):
        iniinfo = Shogi24Lib.inifile()
        self._shogi24login = None
        if iniinfo.readIniFile():
            self._shogi24login = Shogi24Lib.login(iniinfo.getUserName(),iniinfo.getUserPass())
            self.setSearchId(iniinfo.getUserName())
        else:
            username = Shogi24Lib.defaultInput.inputID()
            password = Shogi24Lib.defaultInput.inputPass()
            self._shogi24login = Shogi24Lib.login(username,password)
            self.setSearchId(username)
        self._shogi24login.doLogin()
        return self._shogi24login.getSession()
    
    #検索対象のIDを設定
    def setSearchId(self,id):
        self._searchId = id

    #検索して、ログイン者のIDを取得する
    def setUserId(self,session):
        self._searchUser = Shogi24Lib.searchUser(session,self._searchId)
        self._searchUser.search()
        return self._searchUser.getMatchId()
        

    #スクレイピング
    def doScraping(self,session,userID):
        kifulistpage = Shogi24Lib.kifuListPage(session)
        kifulistpage.setId(userID)
        kifulistpage.getListPage()
        return kifulistpage.scrapingListPage()


    #リストから棋譜をファイル出力
    def makeKifuFile(self,resultList):
        Shogi24Lib.kifu(resultList)

if __name__ == "__main__":
    print("将棋倶楽部２４の棋譜をダウンロードします・・・・")
    dwnkifu = downloadKifu()
    session = dwnkifu.login()
    userId = dwnkifu.setUserId(session)
    resultList = dwnkifu.doScraping(session,userId)
    dwnkifu.makeKifuFile(resultList)
