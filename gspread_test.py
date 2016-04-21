# Should handle "httplib2.ServerNotFoundError: Unable to find the server at www.googleapis.com" 
# In a try/catch by waiting and attempting the connection again.

# Note: this spreadsheet needed to be shared with the client_email field from the json file

import webapp2
import gspread
from oauth2client.service_account import ServiceAccountCredentials 

SCOPES = ['https://spreadsheets.google.com/feeds']

class GssHandler(webapp2.RequestHandler):
  def get(self):
    credentials = ServiceAccountCredentials.from_json_keyfile_name('WFServices-bae6f3ace445.json', SCOPES)
    gc = gspread.authorize(credentials)
    wks = gc.open('').sheet1
    #self.response.write(worksheet.acell('B1').value)
    val = wks.acell('B1').value
    print val
    wks.update_acell('A1', 'No way!')
    val = wks.acell('A1').value
    print val
    
  def post(self: 
    credentials = ServiceAccountCredentials.from_json_keyfile_name('WFServices-bae6f3ace445.json', SCOPES) 
    gss_client = gspread.authorize(credentials) 
    gss = gss_client.open_by_key('1EPJWi7O3KxsmIT56gKXoxsNl62pmRWaIOivy69taU3g')
    worksheet = gss.sheet1 
    val = worksheet.acell('B1').value
    print val
    worksheet.update_acell('A1', 'Yeah way!')
    val = worksheet.acell('A1').value
    print val)


t = GssHandler()
t.get()
