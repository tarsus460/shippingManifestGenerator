import csv

issueList = {1:'broken screen',2:'broken keyboard'}

def lineWriter():
        assetTag = input('AssetTag: ')
        if assetTag.endswith('33'):
                model = 'Dell 3100'
        elif assetTag.startswith('P20'):
                model = 'Lenovo 300e'
        elif assetTag.endswith('962'):
                model = 'Dell Chromebook 11'
        elif assetTag.startswith('5CD026'):
                model = 'HP Chromebook x360'
        elif assetTag.startswith('5CD'):
                model = 'HP Chromebook 11/14'
        elif assetTag.startswith('MP1'):
                model = 'Lenovo Chromebook 14e'
        elif assetTag.startswith('LR0'):
                model = 'Lenovo N42'
        else:
                model = input('Model: ')
        print(issueList)
        issue = int(input('Issue: '))
        if issue in issueList.keys():
                issue = issueList[issue]
        else:
                issue = issue
        rowList = [assetTag,issue,model]
        with open('shippingManifest.csv','a',newline='') as manifest:
                spam = csv.writer(manifest)
                spam.writerow(rowList)
        prompt = input('Add another device? Y/N ')
        if prompt.upper() == 'Y' or prompt == '':
                lineWriter()
        elif prompt.upper() == 'N':
                print('Drink Coke Play Again.')
        else:
                prompt

with open('shippingManifest.csv','w',newline='') as manifest:
	spam = csv.writer(manifest)
	spam.writerow(['Asset Tag','Issue','Model'])

lineWriter()
