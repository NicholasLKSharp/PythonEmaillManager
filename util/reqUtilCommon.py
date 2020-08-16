
def getLabels(service):
    results = service.users().labels().list(userId='me').execute()
    return results.get('labels', [])

def getMessagesByLabel(service, labelids):
    messages = []

    response = service.users().messages().list(userId='me', labelIds=labelids).execute()
    if 'messages' in response:
      messages.extend(response['messages'])
    x = 0
    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId='me', labelIds=labelids,
                                         pageToken=page_token).execute()
      messages.extend(response['messages'])
      x+=1
    return [messages, x]

def getMessages(service):
    messages = []

    response = service.users().messages().list(userId='me').execute()
    if 'messages' in response:
      messages.extend(response['messages'])
    x = 0
    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId='me',
                                         pageToken=page_token).execute()
      messages.extend(response['messages'])
      x+=1
    return [messages, x]

def getMessage(service, msgid):
    return service.users().messages().get(userId='me', id=msgid, format='raw').execute()