# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    downcase_all.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:46:01 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:46:02 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys

def downcase_it(s):
    return (s.lower())

argc = len(sys.argv)
argv = sys.argv
argv.pop(0)
if argc >= 2:
    for arg in argv:
        print(downcase_it(arg))
else:
    print("none")