package hamming
import (
	"errors"
)
//Distance is counting character that similar per strings
func Distance(a, b string) (result int, err error) {
	//check only similar string could be processed
	if len(a) != len(b) {
		return 0, errors.New("there are different length between first and second string")
	}
	// Convert to rune slices to avoid mismatching bytes and runes.
	ar, br := []rune(a), []rune(b)
	//compare string, add with 1 if strings not same
	for i, r := range ar {
		if r != br[i] {
			result++
		}
	}
	return result, err
}
