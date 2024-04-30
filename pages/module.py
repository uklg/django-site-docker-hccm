#!/usr/bin/python3

import boto3

class Send():


#    def __init__(self, submit_name,submit_email,submit_number,submit_message): 
#        self.submit_name=submit_name
#        self.submit_email=submit_email
#        self.submit_number=submit_number
#        self.submit_message=submit_message


    def getsendmailapikey(self):
        fd=open('aws.env','r')
        keyline=fd.readlines()[0].strip()
        delimiter=":"

        splitkey=keyline.split(delimiter)
        keyid=splitkey[0].strip()
        keypass=splitkey[1].strip()
        return(keyid,keypass)


    def sendmessage(self,submit_name='mo',submit_email='''j@d.com''',submit_number='07', submit_message='hi'):

          try:
              creds=self.getsendmailapikey()
              client = boto3.client(
                  'ses',
                  region_name='eu-north-1',
                  aws_access_key_id=creds[0],
                  aws_secret_access_key=creds[1]
              )


              response = client.send_email(
                  Destination={
                      'ToAddresses': ['richmurdo@gmail.com','hollycaston@googlemail.com'],
                  },
                  Message={
                      'Body': {
                          'Text': {
                              'Charset': 'UTF-8',
                              'Data': f"Name: {submit_name} \nFrom email: {submit_email}\n \
                               {submit_number}\n{submit_message}",
                          },
                      },
                      'Subject': {
                          'Charset': 'UTF-8',
                          'Data': 'From hollyschildminding website',
                      },
                  },
                  Source='sender@saturdaynightdj.co.uk',
              )




           #   print(respons)
          except Exception as e:
              print(e)
              #print(e.message)



    def send(self):
        self.sendmessage
     
    

#emp = send("a","b","c","d")

