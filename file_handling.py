import os



def create_project_directory(directory):
    '''
     shall create folders based on datatetime.date
    '''
    
    if not os.path.exist(directory):
        print(f'Creating Directory {directory}')
        os.makedirs(directory)
    else:
        print(f'Directory with the name of {directory} already exits')



def create_file(node):
    queue = node + '-queue.txt'
    crawled = node + '-crawled.txt'
    if not os.path.isfile(crawled):
        write_file(crawled)


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
