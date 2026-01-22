## TIME-MACHINE-picoctf-
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Annotation%202026-01-22%20102301.png?raw=true)

# Deskripsi = What was I last working on? I remember writing a note to help me remember... You can download the challenge files here:
   - challenge.zip

# hints
- The cat command will let you read a file, but that won't help you here!
- Read the chapter on Git from the picoPrimer here(https://primer.picoctf.org/#_git_version_control).
- When committing a file with git, a message can (and should) be included.

# langkah 1 unzip file
unzip file challenge.zip menggunakan ' unzip <filename>

# langkah 2 explore directory 
-setelah menggunakan ls ditemukan satu file bernama message.txt
-setelah di lihat menggunakan command cat <filename> keluar tulisan "This is What I was working on , but I'd need to look ar my commit history to know why..."
-selain message.txt ada directory .git saat ls -a
masuk ke .git menggunakan command cd /<directory>

# langkah 3 temukan flag
-gunakan command git log untuk melihat history file
-ketemu deh filenya 
![alt text](?raw=true)


