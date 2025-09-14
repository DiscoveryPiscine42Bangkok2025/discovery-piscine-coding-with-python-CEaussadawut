# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    advanced_mult.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:44:44 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:44:45 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
	# print("This program have only one argv")
	i = 0	
	while i <= 10:
		print('Table de ', i, ': ',end='', sep='')
		# print(f'Table de {i}: ',end='')
		j = 0
		while j <= 10:
			print(j * i, end=' ')
			j = j + 1
		print('')
		i = i + 1
else:
	print("none")
