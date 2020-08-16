import base64
import email


import util.reqUtilCommon as ruc
from util.emailClass import Email
from util.mailProcessing import processMail


def getAllMail(s, func, end, all):

    messages, pagecount = ruc.getMessages(s)
    print('searched through {0} pages'.format(pagecount))
    print('{0} messages found'.format(len(messages)))

    mailList = []
    size = len(messages)
    for index in range(size):
        mail = processMail(s, messages[index], all)
        if mail==None:
            continue
        mailList.append(mail)
        if func!=None:
            func(mail, index, size)
    end(mailList)


   
