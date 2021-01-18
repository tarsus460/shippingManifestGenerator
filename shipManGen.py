import csv,re

issueList = {1:'broken screen',2:'broken keyboard'}

tagModels = [('.*33','Dell 3100'),('P20.*','Lenovo 300e'),('.*962','Dell Chromebook 11'),
             ('5CD026.*','HP Chromebook x360'),('5CD.*','HP Chromebook 11/14'),
             ('MP1.*','Lenovo Chromebook 14e'),('LR0.*','Lenovo N42')]

def lookups(s,directory):
        for pattern,device in directory:
                if re.search(pattern,s):
                        return device
        return input('Model: ')

def lineWriter():
        assetTag = input('AssetTag: ')
        model = lookups(assetTag,tagModels)
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
