#import pandas as pd
import gspread as gs

gc = gs.service_account(filename='/Users/jose.pacheco/Downloads/service_account.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/15iz8QdhY-ffwIeJXDBvYwKiQNbtC_pTUUhI8ZHLJzZM/edit?usp'
                    '=sharing')


# sh = gc.open("ZAPAS")

# ws = sh.worksheet('ZAPAS')
# df = pd.DataFrame(ws.get_all_records())
# df.head()

# wks = sh.worksheet("ZAPAS")

# print(wks.get_all_records())

class pull_info_action1:
    id = 1
    wks = sh.worksheet("ZAPAS")
    print(wks.get_all_records())
