# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    password.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:44:30 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:44:30 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

password = "Python is awesome"

usrpwd = input().strip()

if usrpwd == password:
	print("ACCESS GRANTED")
else:
	print("ACESS DENIED")
