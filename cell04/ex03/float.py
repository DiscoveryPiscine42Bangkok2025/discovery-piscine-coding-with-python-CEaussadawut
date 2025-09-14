# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    float.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:44:58 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:44:58 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def is_float(val):
	try:
		float(val)
		return True
	except ValueError:
		return False

nb = input('Give me a number: ')
if is_float(nb):
	nb_f = float(nb)
	nb_i = int(nb_f)

	if nb_f == nb_i:
		print('This number is an integer.')
	else:
		print('This number is a decimal.')
