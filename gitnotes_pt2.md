# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 14:32:13 2019

@author: dletran
"""

# I. Git Remove
## A. Delete a file using bash rm

The ```git rm``` command will
1. remove the file in your directory
2. commit the changes as well

```{bash}
git rm file.html
```
## B. Commit
Now you gotta also commit a message.

```{bash}
git commit -m "deleted file.html"
```
## C. Push
Push to remote repository.

```{bash}
# good practice to pull before pushing to remote
git pull
git push
# just check 
git status
```

# II. Git Move
## A. Renaming

Let's say you accidently commited a file as **silver.txt**,
but the file needs to be renamed with a **\*.html** extension.

```{bash}
git mv silver.txt silver.html
```
## B. Just check
just to check...
```{bash}
ls
git status
```

## C. Commit
```{bash}
git commit -m "Rename silver.txt to silver.html"
```
Continue to check status, then pull/push to remote server.

# III. Unstaging Changes
```{bash}
git reset HEAD


# IV. 