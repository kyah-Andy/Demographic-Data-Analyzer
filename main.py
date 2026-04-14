from demographic_data_analyzer import (
    race_count,
    average_age_men,
    percentage_bachelors,
    lower_education_rich,
    higher_education_rich,
    min_work_hours,
    rich_percentage,
    highest_earning_country,
    highest_earning_country_percentage,
    top_IN_occupation
)

def test():
    print("Race Count:\n", race_count)
    print("\nAverage Age of Men:", average_age_men)
    print("\n% Bachelors:", percentage_bachelors)
    print("\n% Rich with Higher Education:", higher_education_rich)
    print("\n% Rich without Higher Education:", lower_education_rich)
    print("\nMin Work Hours:", min_work_hours)
    print("\n% Rich among Min Workers:", rich_percentage)
    print("\nHighest Earning Country:", highest_earning_country)
    print("\nHighest Earning Country %:", highest_earning_country_percentage)
    print("\nTop Occupation in India:", top_IN_occupation)

test()