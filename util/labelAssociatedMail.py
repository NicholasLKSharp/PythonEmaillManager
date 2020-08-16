import base64
import email


import util.reqUtilCommon as ruc
from util.emailClass import Email


def getLabelAssociatedMail(s, labelname):
    labels = ruc.getLabels(s)

    selectedlabel = next(
        (x for x in labels if x['name'] == labelname), None)

    messages, pagecount = ruc.getMessagesByLabel(
        s, [selectedlabel['id']])
    print('searched through {0} pages'.format(pagecount))
    print('{0} messages found'.format(len(messages)))

    mailList = []
    for index in range(len(messages)):
        msgbasic = messages[index]
        print(str(index+1) + "/" + str(len(messages)))
        message = ruc.getMessage(s, msgbasic['id'])
        msg_str = base64.urlsafe_b64decode(
            message['raw'].encode("utf-8")).decode("utf-8")
        mime_msg = email.message_from_string(msg_str)
        i = 0
        try:
            payload = mime_msg.get_payload(i)
        except:
            continue
        output = ""

        while(payload != None):
            p_type = payload.get('Content-Type')
            if p_type[:p_type.index(';')] == 'text/plain':
               output += str(payload)
               output = output[output.index('\n'):]
            i += 1
            try:
                payload = mime_msg.get_payload(i)
            except:
                break

        fromval = str(mime_msg.get('from'))
        fromaddr = fromval[fromval.index('<')+1:fromval.index('>')]
        fromname = fromval.replace(fromaddr, '')[:-2]
        fromname = fromname.lstrip(' ').rstrip(' ')[1:-1]
        mail = Email(msgbasic['id'],[fromaddr,fromname],output)
        mailList.append(mail)
    return mailList


   
