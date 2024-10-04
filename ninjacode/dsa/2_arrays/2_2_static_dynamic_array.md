<div _ngcontent-serverapp-c318="" class="body-text p-24"><p><span style="font-size:17pt;"><strong><u>Static &amp; Dynamic Arrays</u></strong></span></p><p><br><span style="font-size:12pt;">According to the array concept, an array can be defined in two ways per the memory allocation concept.</span><br><br>&nbsp;</p><p><span style="font-size:11pt;"><img src="https://files.codingninjas.in/article_images/gp_dsa_arrays_new_static_dynamic-0-1695366938.webp"></span></p><p><span style="font-size:10pt;">Credits-ukacademe.com</span></p><p>&nbsp;</p><p><span style="font-size:13.999999999999998pt;"><strong><u>Static arrays-</u></strong></span></p><p>&nbsp;</p><ul><li><span style="font-size:12pt;">The size or number of elements in static arrays is fixed. The array size cannot be changed after creating an array and allocating memory space.</span></li><li><span style="font-size:12pt;">The content of the array can be modified, but the memory space allocated to it will remain unchanged.</span></li><li><span style="font-size:12pt;">They may also be referred to as fixed-length arrays or fixed arrays.&nbsp;</span></li><li><span style="font-size:12pt;">It is created on the stack.</span></li><li><span style="font-size:12pt;">No need to delete static arrays. They are deleted automatically after going out of scope.</span></li></ul><p>&nbsp;</p><p><span style="font-size:12pt;"><strong>Static Array Big O notations</strong></span><span style="font-size:13pt;"><strong>-</strong></span></p><p>&nbsp;</p><ul><li><span style="font-size:12pt;">Space: O(n)</span></li><li><span style="font-size:12pt;">Lookup: O(1)</span></li><li><span style="font-size:12pt;">Append: O(1)</span></li><li><span style="font-size:12pt;">Insert: O(n)</span></li><li><span style="font-size:12pt;">Delete: O(n)</span></li></ul><p>&nbsp;</p><p><span style="font-size:12pt;">Example-&nbsp;</span><span style="font-size:12.499999999999998pt;">The following code demonstrates using a static integer array in C++.</span></p><p>&nbsp;</p><pre><code class="language-cpp hljs"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">&lt;iostream&gt;</span></span>
<span class="hljs-keyword">using</span> <span class="hljs-keyword">namespace</span> <span class="hljs-built_in">std</span>;

<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">()</span> </span>{

   <span class="hljs-keyword">int</span> intArray[<span class="hljs-number">4</span>] = {<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">8</span>};
   <span class="hljs-built_in">cout</span> &lt;&lt; <span class="hljs-string">"Array Elements: "</span>;
   <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> j = <span class="hljs-number">0</span>; j &lt; <span class="hljs-number">4</span>; j++) {
       <span class="hljs-built_in">cout</span> &lt;&lt; intArray[j];
       <span class="hljs-built_in">cout</span> &lt;&lt; <span class="hljs-string">" "</span>;
   }
  
   <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
}
</code></pre><p>&nbsp;</p><p><span style="font-size:13.999999999999998pt;"><strong><u>Dynamic arrays-</u></strong></span></p><p>&nbsp;</p><ul><li><span style="font-size:12pt;">The size or number of elements in a dynamic array can change. After an array is created, the size of the array can grow or shrink.</span></li><li><span style="font-size:12pt;">Dynamic arrays allow elements to be added and removed at runtime. The size of a dynamic collection can be modified during the operations performed on it.</span></li><li><span style="font-size:12pt;">It is created on a heap.</span></li><li><span style="font-size:12pt;">Dynamic arrays must be manually deleted after they are no longer required.</span></li></ul><p style="margin-left:36pt;">&nbsp;</p><p><span style="font-size:12pt;"><strong>Dynamic Array Big O notations</strong></span><span style="font-size:13pt;"><strong>-</strong></span></p><p>&nbsp;</p><ul><li><span style="font-size:12pt;">Space: O(n)</span></li><li><span style="font-size:12pt;">Lookup: O(1)</span></li><li><span style="font-size:12pt;">Append: O(n)</span></li><li><span style="font-size:12pt;">Insert: O(n)</span></li><li><span style="font-size:12pt;">Delete: O(n)</span></li></ul><p>&nbsp;</p><p><span style="font-size:12pt;">Example-</span><span style="font-size:11pt;">&nbsp;</span><span style="font-size:12.499999999999998pt;">The following code demonstrates how to use a dynamic integer array in C++.</span></p><p>&nbsp;</p><pre><code class="language-cpp hljs"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">&lt;iostream&gt;</span></span>
<span class="hljs-keyword">using</span> <span class="hljs-keyword">namespace</span> <span class="hljs-built_in">std</span>;

<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">()</span> </span>{

   <span class="hljs-keyword">int</span>* intArray = <span class="hljs-keyword">new</span> <span class="hljs-keyword">int</span>[<span class="hljs-number">4</span>];
   intArray[<span class="hljs-number">0</span>] = <span class="hljs-number">5</span>;
   intArray[<span class="hljs-number">1</span>] = <span class="hljs-number">6</span>;
   intArray[<span class="hljs-number">2</span>] = <span class="hljs-number">7</span>;
   intArray[<span class="hljs-number">3</span>] = <span class="hljs-number">8</span>;
   <span class="hljs-built_in">cout</span> &lt;&lt; <span class="hljs-string">"Array Elements: "</span>;
   <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> j = <span class="hljs-number">0</span>; j &lt; <span class="hljs-number">4</span>; j++) {
       <span class="hljs-built_in">cout</span> &lt;&lt; intArray[j];
       <span class="hljs-built_in">cout</span> &lt;&lt; <span class="hljs-string">" "</span>;
   }
   <span class="hljs-keyword">delete</span>[] intArray;
  
   <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
}
</code></pre><p>&nbsp;</p></div>