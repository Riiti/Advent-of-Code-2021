package day02

import (
	"reflect"
	"testing"
)

func TestOne(t *testing.T) {
	in := []string{
		"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
		"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
		"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
		"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
		"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
	}
	want := 8
	got := extract_possible_lines(in)

	if got != want {
		t.Errorf("got %v but wanted %v", got, want)
	}
}

func TestTwo(t *testing.T) {
	in := []string{
		"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
		"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
		"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
		"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
		"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
	}
	want := 2286
	got := extract_minimums(in)

	if got != want {
		t.Errorf("got %v but wanted %v", got, want)
	}
}

func TestSumColorsInSplit(t *testing.T) {
	in := "Game 1: 3 blue, 4 red;"
	want := map[string]int{"blue": 3, "red": 4, "green": 0}
	got := sum_colors_in_split(in)

	if reflect.DeepEqual(want, got) == false {
		t.Errorf("got %v but wanted %v", got, want)
	}
}

func TestIsOverMax(t *testing.T) {
	t.Run("Over max", func(t *testing.T) {
		in := map[string]int{"blue": 15, "red": 4, "green": 0}
		got := is_over_max(in)
		if got == false {
			t.Error("Value is greater than max")
		}
	})
	t.Run("Under max", func(t *testing.T) {
		in := map[string]int{"blue": 1, "red": 4, "green": 0}
		got := is_over_max(in)
		if got {
			t.Error("Value is less than max")
		}
	})
}

func TestCheckMinimums(t *testing.T) {
	in := []map[string]int{{"blue": 3, "red": 4, "green": 0}, {"blue": 5, "red": 4, "green": 0}}
	got := check_for_minimum(in)
	want := map[string]int{"blue": 5, "red": 4, "green": 0}

	if reflect.DeepEqual(want, got) == false {
		t.Errorf("got %v but wanted %v", got, want)
	}
}
