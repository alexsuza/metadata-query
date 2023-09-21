#!/bin/bash

## stage files for commit
git add .

## commit new files
commit_message="$1"
git commit -m "$commit_message"
#
## push to GitHub
git push origin main


if git push origin main; then
	    echo "Push successful!"
    else
	        echo "Push failed!"
			DB_STRING = mysql+pymysql://admin:admin123@metadb.ctspjxav3xyb.us-east-1.rds.amazonaws.com/metadb
			DB_STRING2 = mysql+pymysql://root:admin123@localhost/metadb
fi
