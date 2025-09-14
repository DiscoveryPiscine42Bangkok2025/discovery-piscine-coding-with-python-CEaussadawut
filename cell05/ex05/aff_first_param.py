# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_first_param.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:45:23 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:45:23 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys

# print(sys.argv)
argc = len(sys.argv)

if argc == 1:
    print("none")
else:
    print(sys.argv[1])