# Sublime PHPMD Plugin

A basic Sublime plugin to check file(s) using [PHPMD](http://phpmd.org/).

## Pre-Requisites

* [PHPMD](http://phpmd.org/download/index.html)

## Installation

The recommended method of installation is via Package Control.

### Package Control

* Install Package Control (if not already installed) by using
  [these instructions](http://wbond.net/sublime_packages/package_control/installation)
* Add this repository by using `Package Control: Add Repository` and using the
  URL of `https://github.com/madedotcom/sublime-phpmd`
* Install by using `Package Control: Install Package` and typing in `Phpmd`

### Using Git

* Make sure you have [git](http://git-scm.com/) installed
* Browse to your Sublime packages directory in a command prompt (if you don't
  know where that is, open Sublime and click on `Preferences` > `Browse Packages`
  to find the directory)
* In your command prompt, type `git clone https://github.com/madedotcom/sublime-phpmd`

### Download Manually

* Download [this file](https://github.com/madedotcom/sublime-phpmd/zipball/master)
* Extract it and rename the directory to `Phpmd`
* Move the directory to your Sublime packages directory (see above if you don't
  know where that is)

## Usage

Simply press `F2` whilst in a .php file (you need to save the file to disk first) -
that's it. If no window pops up, nothing was wrong.

You can also right click a file, directory, or multiples of each, in the sidebar
and choose `PHPMD`. If you choose a directory then please be patient - currently
the work is not done asynchronously so the command blocks Sublime from doing
anything else. This will soon be fixed.
