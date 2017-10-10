## README
# this is an example of setting up git plus a few simple commands
# https://www.youtube.com/watch?v=HVsySz-h9r4

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

## BRANCH
# syntax: git branch <descriptive-branch-name>
# create a branch for desired feature
git branch git-branch # create a new branch
git checkout git-branch #checkout the branch
git branch #similar to git status, but checking which branch you're in
#push branch
git push -u origin <new-branch>

## MERGING
git checkout master
git merge <name-of-branch #merging with master
git branch --merged #if the branch shows up, it means that branch is merged
git branch -d git-branch #deletes branch
git push origin --delete git-branch #delete branch in repository also

#remember, always pull before pushing --
git checkout master
git pull origin master

#checking commit history
git log







