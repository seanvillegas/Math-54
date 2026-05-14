# Superposition Algorithm

ay'' + by' + c = f_1(t) + f_2(t)

# find roots
homogenous_roots = r^2 + r + 1 = 0


######## RHS ########
# find constants
# important to separate constants from equation to make life easier
# f_1(t) = -9t => (-9) * (t * 1) e^{rt} = 0 
find_constants(f_1(t) + f_2(t))

# find multiplicity 

mult_1 = multiplicity_check(f_1(t))
mult_2 = multiplicity_check(f_2(t))


# find if matching roots in forcing function and in homogenous_roots

check_euler_root = find_matching_roots(f_1(t) + f_2(t))
if check_euler_root == homogenous_roots:
    add_t_to_asantz_guess_RHS = true

# incrementally solve

######## ASANTZ the RHS ########
asantz_f1 = find_best_asantz(f_1(t))

# plug in asantz into the LHS equation, i.e. y, and differentiate. Set result equal to the forcing function, f_1(t)
## this can be called the particular function, y_p when you solve for it. 
y_1 = a(asantz_f1)'' + b(asantz_f1)'' + c(asantz_f1) = f_1(t)



######## SOLVE FOR A_m IN y_1 ########

# return the cases of up to A_m solved, i.e. there can exist multiple A_1 to A_m within the cases list. 
# we do this by plugging in y_1 into the y's and differentiating when required. I.e. a(y_1)'' + b(y_1)' + c(y_1) = f_1(t)
cases = find_particular_solution(y_1) 

######## SOLUTION FOR Y_1 ########
solution_to_f1(t) = cases[0] + cases[m] 

######## REPEAT THE ALGORITHM ABOVE FOR F2(T) ########

solution_to_f2(t) = assume_found

######## FINALLY, COMBINE, GIVING SUPERPOSITION ########
superposition_y = solution_to_f1(t) + solution_to_f2(t)