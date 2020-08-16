from util.emailClass import Email
import util.reqUtilCommon as ruc

import base64
import email

def processMail(s, msgbasic, all):
    message = ruc.getMessage(s, msgbasic['id'])
    msg_str = base64.urlsafe_b64decode(
    message['raw'].encode("utf-8")).decode("utf-8")
    mime_msg = email.message_from_string(msg_str)
    i = 0
    try:
        payload = mime_msg.get_payload(i)
    except:
        return
    output = ""

    while(payload != None):
        p_type = payload.get('Content-Type')
        if p_type[:p_type.index(';')] == 'text/plain' or all==True:
           output += str(payload)
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
    return mail