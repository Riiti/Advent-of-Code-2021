package io

// Sum all the numbers in a integer slice
func SumNumbers[V int | float64](nums []V) V {
	var sum V
	for _, num := range nums {
		sum += num
	}
	return sum
}

// Power of values
func PowerOfMapValues(vals map[string]int) int {
	sum := 1
	for _, num := range vals {
		sum *= num
	}
	return sum
}
