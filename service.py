class Bot:
    def __init__(self, name, replies):
        self.name=name
        if isinstance (replies, dict):
            self.replies=replies
        elif isinstance (replies, str):
            repliesDict=dict()
            file=open(replies, "r")
            while True:
                line=file.readline()
                if line:
                    fragments=line.split("#")
                    #fragments[0]=fragments[0].lower()
                    repliesDict[fragments[0].lower()]=fragments[1]
                else:
                    break
            self.replies=repliesDict
            
  
    def replyTo(self, message):
        if message in self.replies:
            return self.replies[message]
        else:
            return "I can't understand you.'"


