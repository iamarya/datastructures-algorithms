<div _ngcontent-serverapp-c318="" class="body-text p-24"><p><span style="font-size:16pt;"><strong>Traversal in an Array</strong></span></p><p>&nbsp;</p><p><span style="background-color:transparent;color:#000000;font-size:12pt;"><img src="https://files.codingninjas.in/article_images/gp_dsa_arrays_new_traversal-0-1695367195.webp"></span></p><p>&nbsp;</p><p><span style="font-size:12pt;">The process of visiting or accessing each element of an array, one by one, is called a&nbsp;<strong>Traversal in an Array</strong>.&nbsp;</span></p><p>&nbsp;</p><p><span style="font-size:12pt;">Counting array elements, printing array values, changing current values, and adding all element values are all possible using traversal operations.&nbsp;</span></p><p>&nbsp;</p><pre><code class="language-cpp hljs"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">()</span> 
</span>{ 
   <span class="hljs-comment">// Declare the array with the size and the array elements </span>
   <span class="hljs-keyword">int</span> <span class="hljs-built_in">array</span>[<span class="hljs-number">10</span>] = { <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>, <span class="hljs-number">10</span> }; 
   <span class="hljs-comment">// Declare a flag variable and initialise it to 0 </span>
   <span class="hljs-keyword">int</span> flag = <span class="hljs-number">0</span>; 
 
   <span class="hljs-comment">// Iterate through the array and compare each element of the array to the item </span>
   <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i &lt; <span class="hljs-number">10</span>; i++) { 
          <span class="hljs-built_in">cout</span>&lt;&lt;<span class="hljs-built_in">array</span>[i];
   } 
      <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>; 
}
</code></pre><p>&nbsp;</p><pre><code class="language-plaintext hljs">Output:
1 2 3 4 5 6 7 8 9 10</code></pre><p>&nbsp;</p><h3><strong>How to Search an Element in an Array</strong></h3><h3>&nbsp;</h3><ul><li><span style="font-size:12pt;">Many search algorithms are available to search for an element in an array, like Linear Search, Binary Search, Hash Table (Dictionary), etc.&nbsp;</span></li></ul><p>&nbsp;</p><ul><li><span style="font-size:12pt;">The most basic one is linear search, where we find an element by traversing each index from first to last.&nbsp;</span></li></ul><p>&nbsp;</p><ul><li><span style="font-size:12pt;">Suppose there are N numbers in an array, and we have to search for a specific number num.</span></li></ul><p>&nbsp;</p><p>&nbsp;</p><p><span style="background-color:transparent;color:#000000;font-size:10pt;"><img src="https://files.codingninjas.in/article_images/gp_dsa_arrays_new_traversal-1-1695367195.webp"></span></p><p><span style="font-size:10pt;">Credits: log2base2.com</span></p><p>&nbsp;</p><p><span style="font-size:12pt;">Let’s code a program to find an element in a given array-</span></p><p>&nbsp;</p><pre><code class="language-cpp hljs"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">&lt;iostream&gt;&nbsp;</span></span>
<span class="hljs-keyword">using</span> <span class="hljs-keyword">namespace</span> <span class="hljs-built_in">std</span>; 
<span class="hljs-function"><span class="hljs-keyword">int</span>&nbsp;<span class="hljs-title">main</span><span class="hljs-params">()</span>&nbsp;
</span>{&nbsp;
   <span class="hljs-comment">// Declare the array&nbsp;with the size and&nbsp;the array&nbsp;elements&nbsp;</span>
  <span class="hljs-keyword">int</span>&nbsp;<span class="hljs-built_in">array</span>[<span class="hljs-number">10</span>] = { <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>, <span class="hljs-number">10</span> };&nbsp;
 
   <span class="hljs-comment">// Declare the element to be searched&nbsp;</span>
  <span class="hljs-keyword">int</span>&nbsp;item;&nbsp;
   <span class="hljs-built_in">cout</span> &lt;&lt;&nbsp;<span class="hljs-string">"Enter the item to be searched: "</span>;&nbsp;
   <span class="hljs-built_in">cin</span> &gt;&gt; item;&nbsp;
 
   <span class="hljs-comment">// Declare a flag variable and&nbsp;initialise it to 0&nbsp;</span>
  <span class="hljs-keyword">int</span>&nbsp;flag = <span class="hljs-number">0</span>;&nbsp;
 
   <span class="hljs-comment">// Iterate through the array&nbsp;and compare each element of the array&nbsp;to the item&nbsp;</span>
   <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i &lt; <span class="hljs-number">10</span>; i++) {&nbsp;
     &nbsp;<span class="hljs-keyword">if</span>&nbsp;(<span class="hljs-built_in">array</span>[i] == item) {&nbsp;
           <span class="hljs-comment">// If the item is found, set the flag to 1&nbsp;</span>
           flag = <span class="hljs-number">1</span>;&nbsp;
           <span class="hljs-keyword">break</span>;&nbsp;
       }&nbsp;
   }&nbsp;
 
   <span class="hljs-comment">// Check the flag value&nbsp;</span>
  <span class="hljs-keyword">if</span>&nbsp;(flag == <span class="hljs-number">1</span>)&nbsp;
       <span class="hljs-built_in">cout</span> &lt;&lt;&nbsp;<span class="hljs-string">"Item found"</span>;&nbsp;
   <span class="hljs-keyword">else</span>
       <span class="hljs-built_in">cout</span> &lt;&lt;&nbsp;<span class="hljs-string">"Item not found"</span>;&nbsp;
 
  <span class="hljs-keyword">return</span>&nbsp;<span class="hljs-number">0</span>;&nbsp;
}
</code></pre><p>&nbsp;</p><p>&nbsp;</p><pre><code class="language-cpp hljs">Output:
Enter the item to be searched: 
<span class="hljs-number">7</span> 
Item found</code></pre><p>&nbsp;</p><p><span style="font-size:16pt;"><strong>Insertion of an Element in an Array&nbsp;</strong></span></p><p>&nbsp;</p><p><span style="font-size:12pt;">The elements can be inserted anywhere in the array. Thus, we can do so at the beginning, middle, end, or elsewhere.</span></p><p>&nbsp;</p><p><span style="font-size:12pt;">The positions or index locations are increased once the element is added to the array, but this does not imply that the array size is growing.</span></p><p>&nbsp;</p><p><span style="background-color:transparent;color:#000000;font-size:16pt;"><strong><img src="https://files.codingninjas.in/article_images/gp_dsa_arrays_new_traversal-2-1695367196.webp"></strong></span></p><p><span style="font-size:10pt;">Credits: log2base2.com</span></p><p>&nbsp;</p><p><span style="font-size:12pt;">Let’s code a program to insert an element in a given array-</span></p><p>&nbsp;</p><pre><code class="language-cpp hljs"><span class="hljs-function"><span class="hljs-keyword">int</span>&nbsp;<span class="hljs-title">main</span><span class="hljs-params">()</span>
</span>{
   <span class="hljs-keyword">int</span> arr[size] = {<span class="hljs-number">1</span>,&nbsp;<span class="hljs-number">20</span>,&nbsp;<span class="hljs-number">5</span>,&nbsp;<span class="hljs-number">78</span>,&nbsp;<span class="hljs-number">30</span>};
   <span class="hljs-keyword">int</span> element, pos, i;
   <span class="hljs-built_in">printf</span>(<span class="hljs-string">"Enter position and element\n"</span>);
   <span class="hljs-built_in">scanf</span>(<span class="hljs-string">"%d%d"</span>,&amp;pos,&amp;element);
   <span class="hljs-keyword">if</span>(pos &lt;= size &amp;&amp; pos &gt;=&nbsp;<span class="hljs-number">0</span>)
   {
       <span class="hljs-comment">//shift all the elements from the last index to pos by 1 position to the right</span>
       <span class="hljs-keyword">for</span>(i = size; i &gt; pos; i--)
           arr[i] = arr[i<span class="hljs-number">-1</span>];
       <span class="hljs-comment">//Insert element at the given position</span>
       arr[pos] = element;
   */
       <span class="hljs-keyword">for</span>(i =&nbsp;<span class="hljs-number">0</span>; i &lt;= size<span class="hljs-number">-1</span>; i++)
           <span class="hljs-built_in">printf</span>(<span class="hljs-string">"%d "</span>, arr[i]);
   }
   <span class="hljs-keyword">else</span>
       <span class="hljs-built_in">printf</span>(<span class="hljs-string">"Invalid Position\n"</span>);
   <span class="hljs-keyword">return</span>&nbsp;<span class="hljs-number">0</span>;
 }</code></pre><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p><span style="font-size:16pt;"><strong>Deletion of an Element in an Array&nbsp;</strong></span></p><p>&nbsp;</p><p><span style="font-size:12pt;">To&nbsp;<strong>delete a specific element</strong> from an array, we have to traverse and perform a search for that element in the array. The deletion of the component does not affect the size of an array. Furthermore, we should also check whether the deletion is possible in an array.</span></p><p><span style="background-color:transparent;color:#000000;font-size:16pt;"><strong><img src="https://files.codingninjas.in/article_images/gp_dsa_arrays_new_traversal-3-1695367196.webp"></strong></span></p><p><span style="font-size:10pt;">Credits: log2base2.com</span></p><p>&nbsp;</p><p><span style="font-size:12pt;">Let’s code a program to delete an element in a given array-</span></p><pre><code class="language-cpp hljs">
<span class="hljs-function"><span class="hljs-keyword">int</span>&nbsp;<span class="hljs-title">main</span><span class="hljs-params">()</span>
</span>{
   <span class="hljs-keyword">int</span> arr[size] = {<span class="hljs-number">1</span>,&nbsp;<span class="hljs-number">20</span>,&nbsp;<span class="hljs-number">5</span>,&nbsp;<span class="hljs-number">78</span>,&nbsp;<span class="hljs-number">30</span>};
   <span class="hljs-keyword">int</span> key, i, index =&nbsp;<span class="hljs-number">-1</span>;
   <span class="hljs-built_in">printf</span>(<span class="hljs-string">"Enter element to delete\n"</span>);
   <span class="hljs-built_in">scanf</span>(<span class="hljs-string">"%d"</span>,&amp;key);
   <span class="hljs-comment">/*
   * iterate the array elements using loop
   * if any element matches the key, store the index
   */</span>
   <span class="hljs-keyword">for</span>(i =&nbsp;<span class="hljs-number">0</span>; i &lt; size; i++)
   {
       <span class="hljs-keyword">if</span>(arr[i] == key)
       {
           index = i;
           <span class="hljs-keyword">break</span>;
 }
   }
   <span class="hljs-keyword">if</span>(index !=&nbsp;<span class="hljs-number">-1</span>)
   {
       <span class="hljs-comment">//shift all the element from index+1 by one position to the left</span>
       <span class="hljs-keyword">for</span>(i = index; i &lt; size -&nbsp;<span class="hljs-number">1</span>; i++)
           arr[i] = arr[i+<span class="hljs-number">1</span>];
       <span class="hljs-built_in">printf</span>(<span class="hljs-string">"New Array : "</span>);
       <span class="hljs-keyword">for</span>(i =&nbsp;<span class="hljs-number">0</span>; i &lt; size -&nbsp;<span class="hljs-number">1</span>; i++)
           <span class="hljs-built_in">printf</span>(<span class="hljs-string">"%d "</span>,arr[i]);
   }
   <span class="hljs-keyword">else</span>
       <span class="hljs-built_in">printf</span>(<span class="hljs-string">"Element Not Found\n"</span>);
   <span class="hljs-keyword">return</span>&nbsp;<span class="hljs-number">0</span>;
  
 }</code></pre></div>