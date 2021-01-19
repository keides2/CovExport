#!/bin/bash

# 実行時に指定された引数の数が 3 でなければエラー終了
if [ $# -ne 3 ]; then
# echo "指定された引数は$#個です。" 1>&2
# echo "実行するには3個の引数が必要です。" 1>&2
  echo "	Usage:"
  echo "	$ ./cov-connect.sh <UserName> <Password> <File listed url>"
  exit 1
fi

while read url
do
	echo ${url}
#	python3 cov-connect.py ${user} ${password} ${url}
	python3 cov-connect.py $1 $2 ${url}
done < $3