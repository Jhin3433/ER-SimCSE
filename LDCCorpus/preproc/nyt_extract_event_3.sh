#1/bin/bash

CLASSPATH=$CLASSPATH:/home/SimCSE-main/LDCCorpus/preproc/ollie-app-latest.jar
CLASSPATH=$CLASSPATH:.

INPUT_BASE=/home/SimCSE-main/LDCCorpus/gigaword_eng_5/data/nyt_eng_parse_2
OUTPUT_BASE=/home/SimCSE-main/LDCCorpus/gigaword_eng_5/data/nyt_ollie_3

export JAVA_OPTS="-Xmx10g"

# compile OpenExtract.scala
scalac -classpath $CLASSPATH OpenExtract.scala

for year in $@; do
    scala -classpath $CLASSPATH ollie.OpenExtract $INPUT_BASE/$year $OUTPUT_BASE/$year.txt
done
# for year in $INPUT_BASE; do
#     scala -classpath $CLASSPATH ollie.OpenExtract $INPUT_BASE/$year $OUTPUT_BASE/$year.txt
# done