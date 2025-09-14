# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scan_it.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:45:35 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:45:35 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys

# def count_word(haystack, needle):
#     word = haystack.split()
#     # print(word)
#     cw = 0
#     for i in range(len(word)):
#         if word[i] == needle:
#             cw += 1
#     return cw

# print(sys.argv)
argc = len(sys.argv)

# print('argc =',argc)
if argc == 3:
    # cw = count_word(sys.argv[2], sys.argv[1])
    haystack = sys.argv[2]
    needle = sys.argv[1]
    cw = haystack.count(needle)

    if (cw == 0):
        print("none")
    else:
        print(cw)
else:
    print("none")