#!/usr/bin/python3
""" TLG NDE Python | LAncheta | Spooky Loopin' Exercise """

def main():
    
    count= 0
    
    with open("dracula.txt", "r") as dracula:
        with open("vampytimes.txt", "w") as drake:    
            for line in dracula:
                    if "vampire" in line.lower():
                        count += 1
                        print(line)
                        drake.write(line)

    print(f"\n\n----->  The total number the word 'vampire' appears in the novel is: {count}  <-----\n")
main()
