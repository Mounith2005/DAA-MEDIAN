from flask import Flask, render_template, request

app = Flask(__name__)

# Recursive Quickselect Implementation
def quickselect_recursive(arr, left, right, k):
    if left == right:
        return arr[left]
    
    pivot_index = partition(arr, left, right)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect_recursive(arr, left, pivot_index - 1, k)
    else:
        return quickselect_recursive(arr, pivot_index + 1, right, k)

# Non-Recursive Quickselect Implementation
def quickselect_non_recursive(arr, left, right, k):
    while left < right:
        pivot_index = partition(arr, left, right)
        
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1
    return arr[left]

# Partition Function (common for both recursive and non-recursive versions)
def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

# Find Median Function using Quickselect (Recursive)
def find_median_recursive(arr):
    n = len(arr)
    k = n // 2 if n % 2 == 1 else n // 2 - 1
    return quickselect_recursive(arr, 0, n - 1, k)

# Find Median Function using Quickselect (Non-Recursive)
def find_median_non_recursive(arr):
    n = len(arr)
    k = n // 2 if n % 2 == 1 else n // 2 - 1
    return quickselect_non_recursive(arr, 0, n - 1, k)

# Route to display the page and accept input
@app.route("/", methods=["GET", "POST"])
def index():
    median_recursive = None
    median_non_recursive = None
    sorted_arr = None
    
    if request.method == "POST":
        # Get input from the user
        input_data = request.form["numbers"]
        
        # Convert input to a list of integers
        arr = list(map(int, input_data.split(',')))
        
        # Store the original array to display sorted version later
        sorted_arr = sorted(arr)
        
        # Calculate median using recursive and non-recursive quickselect
        median_recursive = find_median_recursive(arr)
        median_non_recursive = find_median_non_recursive(arr)

    return render_template(
        "index.html",
        median_recursive=median_recursive,
        median_non_recursive=median_non_recursive,
        sorted_arr=sorted_arr
    )

if __name__ == "__main__":
    app.run(debug=True)
