# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    greetings_for_all.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:46:03 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:46:03 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def greetings(s=None):
    if s:
        if type(s) != str:
            print("Error! It was not a name.")
        else:
            print("Hello, " + s + ".")
    else:
        print("Hello, noble stranger.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
