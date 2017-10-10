## README
# this is an example of setting up git plus a few simple commands

## SYNTAX
# git <verb> <--options> <args>
# example:
# git add --help
# git config --global user.name

## VISUAL
#                             |-------------Commit---->	
# |------------Stage Fixes---------->
# Working Directory			Staging Area		.git directory



## BASICS and SETUP
git --version #check if git exists
git initi #intiatializes the folder for git
#rm -rf .git // this completely removes git from the the folder

#set up first time ever
git config --global user.name "Duke LeTran"
git config --global user.email "duke.letran@gmail.com"

#.gitignore
touch .gitignore
subl .gitignore #add things like *.csv to ignorefile

#Simple commands
git status #checks status





