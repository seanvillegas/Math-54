
with open("links.txt") as f:
  counter = 0 
  for x in f:
    x = x.strip()
    print(f"- [link_{counter}]({x})")
    counter += 1