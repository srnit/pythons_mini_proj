import os
def rename_files():
 current_dir=os.getcwd();
 print("your current working directory is"+current_dir);
 os.chdir("/media/raman/New Volume/prank/prank");
 file_name=os.listdir("/media/raman/New Volume/prank/prank");
 
 
 for files in file_name:
 	 print("files before rename"+" "+files);
	 os.rename(files,files.translate(None,"0123456789"));

rename_files();