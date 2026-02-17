def minimum_road_width(n, h, heights):
    width = 0
    for height in heights:
        if height > h:
            width += 2  
        else:
            width += 1  
    return width
 
def main():
    n, h = map(int, input().split())
    heights = list(map(int, input().split()))
    print(minimum_road_width(n, h, heights))
 
if __name__ == "__main__":
    main()
