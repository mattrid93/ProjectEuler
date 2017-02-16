"""Problem 11: Largest product in a grid.

Brute force."""

def find_largest_product(filename):
    """Finds largest product of 4 squares in a row in any direction."""
    grid = []
    with open(filename) as f:
        for line in f.readlines():
            line = [int(x) for x in line.split()]
            grid.append(line)
    n_rows = len(grid)
    n_columns = len(grid)
    assert n_rows == 20
    assert n_columns == 20
    largest = 0
    # check rows, columns and diags
    for i in range(n_rows):
        for j in range(n_columns - 4):
            products = [1]*4 # horizontal, vertical, up-right, down-left
            for k in range(4):
                products[0] *= grid[i][j+k]
                products[1] *= grid[j+k][i]
                if not (i+j < 3 or i+j > 35) and i > 3 and j < 17:
                    products[2] *= grid[i-k][j+k]
                if not (i-j < -17 or i-j > 15) and i < 17 and j > 3:
                    products[3] += grid[i+k][j+k]
            largest = max(largest, max(products))
    return largest

if __name__ == "__main__":
    print(find_largest_product("inputs/prob11.txt"))
