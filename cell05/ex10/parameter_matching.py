# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parameter_matching.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:45:41 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:45:41 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys

argc = len(sys.argv)

if argc == 2:
    s = input('What was the parameter? ')
    if s == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")