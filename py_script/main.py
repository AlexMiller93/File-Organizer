import os
import shutil

source_folder = ''

destination_folder = ''

extensions_dict = {
    'Images': ['.jpg', '.jpeg', '.png', '.ico', '.ps', '.ai', '.bmp', '.gif', '.psd', '.svg', '.tif'],
    'Audio': ['.wav', '.wma','.mp3', '.mpa','.aac', '.adt', '.adts', '.m4a', '.mid', '.midi'],
    'Video': ['.avi', '.mp4', '.vob', '.wmv', '.3g2', '.3gp', '.flv', '.h264', '.mkv', '.mov', '.mpeg', '.rm', '.swf', '.vob', '.wmv'],
    'Documents': ['.doc', '.docx', '.dotx', '.rtf', '.txt', '.pdf', '.odt', '.ppt', '.pptx', '.tex', '.wpd'],
    'Tables': ['.xlsx', '.xls', '.xlsm', '.ods'],
    'Data': ['.csv', '.dat', '.db', '.log', '.mdb', '.sql', '.tar', '.xml'],
    'Emails': ['.email', '.eml', '.emlx', '.msg', '.oft', '.ost', '.pst', '.vcf'],
    'Executable': ['.exe', '.msi', '.apk', '.bat', '.bin', '.com', '.gadget', '.jar', '.wsf'],
    'Archives': ['.zip', '.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.z', '.tar.gz'],
    'Drawings': ['.dwg'],
    'System': ['.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.drv', '.icns', '.ini', '.lnk', '.sys', '.tmp'],
    'Web_development': ['.asp', '.cer', '.cfm', '.cgi', '.html', '.js', '.css', '.jsp', '.part', '.py', '.rss', '.xhtml'],
    'Fonts': ['.fnt', '.fon','.otf', '.ttf']
    }

folders = ['Directories', 'Other staff']


def copy_files_dict(dir_path, dest_path):
    
    """
    Copy files to new folders due to file's extension
    
    1. parse file's extensions
    2. create new dirs from dict
    3. copy files in new dirs
    
    Behind copying:
    /folder/<>.txt or <>.jpg 
    
    <>.txt -> Documents
    <>.jpg -> Images
    etc.
    
    After copying:
    folder/Documents/<filename>.txt
    folder/Images/<filename>.jpg

    Args:
        dir_path (str): path with files
        dest_path (str): path where files will be copied inside new type folders
    """
    
    # all files in directory
    files = os.listdir(dir_path)
    for file in files:
        # split filename and extension
        filename, extension = os.path.splitext(file)
        
        # loop through dict keys (future names of dirs)
        for key in extensions_dict.keys():
            
            # 1. common case: if extension in extensions_dict
            # check extension in dict values            
            if extension in extensions_dict[key]:
                    
                    # check if key dict's dir exists
                    if os.path.exists(dest_path + '/' + key): 
                        # if dir exists move file in this dir
                        shutil.copy(dir_path + '/' + file, dest_path + '/' + key) 
                        
                    # if not exist - > create this dir
                    else:
                        os.mkdir(dest_path + '/' + key)  
                        shutil.copy(dir_path + '/' + file, dest_path + '/' + key) 
                        
            # 2. case: if extension not in extensions_dict
            else:
                if os.path.exists(dest_path + '/' + folders[1]):
                    shutil.copy(dir_path + '/' + file, 
                                dest_path + '/' + folders[1] + '/' + file)
                
                else:
                    os.mkdir(dest_path + '/' + folders[1])
                    shutil.copy(dir_path + '/' + file, 
                                dest_path + '/' + folders[1] + '/' + file)
                    
        # 3. case with folders inside directory
        if os.path.isdir(dir_path + '/' + file):
            if os.path.exists(dest_path + '/' + folders[0]):
                shutil.copytree(dir_path + '/' + file,
                            dest_path + '/' + folders[0] + '/' + file)
            else:
                os.mkdir(dest_path + '/' + folders[0])
                shutil.copytree(dir_path + '/' + file,
                                dest_path + '/' + folders[0] + '/' + file)
            


                    
def create_dirs_walk_ext(dir_path):
    
    """
    create a nested folders inside type folders from extensions_dict based on file's extensions

    Args:
        dir_path (_type_): path where files were copied inside new type folders
        
    For example:
    
    Before create dirs and copy files:
    ../Images/<file>.jpeg
    ../Tables/<file>.xls
    
    After:
    ../Images/JPEG/<file>.jpeg
    ../Images/<file>.jpeg
    ../Tables/XLS/<file>.xls
    ../Tables/<file>.xls
    
    """
    
    for root, dirs, files in os.walk(dir_path):
        for f in dirs:
            # exclude folder 'Directories' with nested dirs
            if f != folders[0]:
                
                path_dir = os.path.join(root, f)
                files = os.listdir(path_dir)
                for file in files:
                    # split filename and extension
                    filename, extension = os.path.splitext(file)
                    # delete dot and change to uppercase
                    extension = extension[1:].upper()

                    # check if extension's folder doesn't exist
                    if os.path.exists(path_dir + '/' + extension):
                        # check if file not in extension's folder
                        if not os.path.exists(path_dir + '/' + file):
                            shutil.copy(path_dir + '/' + file, path_dir + '/' + extension)
                        continue
                    else:
                        os.mkdir(path_dir + '/' + extension)
                        if not os.path.exists(path_dir + '/' + file):
                            shutil.copy(path_dir + '/' + file, path_dir + '/' + extension)
                        continue

def main():
    copy_files_dict(source_folder, destination_folder)
    create_dirs_walk_ext(destination_folder)
    
if __name__ == '__main__':
    main()