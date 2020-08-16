import util.main.loginUtil as loginUtil
from util.emailClass import Email
from util.labelAssociatedMail import getLabelAssociatedMail

def main():
    s = loginUtil.login()

    mailList = getLabelAssociatedMail(s, "Schools/Other")
    uniqueSenders = []
    for mail in mailList:
        if not mail.sender[0] in (mail_.sender[0] for mail_ in uniqueSenders) and not mail.sender[1] in (mail_.sender[1] for mail_ in uniqueSenders):
            uniqueSenders.append(mail)

    print("{0} mail senders found as duplicate".format(len(mailList) - len(uniqueSenders)))
    print("{0} unique senders".format(len(uniqueSenders)))
    file = open(r"senders.txt","w")
    for mail in uniqueSenders:
        if not str(mail.sender[1]).strip()=='':
            file.write(mail.sender[1])
        else:
            file.write("[] " + mail.sender[0])
        file.write('\n')
    file.flush()
    file.close()

if __name__ == '__main__':
    main()