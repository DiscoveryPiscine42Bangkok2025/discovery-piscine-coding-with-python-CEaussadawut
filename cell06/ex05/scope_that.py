# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scope_that.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:46:09 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:46:09 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def add_one(n):
    return n + 1

def is_float(val):
	try:
		float(val)
		return True
	except ValueError:
		return False

n = 41
print(f'Number before add_one: {n}')
n = add_one(n)
print(f'Number after add_one: {n}')