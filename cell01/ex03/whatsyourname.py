# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatsyourname.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:44:02 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:44:02 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

first_name = input("Hey, what's your first name? : ").strip()
last_name = input("And your last name? : ").strip()
whole_name = first_name + ' ' + last_name
print("Well, pleased to meet you, ", whole_name,'.',sep='')
