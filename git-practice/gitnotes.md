# Duke's Git Cheatsheet #
This is my own personal crib sheet for using git and is not intended to teach
you how to learn git. Imho, the easist way to learn is to just try using the
the commands on any existing project. For some sort of introduction, I highly 
recommend this youtube video: [link][video].


## SYNTAX ##

* syntax: git <_verb_> <--options> <_args_>

example:
````bash
git add --help
git config --global user.name
````

## ASCII VISUAL ##
```
                                            |-----------push----------->
                            |-------------Commit---->	
|------------Stage Fixes---------->
[Working Directory]         [Staging Area]      [.git directory]   [git server]
            <---------------Checkout-----------------
```

## I. BASICS and SETUP

### A. Set-up first time ever

````bash
git --version #check if git exists, version
git init #intiatializes the folder for git
#rm -rf .git # this completely removes git from the the folder
````

### B. Set-up global options (optional)

````bash
git config --global user.name "Duke LeTran"
git config --global user.email "duke.letran@gmail.com"
git config --global --unset <variable> # how to remove something
git config --global --edit <variable> # how to edit
````

### C. Set-up gitignore file

* note: I assume you use sublime as a text-editor; you can use wtv, really

````bash
touch .gitignore
subl .gitignore # add things like *.csv to ignorefile
````
### D. connecting with remote repositories

````bash
git clone <url> <where-to-clone> #must be empty director or new
````

## II. General Workflow Commands
### A. Staging commands

````bash
git status #checks status
git add -A #adds all
git add <file-name>
git reset #moves all files from staging area to wd
````

### B. Commitment commands

````bash
git commit -m "Initial Commit Message"
````

### C. Checking commit history

````bash
#example of using git dif diff
git log
git diff c6f95e09f7da3d1045be1d7de060db1d9088ba68 fd53fc16976ae05da626c6d4493de2aeb99fccc0
````

### D. Branch commands

* syntax: git branch <_descriptive-branch-name_>

* purpose: create a branch for desired feature; doesn't mess with master

````bash
git branch git-branch # create a new branch
git checkout git-branch # checkout the branch
git branch # similar to git status, but checking which branch you're in
git branch -d git-branch #deletes branch
````

### E. Merging Branch to Master

* purpose: merge the branch into the master

````bash
git checkout master
git merge <name-of-branch> #merging with master
git branch --merged #if the branch shows up, it means that branch is merged
#delete branch if necessary
````

### E. Remote commnads 

* purpose: connecting to git servers, i.e., github, bitbucket, etc.

* note: origin is the remote repository, master is the "branch"

* note: remember, always pull before pushing (in case someone pushed before you)

````bash
git pull origin master #always pull to check
git push origin master #pushes commit to git server
git push -u origin <new-branch> #pushes branch to git server
git push origin --delete git-branch #delete branch in repository also
````

[//]: # (link references)
[video]:https://www.youtube.com/watch?v=HVsySz-h9r4




