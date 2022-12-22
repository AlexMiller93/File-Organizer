File Organizer

Before:
../source_folder/<filename>.jpg
../source_folder/<filename>.xls

After copying files and create nested dirs:

../dest_folder/Images/JPG/<filename>.jpg
../dest_folder/Tables/XLS/<filename>.xls


If you want to move files and folders instead of copy, change shutil.copy and shutil.copytree accordingly to shutil.move.

