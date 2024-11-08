---
title: GitHub Authentication Solution
author: Jason
layout: post
date: 2024-11-08
tags: version-control, git, writing, tower 
---

I write in Markdown and LaTeX.  These flat file formats allow me to use version control, which I first learned from my Computer Science colleagues at Truman State.  Thanks, dudes!  Some time ago, I adopted the [Tower application](https://www.git-tower.com/windows) as my git environment of choice.  While I can manage git at the command line, I liked the way Tower displays information, and I like its UI with its buttons and menus.

In this age of computer mobility (I have two Macs at home, a Mac laptop, an iPad, and a Mac descktop in my work office), I use GitHub to host my few git repositories.  As long as I have an internet connection, this allows me to work on my writing from wherever I am.  I love it.  It's part of my work method that has become indisensible to me.  Sure, Dropbox and iCloud sync across machines, but that Black Box is too big for me to trust 100% of the time.  When I write, especially for myself, I like to be closer to the metal.

GitHub requires a use account, and over the years GitHub has changed the way a person (or computer) authenticates to an account or project.  Since I started using GitHub, the service has asked me to start using 2-Factor Authentication (2FA).  it's also asked me to use Personal Access Tokens (PAT).  The Tower application doesn't play so well with either of those.  But I'm a good soldier.  I have my DUO app set up for GitHub 2FA, and I've learned how to generate my PATs and set their expiration.

GitHub's 2FA authentication doesn't effect version control.  In my experience, it comes to play when I want to log in to the web page.  Those PATs are what screw me up.  They have some role in authenticating to make changes to a repository, and it tends to drive me crazy.  This post is meant to describe my latest attempt at describing Tower's crazy-making and how I solved that problem (this time) so next time (and there will be a next time) I **remember** how to solve it and don't have to reinvent this wheel for the twntieth time.

## Authentication Error

Yesterday, in Tower I tried to push a change to a project hosted on GitHub and I received a dialog box titled 'Connection to Remote Failed' Error.  The Git Error message is

Pushing to https://github.com/millerj870/millerj870.github.io.git
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/millerj870/millerj870.github.io.git/'

My heart sunk.  My PAT had probably expired and I needed to reinvent a way to fix the problem.  Indeed, a look at GitHub showed that my PAT had expired.  So I made another and tried to remember what to do with it.

Oddly enough, there's no place in Tower to save a PAT.  Looking in Settings > User Profiles, there is a field dedicated to `signing keys` but that's different.  Mine was blank.  After searching around the application, I could find no place to record the PAT associated with my GitHub account!  (I know that I go through this every time I recreate a solution to this authentication problem.)

Something else I always do is create a new token.  Walking through the instructions for [creating a personal access token (classic)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) felt very familiar to me.  After creating it, and giving it a descriptive name, I copied the new PAT to my password manager for safe keeping and future reference.

But all that happened outside Tower.  Attempting to push a repo change a couple times revealed no way to notify tower of this change in authentication information.  No dialog box appeared.  No CLI opened asking for the token.  Nothing.

## Command Line Git

Screw it, I said to myself, I'm just going to do my versioning with git at the command line.  So I opened up the Terminal, changed my working directory to be the folder containing my repo, and typed `git push`.  I was asked for my password.  I provided it.  To my disappointment, I got an authentication error.

    Password for 'https://millerj870@github.com': 
    remote: Support for password authentication was removed on August 13, 2021.
    remote: Please see https://docs.github.com/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.

I tried again, substituting my PAT for my password.  

    Password for 'https://millerj870@github.com': 
    remote: Invalid username or password.
    fatal: Authentication failed for 'https://github.com/millerj870/millerj870.github.io.git/'

After giving a couple more tries with the same result, I gave up and turned to Google for help.  One search result reminded me that [GitHub has a Command Line Interface](https://cli.github.com).  I installed that with Homebrew, and ran `gh auth login' as directed.  I answered some questions in the Terminal (see below) and was informed my PAT didn't include the permissions GitHub CLI needed, so I made a new PAT with the correct permissions.  

    ? Where do you use GitHub? GitHub.com
    ? What is your preferred protocol for Git operations on this host? HTTPS
    ? Authenticate Git with your GitHub credentials? Yes
    ? How would you like to authenticate GitHub CLI? Paste an authentication token
    Tip: you can generate a Personal Access Token here https://github.com/settings/tokens
    The minimum required scopes are 'repo', 'read:org', 'workflow'.

Executing 'gh auth login' again and providing an eligible PAT seemed to go smoothly.

    ? Where do you use GitHub? GitHub.com
    ? What is your preferred protocol for Git operations on this host? HTTPS
    ? Authenticate Git with your GitHub credentials? Yes
    ? How would you like to authenticate GitHub CLI? Paste an authentication token
    Tip: you can generate a Personal Access Token here https://github.com/settings/tokens
    The minimum required scopes are 'repo', 'read:org', 'workflow'.
    ? Paste your authentication token: ****************************************
    - gh config set -h github.com git_protocol https
    ✓ Configured git protocol
    ✓ Logged in as millerj870

In fact, when I exectued the vanilla `git push` command, it seemed to work!  When I pushed from within the Tower app, that also worked.

So it looks like I found a solution to my authentication problem on MacOS.  Hallelujah!





<!--
SYNTAX FOR IMAGES
* use services to create JPG and to create thumbnail that is 720px wide

[![ALT-TEXT](/assets/images/filename-thumbnail.jpg)](/assets/images/filename.jpg)
-->

<!--
SYNTAX FOR VIDEO
* convert MOV to mp4 using VLC

<video width="480" height="320" controls="controls">
  <source src="/assets/media/filename.m4v" type="video/mp4">
</video>
-->
