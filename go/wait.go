package main

import (
	"log"
	"time"
)

func FixedTimeCheck(getStatusFunc func() int, targetStatus int, checkFunc func(int, int) bool, interval time.Duration) {
	for {
		curStatus := getStatusFunc()
		if checkFunc(curStatus, targetStatus) {
			break
		}
		log.Printf("Current status is %d, waiting to %d\n", curStatus, targetStatus)
		time.Sleep(interval * time.Second)
	}
}

func ExponentialTimeCheck(getStatusFunc func() int, targetStatus int, checkFunc func(int, int) bool, startInterval time.Duration) {
	interval := startInterval
	for {
		curStatus := getStatusFunc()
		if checkFunc(curStatus, targetStatus) {
			break
		}
		log.Printf("Current status is %d, waiting for %d\n", curStatus, targetStatus)
		time.Sleep(interval * time.Second)
		interval *= 2
	}
}

func DiffTimeCheck(getStatusFunc func() int, targetStatus int, checkFunc func(int, int) bool, diffInterval, maxInterval time.Duration) {
	for {
		curStatus := getStatusFunc()
		if checkFunc(curStatus, targetStatus) {
			break
		}
		log.Printf("Current status is %d, waiting for %d\n", curStatus, targetStatus)
		time.Sleep(min(time.Duration((curStatus-targetStatus))*diffInterval, maxInterval) * time.Second)
	}
}

func SelfAdaptiveTimeCheck(getStatusFunc func() int, targetStatus int, checkFunc func(int, int) bool, startInterval, maxInterval time.Duration) {
	startInterval = min(startInterval, maxInterval)
	var preDiff, preInterval time.Duration
	for {
		curStatus := getStatusFunc()
		if checkFunc(curStatus, targetStatus) {
			break
		}
		log.Printf("Current status is %d, waiting for %d\n", curStatus, targetStatus)
		if preDiff == 0 {
			time.Sleep(startInterval * time.Second)
			preDiff, preInterval = time.Duration(abs(curStatus-targetStatus)), startInterval
		} else {
			diff := time.Duration(abs(curStatus - targetStatus))
			unitInterval := preInterval / time.Duration(abs(int(diff-preDiff)))
			interval := min(unitInterval*diff, maxInterval)
			time.Sleep(interval * time.Second)
			preDiff, preInterval = diff, interval
		}
	}
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func min(a, b time.Duration) time.Duration {
	if a < b {
		return a
	}
	return b
}

func main() {
	// Example usage of the functions
	getStatusFunc := func() int {
		// Implement your logic to get the status here
		return 42
	}

	targetStatus := 50

	FixedTimeCheck(getStatusFunc, targetStatus, func(curStatus, targetStatus int) bool {
		return curStatus >= targetStatus
	}, 8)

	// Similar usage for other functions...
}
