The above project is a practical demonstration of my CAT 1 Computer Graphics unit
which answers the questions:

QUESTION 1 - Python3 Development Environment (10 Marks)

1. Set up a new Python3 Development environment for this assessment. Install all the dependencies that you think will be
   relevant.
   1a . Built a Python3 project with the structure of projects in PyCharm then import the
   MASSIVE Dataset mentioned on the Data File above.
   1b . In this dataset, the pivot language is English, given that all the ids of the languages are
   matching, generate a en-xx.xlxs file for all the languages. Do not use Recursive algorithms in this solution as they
   have a time complexity of O(n2), which is bad for memory.
   1bi . Have a look at Flags to help you run this on your generator.sh files

QUESTION 2 - Working with Files (10 Marks)

1. For English (en), Swahili (sw) and German (de), generate separate jsonl files with test, train
   and dev respectively.
2. Generate one large json file showing all the translations from en to xx with id and utt for all
   the train sets.
   a. Pretty print your json file structure.
3. Upload all the files to your Google Drive Backup Folder.
   a. Upload all the changes to GitHub
   b. Write a clean readme.md file

Packages needed:
1. os
2. tarfile
3. json
4. logging
5. tkinter
6. collections