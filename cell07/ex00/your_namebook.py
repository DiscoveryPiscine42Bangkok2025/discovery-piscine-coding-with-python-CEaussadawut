# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    your_namebook.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aussapha <aussapha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/14 20:46:13 by aussapha          #+#    #+#              #
#    Updated: 2025/09/16 20:58:27 by aussapha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def array_of_names(names_dict):
    full_names = []
    for first_name, last_name in names_dict.items():
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(full_name)
    return full_names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))