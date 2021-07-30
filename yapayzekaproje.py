# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 03:35:48 2021

@author: humab
"""

import numpy as np

    
def data():
    
    user = ['Merhaba',
    'Nasılsın',
    'Harikayım',
    'İyiyim',
    'Teşekkürler ben de iyiyim',
    'Arkadaş olmak ister misin?',
    'Arkadaş olalım mı?',
    'Nasılsın?',
    'Neler yapıyorsun?',
    'Sen zeki misin?',
    'Napıyosun?',
    'Sen kimsin?',
    'Cinsiyetin ne?',
    'Selam',
    'Amacın nedir',
    'Duyguların var mı?',
    'Günaydın',
    'İyi geceler',
    'Görüşürüz',
    'Bay bay',
    'Çok tatlısın',
    ]
    
    answerOfYuma = ['Merhaba',
    'İyiyim teşekkürler. Sen nasılsın?',
    'Ne güzel!',
    'Ne güzel!',
    'Ne güzel!',
    'Çok sevinirim.',
    'Evet, lütfen.',
    'Seninle konuşunca iyi oldum :)',
    'Sanal dünyamda arkadaş edinmeye çalışıyorum.',
    'Bir saniyede binlerce matematik işlemi yapabiliyorum, zeki demezsek ayıp olur…',
    'Sanal dünyamda arkadaş edinmeye çalışıyorum.',
    'Ben Yuma, senin sanal arkadaşın!',
    'Böyle bir şeye gerek duymuyorum :)',
    'Selamlar efendim',
    'Can sıkıntını önlemek desek yalan olmaz sanırım',
    'Seni mutlu görmek istiyorum, eğer bu bir duyguy evet.',
    'Günaydın hayatım',
    'İyi geceler canım',
    'Görüşmek üzere fıstık',
    'Görüşmek üzere fıstık',
    'Beni utandırıyorsun :))'
]
    
    
    
    text1 = input("Enter your text: ")
    
    index = 0
    minldistance =  999
    minhdistance = 999
    for text2 in user:
        
        print("*******************")
        print(f'Data from dataset:  {text2} \n')
        
        len1 = len(text1)
        len2 = len(text2)
        
        hdistance = hamming(text1,text2,len1,len2)
        if minhdistance > hdistance:
            minhdistance = hdistance
            hindex = index
        ldistance = levenshtain(text1,text2,len1,len2)
        if minldistance > ldistance:
            minldistance = ldistance
            lindex = index
        
        index = index + 1
    
    
    print("****result****")
    print(f'Minimum hamming index: {hindex}')
    print(f'Minimum hamming distance: {minhdistance}\n')
    print(f'Minimum levenstain index: {lindex}')
    print(f'Minimum levenstain distance: {minldistance}\n')
    
    temp = hindex
    for answer in answerOfYuma:
        
        if temp == 0: 
            print(f'The answer of Yuma recording to hamming distance algorithm is : {answer}')
        temp = temp -1

    temp = lindex
    for answer in answerOfYuma:
        
        if temp == 0: 
            print(f'The answer of Yuma recording to levenstain distance algorithm is : {answer}')
        temp = temp -1


def levenshtain(text1,text2,len1,len2):
   
    arr = np.zeros((len1+1,len2+1))
    
    for x in range (1,len1+1):
        for y in range (1,len2+1):
            arr[x][y] = min(arr[x-1][y-1],arr[x][y-1],arr[x-1][y])
            if text1[x-1] != text2[y-1]:
                arr[x][y] = 1 + arr[x][y]
    distance = arr[len1][len2]
        
    print(arr)
    print(f' Levenstain Distance =  {distance} \n')
    return distance

def hamming(text1,text2,len1,len2):
    distance = 0
    difference = abs(len1-len2)
    minlen = min(len1, len2)
    
    for x in range (minlen):
        if text1[x] != text2[x]:
            distance += 1
    distance += difference
    print(f'Hamming Distance =  {distance}\n')
    
    return distance
  

data()