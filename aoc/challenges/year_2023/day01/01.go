package day01

import (
	"aoc/io"
	"fmt"
	"log"
	"strconv"
	"strings"
	"unicode"
)

func One() {
	lines := io.ReadInput("day01/input.txt")
	nums := numbers_per_lines(lines, false)
	fmt.Printf("Sum of nums -> %v\n", nums)

}

func Two() {
	lines := io.ReadInput("day01/input.txt")
	nums := numbers_per_lines(lines, true)
	fmt.Printf("Sum of nums -> %v\n", nums)

}

// Extracts all the numbers and strings of numbers of each line and return them
// as an integer.
// e.g. one3ds4df -> 14
func numbers_per_lines(lines []string, check_written_chars bool) int {
	numbers := []int{}
	for _, line := range lines {
		numbers_per_line := []string{}
		for char_index, char := range line {
			written_char := check_str_prefix(line[char_index:])
			if unicode.IsNumber(char) {
				numbers_per_line = append(numbers_per_line, string(char))
			} else if check_written_chars && written_char != "" {
				numbers_per_line = append(numbers_per_line, written_char)
			}
		}
		new_number, err := strconv.Atoi(numbers_per_line[0] + numbers_per_line[len(numbers_per_line)-1])
		if err != nil {
			log.Fatalf("Expected int vale fron %v", new_number)
		}
		numbers = append(numbers, new_number)
	}
	sum := io.SumNumbers(numbers)
	return sum
}

// Check if string starts with a written number
func check_str_prefix(line string) string {
	num_mapping := map[string]string{"one": "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9"}
	for word, key := range num_mapping {
		if strings.HasPrefix(line, word) {
			return key
		}
	}
	return ""
}
