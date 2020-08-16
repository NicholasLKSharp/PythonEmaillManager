import util.reqUtilCommon as ruc
from util.emailClass import Email
from util.mailProcessing import processMail


def getLabelAssociatedMail(s, labelname, func):
    labels = ruc.getLabels(s)

    selectedlabel = next(
        (x for x in labels if x['name'] == labelname), None)

    messages, pagecount = ruc.getMessagesByLabel(
        s, [selectedlabel['id']])
    print('searched through {0} pages'.format(pagecount))
    print('{0} messages found'.format(len(messages)))

    mailList = []
    for index in range(len(messages)):
        mail = processMail(s, messages[index])
        if mail==None:
            continue
        mailList.append(mail)
        if func!=None:
            func(mail)
    return mailList


   
