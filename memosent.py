from quick_start import *
import re

def simplify(sentence):
    sentence = sentence.lower()
    # remove multiple whitespaces
    sentence = re.sub(' +', ' ', sentence)
    # remove special characters
    sentence = re.sub('[^\w\d\s]+', '', sentence)
    return sentence


def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1BdcWwp4NB3WjGOdvuGiUuH19Au2QrPH2JqFfttxRKiI'
    rangeName = 'memorize!A2:C'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values:
            res = input(f'{row[0]} >>> ')
            if simplify(res) == simplify(row[1]):
                print("CORRECT!")
            else:
                print("Incorrect. It should be: "+row[1])


if __name__ == '__main__':
    main()
