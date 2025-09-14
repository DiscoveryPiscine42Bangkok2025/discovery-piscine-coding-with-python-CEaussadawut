# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    persons_of_interest.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:46:21 by aussapha          #+#    #+#              #
#    Updated: 2025/09/14 20:46:21 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def get_birth_year(figure):
    return int(figure['date_of_birth'])

def famous_births(data_dict):
    #sort dict by year of birth
    sorted_data = sorted(data_dict.values(), key=get_birth_year)
    for data in sorted_data:
        print(f"{data['name']} is a great scientist born in {data['date_of_birth']}.")

women_scientists = { 
    "ada": { 
        "name": "Ada Lovelace",
        "date_of_birth": "1815" 
        }, 
    "cecilia": { 
        "name": "Cecila Payne", 
        "date_of_birth": "1900" 
        }, 
    "lise": { "name": "Lise Meitner", 
             "date_of_birth": "1878" 
        }, 
    "grace": { "name": "Grace Hopper", 
              "date_of_birth": "1906" 
        } 
}

famous_births(women_scientists)