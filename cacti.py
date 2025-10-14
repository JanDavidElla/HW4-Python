def cacti_number(array): #func is a 2D array
    def wrapper():
        plot = array
        #Everytime there is a 0, it will keep track of index
        #Will compare to top and bottom (array before and after, same index)
        #Will compare to left and right (index after and before)
        openSpots = 0
        for i in range(0, len(plot)):
            row = plot[i]
            for j in range(0, len(row)):
                if row[j] == 0:
                    top = plot[i-1][j] if i>0 else 0
                    bottom = plot[i+1][j] if i<len(plot) - 1 else 0
                    left = row[j-1] if j > 0 else 0
                    right = row[j+1] if j < len(row) - 1 else 0
                    if top == 0 and bottom == 0 and right == 0 and left == 0:
                        openSpots += 1
                        row[j] = 1
        return openSpots
    return wrapper()

