# import glob
# import pandas as pd



import glob
import inquirer
import pandas as pd

def merge_csv(allFiles, path):
    combined = pd.DataFrame()

    for file_ in allFiles:
        try:
            df = pd.read_csv(file_)
            combined = pd.concat((df, combined), axis=0)
            print(f'Imported {file_}')
        except: 
            print(f'Error while importing file: {file_}')
    
    combined.to_csv(path+"/merged.csv")
    print('DONE...')
    
def merge_xlsx(allFiles, path):
    combined = pd.DataFrame()

    for file_ in allFiles:
        try:
            df = pd.read_excel(file_)
            combined = pd.concat((df, combined), axis=0)
            print(f'Imported {file_}')
        except: 
            print(f'Error while importing file: {file_}')
            
    combined.to_csv(path+"/merged.csv")
    print('DONE...')
    

questions = [
    inquirer.Text("path", message="Path of folder containing files"),
    inquirer.List("type", message="What type of files to merge? ", choices=[".csv", ".xlsx"])
]
answers = inquirer.prompt(questions)

allFiles = glob.glob(f'{answers["path"]}/*{answers["type"]}')
print(f'Found {len(allFiles)} files')

if answers["type"] == ".csv":
    merge_csv(allFiles, answers["path"])
elif answers["type"] == ".xlsx":
    merge_xlsx(allFiles, answers["path"])
else:
    print("Filetype is not supported")
