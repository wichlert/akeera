'''
Created on Nov 20, 2018

@author: akeera

/* fb msg bot */ 
0. pip install fbchat

1. find fb numberic id 
https://findmyfbid.com
ex. https://www.facebook.com/akeera.smart
case. open external can search

2. input fb client login and password
3. input thread_id (fb numberic id)
 
'''
from fbchat import Client
from fbchat.models import*
client = Client('wich007@htomail.com', 'Ake0855581411')
for x in range(10):

 print('Own id: {}'.format(client.uid))
 client.send(Message(text='bug akeera life 555!'), thread_id=1061839802, thread_type=ThreadType.USER)
client.logout()