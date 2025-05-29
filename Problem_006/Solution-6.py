
height = int(input("Enter Height:"))
width = int(input("Enter Width:"))

def isLandscape(height, width):
    if width > height:
        return "Landscape"
    else:
      return "Portrait"

print(isLandscape(height, width))