"""
Get Shortest substring containing all characters in the array.
"""


def getShortestSubstring(arr, msg):
    final_str = msg
    for i in range(len(str)):
        temp = ""
        arr_c = arr.copy()
        for j in range(i, len(str)):
            temp = temp + msg[j]
            if msg[j] in arr_c:
                arr_c.remove(msg[j])
            if len(arr_c) == 0:
                final_str = temp if len(temp) < len(final_str) else final_str
                break
    return final_str


# Note:
# Time complexity is n^2
# It can be improved further by starting of the j pointer from previous loop iteration's end pointer.
# as no point of checking from i=j point.

assert getShortestSubstring(["x", "y", "z"], "xyyzyzyyx") == "xyyz"

assert getShortestSubstring(["x", "y", "z"], "xyyzyzyx") == "zyx"
