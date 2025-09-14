# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_arrays.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:45:12 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:45:13 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]

arr_new = []
for i in range(len(arr)):
    if arr[i] > 5:
        arr_new.append(arr[i] + 2)

print(arr)
print(arr_new)