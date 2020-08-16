import util.main.loginUtil as loginUtil
from util.emailClass import Email
from util.allMail import getAllMail

file = open(r"maildata.outp","w")

def mailRecieved(mail, i, t):
    file.write('[split3]'.join(mail.sender))
    file.write('[split2]')
    file.write(mail.message)
    file.write('[split]')
    file.flush()
    print("mail [{0}/{1}]  {2}%".format(i, t, int(i/t)))

def mailEnd(mailList):
    file.close()


def main():
    s = loginUtil.login()
    mailList = getAllMail(s, mailRecieved, mailEnd, True)
    print("{0} mail saved".format(len(mailList)))
    


if __name__ == '__main__':
    main()