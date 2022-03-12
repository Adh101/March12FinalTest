import pandas as pd

columns = ['rownum', 'firstname', 'lastname', 'email', 'Email Pattern']
df = pd.DataFrame(columns=columns)
dff = []
with open("C:/Users/Atish/Downloads/intelligentguessingdataset.csv", "r") as file:
    text_data = file.read()
    strings = text_data.split("\n")
    lst = list()
    for eachdata in strings:
        lst.append(eachdata)
    lastname = []
    for i in lst:
        lastname.append(i.split(",")[2].replace(" ", ""))
    for eachlst in lst[23:]:
        eachlstdata = eachlst.split(",")
        rownum = eachlstdata[0]
        first_name = eachlstdata[1]
        last_name = eachlstdata[2]
        emails = eachlstdata[3]
        email = emails.split('@')[0]
        pattern = ''
        if '.' in email:
            emsplit = email.split(".")
            first_name = ''.join(e for e in first_name if e.isalnum())
            if first_name == emsplit[0] and last_name == emsplit[1] or first_name == '' and last_name == emsplit[1]:
                pattern = ''.join([pattern, '<11>', '<22>'])
            elif first_name == emsplit[0] and last_name.replace(" ", "") == emsplit[
                1] or first_name == '' and last_name.replace(" ", "") == emsplit[1]:
                pattern = ''.join([pattern, '<11>', '<20><21>'])
            elif last_name:
                if first_name == emsplit[0] and last_name.split(' ')[0] == emsplit[1]:
                    pattern = ''.join([pattern, '<11>', '<20>'])
                elif first_name == emsplit[0] and last_name.split(' ')[1] == emsplit[1]:
                    pattern = ''.join([pattern, '<11>', '<21>'])
            elif first_name == emsplit[0] and last_name == '' and emsplit[1] in lastname:
                pattern = ''.join([pattern, '<11>', '<20><21>'])
            else:
                print('error')
        else:
            sum = 0
            for i in email:
                for j in first_name:
                    if i == j:
                        sum += 1
                break
            pattern = ''.join([pattern, '<11-f', str(sum), 'l>', '<22>'])

        df = pd.DataFrame([[rownum, first_name, last_name, emails, pattern]], columns=columns)
        dff.append(df)
df = pd.concat(dff)
df.to_csv("problemset1_submission.csv", index=False)