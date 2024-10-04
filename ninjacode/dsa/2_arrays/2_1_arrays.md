<div _ngcontent-serverapp-c318="" class="body-text p-24"><p><span style="font-size:17pt;"><strong>Arrays&nbsp;</strong></span><br>&nbsp;</p><p style="text-align:justify;"><span style="font-size:11pt;">An array is a&nbsp;<strong>fixed-size&nbsp;</strong>collection of elements of the&nbsp;<strong>same data type&nbsp;</strong>stored in&nbsp;<strong>contiguous memory&nbsp;</strong>locations. It is the simplest data structure where each array element can be accessed by using its index.&nbsp;</span></p><p style="margin-left:18pt;"><span style="font-size:11pt;"><img src="https://files.codingninjas.in/article_images/gp_dsa_arrays_new-0-1695366687.jpg" alt="Arrays (The Java™ Tutorials > Learning the Java Language > Language Basics)"></span></p><p style="margin-left:18pt;"><span style="font-size:10pt;">Credits: Oracle.com</span></p><p style="margin-left:18pt;">&nbsp;</p><p style="margin-left:18pt;">&nbsp;</p><p><span style="font-size:16pt;"><strong>Types of Array: Based on Dimensions</strong></span></p><p>&nbsp;</p><p><span style="font-size:11pt;">We have multiple forms of arrays to ease the process of storing data further.</span></p><p><span style="font-size:11pt;">Array types depend on the number of dimensions an array can have. These are:</span></p><p>&nbsp;</p><p><span style="font-size:12pt;"><strong>Single Dimensional Arrays</strong></span></p><p><span style="font-size:11pt;">The arrays we discussed and declared in the previous section were 1D arrays because they stored elements linearly in contiguous memory locations. A single dimension is used to store elements inside this array. They are denoted as Array_Name [ ].</span><br><br>&nbsp;</p><p><span style="font-size:12pt;"><strong>Multi-Dimensional Arrays</strong></span></p><p><span style="font-size:11pt;">Arrays having more than one dimension are multiple-dimensional arrays, as the name suggests. The&nbsp;<strong>most relevant</strong> multiple-dimensional arrays are 2D and 3D arrays.</span></p><p>&nbsp;</p><ul><li><span style="font-size:11pt;"><strong>Two-dimensional arrays</strong>– 2D arrays give us a tabular representation by storing elements in the form of rows(i) * columns(j), for instance, an A[2][3] will have 2 rows and 3 columns allocating 6 elements. The array starts from A[0][0], giving us the first element in the image below.&nbsp;</span></li></ul><p><span style="font-size:11pt;"><img src="https://files.codingninjas.in/article_images/gp_dsa_arrays_new-1-1695366687.webp"></span></p><p><span style="font-size:10pt;">Credits- Quora.com</span></p><p>&nbsp;</p><ul><li><span style="font-size:11pt;"><strong>Three Dimensional Arrays</strong> – A 3D array extends a 2D array by adding a dimension depth in this data structure, so this array has depth, rows and columns denoted as A[k][i][j] where k, i, j represents depth, rows and columns respectively.</span></li></ul><p>&nbsp;</p><p><br><span style="font-size:17pt;"><strong>Properties of arrays&nbsp;</strong></span></p><p>&nbsp;</p><ul><li><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">Each array element is of the same data type and size. For example, For an array of integers with the int data type, each array element will occupy 4 bytes.</span></p></li><li><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">&nbsp;Elements of the array are stored in contiguous memory locations. For example : 200 is the starting address (base address) assigned to the first element of the array and each element of the array is of integer data type occupying 4 bytes in memory.&nbsp;</span></p></li></ul><p style="margin-left:1.5pt;"><span style="font-size:11pt;"><img src="https://files.codingninjas.in/article_images/gp_dsa_arrays_new-2-1695366688.webp"></span></p><p>&nbsp;</p><p><span style="font-size:17pt;"><strong>Accessing array elements&nbsp;</strong></span></p><p>&nbsp;</p><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">●&nbsp;The elements of the array are accessed by using their index. The index of an array of size N ranges from&nbsp;<strong>0&nbsp;</strong>to&nbsp;<strong>N-1</strong>.&nbsp;</span></p><p style="margin-left:0.5059967041015625pt;"><span style="font-size:11pt;">For example: Accessing element at index 5: Array[5] -&gt; this is the 6th element in the array.&nbsp;</span></p><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">●&nbsp;Every array is identified by its&nbsp;<strong>base address&nbsp;</strong>i.e the location of the first element of the array in memory. So, basically, the base address helps identify the address of all the array elements.&nbsp;</span></p><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">Since the elements of an array are stored in contiguous memory locations, the address of any element can be accessed from the base address itself.&nbsp;</span></p><p style="margin-left:0.93499755859375pt;"><span style="font-size:11pt;">For example : 200 is the base address of the array, so address of element at index 4 will be 200 + 4 * (sizeof(int)) = 216.&nbsp;</span></p><p>&nbsp;</p><p><span style="font-size:17pt;"><strong>Where can arrays be used?&nbsp;</strong></span></p><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">●&nbsp;<strong>Arrays&nbsp;</strong>should be used where the number of elements to be stored is already known.&nbsp;</span></p><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">●&nbsp;<strong>Arrays&nbsp;</strong>are commonly&nbsp;<strong>used&nbsp;</strong>in computer programs to organize data so that a related set of values&nbsp;<strong>can&nbsp;</strong>be easily&nbsp;<strong>sorted&nbsp;</strong>or&nbsp;<strong>searched</strong>.&nbsp;</span></p><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">●&nbsp;Generally, when we require&nbsp;<strong>high-speed access times</strong>, we usually prefer arrays since they provide O(1) access times.&nbsp;</span></p><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">●&nbsp;Arrays work well when we have to&nbsp;<strong>organize data in a multidimensional format</strong>. We can declare arrays of as many dimensions as we want.&nbsp;</span></p><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">●&nbsp;If the element's index to be modified is known beforehand, it can be efficiently modified using arrays due to&nbsp;<strong>quick access time&nbsp;</strong>and&nbsp;<strong>mutability</strong>.&nbsp;</span></p><p style="margin-left:1.529998779296875pt;">&nbsp;</p><p style="margin-left:1.529998779296875pt;"><span style="font-size:17pt;"><strong>Disadvantages of arrays&nbsp;</strong></span></p><p style="margin-left:18.957000732421875pt;text-align:justify;"><span style="font-size:11pt;">●&nbsp;Since&nbsp;<strong>arrays&nbsp;</strong>are&nbsp;<strong>fixed-size&nbsp;</strong>data structures, you cannot dynamically alter their sizes. It creates a problem when the number of elements the array will store is not known beforehand.&nbsp;</span></p><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">●&nbsp;<strong>Insertion&nbsp;</strong>and&nbsp;<strong>Deletion&nbsp;</strong>in arrays are difficult and costly since the elements are stored in contiguous memory locations, hence, we need to shift the elements to create/delete space for elements.&nbsp;</span></p><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">●&nbsp;If more memory is allocated than required, it leads to the&nbsp;<strong>wastage of memory&nbsp;</strong>space and&nbsp;<strong>less allocation of memory&nbsp;</strong>also leads to a problem.&nbsp;</span></p><p>&nbsp;</p><p style="margin-left:0.339996337890625pt;"><span style="font-size:17pt;"><strong>Time Complexity of various operations&nbsp;</strong></span></p><p style="margin-left:0.339996337890625pt;">&nbsp;</p><p style="margin-left:0.339996337890625pt;"><span style="font-size:11pt;"><strong>&nbsp; &nbsp; &nbsp;Accessing elements:&nbsp;&nbsp;</strong></span></p><ul><li><p style="margin-left:0.339996337890625pt;"><span style="font-size:11pt;">&nbsp; &nbsp; Since elements in an array are stored at contiguous memory locations, they can be accessed very efficiently (random access) in&nbsp;<strong>O(1)&nbsp;</strong>time &nbsp; &nbsp; &nbsp;using indices.&nbsp;</span></p></li></ul><p style="margin-left:18.957000732421875pt;">&nbsp;</p><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;"><strong>Inserting elements:&nbsp;</strong></span></p><p style="margin-left:18.957000732421875pt;">&nbsp;</p><ul><li><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">Insertion of elements at the end of the array (at the index located to the right of the last element and there is still available space) takes&nbsp;<strong>O(1)&nbsp;</strong>time.&nbsp;</span></p></li><li><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">If we want to insert an element at index i, all the elements starting from index i must be shifted to the right by one position. Thus, the time complexity for inserting an element at index i is&nbsp;<strong>O(N - i)</strong>.&nbsp;</span></p></li><li><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">Inserting an element at the beginning of the array involves moving all elements by one position to their right, if there is available space, and takes&nbsp;<strong>O(N)&nbsp;</strong>time.&nbsp;</span></p></li></ul><p style="margin-left:18.957000732421875pt;">&nbsp;</p><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;"><strong>Finding elements:&nbsp;</strong></span></p><ul><li><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">Finding an element in an array takes&nbsp;<strong>O(N)&nbsp;</strong>time in the worst case, where N is the size of the array, as you may need to traverse the entire array.&nbsp;</span></p></li></ul><p style="margin-left:18.957000732421875pt;">&nbsp;</p><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;"><strong>Deleting elements:&nbsp;</strong></span></p><p style="margin-left:18.957000732421875pt;">&nbsp;</p><ul><li><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">Deletion of elements from the end of the array takes&nbsp;<strong>O(1)&nbsp;</strong>time. Deleting elements from the beginning or at any array index involves moving elements to the left.&nbsp;</span></p></li><li><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">If we want to delete an element at index i, all the elements starting from index (i + 1) must be shifted to the left by one index. Thus, the time complexity for deleting an element at index i is&nbsp;<strong>O(N - i)</strong>.&nbsp;</span></p></li><li><p style="margin-left:18.957000732421875pt;"><span style="font-size:11pt;">Deleting an element from the beginning involves moving all elements starting from index 1 to the left by one position and takes&nbsp;<strong>O(N)&nbsp;</strong>time.&nbsp;</span></p></li></ul><p style="margin-left:0.49500274658203125pt;">&nbsp;</p></div>