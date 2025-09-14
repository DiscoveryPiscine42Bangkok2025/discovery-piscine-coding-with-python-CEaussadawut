# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count_it.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:45:44 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:45:45 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys

argc = len(sys.argv)

if argc >= 2:
    argv = sys.argv
    argv.pop(0)
    # print(argv)
    print("parameters:",len(argv))
    for i in range (len(argv)):
        print(argv[i], ': ', len(argv[i]),sep='')
        
else:
    print("none")
