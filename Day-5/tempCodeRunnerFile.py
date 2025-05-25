    def characterReplacement(self, s: str, k: int) -> int:
        longestseq=0
        s=list(s)
        win=[]
        print(win)
        for i in range(0,len(s)-1):
            print(win)
            if s[i] != s[i+1]:
                s[i+1]=s[i]
                print(win)