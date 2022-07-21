#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Jun 21 10:37:11 2022

@author: danb22

Copyright (c) <2022>, <Dan Blanchette>
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
"""

import cellCount as count
    

# main Function
def main():
    path = '../pngimgs/'
    filelist = sorted(count.os.listdir(path), 
                   key=lambda x: int(count.os.path.splitext(x)[0]))
    
    for image_file in filelist :
       count.cells_only(path + image_file)


    return 0

if __name__=="__main__":
    main()
