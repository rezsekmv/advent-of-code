package main

import (
	"fmt"
	"strings"
)

func hasStraight(pw string) bool {
	for i := 0; i < len(pw)-2; i++ {
		if pw[i+1] == pw[i]+1 && pw[i+2] == pw[i]+2 {
			return true
		}
	}
	return false
}

func hasValidLetters(pw string) bool {
	return !strings.ContainsAny(pw, "iol")
}

func hasTwoPairs(pw string) bool {
	pairs := make(map[byte]bool)
	for i := 0; i < len(pw)-1; i++ {
		if pw[i] == pw[i+1] {
			pairs[pw[i]] = true
		}
	}
	return len(pairs) >= 2
}

func increment(pw []byte) {
	for i := len(pw) - 1; i >= 0; i-- {
		pw[i]++
		if pw[i] > 'z' {
			pw[i] = 'a'
		} else {
			return
		}
	}
}

func nextValidPassword(pw string) string {
	bytes := []byte(pw)
	for {
		increment(bytes)
		s := string(bytes)
		if hasStraight(s) && hasValidLetters(s) && hasTwoPairs(s) {
			return s
		}
	}
}

func main() {
	pw := "hxbxwxba"
	p1 := nextValidPassword(pw)
	fmt.Println(p1)
	fmt.Println(nextValidPassword(p1))
}
