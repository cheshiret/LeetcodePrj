#!/usr/bin/env bash
#伪代码
#tr -s set1 set2将不规律的空格转换为回车
#sort | uniq -c | sort -r 对字符进行统计，按照降序排列
#awk '{print $2, $1}' 将输出两列更换顺序
cat words.txt | tr -s ' ' '\n' | sort | uniq -c |  sort -r | awk '{ print $2, $1 }'
