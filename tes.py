#! /usr/bin/env python
# -*- coding:utf-8 -*-

data_orig = "日本語"                                 #日本語代入(UTF-8)
print ( data_orig )                              #typeはstr
data_unic = data_orig.decode( 'utf-8' )   #utf-8→unicodeオブジェクト
print type( data_unic )                             #typeはunicodeオブジェクト