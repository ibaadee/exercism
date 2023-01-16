package twofer
// ShareWith function are choosing value that should be place with people names or personal pronouns
func ShareWith(name string) string {
	if name == "" {
		name = "you"
	}
	return "One for " + name + ", one for me."
}
