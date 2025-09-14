# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    string_are_arrays.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:45:46 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:45:47 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys

argc = len(sys.argv)

if argc == 2:
    s = sys.argv[1]
    cz = 0
    for i in range(len(s)):
        if s[i] == 'z':
            cz += 1
    if cz == 0:
        print("none")
    elif s == "The character z is not found in this string":
        print("none")
    else:
        print('z'*cz)

else:
    print("none")