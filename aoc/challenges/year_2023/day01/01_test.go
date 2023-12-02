package day01

import (
	"testing"
)

func TestOne(t *testing.T) {
	in := []string{
		"1abc2",
		"pqr3stu8vwx",
		"a1b2c3d4e5f",
		"treb7uchet",
	}
	want := 142
	got := numbers_per_lines(in, false)

	if got != want {
		t.Errorf("got %v but wanted %v", got, want)
	}
}

func TestTwo(t *testing.T) {
	in := []string{
		"two1nine",
		"eightwothree",
		"abcone2threexyz",
		"xtwone3four",
		"4nineeightseven2",
		"zoneight234",
		"7pqrstsixteen",
	}
	want := 281
	got := numbers_per_lines(in, true)

	if got != want {
		t.Errorf("got %v but wanted %v", got, want)
	}
}

func TestCheckIfStringBeginsWithNum(t *testing.T) {
	t.Run("Starts with written num", func(t *testing.T) {
		in := "nineeightseven2"
		want := "9"
		got := check_str_prefix(in)
		if got != want {
			t.Errorf("got %s but wanted %s", got, want)
		}
	})
	t.Run("Starts random chars", func(t *testing.T) {
		in := "xyznineeightseven2"
		want := ""
		got := check_str_prefix(in)
		if got != want {
			t.Errorf("got %s but wanted %s", got, want)
		}
	})
}
