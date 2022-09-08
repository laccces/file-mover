import glob
import shutil

def filemove():
  filelist=glob.glob(source_files)
  for single_file in filelist:
      # move file with full paths as shutil.move() parameters
      shutil.move(single_file,target_folder) 

# CSV
source_files='/Users/dancoman/Downloads/*.csv'
target_folder='/Users/dancoman/Downloads/CSV'

filemove()

# TXT
source_files='/Users/dancoman/Downloads/*.txt'
target_folder='/Users/dancoman/Downloads/TXT'

filemove()

# PDF
source_files='/Users/dancoman/Downloads/*.pdf'
target_folder='/Users/dancoman/Downloads/PDF'

filemove()

# XLSX
source_files='/Users/dancoman/Downloads/*.xlsx'
target_folder='/Users/dancoman/Downloads/xlsx'

filemove()

# DocX
source_files='/Users/dancoman/Downloads/*.docx'
target_folder='/Users/dancoman/Downloads/Docs'

filemove()

# doc
source_files='/Users/dancoman/Downloads/*.doc'
target_folder='/Users/dancoman/Downloads/Docs'

filemove()

# xls
source_files='/Users/dancoman/Downloads/*.xls'
target_folder='/Users/dancoman/Downloads/Docs'

filemove()

# DMG
source_files='/Users/dancoman/Downloads/*.dmg'
target_folder='/Users/dancoman/Downloads/DMGs'

filemove()

# ZIP
source_files='/Users/dancoman/Downloads/*.zip'
target_folder='/Users/dancoman/Downloads/ZIP'

filemove()

# PNG
source_files='/Users/dancoman/Downloads/*.png'
target_folder='/Users/dancoman/Downloads/Images'

filemove()

# jpg
source_files='/Users/dancoman/Downloads/*.jpg'
target_folder='/Users/dancoman/Downloads/Images'

filemove()

# JPG
source_files='/Users/dancoman/Downloads/*.JPG'
target_folder='/Users/dancoman/Downloads/Images'

filemove()

# JPEG
source_files='/Users/dancoman/Downloads/*.jpeg'
target_folder='/Users/dancoman/Downloads/Images'

filemove()

# SVG
source_files='/Users/dancoman/Downloads/*.svg'
target_folder='/Users/dancoman/Downloads/Images'

filemove()

# HTML
source_files='/Users/dancoman/Downloads/*.html'
target_folder='/Users/dancoman/Downloads/HTML'

filemove()

# EML
source_files='/Users/dancoman/Downloads/*.eml'
target_folder='/Users/dancoman/Downloads/Emails'

filemove()

# MOV
source_files='/Users/dancoman/Downloads/*.mov'
target_folder='/Users/dancoman/Downloads/Videos'

filemove()

# MOV
source_files='/Users/dancoman/Downloads/*.MOV'
target_folder='/Users/dancoman/Downloads/Videos'

filemove()

# mp4
source_files='/Users/dancoman/Downloads/*.mp4'
target_folder='/Users/dancoman/Downloads/Videos'

filemove()

# mp3
source_files='/Users/dancoman/Downloads/*.mp3'
target_folder='/Users/dancoman/Downloads/Music'

filemove()

# ppt
source_files='/Users/dancoman/Downloads/*.pptx'
target_folder='/Users/dancoman/Downloads/Presentations'

filemove()

# ISO
source_files='/Users/dancoman/Downloads/*.iso'
target_folder='/Users/dancoman/Downloads/ISO'

filemove()

# pkg
source_files='/Users/dancoman/Downloads/*.pkg'
target_folder='/Users/dancoman/Downloads/PKG'

filemove()