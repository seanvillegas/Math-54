"""
Your grade will be computed according to the following proportions:
    * 20% for quizzes
    * 20% for each midterm 
    * 40% for the final.
A clobber policy will be applied, replacing the lowest midterm score with the final exam score if it is higher.
The three lowest quiz scores will be dropped.


This script:
    * calculates the total amount of points I earned for 11 quizzes that were scored x/30, then raised to normal unit before its divided by the total number of points I could have earned
    * calculates the total amount of points I earned for 2 midterms that were scored x/50, then raised to normal unit before its divided by the total number of points I could have earned
    * The weights are applied to each sum of quiz and midterm, and then user is expected to enter the amount they wish to score on the final to see the outcome. 

"""
# quizzes
q_1 = 20.5/30 * 100
q_2 = 25/30 * 100
q_3 = 25/30 * 100 
q_4 = 24/30 * 100
q_5 = 15/30 * 100
q_6 = 10/30 * 100 
q_7 = 15/30 * 100
q_8 = 17/30 * 100
q_9 = 17/30 * 100
q_10 = 8/30 * 100
q_11 = 8/30 * 100

# midterms
m_1 = 24/50 * 100 
m_2 = 18/50 * 100

#total_sum_of_quizzes = q_1 + q_2 + q_3 + q_4 + q_5 + q_6 + q_7 + q_8 + q_9 + q_10 + q_11
dropped_quizzes = q_1 + q_2 + q_3 + q_4 + q_5 + q_7 + q_8 + q_9 + 300
sum_of_midterms = m_1 + m_2

total_points_possible_quizzes = 11 * 100
total_points_possible_midterms = 2 * 100


data = input("Enter in desired scores for final (separated by comma) and your current grade will be recomputed based on each respective score. \n")
desired_scores = data.split(",")

for i in desired_scores:
    # Raw Score
    print("Showing raw score with 3 lowest quizzes dropped: \n")
    curr_score = (int(i) / 100) * 100
    current_grade = (0.2 * dropped_quizzes/total_points_possible_quizzes) * 100 + (0.2 * sum_of_midterms/total_points_possible_midterms) * 100+ (0.4 * curr_score)
    #rounded_grade = round(current_grade)
    print(f'If you scored {i} out of 100 on the final you would get: {current_grade}')

    # Clobber Policy
    if curr_score > m_2:
        print("Showing clobber applied: \n")
        clobber_midterm_sum = m_1 + curr_score
        clobber_grade = (0.2 * dropped_quizzes/total_points_possible_quizzes) * 100 + (0.2 * clobber_midterm_sum/total_points_possible_midterms) * 100 + (0.4 * curr_score)
        print(f'If you scored {i} out of 100 on the final you would get (clobbered): {clobber_grade}')
