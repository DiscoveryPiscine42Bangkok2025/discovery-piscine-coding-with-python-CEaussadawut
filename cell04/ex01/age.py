# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    age.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:44:53 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:44:53 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def is_int(val):
	try:
		int(val)
		return True
	except ValueError:
		return False

age = input('Please tell me your age: ').strip()

if is_int(age):
	age = int(age)
	print('You are currently', age, 'years old.')
	print("In 10 years, you'll be",age+10,'years old.')
	print("In 20 years, you'll be",age+20,'years old.')
	print("In 30 years, you'll be",age+30,'years old.')
