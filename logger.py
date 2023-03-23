from datetime import datetime

def logging(result):
    with open ('log.txt', 'a') as output_file:
        data = datetime.now().strftime('%Y.%m.%d %H::%M:%S   ')
        output_file.writelines(f'{data} {result}\n')