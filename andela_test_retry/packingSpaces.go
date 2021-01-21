package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	fmt.Println(packingDilemma([]int{2, 3, 9, 18, 20, 22}, 3))
	fmt.Println(packingDilemma([]int{2, 5, 6, 7, 9, 13, 10}, 2))
}

func packingDilemma(arr []int, k int) int {
	min := math.MaxInt64
	sort.Ints(arr)

	for i := 1; i < len(arr)-k+1; i++ {
		next := arr[i+k-1]
		cur := arr[i]

		temp := next - cur

		if temp < min {
			min = temp
		}
	}
	return min
}
