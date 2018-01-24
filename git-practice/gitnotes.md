# README #
This is an example of setting up git plus a few simple commands

[video]:https://www.youtube.com/watch?v=HVsySz-h9r4

## SYNTAX ##
git <verb> <--options> <args>
example:
`git add --help
git config --global user.name`

## ASCII VISUAL ##
```
                                            |-----------push----------->
                            |-------------Commit---->	
|------------Stage Fixes---------->
[Working Directory]         [Staging Area]      [.git directory]   [git server]
            <---------------Checkout-----------------
```


## BASICS and SETUP

`git --version #check if git exists, version
git init #intiatializes the folder for git
#rm -rf .git // this completely removes git from the the folder`

### Set up first time ever
#### 1. Set-up global options

```bash
git config --global user.name "Duke LeTran"
git config --global user.email "duke.letran@gmail.com"
git config --global --unset <variable> # how to remove something
git config --global --edit <variable> # how to edit
```

#### 2. Set-up gitignore file

```bash
touch .gitignore
subl .gitignore //  add things like *.csv to ignorefile
```
### connecting with remote repositories
git clone <url> <where-to-clone> #must be empty director or new

#### Staging commands

git status #checks status

git add -A #adds all

git add <file-name>

git reset #moves all files from staging area to wd

### commitment

git commit -m "Initial Commit"

git diff 

## REMOTE

### note: origin is the remote repository, master is the "branch"

git pull origin master

git push origin master

## BRANCH

### syntax: git branch <descriptive-branch-name>

### create a branch for desired feature

git branch git-branch # create a new branch

git checkout git-branch #checkout the branch

git branch #similar to git status, but checking which branch you're in

#### push branch

git push -u origin <new-branch>

## MERGING

git checkout master

git merge <name-of-branch> #merging with master

git branch --merged #if the branch shows up, it means that branch is merged

git branch -d git-branch #deletes branch

git push origin --delete git-branch #delete branch in repository also

## remember, always pull before pushing --

git checkout master

git pull origin master

## checking commit history

git log

git diff c6f95e09f7da3d1045be1d7de060db1d9088ba68 fd53fc16976ae05da626c6d4493de2aeb99fccc0







