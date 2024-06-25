def relationship_status(from_member, to_member, social_graph):

    # default is false as the default condition is False unless seen in the list
    from_follow_to = False
    to_follow_from = False
    from_index = 0
    to_index = 0

    # checks over all the followings of both the from_member (the first while loop) and the to_member (the second while loop)
    while from_index <= len(social_graph[from_member]["following"]) - 1:
        if social_graph[from_member]["following"][from_index] == to_member:
            from_follow_to = True
        from_index += 1
    while to_index <= len(social_graph[to_member]["following"]) - 1:
        if social_graph[to_member]["following"][to_index] == from_member:
            to_follow_from = True
        to_index += 1

    # return conditions set by the problem
    if from_follow_to == True and to_follow_from == False:
        return "follower"
    elif from_follow_to == False and to_follow_from == True:
        return "followed by"
    elif from_follow_to == True and to_follow_from == True:
        return "friends"
    else:
        return "no relationship"

def tic_tac_toe(board):

    # row variables
    index_row_checker = 0

    # column variables
    index_column_checker_inner_list = 0
    empty_list_column_checker = []

    # left diagonal variables
    index_left_diagonal_checker_outer_list = 0
    index_left_diagonal_checker_inner_list = 0
    empty_list_left_diagonal_checker = []

    # right diagonal variables
    index_right_diagonal_checker_outer_list = 0
    index_right_diagonal_checker_inner_list = len(board)-1
    empty_list_right_diagnoal_checker = []
    
    # row checker
    while index_row_checker <= len(board) - 1:
        if board[index_row_checker].count("X") == len(board):
            return "X"
        elif board[index_row_checker].count("O") == len(board):
            return "O"
        index_row_checker += 1
        
    # column checker
    while index_column_checker_inner_list <= len(board) - 1:
        index_column_checker_outer_list = 0 # very important for this loop to work, as when it reaches [2][0] on a 3x3, it resets to [0][1]
        while index_column_checker_outer_list <= len(board) - 1:
            empty_list_column_checker.append(board[index_column_checker_outer_list][index_column_checker_inner_list])
            index_column_checker_outer_list += 1
        if empty_list_column_checker.count("X") == len(board):
            return "X"
        elif empty_list_column_checker.count("O") == len(board):
            return "O"
        empty_list_column_checker.clear() # also important so that the next iteration does not contain the elements of the previous
        index_column_checker_inner_list += 1

    # left diagonal checker
    while index_left_diagonal_checker_outer_list <= len(board) - 1 and index_left_diagonal_checker_inner_list <= len(board) - 1:
        empty_list_left_diagonal_checker.append(board[index_left_diagonal_checker_outer_list][index_left_diagonal_checker_inner_list])
        index_left_diagonal_checker_outer_list += 1
        index_left_diagonal_checker_inner_list += 1
        if empty_list_left_diagonal_checker.count("X") == len(board):
            return "X"
        elif empty_list_left_diagonal_checker.count("O") == len(board):
            return "O"

    # right diagonal checker
    while index_right_diagonal_checker_outer_list <= len(board) - 1 and index_right_diagonal_checker_inner_list >= 0:
            empty_list_right_diagnoal_checker.append(board[index_right_diagonal_checker_outer_list][index_right_diagonal_checker_inner_list])
            index_right_diagonal_checker_outer_list += 1
            index_right_diagonal_checker_inner_list -= 1
            if empty_list_right_diagnoal_checker.count("X") == len(board):
                return "X"
            elif empty_list_right_diagnoal_checker.count("O") == len(board):
                return "O"

    # if none is satisfied, then no winner
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # dissects the given dictionary into two separate lists, one with the places and one with the distances
    places_list = list(route_map)
    distances_list = list(route_map.values())

    # looping variables for index tracker of the list of keys
    i = 0
    j = 0

    # looping variables for the summation process itself
    k = 0
    l = 0
    m = 0

    # index of the first_stop and second_stop
    start_start_finder = 0
    end_end_finder = 0

    # variables for the summation of distance
    empty_list_numbers_placeholder_eta = []
    sum_distances = 0

    # finds when the first_stop appears as index 0 on the list of tuples
    while i <= len(places_list) - 1:
        if places_list[i].count(first_stop) == 0 or places_list[i].index(first_stop) != 0:
            start_start_finder += 1
        else:
            break
        i += 1
        
    # finds when the second_stop appears as index 1 on the list of tuples
    while j <= len(places_list) - 1:
        if places_list[j].count(second_stop) == 0 or places_list[j].index(second_stop) != 1:
            end_end_finder += 1
        else:
            break
        j += 1

    # if start_start_finder = end_end_finder, then the distance between the places is already given by the dictionary
    if start_start_finder == end_end_finder:
        sum_distances = distances_list[start_start_finder]["travel_time_mins"]

    # if start_start_finder < end_end_finder, then creates a separate list containing the distances starting from index start_start_finder and ending with the index end_end_finder
    # the sum of the list is then taken, which results to sum_distances
    elif start_start_finder < end_end_finder:
        while start_start_finder <= end_end_finder:
            empty_list_numbers_placeholder_eta.append(distances_list[start_start_finder]["travel_time_mins"])
            start_start_finder += 1
        while k <= len(empty_list_numbers_placeholder_eta) - 1:
            sum_distances = sum_distances + empty_list_numbers_placeholder_eta[k]
            k += 1

    # if start_start_finder > end_end_finder, then creates a separate list containing the distances starting from index start_start_finder and ending with the index end_end_finder
    # just slightly different than the < version because when the beginning has a greater index value than the end, then there needs to be a wrap back to the beginning
    # the sum of the list is then taken, which results to sum_distances
    elif start_start_finder > end_end_finder:
        while start_start_finder <= len(distances_list) - 1:
            empty_list_numbers_placeholder_eta.append(distances_list[start_start_finder]["travel_time_mins"])
            start_start_finder += 1
        while l <= end_end_finder:
            empty_list_numbers_placeholder_eta.append(distances_list[l]["travel_time_mins"])
            l += 1
        while m <= len(empty_list_numbers_placeholder_eta) - 1:
            sum_distances = sum_distances + empty_list_numbers_placeholder_eta[m]
            m += 1
    return sum_distances