sum_mul <- function(n, m){
  if (n > 0 && m > 0){
  res <- 0
  i <- n
  while (i < m) {
    res <- res + i
    i <- i + n
    }
  return (res)
  } else {
    return("INVALID")
  }
}