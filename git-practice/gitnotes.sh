## README
# this is an example of setting up git plus a few simple commands

## SYNTAX
# git <verb> <--options> <args>
# example:
# git add --help
# git config --global user.name

## ASCII VISUAL
#                             |-------------Commit---->	
# |------------Stage Fixes---------->
# [Working Directory]			[Staging Area]		[.git directory]
#             <---------------Checkout-----------------
#

## BASICS and SETUP
git --version #check if git exists, version
git initi #intiatializes the folder for git
#rm -rf .git // this completely removes git from the the folder

#set up first time ever
git config --global user.name "Duke LeTran"
git config --global user.email "daletran@ucdavis.edu"

#.gitignore
touch .gitignore
subl .gitignore #add things like *.csv to ignorefile

#connecting with remote repositories
git clone <url> <where-to-clone> #must be empty director or new

#Staging commands
git status #checks status
git add -A #adds all
git add <file-name>
git reset #moves all files from staging area to wd

#commiment
git commit -m "Initial Commit"
git diff 

## REMOTE
# note: origin is the remote repository, master is the "branch"
git pull origin master
git push origin master








