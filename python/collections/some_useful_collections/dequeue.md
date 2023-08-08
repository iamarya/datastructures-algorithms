<div _ngcontent-serverapp-c231="" class="note-body"><div _ngcontent-serverapp-c231="" class="body-text"><h2><strong>Deque</strong></h2><p>&nbsp;</p><p>Deques are a generalization of basic stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction. Though list objects support similar operations, they are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the underlying data representation.</p><p>Deque (Doubly Ended Queue) is the optimized list for quicker append and pop operations from both sides of the container. It provides O(1) time complexity for append and pop operations as compared to a list with O(n) time complexity.</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">collections</span>.<span class="hljs-title">deque</span>(<span class="hljs-params">list</span>)</span></code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Python code to demonstrate working of append(), appendleft() </span>

<span class="hljs-keyword">from</span> collections <span class="hljs-keyword">import</span> deque 

<span class="hljs-comment"># initializing deque </span>
de = deque([<span class="hljs-number">10</span>,<span class="hljs-number">9</span>,<span class="hljs-number">8</span>]) 

<span class="hljs-comment"># using append() to insert element at right end inserts 'A' at the end of deque </span>
de.append(<span class="hljs-string">"A"</span>) 

<span class="hljs-comment"># printing modified deque </span>
<span class="hljs-keyword">print</span> (<span class="hljs-string">"The deque after appending at right is : "</span>) 
<span class="hljs-keyword">print</span> (de) 

<span class="hljs-comment"># using appendleft() to insert element at right end inserts 6 at the beginning of deque </span>
de.appendleft(<span class="hljs-number">6</span>) 

<span class="hljs-comment"># printing modified deque </span>
<span class="hljs-keyword">print</span> (<span class="hljs-string">"The deque after appending at left is : "</span>) 
<span class="hljs-keyword">print</span> (de)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">The deque after appending at right <span class="hljs-keyword">is</span> :                                                                                         
deque([<span class="hljs-number">10</span>, <span class="hljs-number">9</span>, <span class="hljs-number">8</span>, <span class="hljs-string">'A'</span>])                                                                                                          
The deque after appending at left <span class="hljs-keyword">is</span> :                                                                                          
deque([<span class="hljs-number">6</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>, <span class="hljs-number">8</span>, <span class="hljs-string">'A'</span>])                                                                                                  </code></pre><h2>&nbsp;</h2><h2><strong>Removing Elements</strong></h2><p>&nbsp;</p><p>Elements can also be removed from the deque from both ends. To remove elements from the right use the pop() method and to remove elements from the left use popleft() method.</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Python code to demonstrate working of pop(), and popleft() </span>

<span class="hljs-keyword">from</span> collections <span class="hljs-keyword">import</span> deque 

<span class="hljs-comment"># initializing deque </span>
python_libs = deque([<span class="hljs-string">'Django'</span>,<span class="hljs-string">'Flask'</span>,<span class="hljs-string">'Celery'</span>,<span class="hljs-string">'NumPy'</span>,<span class="hljs-string">'Pandas'</span>]) 

<span class="hljs-comment"># using pop() to delete element from right end deletes 'Pandas' from the right end of deque </span>
python_libs.pop() 

<span class="hljs-comment"># printing modified deque </span>
<span class="hljs-keyword">print</span> (<span class="hljs-string">"The deque after deleting from right is : "</span>) 
<span class="hljs-keyword">print</span> (python_libs) 

<span class="hljs-comment"># using popleft() to delete element from left end deletes 'Django' from the left end of deque </span>
python_libs.popleft() 

<span class="hljs-comment"># printing modified deque </span>
<span class="hljs-keyword">print</span> (<span class="hljs-string">"The deque after deleting from left is : "</span>) 
<span class="hljs-keyword">print</span> (python_libs)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">The deque after deleting <span class="hljs-keyword">from</span> right <span class="hljs-keyword">is</span> :                                                                                        
deque([<span class="hljs-string">'Django'</span>, <span class="hljs-string">'Flask'</span>, <span class="hljs-string">'Celery'</span>, <span class="hljs-string">'NumPy'</span>])                                                                                   
The deque after deleting <span class="hljs-keyword">from</span> left <span class="hljs-keyword">is</span> :                                                                                         
deque([<span class="hljs-string">'Flask'</span>, <span class="hljs-string">'Celery'</span>, <span class="hljs-string">'NumPy'</span>])</code></pre></div></div>