<div _ngcontent-serverapp-c318="" class="body-text p-24"><p><span style="background-color:transparent;font-size:17pt;"><strong>Selection Sort</strong></span></p><p>&nbsp;</p><p><span style="background-color:transparent;font-size:11pt;">Selection Sort is another type of simple technique to sort any array of given elements.</span></p><p><span style="background-color:transparent;font-size:11pt;">The basic idea is that the minimum element comes to its original index of the array.&nbsp;</span></p><p>&nbsp;</p><p><span style="background-color:transparent;font-size:13.999999999999998pt;"><strong>Algorithm of Selection Sort -&nbsp;</strong></span></p><ul><li><span style="background-color:transparent;font-size:11pt;">Selection sort also takes place in steps called&nbsp;<strong>passes.</strong></span></li><li><span style="background-color:transparent;font-size:11pt;">The number of passes are equal to the number of elements in the array - 1.</span></li><li><span style="background-color:transparent;font-size:11pt;">In each pass, we traverse from left to right in the array and then we find the minimum element from that index to the last element of the array.</span></li><li><span style="background-color:transparent;font-size:11pt;"><strong>For Example -&nbsp;In the first pass, we traverse from 0 to n-1. In the second pass, we traverse from 1 to n-1 and so on.</strong></span></li><li><span style="background-color:transparent;font-size:11pt;">If we find the minimum value, we store the&nbsp;<strong>index of the minimum element.&nbsp;</strong></span></li><li><span style="background-color:transparent;font-size:11pt;">After each pass, we&nbsp;<strong>swap</strong> the current element and element at minimum index.</span></li><li><span style="background-color:transparent;font-size:11pt;">In this way, the array becomes sorted.</span></li></ul><p>&nbsp;</p><p><span style="background-color:transparent;font-size:11pt;">The basic idea of selection sort is to&nbsp;<strong>select the minimum element</strong> in the search range and then put that element on the correct index of the array.</span></p><p><span style="background-color:transparent;font-size:11pt;">Eventually the array will be sorted.</span></p><p>&nbsp;</p><p><span style="background-color:transparent;font-size:13.999999999999998pt;"><strong>Visualisation of Selection Sort -</strong></span></p><p><span style="background-color:transparent;font-size:11pt;">Consider the given array -&nbsp;</span></p><p><span style="background-color:transparent;font-size:11pt;"><img src="https://files.codingninjas.in/article_images/selection-sort-dsa-new-0-1702462229.webp"></span></p><p>&nbsp;</p><p><span style="background-color:transparent;font-size:11pt;">Since there are 5 elements in the array, we will have 4 passes.</span></p><p>&nbsp;</p><p><span style="background-color:transparent;font-size:11pt;"><strong>After 1st pass -&nbsp;</strong></span></p><p><span style="background-color:transparent;font-size:11pt;">We consider the minimum element to be 6. Traverse from 0 index to 4th index. The minimum element will be 4 and the index will also be 4th.</span></p><p><span style="background-color:transparent;font-size:11pt;">Thus we swap 6 and 4 in the array.&nbsp;</span></p><p>&nbsp;</p><p><img src="https://files.codingninjas.in/article_images/selection-sort-dsa-new-1-1702462230.webp"></p><p>&nbsp;</p><p>&nbsp;</p><p><span style="background-color:transparent;font-size:11pt;"><strong>After 2nd pass -&nbsp;</strong></span></p><p><span style="background-color:transparent;font-size:11pt;">We consider the minimum element to be 18. Traverse from 1st index to 4th index. The minimum element will be 6 and the index will be 4th.</span></p><p><span style="background-color:transparent;font-size:11pt;">Thus we swap 18 and 6 in the array.</span></p><p><span style="background-color:transparent;font-size:11pt;"><img src="https://files.codingninjas.in/article_images/selection-sort-dsa-new-2-1702462230.webp">&nbsp;</span></p><p>&nbsp;</p><p><span style="background-color:transparent;font-size:11pt;"><strong>After 3rd pass -&nbsp;</strong></span></p><p><span style="background-color:transparent;font-size:11pt;">We consider the minimum element to be 13. Traverse from 2nd index to 4th index. The minimum element will be 11 and the index will be 3rd.</span></p><p><span style="background-color:transparent;font-size:11pt;">Thus we swap 13 and 11 in the array.</span></p><p><span style="background-color:transparent;font-size:11pt;"><img src="https://files.codingninjas.in/article_images/selection-sort-dsa-new-3-1702462231.webp"></span></p><p>&nbsp;</p><p><span style="background-color:transparent;font-size:11pt;"><strong>After 4th pass -&nbsp;</strong></span></p><p><span style="background-color:transparent;font-size:11pt;">We consider the minimum element to be 13. Traverse from 3rd index to 4th index. The minimum element will be 13 and the index will be 3rd.</span></p><p><span style="background-color:transparent;font-size:11pt;">Thus we swap 13 and 13 in the array.</span></p><p><span style="background-color:transparent;font-size:11pt;"><img src="https://files.codingninjas.in/article_images/selection-sort-dsa-new-3-1702462231.webp"></span></p><p>&nbsp;</p><p><span style="background-color:transparent;font-size:11pt;"><strong>Array is sorted.</strong></span></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p><span style="background-color:transparent;font-size:11pt;">The C++ code is shown for selection sort.</span></p><p style="text-align:center;"><span style="background-color:transparent;font-size:11pt;"><img src="https://files.codingninjas.in/article_images/selection-sort-dsa-new-4-1702462231.webp"></span></p><p>&nbsp;</p><p><span style="background-color:transparent;font-size:11pt;"><strong>Time Complexity - Quadratic O(n^2)</strong></span></p><p>&nbsp;</p></div>