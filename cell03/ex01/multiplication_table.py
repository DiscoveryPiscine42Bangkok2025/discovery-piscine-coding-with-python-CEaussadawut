# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multiplication_table.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:44:39 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:44:40 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def is_int(val):
	try:
		int(val)
		return True
	except ValueError:
		return False

print('Enter a number')
nb = input().strip()

if is_int(nb):
	nb = int(nb)
	i = 0
	while i <= 9:
		res = nb * i
		print(i, 'x', nb, '=', res)
		i = i + 1
