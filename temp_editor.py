import csv

class Editor():
    def write (variable, value):
        with open('temp_file.csv', 'w') as file:
            w = csv.DictWriter(file, fieldnames=['variable', 'value'], delimiter='\t') #open the csv in reader mode with fieldnames association for the rows
            w.writeheader() #affiche les fieldanmes dans le csv
            w.writerow({'variable': variable, 'value': value})
            print('done')

    def read (variable):
        with open('temp_file.csv', 'r') as file:
            r = csv.DictReader(file, delimiter='\t') #open the csv in reader mode with fieldnames association for the rows
            next(r) #skip the first line with the headlines
            for line in r :
                if line['variable'] == variable : #look for the variable trought the csv file
                    return line['value']
    
    def reset (): # Reset the csv temp file
        with open('temp_file.csv') as file:
            for line in file:
                del line



if __name__ == '__main__':
    Editor.reset()
    #Editor.write('oui','non')
    #Editor.read('oui')
