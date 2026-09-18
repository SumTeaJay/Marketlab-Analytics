import pandas as pd
import numpy as np

results = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "student": [
        "Анна",
        "Борис",
        "Вика",
        "Глеб",
        "Даша",
        "Егор",
        "Женя",
        "Ира"
    ],
    "attempt_1": [62, 74, 81, 55, 90, 67, 76, 58],
    "attempt_2": [78, 68, 88, 70, 84, 73, 60, 72]
})

long_formate_results = results.melt(id_vars="student", value_vars=["attempt_1", "attempt_2"], value_name="attempts", var_name="count_of_attempts")
wide_formate_results = long_formate_results.pivot_table(index="student", values="attempts", aggfunc="mean")

results["absolute_change"] = abs(results["attempt_1"] - results["attempt_2"])
print(results)