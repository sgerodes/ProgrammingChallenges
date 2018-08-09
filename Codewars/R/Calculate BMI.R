bmi <- function(weight, height) {
  bmi <- weight / height ^ 2
  if (bmi <= 18.5) result <- "Underweight"
  else if (bmi <= 25.0) result <- "Normal"
  else if (bmi <= 30.0) result <- "Overweight"
  else if (bmi > 30) result <- "Obese"
  result
}