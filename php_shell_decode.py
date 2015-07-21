#!/usr/bin/python

import base64
import zlib

#Pre: accepts a base64 encoded shell
#Post: decodes and decompresses until source code is reached
def shell_decode(init):
    codeblob = init
    while '<?php' not in codeblob:
        gzipped = base64.b64decode(codeblob)
        codeblob = zlib.decompress(gzipped, -zlib.MAX_WBITS)
        if '<?php' not in codeblob:
            #remove eval(gzinflate(base64_decode(' and '))); to leave b64 encoded blob
            codeblob = codeblob.split('\'')
            codeblob = codeblob[1]
    print codeblob
