# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    methods_everywhere.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:46:05 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:46:05 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys

def shrink(s):
    x = slice(8)
    print(s[x])

def enlarge(s):
    print(s,'Z'*(8 - (len(s))),sep='')

argc = len(sys.argv)
argv = sys.argv

if argc >= 2:
    argv.pop(0)
    # print(*argv)
    for i in range(len(argv)):
        if len(argv[i]) < 8:
            enlarge(argv[i])
        else:
            shrink(argv[i])
else:
    print("none")