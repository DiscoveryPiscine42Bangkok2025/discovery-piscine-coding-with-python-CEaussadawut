# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    help_your_professor.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:46:19 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:46:19 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def average(score_dict):
    if not score_dict:
        return 0
    sum_score = sum(score_dict.values())
    n_stu = len(score_dict)
    return sum_score / n_stu

class_3B = { 
    "marine": 18, 
    "jean": 15, 
    "coline": 8, 
    "luc": 9 
} 
class_3C = { 
    "quentin": 17, 
    "julie": 15, 
    "marc": 8, 
    "stephanie": 13 
    }

print(f"Average for class 3B: {average(class_3B)}.") 
print(f"Average for class 3C: {average(class_3C)}.")