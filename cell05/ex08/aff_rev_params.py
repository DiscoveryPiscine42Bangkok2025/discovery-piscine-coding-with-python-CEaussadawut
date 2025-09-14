# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_rev_params.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:45:32 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:45:33 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys

# print(sys.argv)
argc = len(sys.argv)

# print('argc =',argc)
if argc <= 3:
    print("none")
else:
    for i in range(argc - 1, 0, -1):
        print(sys.argv[i])