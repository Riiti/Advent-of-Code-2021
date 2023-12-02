package day02

import (
	"aoc/io"
	"fmt"
	"log"
	"regexp"
	"strconv"
	"strings"
)

func One() {
	lines := io.ReadInput("day02/input.txt")
	sum := extract_possible_lines(lines)
	fmt.Printf("Sum of nums -> %v\n", sum)
}

func Two() {
	lines := io.ReadInput("day02/input.txt")
	sum := extract_minimums(lines)
	fmt.Printf("Sum of nums -> %v\n", sum)
}

// Extract all lines where the sum of balls in less then the max values
func extract_possible_lines(lines []string) int {
	possible_lines := []int{}
	for index, line := range lines {
		possible := true
		for _, split := range strings.Split(line, ";") {
			sums := sum_colors_in_split(split)
			if is_over_max(sums) == true {
				possible = false
				break
			}
		}
		if possible {
			possible_lines = append(possible_lines, index+1)
		}
	}
	return io.SumNumbers(possible_lines)
}

// Get the power of minimum colors needed
func extract_minimums(lines []string) int {
	powers := []int{}
	for _, line := range lines {
		sums := []map[string]int{}
		for _, split := range strings.Split(line, ";") {
			sum := sum_colors_in_split(split)
			sums = append(sums, sum)
		}
		minimuns := check_for_minimum(sums)
		powers = append(powers, io.PowerOfMapValues(minimuns))
	}
	return io.SumNumbers(powers)
}

// Extract each color and its corrosponding value and sum them up
func sum_colors_in_split(split string) map[string]int {
	color_sums := map[string]int{"red": 0, "green": 0, "blue": 0}
	re := regexp.MustCompile(`(\d+) (\w+)`)
	matches := re.FindAllStringSubmatch(split, -1)
	for _, match := range matches {
		val, err := strconv.Atoi(match[1])
		if err != nil {
			log.Fatal("Match is no valid integer")
		}
		color_sums[match[2]] += val
	}
	return color_sums
}

// Check if one of the colors if over the max
func is_over_max(extracted map[string]int) bool {
	max_vals := map[string]int{"red": 12, "green": 13, "blue": 14}
	for color, value := range extracted {
		if value > max_vals[color] {
			return true
		}
	}
	return false
}

// Extract the minimum number of colors needed for each game
func check_for_minimum(mins []map[string]int) map[string]int {
	base := mins[0]
	for _, set := range mins {
		for color, value := range set {
			if value > base[color] {
				base[color] = value
			}
		}
	}
	return base
}
