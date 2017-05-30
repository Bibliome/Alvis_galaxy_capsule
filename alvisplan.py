#!/usr/bin/python2

# Filename: grep.py
# Author: Mouhamadou Ba
# Version: 20/07/2016
#
# This script...
#
# alvisAnnotator is launched as follow:
#alvisnlp
#    verbose
#    -noColors
#    -param search subject word -param lemmatize active false  ## deactivate lemmatization
#    -param search subject plain  ## search inside words (deactivates lemmatization)
#    -param search subject prefix ## search at the beginning of words (deactivates lemmatization)
#    -param remove-overlaps active true ## longest only
#    -param lemmatize treeTaggerExecutable /home/rbossy/dist/tree-tagger/bin/tree-tagger
#    -param parFile /home/rbossy/dist/tree-tagger/english-par-linux-3.2.bin
#    -param write fileName "out.txt"
#    -param search dictFile dictionary-lemma.txt
#    -param search trieSource dictionary-lemma.trie
#    alvis-annotator.plan

def main():

